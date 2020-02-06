# swagger_client.CredentialApi

All URIs are relative to *https://<rapid7_insightvm_server>/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_shared_credential**](CredentialApi.md#create_shared_credential) | **POST** /api/3/shared_credentials | Shared Credentials
[**delete_all_shared_credentials**](CredentialApi.md#delete_all_shared_credentials) | **DELETE** /api/3/shared_credentials | Shared Credentials
[**delete_shared_credential**](CredentialApi.md#delete_shared_credential) | **DELETE** /api/3/shared_credentials/{id} | Shared Credential
[**get_shared_credential**](CredentialApi.md#get_shared_credential) | **GET** /api/3/shared_credentials/{id} | Shared Credential
[**get_shared_credentials**](CredentialApi.md#get_shared_credentials) | **GET** /api/3/shared_credentials | Shared Credentials
[**update_shared_credential**](CredentialApi.md#update_shared_credential) | **PUT** /api/3/shared_credentials/{id} | Shared Credential

# **create_shared_credential**
> CreatedReferenceCredentialIDLink create_shared_credential(body=body)

Shared Credentials

Creates a new shared credential.

### Example
```python
from __future__ import print_function
import time
import r7ivm3
from r7ivm3.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = r7ivm3.CredentialApi()
body = r7ivm3.SharedCredential() # SharedCredential | The specification of a shared credential. (optional)

try:
    # Shared Credentials
    api_response = api_instance.create_shared_credential(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialApi->create_shared_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SharedCredential**](SharedCredential.md)| The specification of a shared credential. | [optional] 

### Return type

[**CreatedReferenceCredentialIDLink**](CreatedReferenceCredentialIDLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_shared_credentials**
> Links delete_all_shared_credentials()

Shared Credentials

Deletes all shared credentials.

### Example
```python
from __future__ import print_function
import time
import r7ivm3
from r7ivm3.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = r7ivm3.CredentialApi()

try:
    # Shared Credentials
    api_response = api_instance.delete_all_shared_credentials()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialApi->delete_all_shared_credentials: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shared_credential**
> Links delete_shared_credential(id)

Shared Credential

Deletes the specified shared scan credential.

### Example
```python
from __future__ import print_function
import time
import r7ivm3
from r7ivm3.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = r7ivm3.CredentialApi()
id = 56 # int | The identifier of the credential.

try:
    # Shared Credential
    api_response = api_instance.delete_shared_credential(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialApi->delete_shared_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the credential. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_credential**
> SharedCredential get_shared_credential(id, view=view)

Shared Credential

Retrieves the specified shared credential.

### Example
```python
from __future__ import print_function
import time
import r7ivm3
from r7ivm3.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = r7ivm3.CredentialApi()
id = 56 # int | The identifier of the credential.
view = 'view_example' # str | The depth for the JSON response. Valid values are 'details' (default) and 'summary' (optional)

try:
    # Shared Credential
    api_response = api_instance.get_shared_credential(id, view=view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialApi->get_shared_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the credential. | 
 **view** | **str**| The depth for the JSON response. Valid values are &#x27;details&#x27; (default) and &#x27;summary&#x27; | [optional] 

### Return type

[**SharedCredential**](SharedCredential.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_credentials**
> ResourcesSharedCredential get_shared_credentials(view=view)

Shared Credentials

Retrieves all defined shared credential resources.

### Example
```python
from __future__ import print_function
import time
import r7ivm3
from r7ivm3.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = r7ivm3.CredentialApi()
view = 'view_example' # str | The depth for the JSON response. Valid values are 'details' (default) and 'summary' (optional)

try:
    # Shared Credentials
    api_response = api_instance.get_shared_credentials(view=view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialApi->get_shared_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view** | **str**| The depth for the JSON response. Valid values are &#x27;details&#x27; (default) and &#x27;summary&#x27; | [optional] 

### Return type

[**ResourcesSharedCredential**](ResourcesSharedCredential.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shared_credential**
> Links update_shared_credential(id, body=body)

Shared Credential

Updates the specified shared credential.

### Example
```python
from __future__ import print_function
import time
import r7ivm3
from r7ivm3.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = r7ivm3.CredentialApi()
id = 56 # int | The identifier of the credential.
body = r7ivm3.SharedCredential() # SharedCredential | The specification of the shared credential to update. (optional)

try:
    # Shared Credential
    api_response = api_instance.update_shared_credential(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialApi->update_shared_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the credential. | 
 **body** | [**SharedCredential**](SharedCredential.md)| The specification of the shared credential to update. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

