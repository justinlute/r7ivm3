# r7ivm3.ScanTemplateApi

All URIs are relative to *https://&lt;rapid7_ivm_server_name&gt;/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_scan_template**](ScanTemplateApi.md#create_scan_template) | **POST** /api/3/scan_templates | Scan Templates
[**delete_scan_template**](ScanTemplateApi.md#delete_scan_template) | **DELETE** /api/3/scan_templates/{id} | Scan Template
[**get_scan_template**](ScanTemplateApi.md#get_scan_template) | **GET** /api/3/scan_templates/{id} | Scan Template
[**get_scan_templates**](ScanTemplateApi.md#get_scan_templates) | **GET** /api/3/scan_templates | Scan Templates
[**update_scan_template**](ScanTemplateApi.md#update_scan_template) | **PUT** /api/3/scan_templates/{id} | Scan Template

# **create_scan_template**
> CreatedReferenceScanTemplateIDLink create_scan_template(body=body)

Scan Templates

Creates a new scan template.

### Example
```python
from __future__ import print_function
import time
import r7ivm3
from r7ivm3.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = r7ivm3.ScanTemplateApi()
body = r7ivm3.ScanTemplate() # ScanTemplate | The details of the scan template. (optional)

try:
    # Scan Templates
    api_response = api_instance.create_scan_template(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanTemplateApi->create_scan_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScanTemplate**](ScanTemplate.md)| The details of the scan template. | [optional] 

### Return type

[**CreatedReferenceScanTemplateIDLink**](CreatedReferenceScanTemplateIDLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scan_template**
> Links delete_scan_template(id)

Scan Template

Deletes a scan template.

### Example
```python
from __future__ import print_function
import time
import r7ivm3
from r7ivm3.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = r7ivm3.ScanTemplateApi()
id = 'id_example' # str | The identifier of the scan template

try:
    # Scan Template
    api_response = api_instance.delete_scan_template(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanTemplateApi->delete_scan_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the scan template | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scan_template**
> ScanTemplate get_scan_template(id, view=view)

Scan Template

Returns a scan template.

### Example
```python
from __future__ import print_function
import time
import r7ivm3
from r7ivm3.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = r7ivm3.ScanTemplateApi()
id = 'id_example' # str | The identifier of the scan template
view = 'view_example' # str | The depth for the JSON response. Valid values are 'details' (default) and 'summary' (optional)

try:
    # Scan Template
    api_response = api_instance.get_scan_template(id, view=view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanTemplateApi->get_scan_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the scan template | 
 **view** | **str**| The depth for the JSON response. Valid values are &#x27;details&#x27; (default) and &#x27;summary&#x27; | [optional] 

### Return type

[**ScanTemplate**](ScanTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scan_templates**
> ResourcesScanTemplate get_scan_templates(view=view)

Scan Templates

Returns all scan templates.

### Example
```python
from __future__ import print_function
import time
import r7ivm3
from r7ivm3.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = r7ivm3.ScanTemplateApi()
view = 'view_example' # str | The depth for the JSON response. Valid values are 'details' (default) and 'summary' (optional)

try:
    # Scan Templates
    api_response = api_instance.get_scan_templates(view=view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanTemplateApi->get_scan_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view** | **str**| The depth for the JSON response. Valid values are &#x27;details&#x27; (default) and &#x27;summary&#x27; | [optional] 

### Return type

[**ResourcesScanTemplate**](ResourcesScanTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_scan_template**
> Links update_scan_template(id, body=body)

Scan Template

Updates a scan template.

### Example
```python
from __future__ import print_function
import time
import r7ivm3
from r7ivm3.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = r7ivm3.ScanTemplateApi()
id = 'id_example' # str | The identifier of the scan template
body = r7ivm3.ScanTemplate() # ScanTemplate | The details of the scan template. (optional)

try:
    # Scan Template
    api_response = api_instance.update_scan_template(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanTemplateApi->update_scan_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the scan template | 
 **body** | [**ScanTemplate**](ScanTemplate.md)| The details of the scan template. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

