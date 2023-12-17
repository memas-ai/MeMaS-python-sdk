import typing_extensions

from memas_sdk.apis.tags import TagValues
from memas_sdk.apis.tags.cp_api import CpApi
from memas_sdk.apis.tags.dp_api import DpApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.CP: CpApi,
        TagValues.DP: DpApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.CP: CpApi,
        TagValues.DP: DpApi,
    }
)
