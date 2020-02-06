# swagger_client.ScanApi

All URIs are relative to *https://<rapid7_insightvm_server>/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_scan**](ScanApi.md#get_scan) | **GET** /api/3/scans/{id} | Scan
[**get_scans**](ScanApi.md#get_scans) | **GET** /api/3/scans | Scans
[**get_site_scans**](ScanApi.md#get_site_scans) | **GET** /api/3/sites/{id}/scans | Site Scans
[**set_scan_status**](ScanApi.md#set_scan_status) | **POST** /api/3/scans/{id}/{status} | Scan Status
[**start_scan**](ScanApi.md#start_scan) | **POST** /api/3/sites/{id}/scans | Site Scans

# **get_scan**
> Scan get_scan(id, view=view)

Scan

Returns the specified scan.

### Example
```python
from __future__ import print_function
import time
import r7ivm3
from r7ivm3.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = r7ivm3.ScanApi()
id = 789 # int | The identifier of the scan.
view = 'view_example' # str | The depth for the JSON response. Valid values are 'details' (default) and 'summary' (optional)

try:
    # Scan
    api_response = api_instance.get_scan(id, view=view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanApi->get_scan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the scan. | 
 **view** | **str**| The depth for the JSON response. Valid values are &#x27;details&#x27; (default) and &#x27;summary&#x27; | [optional] 

### Return type

[**Scan**](Scan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scans**
> PageOfGlobalScan get_scans(active=active, page=page, size=size, sort=sort, view=view)

Scans

Returns all scans.

### Example
```python
from __future__ import print_function
import time
import r7ivm3
from r7ivm3.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = r7ivm3.ScanApi()
active = true # bool | Return running scans or past scans (true/false value). (optional)
page = 56 # int | The index of the page (zero-based) to retrieve. (optional)
size = 56 # int | The number of records per page to retrieve. (optional)
sort = ['sort_example'] # list[str] | The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. (optional)
view = 'view_example' # str | The depth for the JSON response. Valid values are 'details' (default) and 'summary' (optional)

try:
    # Scans
    api_response = api_instance.get_scans(active=active, page=page, size=size, sort=sort, view=view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanApi->get_scans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **bool**| Return running scans or past scans (true/false value). | [optional] 
 **page** | **int**| The index of the page (zero-based) to retrieve. | [optional] 
 **size** | **int**| The number of records per page to retrieve. | [optional] 
 **sort** | [**list[str]**](str.md)| The criteria to sort the records by, in the format: &#x60;property[,ASC|DESC]&#x60;. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. | [optional] 
 **view** | **str**| The depth for the JSON response. Valid values are &#x27;details&#x27; (default) and &#x27;summary&#x27; | [optional] 

### Return type

[**PageOfGlobalScan**](PageOfGlobalScan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_scans**
> PageOfScan get_site_scans(id, active=active, page=page, size=size, sort=sort, view=view)

Site Scans

Returns the scans for the specified site.

### Example
```python
from __future__ import print_function
import time
import r7ivm3
from r7ivm3.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = r7ivm3.ScanApi()
id = 56 # int | The identifier of the site.
active = true # bool | Return running scans or past scans (true/false value). (optional)
page = 56 # int | The index of the page (zero-based) to retrieve. (optional)
size = 56 # int | The number of records per page to retrieve. (optional)
sort = ['sort_example'] # list[str] | The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. (optional)
view = 'view_example' # str | The depth for the JSON response. Valid values are 'details' (default) and 'summary' (optional)

try:
    # Site Scans
    api_response = api_instance.get_site_scans(id, active=active, page=page, size=size, sort=sort, view=view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanApi->get_site_scans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **active** | **bool**| Return running scans or past scans (true/false value). | [optional] 
 **page** | **int**| The index of the page (zero-based) to retrieve. | [optional] 
 **size** | **int**| The number of records per page to retrieve. | [optional] 
 **sort** | [**list[str]**](str.md)| The criteria to sort the records by, in the format: &#x60;property[,ASC|DESC]&#x60;. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. | [optional] 
 **view** | **str**| The depth for the JSON response. Valid values are &#x27;details&#x27; (default) and &#x27;summary&#x27; | [optional] 

### Return type

[**PageOfScan**](PageOfScan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_scan_status**
> Links set_scan_status(id, status)

Scan Status

Updates the scan status. Can pause, resume, and stop scans using this resource. In order to stop a scan the scan must be running or paused. In order to resume a scan the scan must be paused. In order to pause a scan the scan must be running.

### Example
```python
from __future__ import print_function
import time
import r7ivm3
from r7ivm3.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = r7ivm3.ScanApi()
id = 789 # int | The identifier of the scan.
status = 'status_example' # str | The status of the scan.

try:
    # Scan Status
    api_response = api_instance.set_scan_status(id, status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanApi->set_scan_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the scan. | 
 **status** | **str**| The status of the scan. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_scan**
> CreatedReferenceScanIDLink start_scan(id, body=body, override_blackout=override_blackout)

Site Scans

Starts a scan for the specified site.

### Example
```python
from __future__ import print_function
import time
import r7ivm3
from r7ivm3.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = r7ivm3.ScanApi()
id = 56 # int | The identifier of the site.
body = r7ivm3.AdhocScan() # AdhocScan | The details for the scan. (optional)
override_blackout = true # bool | Whether to request for the override of an scan blackout window. (optional)

try:
    # Site Scans
    api_response = api_instance.start_scan(id, body=body, override_blackout=override_blackout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanApi->start_scan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **body** | [**AdhocScan**](AdhocScan.md)| The details for the scan. | [optional] 
 **override_blackout** | **bool**| Whether to request for the override of an scan blackout window. | [optional] 

### Return type

[**CreatedReferenceScanIDLink**](CreatedReferenceScanIDLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

