import typing_extensions

from memas_sdk.paths import PathValues
from memas_sdk.apis.paths.dp_memorize import DpMemorize
from memas_sdk.apis.paths.dp_recall import DpRecall
from memas_sdk.apis.paths.cp_user import CpUser
from memas_sdk.apis.paths.cp_corpus import CpCorpus

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.DP_MEMORIZE: DpMemorize,
        PathValues.DP_RECALL: DpRecall,
        PathValues.CP_USER: CpUser,
        PathValues.CP_CORPUS: CpCorpus,
    }
)

path_to_api = PathToApi(
    {
        PathValues.DP_MEMORIZE: DpMemorize,
        PathValues.DP_RECALL: DpRecall,
        PathValues.CP_USER: CpUser,
        PathValues.CP_CORPUS: CpCorpus,
    }
)
