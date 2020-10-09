# coding: utf-8

"""
    Xero Payroll AU

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    OpenAPI spec version: 2.3.4
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class SuperFunds(BaseModel):
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
    openapi_types = {"super_funds": "list[SuperFund]"}

    attribute_map = {"super_funds": "SuperFunds"}

    def __init__(self, super_funds=None):  # noqa: E501
        """SuperFunds - a model defined in OpenAPI"""  # noqa: E501

        self._super_funds = None
        self.discriminator = None

        if super_funds is not None:
            self.super_funds = super_funds

    @property
    def super_funds(self):
        """Gets the super_funds of this SuperFunds.  # noqa: E501


        :return: The super_funds of this SuperFunds.  # noqa: E501
        :rtype: list[SuperFund]
        """
        return self._super_funds

    @super_funds.setter
    def super_funds(self, super_funds):
        """Sets the super_funds of this SuperFunds.


        :param super_funds: The super_funds of this SuperFunds.  # noqa: E501
        :type: list[SuperFund]
        """

        self._super_funds = super_funds
