# coding: utf-8

"""
    MeMaS APIs

    This is the Control Plane and Data Plane APIs for MeMaS (Memory Management Service). See https://github.com/memas-ai/MeMaS for more details.  # noqa: E501

    The version of the OpenAPI document: 0.1.1
    Contact: max.yu@memas.ai
    Generated by: https://openapi-generator.tech
"""

from memas_sdk.paths.dp_memorize.post import Memorize
from memas_sdk.paths.dp_recall.get import Recall


class DpApi(
    Memorize,
    Recall,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass