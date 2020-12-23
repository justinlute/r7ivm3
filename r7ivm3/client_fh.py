# -*- coding: utf-8 -*-

import r7ivm3
import base64
import json
import swagger_client

class ClientForHumans:
    def __init__(self,
                 config_file_path="api_config.json",
                 client_name="r7ivm3_python_client",
                 disable_insecure_request_warnings=True
                 ):

        if disable_insecure_request_warnings == True:
            import urllib3
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        with open(config_file_path, 'r') as infile:
            cfg_file = json.load(infile)

        # Instantiate an instance of the r7_ivm_swag module's Configuration class
        self.config = swagger_client.Configuration(name=client_name)
        self.config.username = cfg_file["rapid7"]["credentials"]["username"]
        self.config.password = cfg_file["rapid7"]["credentials"]["password"]
        self.config.host = cfg_file["rapid7"]["api_url"]
        self.config.verify_ssl = False
        self.config.assert_hostname = False
        self.config.proxy = None
        self.config.ssl_ca_cert = None
        self.config.connection_pool_maxsize = None
        self.config.cert_file = None
        self.config.key_file = None
        self.config.safe_chars_for_path_param = ''

        self.auth = "%s:%s" % (self.config.username, self.config.password)
        self.auth = base64.b64encode(self.auth.encode('ascii')).decode()
        self.api_client = swagger_client.ApiClient(configuration=self.config)
        self.api_client.default_headers['Authorization'] = "Basic %s" % self.auth

        # Create API resources
        self.administration_api = swagger_client.AdministrationApi(self.api_client)
        self.asset_api = swagger_client.AssetApi(self.api_client)
        self.asset_discovery_api = swagger_client.AssetDiscoveryApi(self.api_client)
        self.asset_group_api = swagger_client.AssetGroupApi(self.api_client)
        self.credential_api = swagger_client.CredentialApi(self.api_client)
        self.policy_api = swagger_client.PolicyApi(self.api_client)
        self.policy_override_api = swagger_client.PolicyOverrideApi(self.api_client)
        self.remediation_api = swagger_client.RemediationApi(self.api_client)
        self.report_api = swagger_client.ReportApi(self.api_client)
        self.root_api = swagger_client.RootApi(self.api_client)
        self.scan_api = swagger_client.ScanApi(self.api_client)
        self.scan_engine_api = swagger_client.ScanEngineApi(self.api_client)
        self.scan_template_api = swagger_client.ScanTemplateApi(self.api_client)
        self.site_api = swagger_client.SiteApi(self.api_client)
        self.tag_api = swagger_client.TagApi(self.api_client)
        self.user_api = swagger_client.UserApi(self.api_client)
        self.vulnerability_api = swagger_client.VulnerabilityApi(self.api_client)
        self.vulnerability_check_api = swagger_client.VulnerabilityCheckApi(self.api_client)
        self.vulnerability_exception_api = swagger_client.VulnerabilityExceptionApi(self.api_client)
        self.vulnerability_result_api = swagger_client.VulnerabilityResultApi(self.api_client)

def get_all_pages(api_call, **kwargs):
    di = {}
    di["resources"] = []
    page0 = api_call(**kwargs).to_dict()
    di["resources"].extend(page0["resources"])
    total_pages=page0["page"]["total_pages"]
    for page_no in range(1,total_pages,1):
        additional_page = api_call(page=page_no, **kwargs).to_dict()
        di["resources"].extend(additional_page["resources"])
    return di