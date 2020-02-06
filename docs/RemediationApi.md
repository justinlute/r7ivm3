# swagger_client.RemediationApi

All URIs are relative to *https://<rapid7_insightvm_server>/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_vulnerability_solutions**](RemediationApi.md#get_asset_vulnerability_solutions) | **GET** /api/3/assets/{id}/vulnerabilities/{vulnerabilityId}/solution | Asset Vulnerability Solution

# **get_asset_vulnerability_solutions**
> ResourcesMatchedSolution get_asset_vulnerability_solutions(id, vulnerability_id, view=view)

Asset Vulnerability Solution

Returns the highest-superceding rollup solutions for a vulnerability on an asset. The solution(s) selected will be the most recent and cost-effective means by which the vulnerability can be remediated.

### Example
```python
from __future__ import print_function
import time
import r7ivm3
from r7ivm3.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = r7ivm3.RemediationApi()
id = 789 # int | The identifier of the asset.
vulnerability_id = 'vulnerability_id_example' # str | The identifier of the vulnerability.
view = 'view_example' # str | The depth for the JSON response. Valid values are 'details' (default) and 'summary' (optional)

try:
    # Asset Vulnerability Solution
    api_response = api_instance.get_asset_vulnerability_solutions(id, vulnerability_id, view=view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemediationApi->get_asset_vulnerability_solutions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset. | 
 **vulnerability_id** | **str**| The identifier of the vulnerability. | 
 **view** | **str**| The depth for the JSON response. Valid values are &#x27;details&#x27; (default) and &#x27;summary&#x27; | [optional] 

### Return type

[**ResourcesMatchedSolution**](ResourcesMatchedSolution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

