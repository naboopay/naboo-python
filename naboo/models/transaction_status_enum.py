# coding: utf-8

"""
    NabooApi V1

    Here you have the first version of the naboo api to create checkout automatically

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TransactionStatusEnum(str, Enum):
    """
    TransactionStatusEnum
    """

    """
    allowed enum values
    """
    PENDING = 'pending'
    PAID = 'paid'
    DONE = 'done'
    PART_PAID = 'part_paid'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TransactionStatusEnum from a JSON string"""
        return cls(json.loads(json_str))


