# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.2.2
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Overpayments(BaseModel):
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
    openapi_types = {"overpayments": "list[Overpayment]"}

    attribute_map = {"overpayments": "Overpayments"}

    def __init__(self, overpayments=None):  # noqa: E501
        """Overpayments - a model defined in OpenAPI"""  # noqa: E501

        self._overpayments = None
        self.discriminator = None

        if overpayments is not None:
            self.overpayments = overpayments

    @property
    def overpayments(self):
        """Gets the overpayments of this Overpayments.  # noqa: E501


        :return: The overpayments of this Overpayments.  # noqa: E501
        :rtype: list[Overpayment]
        """
        return self._overpayments

    @overpayments.setter
    def overpayments(self, overpayments):
        """Sets the overpayments of this Overpayments.


        :param overpayments: The overpayments of this Overpayments.  # noqa: E501
        :type: list[Overpayment]
        """

        self._overpayments = overpayments
