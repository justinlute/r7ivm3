# -*- coding: utf-8 -*-

import r7ivm3
import configparser
import base64
import keyring

class ClientForHumans:
    def __init__(self, config_file_path=None, client_name="r7ivm"):
        cfg_file = configparser.ConfigParser()
        cfg_file.read(config_file_path)

        # Capture config details from provided config file
        self.hostname = cfg_file['insightvm']['hostname_or_address']
        self.tcp_port = cfg_file['insightvm']['tcp_port']
        if self.tcp_port == '443':
            self.server_url = f"https://{self.hostname}/"
        else:
            self.server_url = f"https://{self.hostname}:{self.tcp_port}/"
        # For use by policies workaround
        self.api_url = f"{self.server_url}api/3/"
        self.api_username = cfg_file['insightvm']['api_username']
        self.wcm_site_name = cfg_file['insightvm']['windows_cred_mgr_site_name']
        # Extract password from Windows Credential Manager
        self.password = keyring.get_password(self.wcm_site_name, self.api_username)

        # Instantiate an instance of the r7_ivm_swag module's Configuration class
        self.config = r7ivm3.Configuration(name=client_name)
        self.config.username = self.api_username
        self.config.password = self.password
        self.config.host = self.server_url
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
        self.api_client = r7ivm3.ApiClient(configuration=self.config)
        self.api_client.default_headers['Authorization'] = "Basic %s" % self.auth

        # Create API resources
        self.administration_api = r7ivm3.AdministrationApi(self.api_client)
        self.asset_api = r7ivm3.AssetApi(self.api_client)
        self.asset_discovery_api = r7ivm3.AssetDiscoveryApi(self.api_client)
        self.asset_group_api = r7ivm3.AssetGroupApi(self.api_client)
        self.credential_api = r7ivm3.CredentialApi(self.api_client)
        self.policy_api = r7ivm3.PolicyApi(self.api_client)
        self.policy_override_api = r7ivm3.PolicyOverrideApi(self.api_client)
        self.remediation_api = r7ivm3.RemediationApi(self.api_client)
        self.report_api = r7ivm3.ReportApi(self.api_client)
        self.root_api = r7ivm3.RootApi(self.api_client)
        self.scan_api = r7ivm3.ScanApi(self.api_client)
        self.scan_engine_api = r7ivm3.ScanEngineApi(self.api_client)
        self.scan_template_api = r7ivm3.ScanTemplateApi(self.api_client)
        self.site_api = r7ivm3.SiteApi(self.api_client)
        self.tag_api = r7ivm3.TagApi(self.api_client)
        self.user_api = r7ivm3.UserApi(self.api_client)
        self.vulnerability_api = r7ivm3.VulnerabilityApi(self.api_client)
        self.vulnerability_check_api = r7ivm3.VulnerabilityCheckApi(self.api_client)
        self.vulnerability_exception_api = r7ivm3.VulnerabilityExceptionApi(self.api_client)
        self.vulnerability_result_api = r7ivm3.VulnerabilityResultApi(self.api_client)

class ConfigurationForHumans:
    def __init__(self, config_file_path=None):
        cfg_file = configparser.ConfigParser()

        try:
            cfg_file.read(config_file_path)
        except:
            AssertionError("Could not locate or could not read configuration file.")

        # Capture config details from provided config file
        self.hostname = cfg_file['insightvm']['hostname_or_address']
        self.tcp_port = cfg_file['insightvm']['tcp_port']
        if self.tcp_port == '443':
            self.server_url = f"https://{self.hostname}/"
        else:
            self.server_url = f"https://{self.hostname}:{self.tcp_port}/"
        # For use by policies workaround
        self.api_url = f"{self.server_url}api/3/"

        # Extract password from Windows Credential Manager
        self.api_username = cfg_file['insightvm']['api_username']
        self.wcm_site_name = cfg_file['insightvm']['windows_cred_mgr_site_name']
        self.password = keyring.get_password(self.wcm_site_name, self.api_username)