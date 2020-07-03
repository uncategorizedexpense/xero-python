# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.2.6
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Prepayments(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"prepayments": "list[Prepayment]"}

    attribute_map = {"prepayments": "Prepayments"}

    def __init__(self, prepayments=None):  # noqa: E501
        """Prepayments - a model defined in OpenAPI"""  # noqa: E501

        self._prepayments = None
        self.discriminator = None

        if prepayments is not None:
            self.prepayments = prepayments

    @property
    def prepayments(self):
        """Gets the prepayments of this Prepayments.  # noqa: E501


        :return: The prepayments of this Prepayments.  # noqa: E501
        :rtype: list[Prepayment]
        """
        return self._prepayments

    @prepayments.setter
    def prepayments(self, prepayments):
        """Sets the prepayments of this Prepayments.


        :param prepayments: The prepayments of this Prepayments.  # noqa: E501
        :type: list[Prepayment]
        """

        self._prepayments = prepayments
