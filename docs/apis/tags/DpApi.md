<a id="__pageTop"></a>
# memas_sdk.apis.tags.dp_api.DpApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**memorize**](#memorize) | **post** /dp/memorize | Memorize information
[**recall**](#recall) | **get** /dp/recall | Recalls information

# **memorize**
<a id="memorize"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} memorize(any_type)

Memorize information

Memorize information

### Example

```python
import memas_sdk
from memas_sdk.apis.tags import dp_api
from memas_sdk.model.namespace_does_not_exist_error import NamespaceDoesNotExistError
from memas_sdk.model.namespace_illegal_name_error import NamespaceIllegalNameError
from memas_sdk.model.cited_document import CitedDocument
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = memas_sdk.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with memas_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dp_api.DpApi(api_client)

    # example passing only required values which don't have defaults set
    body = None
    try:
        # Memorize information
        api_response = api_instance.memorize(
            body=body,
        )
        pprint(api_response)
    except memas_sdk.ApiException as e:
        print("Exception when calling DpApi->memorize: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[CitedDocument]({{complexTypePrefix}}CitedDocument.md) | [**CitedDocument**]({{complexTypePrefix}}CitedDocument.md) | [**CitedDocument**]({{complexTypePrefix}}CitedDocument.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
[all_of_2](#all_of_2) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
[all_of_3](#all_of_3) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_2

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# all_of_3

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**corpus_pathname** | str,  | str,  | Full name of a corpus, specifying which namespace the corpus is under.  The name takes on the format of \\\&quot;&lt;namespace_pathname&gt;:&lt;corpus_name&gt;\\\&quot; | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#memorize.ApiResponseFor200) | Successful Operation
400 | [ApiResponseFor400](#memorize.ApiResponseFor400) | Failed operation

#### memorize.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**success** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### memorize.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[NamespaceDoesNotExistError]({{complexTypePrefix}}NamespaceDoesNotExistError.md) | [**NamespaceDoesNotExistError**]({{complexTypePrefix}}NamespaceDoesNotExistError.md) | [**NamespaceDoesNotExistError**]({{complexTypePrefix}}NamespaceDoesNotExistError.md) |  | 
[NamespaceIllegalNameError]({{complexTypePrefix}}NamespaceIllegalNameError.md) | [**NamespaceIllegalNameError**]({{complexTypePrefix}}NamespaceIllegalNameError.md) | [**NamespaceIllegalNameError**]({{complexTypePrefix}}NamespaceIllegalNameError.md) |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **recall**
<a id="recall"></a>
> [CitedDocument] recall(any_type)

Recalls information

Recalls relevant information related to the given clue

### Example

```python
import memas_sdk
from memas_sdk.apis.tags import dp_api
from memas_sdk.model.namespace_does_not_exist_error import NamespaceDoesNotExistError
from memas_sdk.model.namespace_illegal_name_error import NamespaceIllegalNameError
from memas_sdk.model.cited_document import CitedDocument
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = memas_sdk.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with memas_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dp_api.DpApi(api_client)

    # example passing only required values which don't have defaults set
    body = dict(
        clue="What's the weather?",
        corpus_pathname="memas:wikipedia",
    )
    try:
        # Recalls information
        api_response = api_instance.recall(
            body=body,
        )
        pprint(api_response)
    except memas_sdk.ApiException as e:
        print("Exception when calling DpApi->recall: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**clue** | str,  | str,  |  | 
**corpus_pathname** | str,  | str,  | Full name of a corpus, specifying which namespace the corpus is under.  The name takes on the format of \\\&quot;&lt;namespace_pathname&gt;:&lt;corpus_name&gt;\\\&quot; | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#recall.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#recall.ApiResponseFor400) | Failed operation

#### recall.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CitedDocument**]({{complexTypePrefix}}CitedDocument.md) | [**CitedDocument**]({{complexTypePrefix}}CitedDocument.md) | [**CitedDocument**]({{complexTypePrefix}}CitedDocument.md) |  | 

#### recall.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[NamespaceDoesNotExistError]({{complexTypePrefix}}NamespaceDoesNotExistError.md) | [**NamespaceDoesNotExistError**]({{complexTypePrefix}}NamespaceDoesNotExistError.md) | [**NamespaceDoesNotExistError**]({{complexTypePrefix}}NamespaceDoesNotExistError.md) |  | 
[NamespaceIllegalNameError]({{complexTypePrefix}}NamespaceIllegalNameError.md) | [**NamespaceIllegalNameError**]({{complexTypePrefix}}NamespaceIllegalNameError.md) | [**NamespaceIllegalNameError**]({{complexTypePrefix}}NamespaceIllegalNameError.md) |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

