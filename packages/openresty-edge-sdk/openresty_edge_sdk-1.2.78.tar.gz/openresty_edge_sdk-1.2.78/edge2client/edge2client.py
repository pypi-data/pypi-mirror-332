# -*- coding: utf-8 -*-
import re
import time
import json
import warnings
import base64
import sys
from os import getenv, popen
import requests
import urllib3
import copy
import io
from subprocess import Popen, PIPE
from urllib.parse import urlencode
from .constants import OFF, DEFAULT, ERROR_LOG_LEVELS, \
    INITIAL_EDGE_VERSION, EDGE_VERSION_24_09_16, EDGE_VERSION_24_09_06

from .edge_common import process_rule_cond, process_conseq, \
        process_waf, process_proxy, process_cache, process_content, \
        process_proxy_patch, proxy_upstream_transform, get_first_ip

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if sys.version_info.major == 3:
    from urllib.parse import urljoin
else:
    from urlparse import urljoin

DEBUG = getenv('EDGE_DEBUG')
# 2018/01/01 00:00:00 UTC
EPOCH = 1514764800


def utf8_encode(content):
    if isinstance(content, str):
        return content.encode('utf-8')
    return content


# all url
GlobalUserUrl = 'user/list'
GlobalUserDefinedActionUrl = 'global/1/user_defined_actions'
GlobalRewriteRuleUrl = 'global/1/rewrite/rules?detail=1'
GlobalWafRuleUrl = 'global/1/waf/rule_sets'
GlobalUpstreamUrl = 'global/1/upstreams/'
GlobalK8sUpstreamUrl = 'global/1/k8s_upstreams'
GlobalDymetricsUrl = 'global/1/dymetrics'
GlobalK8sUrl = 'global/1/k8s'
GlobalIPListUrl = 'global/1/ip_list'
GlobalIPListUrlV2 = 'ip_list'
GlobalIPListItemsUrl = 'global/1/ip_list/{}/items'
ModGlobalIPListUrl = 'ip_list/{}/{}'
K8sUrl = 'k8s'
ApplicationUrl = 'applications'
AppUpstreamUrl = 'applications/http/{}/clusters'
AppK8sUpstreamUrl = 'applications/http/{}/k8s_upstreams'
AppRewriteRuleUrl = 'applications/http/{}/phases/rewrite/rules'
AppRewriteRuleDetailUrl = 'applications/http/{}/phases/rewrite/rules/?detail=1'
APPRewriteRuleReorder = '_reorder/applications/http/{}/phases/rewrite/rules'
AppSslCertUrl = 'applications/http/{}/phases/ssl_cert/certs/'
AppAcmeCertUrl = 'acme_cert/info/'
AppAcmeCertLogsUrl = 'acme_cert/logs'
AppCachePurgeUrl = 'applications/http/{}/purge?detail=1'
AppWafWhiteListUrl = 'applications/http/{}/waf_whitelist?detail=1'
AppIPListUrl = 'applications/http/{}/ip_list'
ModAppIPListUrl = 'app_ip_list/{}/{}/{}'
AppIPListUrlV2 = 'app_ip_list/{}'
AppIPListItemsUrl = 'applications/http/{}/ip_list/{}/items'
PartitionsUrl = 'partitions/?detail=1'
GatewayUrl = 'gateway'
GatewayTagUrl = 'gatewaytag'
VersionUrl = 'version'
DymetricsDataUrl = 'log_server/dymetrics/list_data'
AppMetricsUrl = 'log_server/metrics_http'
AppDymetricsUrl = 'applications/http/{}/dymetrics'
NodeMonitorSystemUrl = 'log_server/node_monitor/{}/system'
SearchK8sUpstreamUrl = 'search/k8s-upstream'
SearchK8sUpstreamHistoryUrl = 'search/k8s-upstream-history'
NodesUrl = 'gateway/{}/nodes/{}'
LmdbBackupUrl = 'nodes/lmdb_backup'
ReferencedUrl = 'referenced/global_cert/{}'
PartitionLuaModuleUrl = 'partitions/{}/lua_modules/{}'
WafLogUrl = 'log_server/waflog/{}'
DosLogUrl = 'log_server/cc_log/{}'
GlobalPageTemplateUrl = 'global/1/page_template'
AppBasicAuthGroupUrl = 'applications/http/{}/auth_list'
AppBasicAuthUserUrl = 'applications/http/{}/auth_list/{}/items'
ListCandidateNodeUrl = "nodecandidate/list"
ApproveCandidateNodeUrl = "nodecandidate/approve"
SyncToAllUrl = "profiles/1/sync_to_all"
UserGroupUrl = "user-group"
GlobalBasicAuthGroupUrl = 'global/1/auth_list'
GlobalBasicAuthUserUrl = 'global/1/auth_list/{}/items'
GlobalK8sEndpointsUrl = 'global/1/k8s_endpoints'
GlobalAcmeProvidersUrl = 'global/1/acme_providers'
ErrorLogsUrl = 'log_server/errlog'

class Edge2Client(object):
    def __init__(self, host, username, password, api_token=None):
        if not host:
            raise Exception('no host arg specified')

        self.api_token = api_token
        if not api_token:
            if not username:
                raise Exception('no username arg specified')
            if not password:
                raise Exception('no password arg specified')

        self.username = username
        self.password = password

        self.base_uri = urljoin(host, '/api/v1/')

        self.timeout = 240

        self.__token = ''
        self.__verify = True
        self.__login_time = 0
        self.app_id = None
        self.dns_id = None

        self.__ok = False

        self.phases = {
            'req-rewrite': 'rewrite',
            'resp-rewrite': 'resp_rewrite',
            'ssl': 'ssl'
        }

        self.waf_actions = {
            'log': True,
            'block': True,
            'edge-captcha': True,
            'hcaptcha': True,
            'redirect': True ,
            'page-template': True,
            'close-connection': True,
            'redirect-validate': True,
            'js-challenge': True
        }

        self.dos_actions = {
            'close_connection': True,
            'error_page': True,
            'enable_hcaptcha': True,
            'enable_edge_captcha': True,
            'redirect_validate': True,
            'js_challenge': True,
            'delay': True,
        }

        self.app_types = {
            'http': 'http',
            'partition': 'partitions_ngx',
        }

    def use_app(self, app_id):
        if not app_id:
            raise Exception('application ID not found')
        if not isinstance(app_id, int):
            raise Exception('Bad application ID obtained: ' + app_id)

        self.app_id = app_id

    def use_dns_app(self, dns_id):
        if not dns_id:
            raise Exception('DNS ID not found')
        if not isinstance(dns_id, int):
            raise Exception('Bad DNS ID obtained: ' + dns_id)

        self.dns_id = dns_id

    def do_request(self, method, path, body=None, files=None):
        login_time = self.__login_time or 0
        if not self.api_token and (not self.__token or time.time() - login_time >= 3600 - 60):
            self.login()

        headers = {}
        if self.__token:
            headers["Auth"] = self.__token

        if self.api_token:
            headers["API-Token"] = self.api_token

        r = requests.request(method, urljoin(self.base_uri, path),
                             headers=headers,
                             json=body, timeout=self.timeout,
                             files=files,
                             verify=self.__verify)

        if DEBUG:
            print(method)
            print(body)
            print(r.url)
            print(r.text)

        if r.status_code != 200:
            warnings.warn('response status is not 200: {}\nresponse body: {}'.format(r.status_code, r.content))
            self.__ok = False
            return None

        return r.content

    def do_api(self, method, path, body=None, files=None):
        login_time = self.__login_time or 0
        if not self.api_token and (not self.__token or time.time() - login_time >= 3600 - 60):
            self.login()

        headers = {}
        if self.__token:
            headers["Auth"] = self.__token

        if self.api_token:
            headers["API-Token"] = self.api_token

        r = requests.request(method, urljoin(self.base_uri, path),
                             headers=headers,
                             json=body, timeout=self.timeout,
                             files=files,
                             verify=self.__verify)

        if DEBUG:
            print(method)
            print(body)
            print(r.url)
            print(r.text)

        if r.status_code != 200:
            warnings.warn('response status is not 200: {}\nresponse body: {}'.format(r.status_code, r.text))
            self.__ok = False
            return None

        response = r.json()
        status = response.get('status')
        if status is not None and status != 0:
            msg = response.get('msg', '')
            err = json.dumps(response.get('err', ''))
            req_body = body or ''
            warnings.warn(
                'Request: {} {} {} failed\nstatus : {}\nmsg : {}\nerr : {}\nresponse body: {}'.format(
                    method, path, req_body, status, msg, err, r.text))
            self.__ok = False
            self.__msg = msg
            return None

        # print(response)
        data = response.get('data')
        self.__ok = True
        self.__msg = None
        return data if data is not None else True

    def get_msg(self):
        return self.__msg

    def get_status(self):
        return self.__ok

    def set_login_time(self, login_time):
        self.__login_time = login_time

    def set_token(self, token):
        self.__token = token

    def set_ssl_verify(self, verify):
        self.__verify = verify

    def get_token(self):
        return self.__token

    def request_ok(self):
        return self.__ok

    def login(self):
        if self.api_token:
            raise Exception("no need to login after the API token is specified")

        r = requests.post(urljoin(self.base_uri,
                                  'user/login'),
                          data=json.dumps({'username': self.username,
                                           'password': self.password}),
                          timeout=self.timeout, verify=self.__verify)
        response = r.json()
        status = response.get('status')
        if status != 0:
            err = response.get('msg', '')
            raise Exception("failed to login: " + err)

        data = response.get('data')
        if not data:
            raise Exception('failed to get data of response')

        token = data.get('token')
        if not token:
            return False

        self.set_login_time(time.time())
        self.set_token(token)

        return True

    def count_all(self, url, has_uri_arg=False):
        t = '&' if has_uri_arg else '?'
        url = '{}{}page=1&page_size=0'.format(url, t)
        ret = self.do_api('GET', url)
        if not self.request_ok():
            raise Exception('request failed.')

        meta = ret.get('meta')
        if not meta:
            raise Exception('invalid response: not "meta" found')

        count = meta.get('count')
        if not count and count != 0:
            raise Exception('invalid response: not "count" found')

        return count

    def get_all(self, url, has_uri_arg=False, page_size=100):
        count = self.count_all(url, has_uri_arg)

        times = 1
        if not page_size and count > 0:
            page_size = count

        if count > page_size:
            times = int(count / page_size + 1)

        infos = []
        t = '&' if has_uri_arg else '?'

        final_url = '{}{}page={}&page_size={}'
        for i in range(1, times + 1):
            ret = self.do_api('GET', final_url.format(url, t, i, page_size))

            if not self.request_ok():
                raise Exception('request failed.')

            data = ret.get('data')
            if not data:
                break

            infos = infos + data

        return infos

    def get_app_id(self):
        return self.app_id

    def new_app(self, **kwargs):
        kwargs['http_verb'] = 'POST'
        data = self.put_app(**kwargs)

        if not self.request_ok():
            raise Exception('request failed.')

        app_id = data.get('id')
        if not app_id:
            raise Exception('application ID not found')

        if not isinstance(app_id, int):
            raise Exception('Bad application ID obtained: ' + app_id)

        self.app_id = app_id

        return app_id

    def put_app(
            self,
            app_id=None, http_verb='PUT',
            domains=None,
            http_ports=None, https_ports=None,
            label=None,
            cluster_groups=None, offline=None, access_log=dict()):
        if http_verb == 'PUT' and not app_id:
            raise Exception('no active application selected')

        if not domains:
            raise Exception('no domains arg specified')

        domain_specs = []
        for domain in domains:
            is_wildcard = domain.startswith('*')
            domain_specs.append({'domain': domain, 'is_wildcard': is_wildcard})

        body = {
            'domains': domain_specs,
            'allow_access_by_ip': False,
        }

        if label is not None:
            body['name'] = label

        non_standard_ports = False
        body['type'] = []
        if http_ports:
            body['http_ports'] = http_ports
            body['type'].append('http')
            non_standard_ports = True

        if https_ports:
            body['https_ports'] = https_ports
            body['type'].append('https')
            non_standard_ports = True

        if not non_standard_ports:
            body['type'] = ['http', 'https']

        if cluster_groups:
            if not isinstance(cluster_groups, list):
                raise Exception('The type of cluster_groups should be list')
            body['partitions'] = cluster_groups

        if offline is not None:
            if isinstance(offline, bool):
                body['offline'] = {'enabled': offline}
            else:
                raise Exception('bad parameter offline: bool is expected')

        if access_log is None:
            body['config'] = {
                'access_log': None,
            }
        elif access_log:
            access_log_name = access_log.get('name', None)
            if access_log_name is None:
                raise Exception('missing access log name')

            access_log_filename = access_log.get('filename', "access.log")

            body['config'] = {
                'access_log': {
                    'filename': access_log_filename,
                    'name': access_log_name,
                }
            }

        url = 'applications/'
        if http_verb == 'PUT':
            url = url + str(app_id)

        return self.do_api(http_verb, url, body)

    def put_app_config(self, app_id=None, limiter=None,
                       enable_websocket=None, access_log=dict(),
                       client_max_body_size=DEFAULT,
                       client_max_body_size_unit=DEFAULT):
        http_verb = 'PUT'
        if not app_id:
            raise Exception('no active application selected')

        if client_max_body_size is not DEFAULT:
            if client_max_body_size is not None and not isinstance(client_max_body_size, int):
                raise Exception('bad parameter client_max_body_size: int or None is expected')

        if client_max_body_size_unit is not DEFAULT:
            if client_max_body_size_unit is not None:
                if not isinstance(client_max_body_size_unit, str):
                    raise Exception('bad parameter client_max_body_size_unit: str or None is expected')

                if client_max_body_size_unit not in ['m', 'k']:
                    raise Exception('bad parameter client_max_body_size_unit: m or k is expected')

        url = 'applications/' + str(app_id) + '/config'
        body = {}

        if limiter is not None:
            body['limiter'] = limiter

        if enable_websocket is not None:
            if isinstance(enable_websocket, bool):
                body['enable_websocket'] = enable_websocket
            else:
                raise Exception('bad parameter enable_websocket: bool is expected')

        if access_log is None:
            body['access_log'] = None

        elif access_log:
            access_log_name = access_log.get('name', None)
            if access_log_name is None:
                raise Exception('missing access log name')

            access_log_filename = access_log.get('filename', "access.log")

            body['access_log'] = {
                'filename': access_log_filename,
                'name': access_log_name,
            }
        # else # empty dict, do nothing

        if client_max_body_size is not DEFAULT:
            if client_max_body_size is None:
                client_max_body_size = None
                client_max_body_size_unit = None
            else:
                if client_max_body_size_unit is DEFAULT or client_max_body_size_unit is None:
                    client_max_body_size_unit = "m"

            body['client_max_body_size'] = client_max_body_size
            body['client_max_body_size_unit'] = client_max_body_size_unit

        return self.do_api(http_verb, url, body)

    def get_app_config(self, app_id=None):
        http_verb = 'GET'
        if not app_id:
            raise Exception('no active application selected')
        url = 'applications/' + str(app_id) + '/config'

        return self.do_api(http_verb, url)

    def get_app_domains(self, app_id=None):
        http_verb = 'GET'
        if not app_id:
            raise Exception('no active application selected')

        url = 'applications/http/' + str(app_id) + '/domains'
        return self.do_api(http_verb, url)

    def append_app_domain(self, app_id=None, domain=None, is_wildcard=False):
        if not app_id:
            raise Exception('no active application selected')

        if not domain:
            raise Exception('no domain arg specified')
        body = {
            'domain': domain,
            'is_wildcard': is_wildcard
        }

        return self.do_api(
            'POST', 'applications/http/{}/domains'.format(self.app_id), body)

    def get_app(self):
        if not self.app_id:
            raise Exception('no active application selected')

        return self.do_api(
            'GET', 'applications/http/{}?detail=1'.format(self.app_id))

    def del_app(self, app_id):
        if not app_id:
            raise Exception('no active application selected')

        return self.do_api('DELETE', 'applications/http/' + str(app_id))

    def new_release(self, app_type="http", app_id=None, gray=None):
        if app_type not in self.app_types:
            raise Exception('unsupported app type: {}'.format(app_type))

        if app_type == "http":
            if not self.app_id and not app_id:
                raise Exception('no active http application selected')
            if not app_id:
                app_id = self.app_id

        elif app_type == "partition":
            if not app_id:
                raise Exception('no active partition selected')

        body = {
            'comment': 'a new release'
        }

        if gray is not None:
            body['gray'] = gray

        app_type = self.app_types[app_type]
        url = 'txlogs/release/{}/{}'.format(app_type, app_id)
        return self.do_api('POST', url, body)

    def clear_pending_changes(self, app_type="http", app_id=None):
        if app_type not in self.app_types:
            raise Exception('unsupported app type: {}'.format(app_type))

        if app_type == "http":
            if not self.app_id and not app_id:
                raise Exception('no active http application selected')
            if not app_id:
                app_id = self.app_id

        elif app_type == "partition":
            if not app_id:
                raise Exception('no active partition selected')

        app_type = self.app_types[app_type]
        url = 'txlogs/revert/{}/{}'.format(app_type, app_id)
        return self.do_api('GET', url)

    def sync_status(self):
        if not self.app_id:
            raise Exception('no active application selected')

        data = self.do_api(
            'GET', 'status/application/' + str(self.app_id))

        if not self.request_ok():
            raise Exception('request failed.')

        synced = data.get('catch_uped', 0)
        total = data.get('total', 0)

        return total, synced

    def pending_changes(self, app_type="http", app_id=None):
        if app_type not in self.app_types:
            raise Exception('unsupported app type: {}'.format(app_type))

        if app_type == "http":
            if not self.app_id and not app_id:
                raise Exception('no active http application selected')
            if not app_id:
                app_id = self.app_id

        elif app_type == "partition":
            if not app_id:
                raise Exception('no active partition selected')

        app_type = self.app_types[app_type]
        url = 'txlogs/pending-count/{}/{}'.format(app_type, app_id)
        changes = self.do_api('GET', url)

        if not self.request_ok():
            raise Exception('request failed.')
        if not isinstance(changes, int):
            raise Exception('No pending change count returned by the API')

        return changes

    def new_upstream(self, **kwargs):
        kwargs['http_verb'] = 'POST'
        data = self.put_upstream(**kwargs)

        if not self.request_ok():
            raise Exception('request failed.')

        up_id = data.get('id')
        if not up_id:
            raise Exception('upstream ID not found')
        if not isinstance(up_id, int):
            raise Exception('Bad upstream ID obtained: ' + up_id)

        return up_id

    def put_upstream(self, up_id=None, http_verb='PUT', name=None,
                     servers=None, health_checker=None, ssl=False,
                     group=None, disable_ssl_verify=None):
        if not self.app_id:
            raise Exception('no active application selected')

        if http_verb == 'PUT' and not up_id:
            raise Exception('no active upstream selected')

        if not name:
            raise Exception('no name arg specified')
        if not servers:
            raise Exception('no servers arg specified')

        i = 0
        node_specs = []
        for server in servers:
            i += 1

            domain = server.get('domain')
            server_ip = server.get('ip')

            if not domain and not server_ip:
                raise Exception(
                    'No domain or ip field specified '
                    'for the {}-th upstream server'.format(str(i)))

            port = server.get('port')
            if not port:
                raise Exception(
                    'No port field specified for '
                    'the {}-th upstream server'.format(str(i)))

            weight = server.get('weight', 1)
            status = server.get('status', 1)
            node = {
                'domain': domain,
                'ip': server_ip,
                'port': port,
                'weight': weight,
                'status': status
            }
            node_id = server.get('id')
            if node_id:
                node['id'] = node_id

            node_specs.append(node)

        body = {
            'name': name,
            'group': group,
            'ssl': ssl,
            'disable_ssl_verify': disable_ssl_verify,
            'nodes': node_specs
        }

        if health_checker:
            health_checker['concurrency'] = 5
            body['enable_checker'] = True
            body['checker'] = health_checker
        else:
            body['enable_checker'] = False

        url = 'applications/http/{}/clusters/'.format(self.app_id)
        if http_verb == 'PUT':
            url = url + str(up_id)

        return self.do_api(http_verb, url, body)

    def get_upstream(self, up_id):
        if not self.app_id:
            raise Exception('no active application selected')
        if not up_id:
            raise Exception('no active upstream selected')

        return self.do_api(
            'GET', 'applications/http/{}/clusters/{}?detail=1'
            .format(self.app_id, up_id))

    def get_all_upstreams(self, detail=False):
        if not self.app_id:
            raise Exception('no active application selected')

        if detail:
            data = self.get_all(AppUpstreamUrl.format(self.app_id) + '?detail=1', True)
        else:
            data = self.get_all(AppUpstreamUrl.format(self.app_id))

        if detail:
            return data

        upstreams = {}
        for upstream in data:
            upstreams[upstream['name']] = upstream['id']

        return upstreams

    def del_upstream(self, up_id):
        if not self.app_id:
            raise Exception('no active application selected')
        if not up_id:
            raise Exception('no active upstream selected')

        return self.do_api(
            'DELETE', 'applications/http/{}/clusters/{}'.format(self.app_id, up_id))

    def new_k8s_upstream(self, **kwargs):
        kwargs['http_verb'] = 'POST'
        data = self.put_k8s_upstream(**kwargs)

        if not self.request_ok():
            raise Exception('request failed.')

        up_id = data.get('id')
        if not up_id:
            raise Exception('k8s upstream ID not found')
        if not isinstance(up_id, int):
            raise Exception('Bad k8s upstream ID obtained: ' + up_id)

        return up_id

    def copy_upstream_to_k8s_upstream(self, up_id, k8s_services=None, rules=None):
        if not self.app_id:
            raise Exception('no active application selected')
        if not up_id:
            raise Exception('no active upstream selected')

        if k8s_services is None:
            raise Exception('no k8s_services arg specified')

        upstream = self.get_upstream(up_id)

        if not self.request_ok():
            raise Exception('upsteam {} is not exist.'.format(up_id))

        name = upstream.get('name')

        if upstream.get('enable_checker', False):
            health_checker = upstream.get('checker')
        else:
            health_checker = None

        ssl = upstream.get("ssl")
        disable_ssl_verify = upstream.get("disable_ssl_verify")

        k8s_tmp_name = name + "_k8s"

        k8s_up_id = self.new_k8s_upstream(
            name=k8s_tmp_name,
            k8s_services=k8s_services,
            health_checker=health_checker,
            ssl=ssl,
            disable_ssl_verify=disable_ssl_verify)

        if rules is None:
            rules = self.get_all_rules()

        for rule in rules:
            rule_id = rule.get('id', None)
            proxy = rule.get('proxy', None)

            if rule_id is None:
                continue

            if proxy is None:
                continue

            need_update = False

            upstreams = proxy.get('upstream', None)

            if upstreams is not None:
                for upstream in upstreams:
                    upstream_cluster = upstream.get('cluster', None)
                    if up_id == upstream_cluster:
                        del upstream['cluster']
                        upstream['k8s_upstream'] = k8s_up_id
                        need_update = True

            backup_upstreams = proxy.get('backup_upstream', None)

            if backup_upstreams is not None:
                for upstream in backup_upstreams:
                    upstream_cluster = upstream.get('cluster', None)
                    if up_id == upstream_cluster:
                        del upstream['cluster']
                        upstream['k8s_upstream'] = k8s_up_id
                        need_update = True

            if need_update:
                if upstreams is not None:
                    for upstream in upstreams:
                        proxy_upstream_transform(upstream)
                if backup_upstreams is not None:
                    for upstream in backup_upstreams:
                        proxy_upstream_transform(upstream)
                self.put_rule(rule_id=rule_id, proxy=proxy)


        ok = self.del_upstream(up_id)

        if not ok:
            raise Exception('del origin upstream failed.')

        ok = self.put_k8s_upstream(
            up_id=k8s_up_id,
            name=name,
            k8s_services=k8s_services,
            health_checker=health_checker,
            ssl=ssl,
            disable_ssl_verify=disable_ssl_verify)

        if not ok:
            raise Exception('rename k8s upstream name {} to {} failed.'
                    .format(k8s_tmp_name, name))

        return k8s_up_id

    def put_k8s_upstream(self, up_id=None, http_verb='PUT', name=None,
                         k8s_services=None, health_checker=None, ssl=False,
                         group=None, disable_ssl_verify=None, nodes=None):
        if not self.app_id:
            raise Exception('no active application selected')

        if http_verb == 'PUT' and not up_id:
            raise Exception('no active upstream selected')

        if not name:
            raise Exception('no name arg specified')
        if not k8s_services:
            raise Exception('no k8s_services arg specified')

        i = 0

        for service in k8s_services:
            i += 1
            k8s = service.get('k8s')
            k8s_namespace = service.get('k8s_namespace')
            k8s_service = service.get('k8s_service')
            k8s_service_port = service.get('k8s_service_port')

            if not k8s:
                raise Exception(
                    'No k8s field specified for '
                    'for the {}-th upstream k8s_services'.format(str(i)))

            if not isinstance(k8s, int):
                raise Exception(
                    'Bad k8s field type for '
                    'for the {}-th upstream k8s_services'.format(str(i)))

            if not k8s_namespace:
                raise Exception(
                    'No k8s_namespace field specified for '
                    'for the {}-th upstream k8s_services'.format(str(i)))

            if not k8s_service:
                raise Exception(
                    'No k8s_service field specified for '
                    'for the {}-th upstream k8s_services'.format(str(i)))

            if not k8s_service_port:
                raise Exception(
                    'No k8s_service_port field specified for '
                    'for the {}-th upstream k8s_services'.format(str(i)))

            if not isinstance(k8s_service_port, int):
                raise Exception(
                    'Bad k8s_service_port field type for '
                    'for the {}-th upstream k8s_services'.format(str(i)))

        body = {
            'name': name,
            'group': group,
            'ssl': ssl,
            'disable_ssl_verify': disable_ssl_verify,
            'k8s_services': k8s_services,
            'is_k8s_service': True
        }

        if health_checker:
            health_checker['concurrency'] = 5
            body['enable_checker'] = True
            body['checker'] = health_checker
        else:
            body['enable_checker'] = False

        i = 0;

        if nodes is not None:

            if not isinstance(nodes, list):
               raise Exception('The type of nodes should be list')

            for node in nodes:
                i += 1
                ip = node.get("ip")
                port = node.get("port")
                weight = node.get("weight")

                if not ip:
                    raise Exception(
                        'No ip field specified for '
                        'for the {}-th upstream nodes'.format(str(i)))

                if not port:
                    raise Exception(
                        'No port field specified for '
                        'for the {}-th upstream nodes'.format(str(i)))

                if not isinstance(port, int):
                    raise Exception(
                        'Bad port field type for '
                        'for the {}-th upstream nodes'.format(str(i)))

                if not weight:
                    raise Exception(
                        'No weight field specified for '
                        'for the {}-th upstream nodes'.format(str(i)))

                if not isinstance(weight, int):
                    raise Exception(
                        'Bad weight field type for '
                        'for the {}-th upstream nodes'.format(str(i)))

            body['nodes'] = nodes

        url = AppK8sUpstreamUrl.format(self.app_id)
        if http_verb == 'PUT':
            url = url + '/' + str(up_id)

        return self.do_api(http_verb, url, body)

    def get_k8s_upstream(self, up_id):
        if not self.app_id:
            raise Exception('no active application selected')
        if not up_id:
            raise Exception('no active k8s upstream selected')

        return self.do_api(
            'GET', 'applications/http/{}/k8s_upstreams/{}?detail=1'
            .format(self.app_id, up_id))

    def get_all_k8s_upstreams(self, detail=False, page_size=1000, with_service=False):
        if not self.app_id:
            raise Exception('no active application selected')

        url = AppK8sUpstreamUrl.format(self.app_id)
        has_uri_arg = False
        if with_service:
            url = f"{url}?detail=1"
            has_uri_arg = True

        data = self.get_all(url, has_uri_arg=has_uri_arg)

        if detail:
            return data

        upstreams = {}
        for upstream in data:
            upstreams[upstream['name']] = upstream['id']

        return upstreams

    def del_k8s_upstream(self, up_id):
        if not self.app_id:
            raise Exception('no active application selected')
        if not up_id:
            raise Exception('no active upstream selected')

        return self.do_api(
            'DELETE', 'applications/http/{}/k8s_upstreams/{}'.format(self.app_id, up_id))

    def new_rule(self, **kwargs):
        kwargs['http_verb'] = 'POST'
        data = self.put_rule(**kwargs)

        if not self.request_ok():
            raise Exception('request failed.')

        rule_id = data.get('id')
        if not rule_id:
            raise Exception('rule id not found')
        if not isinstance(rule_id, int):
            raise Exception('Bad rule id obtained: ' + rule_id)

        return rule_id

    def reorder_rules(self, orders):
        if not self.app_id:
            raise Exception('no active application selected')

        if not isinstance(orders, dict):
            raise Exception('invalid rule orders')

        if not orders:
            # empty dict
            return True

        for k in orders.keys():
            v = orders[k]

            if not isinstance(k, int) or not isinstance(v, int):
                raise Exception('invalid rule order, rule id: {}, order: {}'.format(k, v))

        url = APPRewriteRuleReorder.format(self.app_id)
        return self.do_api('PUT', url, orders)

    def prepare_conseq(self, conseq):
        if not conseq:
            raise Exception('No conseq field specified')
        if isinstance(conseq, dict):
            conseq = [conseq]
        elif not isinstance(conseq, list):
            raise Exception('Bad conseq field value type: ' + str(type(conseq)))

        return conseq

    def prepare_waf_data(self, waf):
        # allow rule name or id
        rule_sets = waf.get('rule_sets', None)
        if not rule_sets:
            # none or empty
            return waf

        # get waf rules
        rule_names = dict()
        rule_ids = dict()
        rules = self.get_all_global_waf_rules()
        for rule in rules:
            rule_id = rule['id']
            rule_name = rule['name']
            rule_names[rule_name] = rule_id
            rule_ids[rule_id] = True

        for i, name in enumerate(rule_sets):
            if name not in rule_names and name not in rule_ids:
                raise Exception('waf rule set not found: ' + name)

            if name in rule_names:
                rule_sets[i] = rule_names[name]

        return waf

    def put_rule(self, rule_id=None, http_verb='PUT',
                 condition=None, conseq=None, waf=None,
                 cache=None, proxy=None, content=None,
                 top=0, last=None, order=None, reorder=False,
                 enable=None, comment=None):
        if not self.app_id:
            raise Exception('no active application selected')

        if http_verb == 'PUT' and not rule_id:
            raise Exception('no active rule selected')

        if not conseq and not waf and not proxy and not cache and not content:
            raise Exception(
                'No conseq or waf or proxy or cache or '
                'content field specified')

        sections = [
            { 'value': condition, 'handler': process_rule_cond, 'key': 'conditions'},
            { 'value': conseq, 'handler': process_conseq, 'prepare': self.prepare_conseq, 'key': 'actions'},
            { 'value': waf, 'handler': process_waf, 'prepare': self.prepare_waf_data, 'key': 'waf'},
            { 'value': proxy, 'handler': process_proxy, 'key': 'proxy'},
            { 'value': cache, 'handler': process_cache, 'key': 'cache'},
            { 'value': content, 'handler': process_content, 'key': 'content'},
        ]

        body = {}
        for s in sections:
            value = s['value']
            key = s['key']
            handler = s['handler']
            prepare = s.get('prepare', None)

            if value == OFF:
                body[key] = None
            elif value is not None:
                if prepare:
                    value = prepare(value)

                spec = handler(value)
                if spec:
                    body[key] = spec

        if top != 0:
            body['top'] = top

        if last is not None:
            body['last'] = last
        elif http_verb == "POST":
            if cache or proxy or content:
                body['last'] = True
            else:
                body['last'] = False

        if order is not None:
            body['order'] = order

        if enable is not None:
            body['enable_rule'] = enable

        if comment is not None:
            if comment == "":
                body['comment'] = None
            else:
                body['comment'] = comment

        url = 'applications/http/{}/phases/rewrite/rules/'.format(self.app_id)
        if http_verb == 'PUT':
            url = url + str(rule_id)

        data = self.do_api(http_verb, url, body)

        if http_verb == 'POST' and reorder == True:
            if not self.request_ok():
                raise Exception('new page rule failed.')

            rule_id = data.get('id')
            if not rule_id:
                raise Exception('rule ID not found')
            if not isinstance(rule_id, int):
                raise Exception('bad rule id obtained: ' + rule_id)

            # get all rule
            rules = self.get_all_rules(self.app_id)

            # reorder
            i = 1
            new_orders = dict()
            for rule in rules:
                new_orders[rule['id']] = i
                i = i + 1

            ok = self.reorder_rules(new_orders)
            if not ok:
                warnings.warn('failed to reorder rules after insert rule')

        return data

    def patch_rule(self, rule_id=None, condition=None, conseq=None, waf=None,
                   cache=None, proxy=None, content=None,
                   top=0, last=False, order=None):
        if not self.app_id:
            raise Exception('no active application selected')

        if not rule_id:
            raise Exception('no active rule selected')

        sections = [
            { 'value': condition, 'handler': process_rule_cond, 'key': 'conditions'},
            { 'value': conseq, 'handler': process_conseq, 'key': 'actions'},
            { 'value': waf, 'handler': process_waf, 'key': 'waf'},
            { 'value': proxy, 'handler': process_proxy, 'key': 'proxy'},
            { 'value': cache, 'handler': process_cache, 'key': 'cache'},
            { 'value': content, 'handler': process_content, 'key': 'content'},
        ]

        body = {}
        for s in sections:
            value = s['value']
            key = s['key']
            handler = s['handler']

            if value == OFF:
                body[key] = None
            elif value is not None:
                spec = handler(value)
                if spec:
                    body[key] = spec

        if top != 0:
            body['top'] = top

        if last is not None:
            body['last'] = last

        if order is not None:
            body['order'] = order

        url = 'applications/http/{}/phases/rewrite/rules/{}'.format(self.app_id,
                                                               str(rule_id))

        return self.do_api('PUT', url, body)

    def put_proxy_rule(self, rule_id=None, proxy=None, need_process=True):
        if not self.app_id:
            raise Exception('no active application selected')

        if not rule_id:
            raise Exception('no active rule selected')

        if not proxy:
            raise Exception('No proxy field specified')

        if need_process:
            proxy = process_proxy(proxy)

        url = 'applications/http/{}/phases/rewrite/rules/{}/proxy'.format(
            self.app_id, rule_id)

        return self.do_api('PUT', url, proxy)

    def get_rule(self, rule_id):
        if not self.app_id:
            raise Exception('no active application selected')
        if not rule_id:
            raise Exception('no active req rewrite rule selected')

        url = 'applications/http/{}/phases/rewrite/rules/{}?detail=1'
        return self.do_api('GET', url.format(self.app_id, rule_id))

    def get_all_rules(self, app_id=None):
        app_id = app_id or self.app_id
        if not app_id:
            raise Exception('no active application selected')

        return self.do_api('GET', AppRewriteRuleDetailUrl.format(app_id))

    def del_rule(self, rule_id):
        if not self.app_id:
            raise Exception('no active application selected')
        if not rule_id:
            raise Exception('no active upstream selected')

        url = 'applications/http/{}/phases/rewrite/rules/{}'
        return self.do_api('DELETE', url.format(self.app_id, rule_id))

    def get_global_actions_used_in_app(self, app_id=None):
        rules = self.get_all_rules(app_id)

        if not isinstance(rules, list):
            return []

        global_actions_rules = []
        for rule in rules:
            actions = rule.get('actions', [])
            for action in actions:
                global_action_id = action.get('global_action_id')
                if global_action_id:
                    global_actions_rules.append(global_action_id)

        return global_actions_rules

    def get_all_waf_rules(self, app_id=None):
        app_id = app_id or self.app_id
        if not app_id:
            raise Exception('no active application selected')

        rules = self.do_api('GET', AppRewriteRuleDetailUrl.format(app_id))

        waf_rules = []
        for rule in rules:
            if rule.get('waf', None):
                waf_rules.append(rule)

        return waf_rules

    def upload_favicon(self, name, favicon_content, gid=None):
        file_type = "image/vnd.microsoft.icon"

        encoded_data = base64.b64encode(utf8_encode(favicon_content))
        content = utf8_encode("data:$type;base64,") + encoded_data
        if not isinstance(content, str):
            content = content.decode('ascii')

        body = {
            'label': name,
            'content_file':
            [{
                'content': content,
                'type': file_type,
                'name': name + '.ico',
                'size': len(favicon_content)
            }]
        }

        if gid:
            body['gid'] = gid

        data = self.do_api('POST', 'files', body)

        if not self.request_ok():
            raise Exception('request failed.')

        file_id = data.get('id')
        if not file_id:
            raise Exception('file ID not found')
        if not isinstance(file_id, int):
            raise Exception('Bad file id obtained: ' + file_id)

        return file_id

    def del_favicon(self, file_id):
        if not file_id:
            raise Exception('no file selected')

        return self.do_api('DELETE', 'files/' + str(file_id))

    def create_static_file_directory(self, name, path="", label=None, gid=None):
        gids = ""
        if gid:
            gids = ",".join(str(id) for id in gid)

        url = "static/mkdir?name={}&gid={}&label={}&path={}".format(name, gids, label, path)

        data = self.do_api('POST', url)

        if not self.request_ok():
            raise Exception('request failed.')

        file_id = data.get('id')
        if not file_id:
            raise Exception('file ID not found')
        if not isinstance(file_id, int):
            raise Exception('Bad file id obtained: ' + file_id)

        return file_id

    def upload_static_file(self, filename, content, label=None, gid=None, path=""):
        gids = ""
        if gid:
            gids = ",".join(str(id) for id in gid)

        url = "static/file?gid={}&name={}&label={}&path={}".format(gids, filename, label, path)
        files = {"file": (filename, content)}

        data = self.do_api('POST', url, files=files)

        if not self.request_ok():
            raise Exception('request failed.')

        file_id = data.get('id')
        if not file_id:
            raise Exception('file ID not found')
        if not isinstance(file_id, int):
            raise Exception('Bad file id obtained: ' + file_id)

        return file_id

    def set_static_file(self, id, filename=None, content=None, label=None, gid=None, path=""):
        if id is None:
            raise Exception('no file selected')

        gids = ""
        if gid:
            gids = ",".join(str(id) for id in gid)

        url = "static/update?gid={}&name={}&label={}&path={}&id={}".format(gids, filename, label, path, id)

        files=None
        if content is not None:
            files = {"file": (filename, content)}

        return self.do_api('PUT', url, files=files)

    def get_static_file(self, file_id):
        if not file_id:
            raise Exception('no file selected')

        return self.do_api('GET', 'static/file/' + str(file_id))

    def get_static_file_content(self, file_id):
        if not file_id:
            raise Exception('no file selected')

        return self.do_request('GET', 'preview/file/' + str(file_id))

    def del_static_file(self, file_id):
        if not file_id:
            raise Exception('no file selected')

        return self.do_api('DELETE', 'static/delete?id=' + str(file_id))

    def get_all_static_files(self, path=""):
        return self.get_all(f"static/list?path={path}", True)

    def get_el(self, phase="req-rewrite"):
        if not self.app_id:
            raise Exception('no active application selected')

        api_phase = self.phases.get(phase)
        if not api_phase:
            raise Exception('unknown phase $phase')

        url = 'applications/http/{}/phases/{}/user_code'.format(
            self.app_id, api_phase)
        return self.do_api('GET', url)

    def new_el(self, phase, code, pre=False, post=False):
        if not self.app_id:
            raise Exception('no active application selected')
        if not phase:
            raise Exception('no phase arg specified')

        api_phase = self.phases.get(phase)
        if not api_phase:
            raise Exception('unknown phase $phase')

        if code is None:
            raise Exception('no code arg specified')

        if not pre and not post:
            raise Exception('neither pre nor post args are specified')
        postion = 'before' if pre else 'after'

        url = 'applications/http/{}/phases/{}/user_code'.format(
            self.app_id, api_phase)
        return self.do_api('PUT', url, {postion: code})

    def set_le_cert(self, **kwargs):
        kwargs['http_verb'] = 'POST'
        data = self.put_le_cert(**kwargs)

        if not self.request_ok():
            raise Exception('request failed.')

        cert_id = data.get('id')

        if not cert_id:
            raise Exception('cert id not found')
        if not isinstance(cert_id, int):
            raise Exception('Bad cert id obtained: ' + cert_id)

        return cert_id

    def set_cert_key(self, **kwargs):
        kwargs['http_verb'] = 'POST'
        data = self.put_cert_key(**kwargs)

        if not self.request_ok():
            raise Exception('request failed.')

        cert_id = data.get('id')

        if not cert_id:
            raise Exception('cert id not found')
        if not isinstance(cert_id, int):
            raise Exception('Bad cert id obtained: ' + cert_id)

        return cert_id

    def put_le_cert(self, cert_id=None, http_verb='PUT', domains=None, gid=None,
            resign=None, acme_provider=None, acme_csr_type=None, enabled=None):
        if not self.app_id:
            raise Exception('no active application selected')

        if not domains:
            raise Exception('no domains specified')

        url = AppSslCertUrl.format(self.app_id)
        if http_verb == 'PUT':
            url = url + str(cert_id)

        body = {'acme_host': domains}
        if gid:
            body['gid'] = gid
        # NB: this will trigger ACME to reissue the certificate
        if resign:
            body['id'] = cert_id

        if acme_provider is not None:
            body['acme_provider'] = acme_provider

        if acme_csr_type is not None:
            if acme_csr_type not in ['ec', 'rsa']:
                raise Exception(f"invalid acme_csr_type specified: {acme_csr_type}, expected 'ec' or 'rsa'")

            body['acme_csr_type'] = acme_csr_type

        if enabled is not None:
            if enabled not in [True, False]:
                raise Exception(f"invalid enabled specified: {enabled}, expected True or False")

            body['enabled'] = enabled

        return self.do_api(http_verb, url, body)

    def get_le_cert(self, cert_id=None):
        if not self.app_id:
            raise Exception('no active application selected')

        url = AppAcmeCertUrl + str(cert_id)

        return self.do_api('GET', url)

    def put_cert_key(self, cert_id=None, global_cert_id=None, http_verb='PUT',
                     cert=None, key=None, ca_chain=None, gid=None):
        if not self.app_id:
            raise Exception('no active application selected')

        if not global_cert_id:
            if not key:
                raise Exception('no key arg specified')
            if not cert and not ca_chain:
                raise Exception('neither cert nor ca_chain args specified')

        if http_verb == 'PUT' and not cert_id and not global_cert_id:
            raise Exception('no active cert selected')

        url = AppSslCertUrl.format(self.app_id)
        if http_verb == 'PUT':
            url = url + str(cert_id)

        if global_cert_id:
            body = {'global_cert': global_cert_id}
        else:
            body = {'priv_key': key}
            if cert:
                body['server_cert'] = cert
            if ca_chain:
                body['ca_chain'] = ca_chain

        if gid:
            body['gid'] = gid

        return self.do_api(http_verb, url, body)

    def get_cert_key(self, cert_id):
        if not self.app_id:
            raise Exception('no active application selected')
        if not cert_id:
            raise Exception('no active cert selected')

        url = 'applications/http/{}/phases/ssl_cert/certs/{}'.format(
            self.app_id, cert_id)
        return self.do_api('GET', url)

    def get_all_cert_keys(self, app_id=None):
        app_id = app_id or self.app_id
        if not app_id:
            raise Exception('no active application selected')

        return self.get_all(AppSslCertUrl.format(app_id))

    def del_cert_key(self, cert_id):
        if not self.app_id:
            raise Exception('no active application selected')
        if not cert_id:
            raise Exception('no active cert selected')

        url = 'applications/http/{}/phases/ssl_cert/certs/{}'.format(
            self.app_id, cert_id)
        return self.do_api('DELETE', url)

    def new_dns_app(self, **kwargs):
        kwargs['http_verb'] = 'POST'
        data = self.put_dns_app(**kwargs)

        if not self.request_ok():
            raise Exception('request failed.')

        dns_id = data.get('id')
        if not dns_id:
            raise Exception('DNS ID not found')
        if not isinstance(dns_id, int):
            raise Exception('Bad DNS ID obtained: ' + dns_id)

        self.dns_id = dns_id

        return dns_id

    def put_dns_app(self, http_verb='PUT', zone=None,
                    authority=None, soa_email=''):
        if http_verb == 'PUT' and not self.dns_id:
            raise Exception('no active DNS selected')

        if not zone:
            raise Exception('no zone arg specified')
        if not authority:
            raise Exception('no authority arg specified')

        # the ttl in authority will be modified,
        # so do a deep copy here to avoid affecting the original authority
        authority = copy.deepcopy(authority)

        for server in authority:
            domain = server.get('domain', None)
            if not domain:
                raise Exception('No domain field defined')
            ttl = server.get('ttl', '1 day')
            matched = re.match(r'^(\d+(?:\.\d+)?)\s+(\w+)$', ttl)
            if not matched:
                raise Exception('authority: bad ttl format: ' + ttl)
            server['ttl'] = int(matched.group(1))
            server['unit'] = matched.group(2)

        body = {
            'zone': zone,
            'nameserver': authority,
            'soa_email': soa_email
        }

        url = 'dns/'
        if http_verb == 'PUT':
            url = url + str(self.dns_id)

        return self.do_api(http_verb, url, body)

    def del_dns_app(self, dns_id):
        if not dns_id:
            raise Exception('no active DNS selected')

        return self.do_api('DELETE', 'dns/' + str(dns_id))

    def get_dns_app(self, dns_id):
        if not dns_id:
            raise Exception('no active DNS selected')
        return self.do_api('GET', 'dns/' + str(dns_id))

    def new_dns_record(self, **kwargs):
        kwargs['http_verb'] = 'POST'
        data = self.put_dns_record(**kwargs)

        if not self.request_ok():
            raise Exception('request failed.')

        record_id = data.get('id')
        if not record_id:
            raise Exception('record ID not found')
        if not isinstance(record_id, int):
            raise Exception('Bad record ID obtained: ' + record_id)

        return record_id

    def put_dns_record(self, record_id=None, http_verb='PUT', line=None, cidr=None,
                       sub_domain=None, record_type=None, ttl='5 min', ip=None,
                       text=None, domain=None, priority=1, gateway=None):
        if not self.dns_id:
            raise Exception('No dns id field defined')
        if not sub_domain:
            raise Exception('no sub_domain arg specified')
        if not record_type:
            raise Exception('no record_type arg specified')
        if cidr and line:
            raise Exception('cannot use line and cidr at the same time')
        if ip and gateway:
            raise Exception('cannot use ip and gateway at the same time')

        if http_verb == 'PUT' and not record_id:
            raise Exception('no active DNS record selected')

        matched = re.match(r'^(\d+(?:\.\d+)?)\s+(\w+)$', ttl)
        if not matched:
            raise Exception('dns record: bad ttl format: ' + ttl)
        ttl_v = int(matched.group(1))
        ttl_u = matched.group(2)

        body = {
            'sub_domain': sub_domain,
            'type': record_type,
            'ttl': ttl_v,
            'unit': ttl_u
        }
        if ip:
            body['ip'] = ip
        if gateway:
            body['gateway'] = gateway
        if text:
            body['text'] = text
        if domain:
            body['domain'] = domain
        if record_type == 'MX':
            body['priority'] = priority
        if cidr:
            body['cidr'] = cidr
        elif line:
            body['line'] = line
        else:
            body['line'] = 0

        url = 'dns/{}/record/'.format(self.dns_id)
        if http_verb == 'PUT':
            url = url + str(record_id)

        return self.do_api(http_verb, url, body)

    def del_dns_record(self, record_id):
        if not self.dns_id:
            raise Exception('no active DNS selected')
        if not record_id:
            raise Exception('no active DNS record selected')

        return self.do_api(
            'DELETE', 'dns/{}/record/{}'.format(self.dns_id, record_id))

    def get_dns_record(self, record_id):
        if not self.dns_id:
            raise Exception('no active DNS selected')
        if not record_id:
            raise Exception('no active DNS record selected')

        return self.do_api(
            'GET', 'dns/{}/record/{}'.format(self.dns_id, record_id))

    def get_dns_records(self, page=1, page_size=100):
        if not self.dns_id:
            raise Exception('no active DNS selected')

        url = 'dns/{}/record?page={}&page_size={}'.format(self.dns_id, page, page_size)
        return self.do_api('GET', url)

    def set_global_cert_key(self, **kwargs):
        kwargs['http_verb'] = 'POST'
        data = self.put_global_cert_key(**kwargs)

        if not self.request_ok():
            raise Exception('request failed.')

        cert_id = data.get('id')
        if not cert_id:
            raise Exception('cert id not found')
        if not isinstance(cert_id, int):
            raise Exception('Bad cert id obtained: ' + cert_id)

        return cert_id

    def put_global_cert_key(self, cert_id=None, http_verb='PUT', label=None,
                            cert=None, key=None, ca_chain=None):
        if not key:
            raise Exception('no key arg specified')
        if not cert and not ca_chain:
            raise Exception('neither cert nor ca_chain args specified')
        if http_verb == 'PUT' and not cert_id:
            raise Exception('no active cert selected')

        url = 'global/1/certs/'
        if http_verb == 'PUT':
            url = url + str(cert_id)

        body = {'priv_key': key}
        if cert:
            body['server_cert'] = cert
        if ca_chain:
            body['ca_chain'] = ca_chain
        if label:
            body['label'] = label

        return self.do_api(http_verb, url, body)

    def get_global_cert_key(self, cert_id):
        if not cert_id:
            raise Exception('no active cert selected')

        url = 'global/1/certs/' + str(cert_id)
        return self.do_api('GET', url)

    def del_global_cert_key(self, cert_id):
        if not cert_id:
            raise Exception('no active cert selected')

        url = 'global/1/certs/' + str(cert_id)
        return self.do_api('DELETE', url)

    def get_all_global_cert_key(self):
        data = self.do_api('GET', 'global/1/certs/')

        if not self.request_ok():
            raise Exception('request failed.')

        return data.get('data', None)

    def search_app(self, app_domain=None, upstream_ip=None,
                   upstream_domain=None, page=None, pagesize=None, type_list=None):

        np = 0
        if app_domain:
            np = np + 1

        if upstream_ip:
            np = np + 1

        if upstream_domain:
            np = np + 1

        if np == 0:
            raise Exception('no app domain or upstram ip or upstream name arg specified')

        if np > 1:
            raise Exception('only one of app domain or upstram ip or upstream name arg specified')

        url = None
        if app_domain:
            url = 'search/http?domain=' + app_domain
        elif upstream_ip:
            url = 'search/upstream?ip=' + upstream_ip
            if type_list is not None:
                if not isinstance(type_list, list):
                    raise Exception('bad type_list obtain')
                url = url + "&type=" + str.join(",", type_list)
        elif upstream_domain:
            url = 'search/upstream?name=' + upstream_domain
            if type_list is not None:
                if not isinstance(type_list, list):
                    raise Exception('bad type_list obtain')
                url = url + "&type=" + str.join(",", type_list)

        if url:
            if page:
                url = url + "&page=" + str(page)
            if pagesize:
                url = url + "&page_size=" + str(pagesize)

        if url:
            data = self.do_api('GET', url)
            return data['data']

        return None

    def search_upstream_by_ip(self, ip, page=None, pagesize=None):
        return self.search_app(upstream_ip=ip, page=page,
                               pagesize=pagesize, type_list=["http", "global"])

    def search_k8s_upstream_by_ip(self, ip, page=None, pagesize=None):
        return self.search_app(upstream_ip=ip, page=page,
                               pagesize=pagesize,
                               type_list=["k8s_http", "k8s_global"]);

    def search_upstream_by_name(self, name, page=None, pagesize=None):
        return self.search_app(upstream_domain=name, page=page,
                               pagesize=pagesize, type_list=["http", "global"])

    def search_k8s_upstream_by_name(self, name, page=None, pagesize=None):
        return self.search_app(upstream_domain=name, page=page,
                               pagesize=pagesize,
                               type_list=["k8s_http", "k8s_global"])

    def search_k8s_upstream(self, namespace=None, service=None, port=None,
                                page=None, pagesize=None, type_list=['k8s_http', 'k8s_global']):

        url = SearchK8sUpstreamUrl + '?'

        if type_list is None:
            type_list = ['k8s_http', 'k8s_global']

        if type_list is not None:
            if not isinstance(type_list, list):
                raise Exception('bad type_list obtain')

            if len(type_list) == 0:
                type_list = ['k8s_http', 'k8s_global']

            url = url + 'type=' + str.join(',', type_list)

        if namespace is not None:
            if not isinstance(namespace, str):
                raise Exception('bad namespace obtain')

            url = url + '&namespace=' + namespace

        if service is not None:
            if not isinstance(service, str):
                raise Exception('bad service obtain')

            url = url + '&service=' + service

        if port is not None:
            if not isinstance(port, int):
                raise Exception('bad port obtain')

            url = url + '&port=' + str(port)

        if page:
            url = url + "&page=" + str(page)
        if pagesize:
            url = url + "&page_size=" + str(pagesize)

        data = self.do_api('GET', url)

        if data is not None:
            return data.get('data', None)

        return None

    def search_k8s_upstream_history(self, page=None, pagesize=None, start_time=None, end_time=None):

        url = SearchK8sUpstreamHistoryUrl + '?'

        if page:
            url = url + "&page=" + str(page)
        if pagesize:
            url = url + "&page_size=" + str(pagesize)
        if start_time:
            url = url + "&start_time=" + str(start_time)
        if end_time:
            url = url + "&end_time=" + str(end_time)

        data = self.do_api('GET', url)

        if data is not None:
            return data.get('data', None)

        return None


    def search_http_app_by_keyword(self, keyword, page=None, pagesize=None):
        return self.search_app(app_domain=keyword, page=page,
                               pagesize=pagesize)

    def get_all_rules_by_app_domain(self, domain):
        if not domain:
            raise Exception('no app name arg specified')

        apps = self.search_app(app_domain=domain)
        for app in apps:
            for data in app['domains']:
                if domain == data['domain']:
                    app_id = app['id']
                    return self.get_all_rules(app_id)

        return None

    def get_all_rules_by_upstream_ip(self, ip):
        if not ip:
            raise Exception('no upstream ip arg specified')

        rules = {}
        apps = self.search_app(upstream_ip=ip)
        for app in apps:
            app_id = app['app']['id']
            rules[app_id] = self.get_all_rules(app_id)

        return rules

    def get_all_user_groups(self):
        return self.do_api('GET', UserGroupUrl)

    def add_global_user(self, name=None, pwd=None, gid=None, login_type=None, requires_password_change=None):
        if not name or not pwd or not gid:
            raise Exception('no name, pwd or gid arg specified')

        body = {
            'username': name,
            'password': pwd,
            'gid': gid
        }

        if login_type is not None:
            body['login_type'] = login_type

        if requires_password_change is not None:
            body['requires_password_change'] = requires_password_change

        return self.do_api('POST', 'user/', body)

    def search_global_user(self, name):
        if not name:
            raise Exception('no name arg specified')

        url = 'user/search?name=' + name
        return self.do_api('GET', url)

    def add_app_user(self, **kwargs):
        kwargs['http_verb'] = 'POST'
        data = self.put_app_user(**kwargs)

        if not self.request_ok():
            raise Exception('request failed.')

        if not data:
            return 'no "{}" user found'.format(kwargs.get('name'))

        user_id = data.get('id')
        if not isinstance(user_id, int):
            raise Exception('Bad user ID obtained: ' + user_id)

        return user_id

    def put_app_user(self, id=None, name=None, read=True,
                     write=True, release=False, http_verb='PUT',
                     dns_read=False, dns_write=False):
        if not self.app_id:
            raise Exception('no active application selected')
        if not name:
            raise Exception('no name arg specified')
        if http_verb == 'PUT' and not id:
            raise Exception('no active user selected')

        data = self.search_global_user(name)

        if not self.request_ok():
            raise Exception('request failed.')

        uid = data.get('id')
        if not uid:
            return None

        body = {
            'uid': uid, 'read': read,
            'write': write, 'release': release,
            'dns_read': dns_read, 'dns_write': dns_write}

        url = 'applications/http/{}/users/'.format(self.app_id)
        if http_verb == 'PUT':
            url = url + str(id)
            body['id'] = id

        return self.do_api(http_verb, url, body)

    def get_app_user(self, id=None, name=None, app_id=None, user_id=None):
        app_id = app_id or self.app_id
        if not app_id:
            raise Exception('no active application selected')
        if not name and not id and not user_id:
            raise Exception('no name or id arg specified')

        if name or user_id:
            users = self.get_all_app_users()
            if not users:
                return {}
            for user in users:
                if name and user.get('username') == name:
                    id = user.get('id')
                    break
                if user_id and user.get('uid') == user_id:
                    id = user.get('id')
                    break
        if not id:
            return {}

        url = 'applications/http/{}/users/{}'.format(self.app_id, id)
        return self.do_api('GET', url)

    def get_all_app_users(self, app_id=None):
        app_id = app_id or self.app_id
        if not app_id:
            raise Exception('no active application selected')

        url = 'applications/http/{}/users/'.format(self.app_id)

        response = self.do_api('GET', url)
        data = response.get('data')
        if not data:
            return {}

        return data

    def del_app_user(self, id=None, name=None, app_id=None, user_id=None):
        app_id = app_id or self.app_id
        if not app_id:
            raise Exception('no active application selected')
        if not name and not id and not user_id:
            raise Exception('no name or id arg specified')

        if name or user_id:
            users = self.get_all_app_users()
            if not users:
                return False
            for user in users:
                if name and user.get('username') == name:
                    id = user.get('id')
                    break
                if user_id and user.get('uid') == user_id:
                    id = user.get('id')
                    break
        if not id:
            return False

        url = 'applications/http/{}/users/{}'.format(self.app_id, id)
        return self.do_api('DELETE', url)

    def count_all_global_users(self):
        return self.count_all(GlobalUserUrl)

    def get_all_global_users(self, detail=False):
        users = self.get_all(GlobalUserUrl)
        if detail:
            return users

        ids = []
        for ele in users:
            ele_id = ele.get('id')
            if ele_id:
                ids.append(ele_id)

        return ids

    def get_all_apps(self, detail=False):
        apps = []
        if detail:
            apps = {}

        url = ApplicationUrl
        # page_size = 0: get all applications in one request
        data = self.get_all(url, False, page_size=0)
        for ele in data:
            ele_id = ele.get('id', None)
            if ele_id:
                if detail:
                    apps[ele_id] = {
                        'label': ele.get('name', ''),
                        'domains': ele.get('domains', {}),
                        'http_ports': ele.get('http_ports'),
                        'https_ports': ele.get('https_ports'),
                        'partitions': ele.get('partitions')}
                else:
                    apps.append(ele_id)

        return apps

    def add_user_for_all_apps(self, **kwargs):
        kwargs['http_verb'] = 'POST'
        return self.put_user_for_all_apps(**kwargs)

    def put_user_for_all_apps(self, id=None, name=None, read=True,
                              write=True, release=False, http_verb='PUT',
                              dns_read=False, dns_write=False):
        if not name:
            raise Exception('no name arg specified')
        if http_verb == 'PUT' and not id:
            raise Exception('no active user selected')

        data = self.search_global_user(name)

        if not self.request_ok():
            raise Exception('request failed.')

        uid = data.get('id')
        if not uid:
            return None

        body = {
            'uid': uid, 'read': read,
            'write': write, 'release': release,
            'dns_read': dns_read, 'dns_write': dns_write}

        all_apps = self.get_all_apps()
        for app_id in all_apps:
            url = 'applications/http/{}/users/'.format(app_id)
            if http_verb == 'PUT':
                url = url + str(id)
                body['id'] = id

            self.do_api(http_verb, url, body)

        return True

    def add_all_users_for_app(self, **kwargs):
        kwargs['http_verb'] = 'POST'
        return self.put_all_users_for_app(**kwargs)

    def put_all_users_for_app(
            self,
            read=True,
            write=True,
            release=False,
            http_verb='PUT',
            dns_read=False,
            dns_write=False):
        if not self.app_id:
            raise Exception('no active application selected')

        users = self.get_all_global_users()
        for user_id in users:
            url = 'applications/http/{}/users/'.format(self.app_id)
            body = {
                'uid': user_id,
                'read': read,
                'write': write,
                'release': release,
                'dns_read': dns_read,
                'dns_write': dns_write}
            # if user already exist in this app
            # if http_verb == 'POST' and self.get_app_user(user_id = user_id):
            #     continue
            self.do_api(http_verb, url, body)

        return True

    def new_global_rule(self, **kwargs):
        kwargs['http_verb'] = 'POST'
        data = self.put_global_rule(**kwargs)

        if not self.request_ok():
            raise Exception('request failed.')

        rule_id = data.get('id')
        if not rule_id:
            raise Exception('rule id not found')
        if not isinstance(rule_id, int):
            raise Exception('Bad rule id obtained: ' + rule_id)

        return rule_id

    def put_global_rule(self, rule_id=None, http_verb='PUT',
                        condition=None, conseq=None, gid=None):
        if http_verb == 'PUT' and not rule_id:
            raise Exception('no active rule selected')

        if not conseq:
            raise Exception('No conseq field specified')

        sections = [
            { 'value': condition, 'handler': process_rule_cond, 'key': 'conditions'},
            { 'value': conseq, 'handler': process_conseq, 'key': 'actions'},
        ]

        body = {}
        for s in sections:
            value = s['value']
            key = s['key']
            handler = s['handler']

            if value == OFF:
                body[key] = None
            elif value is not None:
                spec = handler(value)
                if spec:
                    body[key] = spec

        if gid:
            body['gid'] = gid

        url = 'global/1/rewrite/rules/'
        if http_verb == 'PUT':
            url = url + str(rule_id)

        return self.do_api(http_verb, url, body)

    def get_global_rule(self, rule_id):
        if not rule_id:
            raise Exception('no global rule id selected')

        return self.do_api(
            'GET', 'global/1/rewrite/rules/{}?detail=1'.format(rule_id))

    def get_all_global_rules(self):
        return self.do_api('GET', GlobalRewriteRuleUrl)

    def del_global_rule(self, rule_id):
        if not rule_id:
            raise Exception('no global rule id specified')

        return self.do_api(
            'DELETE',
            'global/1/rewrite/rules/{}'.format(rule_id))

    def new_global_var(self, **kwargs):
        kwargs['http_verb'] = 'POST'
        data = self.put_global_var(**kwargs)

        if not self.request_ok():
            raise Exception('request failed.')

        var_id = data.get('id')
        if not var_id:
            raise Exception('var id not found')
        if not isinstance(var_id, int):
            raise Exception('Bad var id obtained: ' + var_id)

        return var_id

    def put_global_var(self, var_id=None, http_verb='PUT',
                       name=None, var_type=None, default=None, values=None, gid=None):
        if http_verb == 'PUT' and not var_id:
            raise Exception('no active var selected')

        if not name:
            raise Exception('No name field specified')
        if not var_type:
            raise Exception('No type field specified')
        if not default:
            raise Exception('No default field specified')

        url = 'global/1/variables/'
        if http_verb == 'PUT':
            url = url + str(var_id)

        body = {'name': name, 'type': var_type, 'default': default}
        if values:
            body['values'] = values
        if gid:
            body['gid'] = gid

        return self.do_api(http_verb, url, body)

    def get_global_var(self, var_id):
        if not var_id:
            raise Exception('no global var id selected')

        return self.do_api('GET', 'global/1/variables/{}'.format(var_id))

    def get_all_global_vars(self):
        url = 'global/1/variables'
        variables = self.get_all(url)

        if not self.request_ok():
            raise Exception('request failed.')

        return variables

    def del_global_var(self, var_id):
        if not var_id:
            raise Exception('no global var id specified')

        return self.do_api('DELETE', 'global/1/variables/{}'.format(var_id))

    def get_global_ngx_config(self, detail=False):
        url = 'global/1/ngx'
        if detail == True:
            url = 'global/1/ngx?detail=1'

        return self.do_api('GET', url)

    def set_global_ngx_config(self, config):
        url = 'global/1/ngx'
        return self.do_api('PUT', url, config)

    def get_partition_ngx_config(self, partition_id, detail=False):
        url = 'partitions/{}/ngx'.format(partition_id)
        if detail == True:
            url = 'partitions/{}/ngx?detail=1'.format(partition_id)

        return self.do_api('GET', url)

    def set_partition_ngx_config(self, config, partition_id):
        url = 'partitions/{}/ngx'.format(partition_id)
        ok = self.do_api('PUT', url, config)
        if not ok:
            raise Exception(f'update partition general config failed: {self.__msg}')

        return ok

    def get_global_misc_config(self):
        url = 'global/1/misc'
        return self.do_api('GET', url)

    def set_global_misc_config(self, config):
        url = 'global/1/misc'
        return self.do_api('PUT', url, config)

    def get_request_id_status(self):
        url = 'global/1/misc'
        data = self.do_api('GET', url)

        if not self.request_ok():
            raise Exception('request failed.')

        return data.get('enabled_req_id')

    def enable_request_id(self):
        url = 'global/1/misc'
        return self.do_api('PUT', url, {'enabled_req_id': True})

    def disable_request_id(self):
        url = 'global/1/misc'
        return self.do_api('PUT', url, {'enabled_req_id': False})

    def new_global_waf_rule(self, **kwargs):
        kwargs['http_verb'] = 'POST'
        data = self.put_global_waf_rule(**kwargs)

        if not self.request_ok():
            raise Exception('request failed.')

        rule_id = data.get('id')
        if not rule_id:
            raise Exception('waf rule id not found')
        if not isinstance(rule_id, int):
            raise Exception('Bad waf rule id obtained: ' + rule_id)

        return rule_id

    def put_global_waf_rule(
            self,
            rule_id=None,
            http_verb='PUT',
            name=None,
            code=None):
        if http_verb == 'PUT' and not rule_id:
            raise Exception('no active waf rule selected')

        if not name:
            raise Exception('No name field specified')
        if not code:
            raise Exception('No code field specified')

        url = 'global/1/waf/rule_sets/'
        if http_verb == 'PUT':
            url = url + str(rule_id)

        body = {'name': name, 'code': code}

        return self.do_api(http_verb, url, body)

    def get_global_waf_rule(self, rule_id):
        if not rule_id:
            raise Exception('no global waf rule id selected')

        return self.do_api('GET', 'global/1/waf/rule_sets/{}'.format(rule_id))

    def del_global_waf_rule(self, rule_id):
        if not rule_id:
            raise Exception('no global waf rule id selected')

        return self.do_api(
            'DELETE',
            'global/1/waf/rule_sets/{}'.format(rule_id))

    def get_all_global_waf_rules(self, detail=False):
        rules = self.get_all(GlobalWafRuleUrl)

        if not detail:
            for rule in rules:
                rule.pop('code', None)

        return rules

    def new_global_action(self, **kwargs):
        kwargs['http_verb'] = 'POST'
        data = self.put_global_action(**kwargs)

        if not self.request_ok():
            raise Exception('request failed.')

        action_id = data.get('id')
        if not action_id:
            raise Exception('action id not found')
        if not isinstance(action_id, int):
            raise Exception('Bad action id obtained: ' + action_id)

        return action_id

    def put_global_action(self, name=None, action_id=None, http_verb='PUT',
                          condition=None, conseq=None, gid=None):
        if http_verb == 'PUT' and not action_id:
            raise Exception('no active action selected')

        if not name:
            raise Exception('No name field specified')

        if not conseq:
            raise Exception('No conseq field specified')

        sections = [
            { 'value': condition, 'handler': process_rule_cond, 'key': 'conditions'},
            { 'value': conseq, 'handler': process_conseq, 'key': 'actions'},
        ]

        body = {'name': name}
        for s in sections:
            value = s['value']
            key = s['key']
            handler = s['handler']

            if value == OFF:
                body[key] = None
            elif value is not None:
                spec = handler(value)
                if spec:
                    body[key] = spec

        if gid:
            body['gid'] = gid

        url = 'global/1/user_defined_actions/'
        if http_verb == 'PUT':
            url = url + str(action_id)

        return self.do_api(http_verb, url, body)

    def get_global_action(self, action_id):
        if not action_id:
            raise Exception('no global action id selected')

        return self.do_api(
            'GET', 'global/1/user_defined_actions/{}?detail=1'
            .format(action_id))

    def count_global_actions(self):
        return self.count_all(GlobalUserDefinedActionUrl)

    def get_all_global_actions(self, detail=False):
        url = GlobalUserDefinedActionUrl
        has_uri_arg = False
        if detail:
            url += '?detail=1'
            has_uri_arg = True

        return self.get_all(url, has_uri_arg=has_uri_arg)

    def get_all_global_el_user_code(self):
        global_actions = self.get_all_global_actions()

        if not isinstance(global_actions, list):
            return []

        el_user_code_actions = []
        for global_action in global_actions:
            if global_action.get('user_code'):
                el_user_code_actions.append(global_action)

        return el_user_code_actions

    def get_global_action_by_name(self, name=None):
        if not name:
            raise Exception('no action name specified.')

        all_global_actions = self.get_all_global_actions()

        if not isinstance(all_global_actions, list):
            return None

        global_action_id = None
        for global_action in all_global_actions:
            if global_action.get('name') == name:
                global_action_id = global_action.get('id')

        return global_action_id

    def del_global_action(self, action_id):
        if not action_id:
            raise Exception('no global action id specified')

        return self.do_api(
            'DELETE',
            'global/1/user_defined_actions/{}'.format(action_id))

    def new_user_var(self, **kwargs):
        kwargs['http_verb'] = 'POST'
        data = self.put_user_var(**kwargs)

        if not self.request_ok():
            raise Exception('request failed.')

        var_id = data.get('id')
        if not var_id:
            raise Exception('var id not found')
        if not isinstance(var_id, int):
            raise Exception('Bad var id obtained: ' + var_id)

        return var_id

    def put_user_var(self, var_id=None, http_verb='PUT',
                     name=None, var_type=None, default=None, values=None):
        if not self.app_id:
            raise Exception('no active application selected')
        if http_verb == 'PUT' and not var_id:
            raise Exception('no active var selected')

        if not name:
            raise Exception('No name field specified')
        if not var_type:
            raise Exception('No type field specified')
        if not default:
            raise Exception('No default field specified')

        if var_type == 'enum':
            if values is None:
                raise Exception('No values field specified for enum type')

            if not isinstance(values, list):
                raise Exception('values field must be a list')

            if default not in values:
                raise Exception('default value not in enum values')

        url = 'applications/http/{}/variables/'.format(self.app_id)
        if http_verb == 'PUT':
            url = url + str(var_id)

        body = {'name': name, 'type': var_type, 'default': default}

        if values is not None:
            body['values'] = values

        return self.do_api(http_verb, url, body)

    def get_user_var(self, var_id):
        if not self.app_id:
            raise Exception('no active application selected')
        if not var_id:
            raise Exception('no user var id selected')

        return self.do_api(
            'GET', 'applications/http/{}/variables/{}'.format(self.app_id, var_id))

    def get_all_user_vars(self):
        if not self.app_id:
            raise Exception('no active application selected')

        url = 'applications/http/{}/variables/'.format(self.app_id)

        return self.get_all(url)

    def del_user_var(self, var_id):
        if not self.app_id:
            raise Exception('no active application selected')
        if not var_id:
            raise Exception('no user var id specified')

        return self.do_api(
            'DELETE', 'applications/http/{}/variables/{}'
            .format(self.app_id, var_id))

    def node_sync_status(self):
        node_sync_status_result = {}

        gateways = self.do_api('GET', 'status/report')

        for k, gateway_nodes in gateways.items():
            # this key will exist when the log server is unavailable
            if k == 'err':
                continue
            nodes = gateway_nodes.get('nodes')
            node_sync_status_result.update(nodes)

        return node_sync_status_result

    def new_global_upstream(self, **kwargs):
        kwargs['http_verb'] = 'POST'
        data = self.put_global_upstream(**kwargs)

        if not self.request_ok():
            raise Exception('request failed.')

        up_id = data.get('id')
        if not up_id:
            raise Exception('upstream ID not found')
        if not isinstance(up_id, int):
            raise Exception('Bad upstream ID obtained: ' + up_id)

        return up_id

    def put_global_upstream(self, up_id=None, http_verb='PUT', name=None,
                            servers=None, health_checker=None, ssl=False,
                            gid=None, disable_ssl_verify=None):
        if http_verb == 'PUT' and not up_id:
            raise Exception('no active upstream selected')

        if not name:
            raise Exception('no name arg specified')
        if not servers:
            raise Exception('no servers arg specified')

        i = 0
        node_specs = []
        for server in servers:
            i += 1

            domain = server.get('domain')
            server_ip = server.get('ip')

            if not domain and not server_ip:
                raise Exception(
                    'No domain or ip field specified for '
                    'the {}-th upstream server'.format(str(i)))

            port = server.get('port')
            if not port:
                raise Exception(
                    'No port field specified for '
                    'the {}-th upstream server'.format(str(i)))

            weight = server.get('weight', 1)
            status = server.get('status', 1)
            node = {
                'domain': domain,
                'ip': server_ip,
                'port': port,
                'weight': weight,
                'status': status
            }
            node_id = server.get('id')
            if node_id:
                node['id'] = node_id

            node_specs.append(node)

        body = {
            'name': name,
            'ssl': ssl,
            'disable_ssl_verify': disable_ssl_verify,
            'nodes': node_specs
        }

        if health_checker:
            health_checker['concurrency'] = 5
            body['enable_checker'] = True
            body['checker'] = health_checker
        else:
            body['enable_checker'] = False

        if gid:
            body['gid'] = gid

        url = GlobalUpstreamUrl + '/'
        if http_verb == 'PUT':
            url = url + str(up_id)

        return self.do_api(http_verb, url, body)

    def get_global_upstream(self, up_id):
        if not up_id:
            raise Exception('no active upstream selected')

        return self.do_api(
            'GET', 'global/1/upstreams/{}?detail=1'.format(up_id))

    def get_all_global_upstreams(self, detail=True):
        if detail:
            return self.get_all(GlobalUpstreamUrl + '?detail=1', True)

        return self.get_all(GlobalUpstreamUrl)

    def del_global_upstream(self, up_id):
        if not up_id:
            raise Exception('no active upstream selected')

        return self.do_api('DELETE', 'global/1/upstreams/{}'.format(up_id))

    def new_global_k8s_upstream(self, **kwargs):
        kwargs['http_verb'] = 'POST'
        data = self.put_global_k8s_upstream(**kwargs)

        if not self.request_ok():
            raise Exception('request failed.')

        up_id = data.get('id')
        if not up_id:
            raise Exception('k8s upstream ID not found')
        if not isinstance(up_id, int):
            raise Exception('Bad k8s upstream ID obtained: ' + up_id)

        return up_id

    def put_global_k8s_upstream(self, up_id=None, http_verb='PUT', name=None,
                                k8s_services=None, health_checker=None, ssl=False,
                                gid=None, disable_ssl_verify=None, nodes=None):
        if http_verb == 'PUT' and not up_id:
            raise Exception('no active k8s upstream selected')

        if not name:
            raise Exception('no name arg specified')
        if not k8s_services:
            raise Exception('no k8s_services arg specified')

        i = 0

        for service in k8s_services:
            i += 1

            k8s = service.get('k8s')
            k8s_namespace = service.get('k8s_namespace')
            k8s_service = service.get('k8s_service')
            k8s_service_port = service.get('k8s_service_port')

            if not k8s:
                raise Exception(
                    'No k8s field specified for '
                    'for the {}-th upstream k8s_services'.format(str(i)))

            if not isinstance(k8s, int):
                raise Exception(
                    'Bad k8s field type for '
                    'for the {}-th upstream k8s_services'.format(str(i)))

            if not k8s_namespace:
                raise Exception(
                    'No k8s_namespace field specified for '
                    'for the {}-th upstream k8s_services'.format(str(i)))

            if not k8s_service:
                raise Exception(
                    'No k8s_service field specified for '
                    'for the {}-th upstream k8s_services'.format(str(i)))

            if not k8s_service_port:
                raise Exception(
                    'No k8s_service_port field specified for '
                    'for the {}-th upstream k8s_services'.format(str(i)))

            if not isinstance(k8s_service_port, int):
                raise Exception(
                    'Bad k8s_service_port field type for '
                    'for the {}-th upstream k8s_services'.format(str(i)))

        body = {
            'name': name,
            'ssl': ssl,
            'disable_ssl_verify': disable_ssl_verify,
            'k8s_services': k8s_services,
            'is_k8s_service': True
        }

        if health_checker:
            health_checker['concurrency'] = 5
            body['enable_checker'] = True
            body['checker'] = health_checker
        else:
            body['enable_checker'] = False

        if gid:
            body['gid'] = gid


        if nodes is not None:
            if not isinstance(nodes, list):
               raise Exception('The type of nodes should be list')

            for node in nodes:
                i += 1
                ip = node.get("ip")
                port = node.get("port")
                weight = node.get("weight")

                if not ip:
                    raise Exception(
                        'No ip field specified for '
                        'for the {}-th upstream nodes'.format(str(i)))

                if not port:
                    raise Exception(
                        'No port field specified for '
                        'for the {}-th upstream nodes'.format(str(i)))

                if not isinstance(port, int):
                    raise Exception(
                        'Bad port field type for '
                        'for the {}-th upstream nodes'.format(str(i)))

                if not weight:
                    raise Exception(
                        'No weight field specified for '
                        'for the {}-th upstream nodes'.format(str(i)))

                if not isinstance(weight, int):
                    raise Exception(
                        'Bad weight field type for '
                        'for the {}-th upstream nodes'.format(str(i)))

            body['nodes'] = nodes

        url = GlobalK8sUpstreamUrl + '/'
        if http_verb == 'PUT':
            url = url + str(up_id)

        return self.do_api(http_verb, url, body)

    def get_global_k8s_upstream(self, up_id):
        if not up_id:
            raise Exception('no active k8s upstream selected')

        return self.do_api(
            'GET', 'global/1/k8s_upstreams/{}?detail=1'.format(up_id))

    def get_all_global_k8s_upstreams(self, detail=False):
        if detail:
            return self.get_all(GlobalK8sUpstreamUrl + '?detail=1', True)

        return self.get_all(GlobalK8sUpstreamUrl)

    def del_global_k8s_upstream(self, up_id):
        if not up_id:
            raise Exception('no active upstream selected')

        return self.do_api('DELETE', 'global/1/k8s_upstreams/{}'.format(up_id))

    def new_global_dymetrics(self, name=None, note=None, interval=60, sql=None):
        data = self.put_global_dymetrics(name=name, note=note,
                                         interval=interval, sql=sql,
                                         http_verb="POST")
        return data.get('id')

    def put_global_dymetrics(self, id=None, name=None, note=None, interval=60, sql=None, http_verb="PUT"):
        if http_verb == "PUT" and id is None:
            raise Exception('no id arg specified')

        if name is None:
            raise Exception('no name arg specified')

        if http_verb == "POST" and sql is None:
            raise Exception('no sql arg specified')

        if http_verb == "PUT" and sql:
            raise Exception('can not modify dynamic metrics SQL')

        if http_verb == "PUT":
            data = self.get_global_dymetrics(id)
            sql = data['sql']

        body = {
            "name": name,
            "interval": int(interval),
            "note": note,
            "sql": sql
        }

        url = GlobalDymetricsUrl
        if http_verb == 'PUT':
            url = "{}/{}".format(url, str(id))

        return self.do_api(http_verb, url, body)

    def del_global_dymetrics(self, id):
        url = "{}/{}".format(GlobalDymetricsUrl, str(id))
        return self.do_api("DELETE", url)

    def get_global_dymetrics(self, id):
        url = "{}/{}".format(GlobalDymetricsUrl, str(id))
        data = self.do_api("GET", url)
        if data and 'lua_src' in data:
            del data['lua_src']

        return data

    def get_all_global_dymetrics(self):
        return self.get_all(GlobalDymetricsUrl)

    def get_global_dymetrics_data(self, id, chart_type='line',
                                  start_time=None, end_time=None,
                                  node_id=None, limit=None):
        if start_time is None:
            start_time = int(time.time() - 1800)

        if end_time is None:
            end_time = int(time.time())

        params = [
            'type=global',
            f"id={id}",
        ]

        if node_id:
            params.append(f"node_id={node_id}")

        if chart_type:
            params.append(f"chart_type={chart_type}")

        if start_time:
            params.append(f"start_time={start_time}")

        if end_time:
            params.append(f"end_time={end_time}")

        if limit:
            params.append(f"limit={limit}")

        url = "{}?{}".format(DymetricsDataUrl, "&".join(params))
        return self.do_api("GET", url)

    def put_app_dymetrics(self, app_id=None, id=None, name=None, note=None, interval=60, sql=None, http_verb="PUT"):
        if not app_id:
            raise Exception('no active application selected')

        if http_verb == "PUT" and id is None:
            raise Exception('no id arg specified')

        if name is None:
            raise Exception('no name arg specified')

        if http_verb == "POST" and sql is None:
            raise Exception('no sql arg specified')

        if http_verb == "PUT" and sql:
            raise Exception('can not modify dymetrics SQL')

        if http_verb == "PUT":
            data = self.get_app_dymetrics(app_id, id)
            sql = data['sql']

        body = {
            "name": name,
            "note": note,
            "interval": int(interval),
            "sql": sql,
        }

        url = AppDymetricsUrl.format(app_id)
        if http_verb == 'PUT':
            url = "{}/{}".format(url, str(id))

        return self.do_api(http_verb, url, body)

    def new_app_dymetrics(self, app_id=None, name=None, note=None, interval=60, sql=None):
        data = self.put_app_dymetrics(app_id=app_id, name=name, note=note,
                                      interval=interval, sql=sql,
                                      http_verb="POST")
        return data.get('id')

    def del_app_dymetrics(self, app_id, id):
        if not app_id:
            raise Exception('no active application selected')

        url = AppDymetricsUrl.format(app_id)
        url = "{}/{}".format(url, str(id))
        return self.do_api("DELETE", url)

    def get_app_dymetrics(self, app_id, id):
        if not app_id:
            raise Exception('no active application selected')

        url = AppDymetricsUrl.format(app_id)
        url = "{}/{}".format(url, str(id))
        data = self.do_api("GET", url)
        if data and 'lua_src' in data:
            del data['lua_src']

        return data

    def get_all_app_dymetrics(self, app_id):
        if not app_id:
            raise Exception('no active application selected')

        url = AppDymetricsUrl.format(app_id)
        return self.get_all(url)

    def get_app_dymetrics_data(self, app_id, id, chart_type='line',
                               start_time=None, end_time=None,
                               node_id=None, limit=None):
        if not app_id:
            raise Exception('no active application selected')

        if start_time is None:
            start_time = int(time.time() - 1800)

        if end_time is None:
            end_time = int(time.time())

        metric_id = "{}_{}".format(app_id, id)
        params = [
            'type=app',
            f"id={metric_id}",
        ]

        if node_id:
            params.append(f"node_id={node_id}")

        if chart_type:
            params.append(f"chart_type={chart_type}")

        if start_time:
            params.append(f"start_time={start_time}")

        if end_time:
            params.append(f"end_time={end_time}")

        if limit:
            params.append(f"limit={limit}")

        url = "{}?{}".format(DymetricsDataUrl, "&".join(params))
        return self.do_api("GET", url)

    def get_app_metrics(self, id, start_time=None, end_time=None):
        if start_time is None:
            start_time = int(time.time() - 1800)

        if end_time is None:
            end_time = int(time.time())

        url = "{}/{}?start_time={}&end_time={}".format(
            AppMetricsUrl, id, start_time, end_time)

        return self.do_api("GET", url)

    def new_global_ip_list(self, **kwargs):
        kwargs['http_verb'] = 'POST'
        data = self.put_global_ip_list(**kwargs)

        if not self.request_ok():
            raise Exception('request failed')

        rule_id = data.get('id')
        if not rule_id:
            raise Exception('rule id not found')
        if not isinstance(rule_id, int):
            raise Exception('Bad rule id obtained: ' + rule_id)

        return rule_id

    def put_global_ip_list(self, rule_id=None, http_verb='PUT',
                           name=None, type='ipv4', items=None):
        if http_verb == 'PUT' and not rule_id:
            raise Exception('no active rule selected')

        if http_verb == 'POST' and not name:
            raise Exception('no name arg specified')

        body = {'type': type}

        if name:
            body['name'] = name
        if items is not None:
            body['items'] = items

        if self.is_version_at_least(EDGE_VERSION_24_09_16):
            url = GlobalIPListUrlV2
        else:
            url = GlobalIPListUrl

        if http_verb == 'PUT':
            url = f"{url}/{rule_id}"

        return self.do_api(http_verb, url, body)

    def get_global_ip_list_items(self, ip_list_id, page_size=10000):
        url = GlobalIPListItemsUrl.format(ip_list_id)
        return self.get_all(url, page_size=page_size)

    def get_global_ip_list(self, rule_id, detail=True):
        if not rule_id:
            raise Exception('no active IP list selected')

        url = f"{GlobalIPListUrl}/{rule_id}"
        ge_version_240916 = self.is_version_at_least(EDGE_VERSION_24_09_16)
        if detail is True and ge_version_240916 is False:
            url = f"{url}?detail=1"

        data = self.do_api('GET', url)

        if detail is True:
            if ge_version_240916 is True:
                if 'items' not in data:
                    data['items'] = self.get_global_ip_list_items(rule_id)
        else:
            if 'items' in data:
                del data['items']

        return data

    def get_all_global_ip_lists(self, detail=True):
        has_uri_args = False
        url = GlobalIPListUrl
        ge_version_240916 = self.is_version_at_least(EDGE_VERSION_24_09_16)
        if detail is True and ge_version_240916 is False:
            url = f"{url}?detail=1"
            has_uri_args = True

        ge_version_240906 = self.is_version_at_least(EDGE_VERSION_24_09_06)
        if ge_version_240906 is True:
            ip_lists = self.get_all(url, has_uri_args)
        else:
            ip_lists = self.do_api('GET', url)

        if detail is True:
            if ge_version_240916 is True:
                for ip_list in ip_lists:
                    if 'items' not in ip_list:
                        ip_list['items'] = self.get_global_ip_list_items(ip_list['id'])
        else:
            for ip_list in ip_lists:
                if 'items' in ip_list:
                    del ip_list['items']

        return ip_lists

    def del_global_ip_list(self, rule_id=None):
        if not rule_id:
            raise Exception('no active ip list selected')

        return self.do_api('DELETE', '{}/{}'.format(GlobalIPListUrl, rule_id))

    def mod_global_ip_list(self, rule_id=None, http_verb='PUT',
                           items=None, action=None, remove_expired=False):
        body = {'items': items, 'remove_expired': remove_expired}

        url = ModGlobalIPListUrl.format(rule_id, action)

        return self.do_api(http_verb, url, body)

    def append_to_global_ip_list(self, rule_id=None, items=None, remove_expired=False):
        if not rule_id:
            raise Exception('no active ip list selected')

        return self.mod_global_ip_list(rule_id=rule_id, items=items,
                                       action='append', remove_expired=remove_expired)

    def remove_from_global_ip_list(self, rule_id=None, items=None):
        if not rule_id:
            raise Exception('no active ip list selected')

        return self.mod_global_ip_list(rule_id=rule_id, items=items,
                                       action='remove')

    def new_waf_whitelist(self, **kwargs):
        if not self.app_id:
            raise Exception('no active application selected')

        kwargs['http_verb'] = 'POST'
        data = self.put_waf_whitelist(**kwargs)

        if not self.request_ok():
            raise Exception('request failed.')

        whitelist_id = data.get('id')
        if not whitelist_id:
            raise Exception('whitelist id not found')
        if not isinstance(whitelist_id, int):
            raise Exception('Bad whitelist id obtained: ' + whitelist_id)

        return whitelist_id

    def put_waf_whitelist(self, whitelist_id=None, http_verb='PUT',
                          condition=None, rule_sets=None, rules=None):
        if not self.app_id:
            raise Exception('no active application selected')

        if http_verb == 'PUT' and not whitelist_id:
            raise Exception('no active whitelist selected')

        if not condition:
            raise Exception('condition not found')
        if not rule_sets and not rules:
            raise Exception('rule_sets and rules not found')

        if rule_sets is not None and not isinstance(rule_sets, list):
            raise Exception(
                'Bad rule_sets field value type: ' + str(type(rule_sets)))

        cond_specs = process_rule_cond(condition)

        body = {
            'conditions': cond_specs
        }

        if rules is not None:
            body['rule_sets'] = rule_sets

        if rules is not None:
            body['rules'] = rules

        url = 'applications/http/{}/waf_whitelist/'.format(self.app_id)
        if http_verb == 'PUT':
            url = url + str(whitelist_id)

        return self.do_api(http_verb, url, body)

    def get_waf_whitelist(self, whitelist_id):
        if not self.app_id:
            raise Exception('no active application selected')

        if not whitelist_id:
            raise Exception('no whitelist id selected')

        return self.do_api(
            'GET', 'applications/http/{}/waf_whitelist/{}?detail=1'
            .format(self.app_id, whitelist_id))

    def get_all_waf_whitelists(self):
        if not self.app_id:
            raise Exception('no active application selected')

        return self.get_all(AppWafWhiteListUrl.format(self.app_id), True)

    def del_waf_whitelist(self, whitelist_id):
        if not self.app_id:
            raise Exception('no active application selected')

        if not whitelist_id:
            raise Exception('no whitelist id specified')

        return self.do_api(
            'DELETE', 'applications/http/{}/waf_whitelist/{}?detail=1'
            .format(self.app_id, whitelist_id))

    def get_healthcheck_status(self, node_id, page=1, page_size=1000):
        if not node_id:
            raise Exception('no node id specified')

        data = self.do_api(
            'GET',
            'log_server/health/?page={}&page_size={}&fetch_by=node&node_id={}'
            .format(page, page_size,node_id))

        if not self.request_ok():
            raise Exception('request failed.')

        return data

    def get_upstream_healthcheck_status(self, app_id, upstream_id, app_type="http"):
        if not app_id and app_id != 0:
            raise Exception('no application id specified')

        if not upstream_id:
            raise Exception('no upstream id specified')

        types = ["http", "stream", "k8s_http", "k8s_stream"]
        if app_type not in types:
            raise Exception('unsupported app type: {}, expected {}'.format(app_type, types))

        data = self.do_api(
            'GET',
            'log_server/health/{}?upstream_id={}&app_type={}'
            .format(app_id, upstream_id, app_type))

        if not self.request_ok():
            raise Exception('request failed.')

        return data

    def get_global_upstream_healthcheck_status(self, upstream_id, app_type="http"):
        return self.get_upstream_healthcheck_status(app_id=0, upstream_id=upstream_id, app_type=app_type)

    def new_cluster_group(self, group_name):
        data = self.put_cluster_group(group_name=group_name, http_verb='POST')

        if not self.request_ok():
            raise Exception('request failed.')

        group_id = data.get('id')
        if not group_id:
            raise Exception('group ID not found')
        if not isinstance(group_id, int):
            raise Exception('Bad group ID obtained: ' + group_id)

        return group_id

    def put_cluster_group(
            self,
            group_id=None,
            group_name=None,
            http_verb='PUT'):
        if http_verb == 'PUT' and not group_id:
            raise Exception('no active group selected')

        if not group_name:
            raise Exception('no group_name arg specified')

        body = {
            'name': group_name
        }

        url = 'partitions/'
        if http_verb == 'PUT':
            url = url + str(group_id)

        return self.do_api(http_verb, url, body)

    def get_cluster_group(self, group_id):
        if not group_id:
            raise Exception('no active group selected')

        return self.do_api('GET', 'partitions/' + str(group_id))

    def get_all_cluster_groups(self):
        return self.do_api('GET', PartitionsUrl)

    def del_cluster_group(self, group_id):
        if not group_id:
            raise Exception('no active group selected')

        return self.do_api('DELETE', 'partitions/' + str(group_id))

    def new_cache_purge_task(self, condition=None):
        if not self.app_id:
            raise Exception('no active application selected')

        if not condition:
            raise Exception('No condition field specified')

        cond_specs = process_rule_cond(condition)
        body = {}
        body['conditions'] = cond_specs
        body['type'] = 'conditional'

        data = self.do_api(
            'POST', 'applications/http/{}/purge'.format(self.app_id), body)

        if not self.request_ok():
            raise Exception('request failed.')

        task_id = data.get('id')
        if not task_id:
            raise Exception('task id not found')
        if not isinstance(task_id, int):
            raise Exception('Bad task id obtained: ' + task_id)

        return task_id

    def get_cache_purge_task(self, task_id):
        if not self.app_id:
            raise Exception('no active application selected')
        if not task_id:
            raise Exception('no active task rule selected')

        url = 'applications/http/{}/purge/{}?detail=1'
        return self.do_api('GET', url.format(self.app_id, task_id))

    def get_all_cache_purge_tasks(self, app_id=None):
        app_id = app_id or self.app_id
        if not app_id:
            raise Exception('no active application selected')

        return self.get_all(AppCachePurgeUrl.format(app_id), True)

    def del_cache_purge_task(self, task_id):
        if not self.app_id:
            raise Exception('no active application selected')
        if not task_id:
            raise Exception('no active task selected')

        url = 'applications/http/{}/purge/{}'
        return self.do_api('DELETE', url.format(self.app_id, task_id))

    def emergency_conf(self, partition):
        if not partition:
            raise Exception('no active partition selected')

        url = 'emergency?partition={}'
        return self.do_api('GET', url.format(partition))

    def decode_request_id(self, request_id):
        if not request_id or len(request_id) != 24:
            raise Exception('need request id')

        buf = [0] * 12
        for i in range(12):
            value = 0
            left = ord(request_id[i * 2])
            right = ord(request_id[i * 2 + 1])

            if left <= 57:
                value = (left - 48) * 16
            else:
                value = (left - 87) * 16

            if right <= 57:
                value = value + (right - 48)
            else:
                value = value + (right - 87)

            buf[i] = value

        data = {
            'node_id': 0,
            'app_id': 0,
            'timestamp': 0,
            'is_stream': False,
            'sequence': 0
        }

        if buf[0] & 240 != 0:
            raise Exception('invalid request id')

        # reserved: 2-bit, must be 0
        if buf[9] & 6 != 0:
            raise Exception('reserved bits being abused')

        data['node_id'] = (buf[0] & 15) << 17 | \
            buf[1] << 9 | \
            buf[2] << 1 | \
            buf[3] >> 7

        data['app_id'] = (buf[3] & 127) << 14 | \
            buf[4] << 6 | \
            buf[5] >> 2

        data['timestamp'] = (buf[5] & 3) << 29 | \
            buf[6] << 21 | \
            buf[7] << 13 | \
            buf[8] << 5 | \
            buf[9] >> 3

        data['timestamp'] += EPOCH
        data['is_stream'] = (buf[9] & 1) != 0
        data['sequence'] = (buf[10] << 8) | buf[11]

        return data

    def search_waf_log(self, request_id):
        info = self.decode_request_id(request_id)
        if not info or not info["app_id"]:
            raise Exception('decode request id error')

        app_id = info["app_id"]
        url = 'log_server/waflog/{}?request_id={}'
        result = self.do_api('GET', url.format(app_id, request_id))

        if not self.request_ok():
            raise Exception('search waf log error')

        data = result.get('data')
        if not data:
            return None

        return data[0]

    def add_api_token(self, name=None, expire=0):
        url = 'api_token/'
        body = {'name': name, 'expire': expire}
        mothod = 'POST'

        return self.do_api(mothod, url, body)

    def get_api_token(self, id=None, limit=20):
        url = 'api_token/'
        if id:
            url = "{}{}/".format(url, id)

        if limit:
            url = "{}?page_size={}".format(url, limit)

        mothod = 'GET'

        return self.do_api(mothod, url)

    def del_api_token(self, id):
        if not id:
            raise Exception('bad api token id')

        url = 'api_token/{}'.format(id)
        mothod = 'DELETE'

        return self.do_api(mothod, url)

    def add_gateway_tag(self, name):
        r = self.do_api('POST', GatewayTagUrl, { 'name': name })
        if r is not None:
            return r['id']
        return None

    def del_gateway_tag(self, tag_id):
        r = self.do_api('DELETE', GatewayTagUrl + '/' + str(tag_id))

    def get_all_gateway_tag(self):
        ret = self.do_api('GET', GatewayTagUrl)
        return ret

    def add_gateway(self, name, partition, tag = None):
        if not name:
            raise Exception('name not found')
        if not partition:
            raise Exception('partition not found')

        body = {
            'name': name,
            'partition': partition,
        }

        if tag is not None:
            body['tag'] = tag

        r = self.do_api('POST', GatewayUrl, body)

        if r is not None:
            return r['id']

        return None

    def del_gateway(self, gateway_id):
        return self.do_api('DELETE', GatewayUrl + '/' + str(gateway_id))

    def get_all_gateway(self):
        tags = self.get_all_gateway_tag()
        tags_map = {}

        if tags is None:
            tags = []

        for tag in tags:
            tags_map[tag['id']] = tag

        gateways = self.get_all(GatewayUrl + '?detail=1', True)
        for i, gateway in enumerate(gateways):
            gateway['tags'] = list()
            tag_ids = gateway.get('tag', [])
            for tag_id in tag_ids:
                gateway['tags'].append(tags_map[int(tag_id)])
            gateway.pop('tag', None)

        return gateways

    def new_ip_list(self, **kwargs):
        kwargs['http_verb'] = 'POST'
        data = self.put_ip_list(**kwargs)

        if not self.request_ok():
            raise Exception('request failed')

        rule_id = data.get('id')
        if not rule_id:
            raise Exception('IP List ID not found')
        if not isinstance(rule_id, int):
            raise Exception('Bad IP List ID obtained: ' + rule_id)

        return rule_id

    def put_ip_list(self, rule_id=None, http_verb='PUT', name=None,
                    type='ipv4', items=None):
        if not self.app_id:
            raise Exception('no active applicatoin selected')

        if http_verb == 'PUT' and not rule_id:
            raise Exception('no active ip list selected')

        if http_verb == 'POST' and not name:
            raise Exception('no name arg specified')

        body = {'type': type}

        if name:
            body['name'] = name
        if items is not None:
            body['items'] = items

        ge_version_240916 = self.is_version_at_least(EDGE_VERSION_24_09_16)
        if ge_version_240916:
            url = AppIPListUrlV2.format(self.app_id)
            if http_verb == 'PUT':
                url = f"{url}/update/{rule_id}"
        else:
            url = AppIPListUrl.format(self.app_id)
            if http_verb == 'PUT':
                url = f"{url}/{rule_id}"

        return self.do_api(http_verb, url, body)

    def get_ip_list_items(self, ip_list_id, page_size=10000):
        if not self.app_id:
            raise Exception('no active application selected')

        url = AppIPListItemsUrl.format(self.app_id, ip_list_id)
        return self.get_all(url, page_size=page_size)

    def get_ip_list(self, rule_id=None, detail=True):
        if not self.app_id:
            raise Exception('no active application selected')
        if not rule_id:
            raise Exception('no active IP List selected')

        url = AppIPListUrl.format(self.app_id) + f"/{rule_id}"
        ge_version_240916 = self.is_version_at_least(EDGE_VERSION_24_09_16)
        if detail is True and ge_version_240916 is False:
            url = f"{url}?detail=1"

        data = self.do_api('GET', url)

        if detail is True:
            if ge_version_240916 is True:
                if 'items' not in data:
                    data['items'] = self.get_ip_list_items(rule_id)
        else:
            if 'items' in data:
                del data['items']

        return data

    def get_all_ip_lists(self, detail=True):
        if not self.app_id:
            raise Exception('no active application selected')

        has_uri_args = False
        url = AppIPListUrl.format(self.app_id)
        ge_version_240916 = self.is_version_at_least(EDGE_VERSION_24_09_16)
        if detail is True and ge_version_240916 is False:
            url = f"{url}?detail=1"
            has_uri_args = True

        ge_version_240906 = self.is_version_at_least(EDGE_VERSION_24_09_06)
        if ge_version_240906 is True:
            ip_lists = self.get_all(url, has_uri_args)
        else:
            ip_lists = self.do_api('GET', url)

        if detail is True:
            if ge_version_240916 is True:
                for ip_list in ip_lists:
                    if 'items' not in ip_list:
                        ip_list['items'] = self.get_ip_list_items(ip_list['id'])
        else:
            for ip_list in ip_lists:
                if 'items' in ip_list:
                    del ip_list['items']

        return ip_lists

    def del_ip_list(self, rule_id=None):
        if not self.app_id:
            raise Exception('no active application selected')

        if not rule_id:
            raise Exception('no active IP List selected')

        return self.do_api('DELETE', AppIPListUrl.format(self.app_id) + '/' +
                           str(rule_id))

    def mod_ip_list(self, app_id=None, rule_id=None, http_verb='PUT',
                    items=None, action=None, remove_expired=False):
        body = {'items': items, 'remove_expired': remove_expired}

        url = ModAppIPListUrl.format(app_id, action, rule_id)

        return self.do_api(http_verb, url, body)

    def append_to_ip_list(self, rule_id=None, items=None, remove_expired=False):
        if not self.app_id:
            raise Exception('no active application selected')
        if not rule_id:
            raise Exception('no active IP List selected')

        return self.mod_ip_list(app_id=self.app_id, rule_id=rule_id,
                                items=items, action='append', remove_expired=remove_expired)

    def remove_from_ip_list(self, rule_id=None, items=None):
        if not self.app_id:
            raise Exception('no active application selected')
        if not rule_id:
            raise Exception('no active IP List selected');

        return self.mod_ip_list(app_id=self.app_id, rule_id=rule_id,
                                items=items, action='remove')

    def get_version(self):
        return self.do_api('GET', VersionUrl)

    def is_version_at_least(self, version):
        versions = self.get_version()
        ver = versions.get("version", None)
        if not ver:
            raise Exception('version not found')

        if ver == INITIAL_EDGE_VERSION:
            warnings.warn(f"current edge version is {ver}")
            return True

        return ver >= version

    def node_monitor(self, node_id, start_time=None, end_time=None, step=60):
        if not isinstance(node_id, int) or node_id <= 0:
            raise Exception('invalid node id')

        if start_time is None:
            start_time = int(time.time() - 1800)

        if end_time is None:
            end_time = int(time.time())

        url = NodeMonitorSystemUrl.format(node_id)
        url = "{}/?start_utime={}&end_utime={}&step={}".format(
            url, start_time, end_time, step)

        return self.get_all(url, True)

    def new_global_k8s(self, **kwargs):
        kwargs['http_verb'] = 'POST'
        data = self.put_global_k8s(**kwargs)

        if not self.request_ok():
            raise Exception('request failed.')

        k8s_id = data.get('id')
        if not k8s_id:
            raise Exception('k8s ID not found')
        if not isinstance(k8s_id, int):
            raise Exception('k8s ID obtained: ' + k8s_id)

        return k8s_id

    def put_global_k8s(self, k8s_id=None, http_verb='PUT', name=None,
                        host=None, port=None, ssl_verify=True,
                        token=None, domain=None,
                        connect_timeout=None, read_timeout=None, send_timeout=None):
        if http_verb == 'PUT' and not k8s_id:
            raise Exception('no active k8s selected')

        if http_verb == 'POST':
            if not name:
                raise Exception('no name arg specified')
            if not host and not domain:
                raise Exception('no host and no domain arg specified')
            if not port:
                raise Exception('no port arg specified')
            if not token:
                raise Exception('no token arg specified')

        if host and domain:
            raise Exception('only one of host or domain can be specified')

        if not isinstance(port, int):
            raise Exception('Bad port obtained')

        body = {
            'name': name,
            'host': host,
            'domain': domain,
            'port': port,
            'connect_timeout': connect_timeout,
            'read_timeout': read_timeout,
            'send_timeout': send_timeout,
            'ssl_verify': ssl_verify,
            'token': token,
        }

        url = GlobalK8sUrl + '/'
        if http_verb == 'PUT':
            url = url + str(k8s_id)

        return self.do_api(http_verb, url, body)

    def get_global_k8s(self, k8s_id):
        if not k8s_id:
            raise Exception('no active k8s selected')

        return self.do_api(
            'GET', '{}/{}?detail=1'.format(GlobalK8sUrl, k8s_id))

    def get_k8s_services_detail(self, k8s_id):
        if not k8s_id:
            raise Exception('no active k8s selected')

        return self.do_api(
            'GET', '{}/{}?detail=1'.format(K8sUrl, k8s_id))

    def get_all_global_k8s(self):
        return self.get_all(GlobalK8sUrl)

    def del_global_k8s(self, k8s_id):
        if not k8s_id:
            raise Exception('no active k8s selected')

        return self.do_api('DELETE', '{}/{}'.format(GlobalK8sUrl, k8s_id))

    def get_all_nodes(self):
        nodes = []
        gateways = self.get_all(GatewayUrl + '?detail=1', True)
        for i, gateway in enumerate(gateways):
            gw_nodes = gateway.get('nodes', [])
            for i, n in enumerate(gw_nodes):
                n['gateway_id'] = gateway.get('id')
                nodes.append(n)
            # nodes.extend(gw_nodes)

        return nodes

    def get_node(self, node_id, gateway_id=None):
        if not isinstance(node_id, int):
            raise Exception('Node id should be of type int')

        node = None
        if gateway_id is None:
            nodes = self.get_all_nodes()
            for i, n in enumerate(nodes):
                if n.get('id') == node_id:
                    node = n
                    break
        else:
            url = NodesUrl.format(gateway_id, node_id)+ '?detail=1'
            node = self.do_api('GET', url)

        return node

    def get_node_by_mac_address(self, mac_address):
        if not isinstance(mac_address, str):
            raise Exception('MAC address should be of type str')

        nodes = self.get_all_nodes()
        for node in nodes:
            mac_addrs = node['mac_address'].split(" ")
            for mac_addr in mac_addrs:
                if mac_addr == mac_address:
                    return node

        return None

    def del_node(self, node_id, gateway_id=None):
        if not isinstance(node_id, int):
            raise Exception('Node id should be of type int')

        if gateway_id is None:
            nodes = self.get_all_nodes()
            for i, n in enumerate(nodes):
                if n.get('id') == node_id:
                    gateway_id = n.get('gateway_id')
                    break

            if gateway_id is None:
                raise Exception('not found the node in any gateway')

        url = NodesUrl.format(gateway_id, node_id)

        return self.do_api('DELETE', url)

    def put_node(self, node_id, gateway_id=None, \
            name=None, status = None, is_gray=None, external_ip=None, \
            external_ipv6=None, internal_ip=None):

        if not isinstance(node_id, int):
            raise Exception('Node id should be of type int')

        if is_gray is not None and not isinstance(is_gray, bool):
            raise Exception('is_gray should be of type boolean')

        if status is not None and not isinstance(status, int):
            raise Exception('status should be of type boolean')

        if gateway_id is None:
            nodes = self.get_all_nodes()
            for i, n in enumerate(nodes):
                if n.get('id') == node_id:
                    gateway_id = n.get('gateway_id')
                    break

            if gateway_id is None:
                raise Exception('node not found in any gateway')

        body = dict()
        if name is not None:
            body['name'] = name
        if status is not None:
            body['status'] = status
        if is_gray is not None:
            body['is_gray'] = is_gray
        if external_ip is not None:
            body['external_ip'] = external_ip
        if external_ipv6 is not None:
            body['external_ipv6'] = external_ipv6
        if internal_ip is not None:
            body['internal_ip'] = internal_ip

        url = NodesUrl.format(gateway_id, node_id)

        return self.do_api('PUT', url, body)

    def lmdb_backup(self):
        res = self.do_api('POST', LmdbBackupUrl)
        if not res:
            if not self.__ok and self.__msg:
                return self.__msg
            else:
                raise Exception('failed to backup LMDB')

        return res

    def get_global_cert_referenced(self, id):
        if not isinstance(id, int):
            raise Exception('global cert id should be of type int')

        url = ReferencedUrl.format(id)

        return self.get_all(url)

    def get_all_partition_lua_module(self, partition_id):
        if not isinstance(partition_id, int):
            raise Exception('partition id should be of type int')

        url = PartitionLuaModuleUrl.format(partition_id, "")
        return self.get_all(url)

    def get_partition_lua_module(self, partition_id, module_id):
        if not isinstance(partition_id, int):
            raise Exception('partition id should be of type int')

        if not isinstance(module_id, int):
            raise Exception('lua module id should be of type int')

        url = PartitionLuaModuleUrl.format(partition_id, module_id)

        return self.do_api('GET', url)

    def put_partition_lua_module(self, partition_id, module_id, name=None, code=None):
        if not isinstance(partition_id, int):
            raise Exception('partition id should be of type int')

        if not isinstance(module_id, int):
            raise Exception('lua module id should be of type int')

        if name is not None and (not isinstance(name, str) or name == ""):
            raise Exception('lua module name should be of type str and not empty')

        if code is not None and (not isinstance(code, str) or code == ""):
            raise Exception('lua module code should be of type str and not empty')

        body = dict()
        if name is not None:
            body['name'] = name
        if code is not None:
            body['code'] = code

        if not body:
            raise Exception('missing lua module name or code')

        url = PartitionLuaModuleUrl.format(partition_id, module_id)

        return self.do_api('PUT', url, body)

    def new_partition_lua_module(self, partition_id, name, code):
        if not isinstance(partition_id, int):
            raise Exception('partition id should be of type int')

        if not isinstance(name, str) or name == "":
            raise Exception('lua module name should be of type str and not empty')

        if not isinstance(code, str) or code == "":
            raise Exception('lua module code should be of type str and not empty')

        body = {
            'name': name,
            'code': code,
        }

        url = PartitionLuaModuleUrl.format(partition_id, "")

        return self.do_api('POST', url, body)

    def del_partition_lua_module(self, partition_id, module_id):
        if not isinstance(partition_id, int):
            raise Exception('partition id should be of type int')

        if not isinstance(module_id, int):
            raise Exception('lua module id should be of type int')

        url = PartitionLuaModuleUrl.format(partition_id, module_id)

        return self.do_api('DELETE', url)

    def conv_crl_to_lua_module(self, files):
        code = '''local ngx_var = ngx.var
local ngx_log = ngx.log
local ngx_ERR = ngx.ERR
local ngx_exit = ngx.exit

local _M = {}

local serials = {
'''
        prog = re.compile("\s+Serial Number:\s+([A-F0-9]+)$")
        for f in files:
            p = Popen('openssl crl -inform DER -text -noout -in %s' % (f),
                        shell=True, bufsize=4096*1024, stdin=PIPE,
                        stdout=PIPE, stderr=PIPE, close_fds=True)
            if p.wait() != 0:
                err = p.stderr.read().decode()
                raise Exception(err)

            for line in io.TextIOWrapper(p.stdout, encoding="utf-8"):
                m = prog.match(line)
                if m:
                    code = code + "    [\"{}\"] = 1,\n".format(m.group(1))

        code = code + '''}

function _M.verify_client_serial()
    local serial = ngx_var["ssl_client_serial"]
    if not serial or serial == "" then
        ngx_log(ngx_ERR, "ssl client serial not found")
        ngx_exit(403)
    end

    if serials[serial] ~= nil then
        ngx_log(ngx_ERR, "ssl client serial ", serial, " is in clr list")
        ngx_exit(403)
    end

    return true
end

return _M
'''
        return code

    def get_waf_logs(self, app_id, page=1, pagesize=20, request_id=None,
                     start_time=None, end_time=None, host=None, header=None,
                     rule_set_id=None, resp_status=None, action=None,
                     remote_addr=None, show_all=False):

        if not app_id:
            raise Exception('no active application selected')

        if page <= 0:
            raise Exception('bad page')

        if pagesize <= 0:
            raise Exception('bad pagesize')

        args = list()

        args.append("page={}".format(page))
        args.append("page_size={}".format(pagesize))

        if request_id is not None:
            info = self.decode_request_id(request_id)
            if not info or not info["app_id"]:
                raise Exception('decode request id error')

            if app_id != info["app_id"]:
                raise Exception('request id {} does not belong to app {}, but belongs to {}'.format(request_id, app_id, info["app_id"]))

            args.append("request_id={}".format(request_id))

        if start_time is not None:
            if start_time <= 0:
                raise Exception('bad start_time')

            args.append("start_time={}".format(start_time))

        if end_time is not None:
            if end_time <= 0:
                raise Exception('bad end_time')

            args.append("end_time={}".format(end_time))

        if host is not None:
            args.append("host={}".format(host))

        if header is not None:
            args.append("header={}".format(header))

        if rule_set_id is not None:
            if rule_set_id <= 0:
                raise Exception('bad rule_set_id')

            args.append("rule_set_id={}".format(rule_set_id))

        if resp_status is not None:
            if resp_status <= 100 or resp_status >= 600:
                raise Exception('bad resp_status')

            args.append("resp_status={}".format(resp_status))

        if action is not None:
            if action not in self.waf_actions:
                raise Exception('unknown action: ' + action)

            args.append("action={}".format(action))

        if remote_addr is not None:
            args.append("remote_addr={}".format(remote_addr))

        if show_all == True:
            args.append("show_all=true")

        uri_args = ""
        if len(args) > 0:
            uri_args = "?" + "&".join(args)

        url = WafLogUrl.format(app_id) + uri_args
        url = url.format(app_id, request_id)
        result = self.do_api('GET', url)

        if not self.request_ok():
            raise Exception('get waf logs error')

        data = result.get('data', None)
        if not data:
            return None, 0

        meta = result.get('meta', None)
        if not meta:
            return None, 0

        count = meta.get('count', None)
        if not count:
            return None, 0

        return data, count

    def get_dos_logs(self, app_id, page=1, pagesize=20, request_id=None,
                     start_time=None, end_time=None, host=None, uri=None,
                     user_agent=None, action=None, remote_addr=None):

        if not app_id:
            raise Exception('no active application selected')

        if page <= 0:
            raise Exception('bad page')

        if pagesize <= 0:
            raise Exception('bad pagesize')

        args = list()

        args.append("page={}".format(page))
        args.append("page_size={}".format(pagesize))

        if request_id is not None:
            info = self.decode_request_id(request_id)
            if not info or not info["app_id"]:
                raise Exception('decode request id error')

            if app_id != info["app_id"]:
                raise Exception('request id {} does not belong to app {}, but belongs to {}'.format(request_id, app_id, info["app_id"]))

            args.append("request_id={}".format(request_id))

        if start_time is not None:
            if start_time <= 0:
                raise Exception('bad start_time')

            args.append("start_time={}".format(start_time))

        if end_time is not None:
            if end_time <= 0:
                raise Exception('bad end_time')

            args.append("end_time={}".format(end_time))

        if host is not None:
            args.append("host={}".format(host))

        if uri is not None:
            args.append("uri={}".format(uri))

        if user_agent is not None:
            args.append("user_agent={}".format(user_agent))

        if action is not None:
            if action not in self.dos_actions:
                raise Exception('unknown action: ' + action)

            args.append("limit_action={}".format(action))

        if remote_addr is not None:
            args.append("client_ip={}".format(remote_addr))

        uri_args = ""
        if len(args) > 0:
            uri_args = "?" + "&".join(args)

        url = DosLogUrl.format(app_id) + uri_args
        url = url.format(app_id, request_id)
        result = self.do_api('GET', url)

        if not self.request_ok():
            raise Exception('get dos logs error')

        data = result.get('data', None)
        if not data:
            return None, 0

        meta = result.get('meta', None)
        if not meta:
            return None, 0

        count = meta.get('count', None)
        if not count:
            return None, 0

        return data, count

    def get_global_page_template(self, id):
        if not id:
            raise Exception('no active upstream selected')

        return self.do_api(
            'GET', 'global/1/page_template/{}?detail=1'.format(id))

    def get_all_global_page_templates(self):
        return self.get_all(GlobalPageTemplateUrl)

    def del_global_page_template(self, id):
        if not id:
            raise Exception('no active page template selected')

        return self.do_api('DELETE', 'global/1/page_template/{}'.format(id))

    def put_global_page_template(self, id, name=None, content=None):
        if name is None and content is None:
            raise Exception('no name or content arg specified')

        if name is None or content is None:
            data = self.get_global_page_template(id)
            if name is None:
                name = data['name']

            if content is None:
                content = data['content']

        body = {
            "name": name,
            "content": content,
        }

        url = "{}/{}".format(GlobalPageTemplateUrl, str(id))
        return self.do_api("PUT", url, body)

    def new_global_page_template(self, name, content):
        body = {
            "name": name,
            "content": content,
        }

        url = GlobalPageTemplateUrl
        data = self.do_api("POST", url, body)
        return data.get('id')

    def get_global_basic_auth_user_group(self, id):
        if not id:
            raise Exception('no active basic auth user group selected')

        url = '{}/{}'.format(GlobalBasicAuthGroupUrl, id)
        return self.do_api('GET', url)

    def get_all_global_basic_auth_user_groups(self):
        return self.get_all(GlobalBasicAuthGroupUrl)

    def del_global_basic_auth_user_group(self, id):
        if not id:
            raise Exception('no active basic auth user group selected')

        url = '{}/{}'.format(GlobalBasicAuthGroupUrl, id)
        return self.do_api('DELETE', url)

    def put_global_basic_auth_user_group(self, id, name=None, label=None):
        if not id:
            raise Exception('no active basic auth user group selected')

        if name is None and label is None:
            raise Exception('no name or label specified')

        if name is None or label is None:
            data = self.get_global_basic_auth_user_group(id)
            if name is None:
                name = data['name']

            if label is None:
                label = data['label']

        body = {
            "name": name,
            "label": label,
        }

        url = '{}/{}'.format(GlobalBasicAuthGroupUrl, id)
        return self.do_api("PUT", url, body)

    def new_global_basic_auth_user_group(self, name, label=None):
        body = {
            "name": name,
            "label": label,
        }

        data = self.do_api("POST", GlobalBasicAuthGroupUrl, body)
        return data.get('id')

    def get_global_basic_auth_user(self, id, group_id):
        if not group_id:
            raise Exception('no active basic auth user group selected')

        if not id:
            raise Exception('no active basic auth user selected')

        url = '{}/{}'.format(GlobalBasicAuthUserUrl, id)
        user = self.do_api('GET', url)
        if user:
            user["password"] = None

        return user

    def get_global_basic_auth_users_in_group(self, group_id):
        if not group_id:
            raise Exception('no active basic auth user group selected')

        url = GlobalBasicAuthUserUrl.format(group_id)

        # NOTE: should support paging
        users = self.do_api('GET', url)
        if users:
            for user in users:
                user['password'] = None

        return users

    def del_global_basic_auth_user(self, id, group_id):
        if not group_id:
            raise Exception('no active basic auth user group selected')

        if not id:
            raise Exception('no active basic auth user selected')

        url = GlobalBasicAuthUserUrl.format(group_id)
        url = '{}/{}'.format(url, id)
        return self.do_api('DELETE', url)

    def put_global_basic_auth_user(self, id, group_id, username, password):
        if not group_id:
            raise Exception('no active basic auth user group selected')

        if not id:
            raise Exception('no active basic auth user selected')

        if username is None or password is None:
            raise Exception('no username or password specified')

        body = {
            "username": username,
            "password": password,
        }

        url = GlobalBasicAuthUserUrl.format(group_id)
        url = '{}/{}'.format(url, id)
        return self.do_api("PUT", url, body)

    def new_global_basic_auth_user(self, group_id, username, password):
        if not group_id:
            raise Exception('no active basic auth user group selected')

        body = {
            "username": username,
            "password": password,
        }

        url = GlobalBasicAuthUserUrl.format(group_id)
        data = self.do_api("POST", url, body)
        return data.get('id')

    def get_app_basic_auth_user_group(self, id, app_id=None):
        app_id = app_id or self.app_id
        if not app_id:
            raise Exception('no active application selected')

        if not id:
            raise Exception('no active basic auth user group selected')

        url = AppBasicAuthGroupUrl.format(app_id)
        url = '{}/{}'.format(url, id)
        return self.do_api('GET', url)

    def get_all_app_basic_auth_user_groups(self, app_id=None):
        app_id = app_id or self.app_id
        if not app_id:
            raise Exception('no active application selected')

        url = AppBasicAuthGroupUrl.format(app_id)
        return self.get_all(url)

    def del_app_basic_auth_user_group(self, id, app_id=None):
        app_id = app_id or self.app_id
        if not app_id:
            raise Exception('no active application selected')

        if not id:
            raise Exception('no active basic auth user group selected')

        url = AppBasicAuthGroupUrl.format(app_id)
        url = '{}/{}'.format(url, id)
        return self.do_api('DELETE', url)

    def put_app_basic_auth_user_group(self, id, name=None, label=None, app_id=None):
        app_id = app_id or self.app_id
        if not app_id:
            raise Exception('no active application selected')

        if not id:
            raise Exception('no active basic auth user group selected')

        if name is None and label is None:
            raise Exception('no name or label specified')

        if name is None or label is None:
            data = self.get_app_basic_auth_user_group(id, app_id)
            if name is None:
                name = data['name']

            if label is None:
                label = data['label']

        body = {
            "name": name,
            "label": label,
        }

        url = AppBasicAuthGroupUrl.format(app_id)
        url = '{}/{}'.format(url, id)
        return self.do_api("PUT", url, body)

    def new_app_basic_auth_user_group(self, name, label=None, app_id=None):
        app_id = app_id or self.app_id
        if not app_id:
            raise Exception('no active application selected')

        body = {
            "name": name,
            "label": label,
        }

        url = AppBasicAuthGroupUrl.format(app_id)
        data = self.do_api("POST", url, body)
        return data.get('id')

    def get_app_basic_auth_user(self, id, group_id, app_id=None):
        app_id = app_id or self.app_id
        if not app_id:
            raise Exception('no active application selected')

        if not group_id:
            raise Exception('no active basic auth user group selected')

        if not id:
            raise Exception('no active basic auth user selected')

        url = AppBasicAuthUserUrl.format(app_id, group_id)
        url = '{}/{}'.format(url, id)
        user = self.do_api('GET', url)
        if user:
            user["password"] = None

        return user

    def get_app_basic_auth_users_in_group(self, group_id, app_id=None):
        app_id = app_id or self.app_id
        if not app_id:
            raise Exception('no active application selected')

        if not group_id:
            raise Exception('no active basic auth user group selected')

        url = AppBasicAuthUserUrl.format(app_id, group_id)

        # NOTE: should support paging
        users = self.do_api('GET', url)
        if users:
            for user in users:
                user['password'] = None

        return users

    def del_app_basic_auth_user(self, id, group_id, app_id=None):
        app_id = app_id or self.app_id
        if not app_id:
            raise Exception('no active application selected')

        if not group_id:
            raise Exception('no active basic auth user group selected')

        if not id:
            raise Exception('no active basic auth user selected')

        url = AppBasicAuthUserUrl.format(app_id, group_id)
        url = '{}/{}'.format(url, id)
        return self.do_api('DELETE', url)

    def put_app_basic_auth_user(self, id, group_id, username, password, app_id=None):
        app_id = app_id or self.app_id
        if not app_id:
            raise Exception('no active application selected')

        if not group_id:
            raise Exception('no active basic auth user group selected')

        if not id:
            raise Exception('no active basic auth user selected')

        if username is None or password is None:
            raise Exception('no username or password specified')

        body = {
            "username": username,
            "password": password,
        }

        url = AppBasicAuthUserUrl.format(app_id, group_id)
        url = '{}/{}'.format(url, id)
        return self.do_api("PUT", url, body)

    def new_app_basic_auth_user(self, group_id, username, password, app_id=None):
        app_id = app_id or self.app_id
        if not app_id:
            raise Exception('no active application selected')

        if not group_id:
            raise Exception('no active basic auth user group selected')

        body = {
            "username": username,
            "password": password,
        }

        url = AppBasicAuthUserUrl.format(app_id, group_id)
        data = self.do_api("POST", url, body)
        return data.get('id')

    def get_all_candidate_node(self):
        return self.get_all(ListCandidateNodeUrl)

    def approve_candidate_node(self, gateway_id, mac_address,
                                internal_ip=None, external_ip=None,
                                name=None, external_ipv6=None, status=1):
        target = None
        candidates = self.get_all_candidate_node()
        for candidate in candidates:
            mac_addrs = candidate['mac_address'].split(" ")
            for mac_addr in mac_addrs:
                if mac_addr == mac_address:
                    target = candidate
                    break
            if target is not None:
                break

        if target is None:
            raise Exception('can not found the candidate node: ' + str(mac_address))

        gateways = self.get_all_gateway()
        found = False
        for gateway in gateways:
            if gateway['id'] == int(gateway_id):
                found = True

        if not found:
            raise Exception('can not found the gateway cluster: ' + str(gateway_id))

        if name is None or name == "":
            target['name'] = target['hostname']
        else:
            target['name'] = name

        if internal_ip is not None:
            target['internal_ip'] = internal_ip
        else:
            target['internal_ip'] = get_first_ip(target['internal_ip'])

        if external_ip is not None:
            target['external_ip'] = external_ip
        else:
            target['external_ip'] = get_first_ip(target['external_ip'])

        if external_ipv6 is not None:
            target['external_ipv6'] = external_ipv6
        else:
            target['external_ipv6'] = get_first_ip(target['external_ipv6'])

        if status is not None:
            target['status'] = int(status)

        target['cluster'] = int(gateway_id)

        return self.do_api('POST', ApproveCandidateNodeUrl, target)

    def sync_to_all(self, general=None, lua_module=None):
        body = dict()

        if general == True or general == False:
            body['ngx'] = general

        if lua_module == True or lua_module == False:
            body['lua_module'] = lua_module

        return self.do_api('PUT', SyncToAllUrl, body=body)

    def get_sync_to_all(self):
        return self.do_api('GET', SyncToAllUrl)

    def get_all_k8s_endpoints(self):
        return self.get_all(GlobalK8sEndpointsUrl)

    def del_k8s_endpoint(self, id):
        url = '{}/{}'.format(GlobalK8sEndpointsUrl, id)
        return self.do_api('DELETE', url)

    def del_k8s_endpoints(self, k8s_id):
        endpoints = self.get_all_k8s_endpoints()
        for endpoint in endpoints:
            if endpoint['k8s'] == k8s_id:
                self.del_k8s_endpoint(endpoint['id'])

    def get_all_acme_providers(self):
        # return self.get_all(GlobalAcmeProvidersUrl)
        return self.do_api('GET', GlobalAcmeProvidersUrl)

    def get_acme_provider(self, id):
        url = '{}/{}'.format(GlobalAcmeProvidersUrl, id)
        return self.do_api('GET', url)

    def del_acme_provider(self, id):
        url = '{}/{}'.format(GlobalAcmeProvidersUrl, id)
        return self.do_api('DELETE', url)

    def put_acme_provider(self, id=None, name=None, endpoint=None,
                          eab_hmac_key=None, eab_kid=None,
                          email=None, http_verb="PUT"):

        if http_verb == "PUT" and id is None:
            raise Exception('no id arg specified')

        if name is None:
            raise Exception('no name arg specified')

        if endpoint is None:
            raise Exception('no endpoint arg specified')

        body = {
            "name": name,
            "endpoint": endpoint,
        }

        if eab_hmac_key is not None:
            body['eab_hmac_key'] = eab_hmac_key

        if eab_kid is not None:
            body['eab_kid'] = eab_kid

        if email is not None:
            body['email'] = email

        if http_verb == 'PUT':
            body['id'] = id

        url = GlobalAcmeProvidersUrl
        if http_verb == 'PUT':
            url = '{}/{}'.format(url, id)

        return self.do_api(http_verb, url, body)

    def new_acme_provider(self, **kwargs):
        kwargs['http_verb'] = 'POST'
        data = self.put_acme_provider(**kwargs)
        return data.get('id')

    def get_acme_logs(self, cert_id):
        url = f"{AppAcmeCertLogsUrl}/{cert_id}"
        data = self.do_api('GET', url)
        count = 0
        if data is not None and data.get('meta') is not None:
            count = data.get('meta').get('count')

        logs = list()
        if data is not None:
            logs = data.get('data')

        return logs, count


    def get_error_logs(self, page=1, page_size=10, node_type=None,
                       node_id=None, app_id=None, req_id=None,
                       level=None, start_time=None, end_time=None):

        if level is not None and level not in ERROR_LOG_LEVELS:
            raise Exception(f'invalid log level: {level}')

        if level is not None:
            level = ERROR_LOG_LEVELS[level]

        if page is None:
            page = 1

        if page_size is None:
            page_size = 10

        if start_time is None:
            start_time = int(time.time() - 86400)

        if end_time is None:
            end_time = int(time.time())

        params = {
            'page': page,
            'page_size': page_size,
        }

        if node_type is not None:
            params['node_type'] = node_type

        if node_id is not None:
            params['node_id'] = node_id

        if app_id is not None:
            params['app_id'] = app_id

        if req_id is not None:
            params['req_id'] = req_id

        if level is not None:
            params['level'] = level

        if start_time is not None:
            params['start_time'] = start_time

        if end_time is not None:
            params['end_time'] = end_time

        url = f"{ErrorLogsUrl}?{urlencode(params)}"
        data = self.do_api('GET', url)
        count = 0
        if data is not None and data.get('meta') is not None:
            count = data.get('meta').get('count')

        logs = list()
        if data is not None:
            logs = data.get('data')

        return logs, count

    def get_node_error_logs(self, **kwargs):
        kwargs['node_type'] = 0
        return self.get_error_logs(**kwargs)

    def get_admin_error_logs(self, **kwargs):
        kwargs['node_type'] = 2
        return self.get_error_logs(**kwargs)

    def get_log_server_error_logs(self, **kwargs):
        kwargs['node_type'] = 1
        return self.get_error_logs(**kwargs)

    def get_http_app_error_logs(self, app_id=None, **kwargs):
        app_id = app_id or self.app_id
        if not app_id:
            raise Exception('no active application selected')

        kwargs['app_id'] = app_id

        return self.get_error_logs(**kwargs)
