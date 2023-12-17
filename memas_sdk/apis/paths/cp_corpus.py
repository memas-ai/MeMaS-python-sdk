from memas_sdk.paths.cp_corpus.post import ApiForpost
from memas_sdk.paths.cp_corpus.delete import ApiFordelete


class CpCorpus(
    ApiForpost,
    ApiFordelete,
):
    pass
