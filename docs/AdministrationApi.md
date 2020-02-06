# swagger_client.AdministrationApi

All URIs are relative to *https://insightvm.lb.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_license**](AdministrationApi.md#activate_license) | **POST** /api/3/administration/license | License
[**execute_command**](AdministrationApi.md#execute_command) | **POST** /api/3/administration/commands | Console Commands
[**get_info**](AdministrationApi.md#get_info) | **GET** /api/3/administration/info | Information
[**get_license**](AdministrationApi.md#get_license) | **GET** /api/3/administration/license | License
[**get_properties**](AdministrationApi.md#get_properties) | **GET** /api/3/administration/properties | Properties
[**get_settings**](AdministrationApi.md#get_settings) | **GET** /api/3/administration/settings | Settings

# **activate_license**
> Links activate_license(license=license, key=key)

License

Licenses the product with an activation key or a provided license file. If both are provided, the license file is preferred. <span class=\"authorization\">Global Administrator</span>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationApi()
license = 'license_example' # str |  (optional)
key = 'key_example' # str | A license activation key. (optional)

try:
    # License
    api_response = api_instance.activate_license(license=license, key=key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->activate_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license** | **str**|  | [optional] 
 **key** | **str**| A license activation key. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_command**
> ConsoleCommandOutput execute_command(body=body)

Console Commands

Executes a console command against the Security Console. <span class=\"authorization\">Global Administrator</span>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationApi()
body = 'body_example' # str | The console command to execute. (optional)

try:
    # Console Commands
    api_response = api_instance.execute_command(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->execute_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| The console command to execute. | [optional] 

### Return type

[**ConsoleCommandOutput**](ConsoleCommandOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_info**
> Info get_info(view=view)

Information

Returns system details, including host and version information.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationApi()
view = 'view_example' # str | The depth for the JSON response. Valid values are 'details' (default) and 'summary' (optional)

try:
    # Information
    api_response = api_instance.get_info(view=view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->get_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view** | **str**| The depth for the JSON response. Valid values are &#x27;details&#x27; (default) and &#x27;summary&#x27; | [optional] 

### Return type

[**Info**](Info.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license**
> License get_license(view=view)

License

Returns the enabled features and limits of the current license. <span class=\"authorization\">Global Administrator</span>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationApi()
view = 'view_example' # str | The depth for the JSON response. Valid values are 'details' (default) and 'summary' (optional)

try:
    # License
    api_response = api_instance.get_license(view=view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->get_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view** | **str**| The depth for the JSON response. Valid values are &#x27;details&#x27; (default) and &#x27;summary&#x27; | [optional] 

### Return type

[**License**](License.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_properties**
> EnvironmentProperties get_properties(view=view)

Properties

Returns system details, including host and version information.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationApi()
view = 'view_example' # str | The depth for the JSON response. Valid values are 'details' (default) and 'summary' (optional)

try:
    # Properties
    api_response = api_instance.get_properties(view=view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->get_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view** | **str**| The depth for the JSON response. Valid values are &#x27;details&#x27; (default) and &#x27;summary&#x27; | [optional] 

### Return type

[**EnvironmentProperties**](EnvironmentProperties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings**
> Settings get_settings(view=view)

Settings

Returns the current administration settings. <span class=\"authorization\">Global Administrator</span>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationApi()
view = 'view_example' # str | The depth for the JSON response. Valid values are 'details' (default) and 'summary' (optional)

try:
    # Settings
    api_response = api_instance.get_settings(view=view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->get_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view** | **str**| The depth for the JSON response. Valid values are &#x27;details&#x27; (default) and &#x27;summary&#x27; | [optional] 

### Return type

[**Settings**](Settings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

