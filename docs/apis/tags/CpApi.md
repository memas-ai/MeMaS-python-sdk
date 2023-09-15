<a id="__pageTop"></a>
# memas_sdk.apis.tags.cp_api.CpApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_corpus**](#create_corpus) | **post** /cp/create_corpus | Create corpus
[**create_user**](#create_user) | **post** /cp/create_user | Create user

# **create_corpus**
<a id="create_corpus"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_corpus(any_type)

Create corpus

Create a corpus under a namespace

### Example

```python
import memas_sdk
from memas_sdk.apis.tags import cp_api
from memas_sdk.model.namespace_exist_error import NamespaceExistError
from memas_sdk.model.namespace_illegal_name_error import NamespaceIllegalNameError
from memas_sdk.model.corpus_type import CorpusType
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = memas_sdk.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with memas_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cp_api.CpApi(api_client)

    # example passing only required values which don't have defaults set
    body = dict(
        corpus_pathname="memas.wikipedia",
        corpus_type=CorpusType("knowledge"),
    )
    try:
        # Create corpus
        api_response = api_instance.create_corpus(
            body=body,
        )
        pprint(api_response)
    except memas_sdk.ApiException as e:
        print("Exception when calling CpApi->create_corpus: %s\n" % e)
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
**corpus_pathname** | str,  | str,  | full corpus name | 
**corpus_type** | [**CorpusType**]({{complexTypePrefix}}CorpusType.md) | [**CorpusType**]({{complexTypePrefix}}CorpusType.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_corpus.ApiResponseFor200) | Successful Operation
400 | [ApiResponseFor400](#create_corpus.ApiResponseFor400) | Failed operation

#### create_corpus.ApiResponseFor200
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

#### create_corpus.ApiResponseFor400
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
[NamespaceExistError]({{complexTypePrefix}}NamespaceExistError.md) | [**NamespaceExistError**]({{complexTypePrefix}}NamespaceExistError.md) | [**NamespaceExistError**]({{complexTypePrefix}}NamespaceExistError.md) |  | 
[NamespaceIllegalNameError]({{complexTypePrefix}}NamespaceIllegalNameError.md) | [**NamespaceIllegalNameError**]({{complexTypePrefix}}NamespaceIllegalNameError.md) | [**NamespaceIllegalNameError**]({{complexTypePrefix}}NamespaceIllegalNameError.md) |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_user**
<a id="create_user"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_user(any_type)

Create user

Create a namespace user

### Example

```python
import memas_sdk
from memas_sdk.apis.tags import cp_api
from memas_sdk.model.namespace_exist_error import NamespaceExistError
from memas_sdk.model.namespace_illegal_name_error import NamespaceIllegalNameError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = memas_sdk.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with memas_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cp_api.CpApi(api_client)

    # example passing only required values which don't have defaults set
    body = dict(
        namespace_pathname="memas.chatbot.persona1",
    )
    try:
        # Create user
        api_response = api_instance.create_user(
            body=body,
        )
        pprint(api_response)
    except memas_sdk.ApiException as e:
        print("Exception when calling CpApi->create_user: %s\n" % e)
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
**namespace_pathname** | str,  | str,  | Full namespace name, where child namespaces are appended after their parents&#x27; names with &#x27;.&#x27; | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_user.ApiResponseFor200) | Successful Operation
400 | [ApiResponseFor400](#create_user.ApiResponseFor400) | Failed operation

#### create_user.ApiResponseFor200
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

#### create_user.ApiResponseFor400
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
[NamespaceExistError]({{complexTypePrefix}}NamespaceExistError.md) | [**NamespaceExistError**]({{complexTypePrefix}}NamespaceExistError.md) | [**NamespaceExistError**]({{complexTypePrefix}}NamespaceExistError.md) |  | 
[NamespaceIllegalNameError]({{complexTypePrefix}}NamespaceIllegalNameError.md) | [**NamespaceIllegalNameError**]({{complexTypePrefix}}NamespaceIllegalNameError.md) | [**NamespaceIllegalNameError**]({{complexTypePrefix}}NamespaceIllegalNameError.md) |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

