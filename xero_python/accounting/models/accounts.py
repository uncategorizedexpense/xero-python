# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.3.4
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Accounts(BaseModel):
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
    openapi_types = {"accounts": "list[Account]"}

    attribute_map = {"accounts": "Accounts"}

    def __init__(self, accounts=None):  # noqa: E501
        """Accounts - a model defined in OpenAPI"""  # noqa: E501

        self._accounts = None
        self.discriminator = None

        if accounts is not None:
            self.accounts = accounts

    @property
    def accounts(self):
        """Gets the accounts of this Accounts.  # noqa: E501


        :return: The accounts of this Accounts.  # noqa: E501
        :rtype: list[Account]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this Accounts.


        :param accounts: The accounts of this Accounts.  # noqa: E501
        :type: list[Account]
        """

        self._accounts = accounts
