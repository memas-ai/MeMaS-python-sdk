# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from memas_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from memas_sdk.model.citation import Citation
from memas_sdk.model.cited_document import CitedDocument
from memas_sdk.model.corpus_pathname import CorpusPathname
from memas_sdk.model.corpus_type import CorpusType
from memas_sdk.model.namespace_does_not_exist_error import NamespaceDoesNotExistError
from memas_sdk.model.namespace_exist_error import NamespaceExistError
from memas_sdk.model.namespace_illegal_name_error import NamespaceIllegalNameError
from memas_sdk.model.namespace_pathname import NamespacePathname
