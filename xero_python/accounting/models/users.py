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


class Users(BaseModel):
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
    openapi_types = {"users": "list[User]"}

    attribute_map = {"users": "Users"}

    def __init__(self, users=None):  # noqa: E501
        """Users - a model defined in OpenAPI"""  # noqa: E501

        self._users = None
        self.discriminator = None

        if users is not None:
            self.users = users

    @property
    def users(self):
        """Gets the users of this Users.  # noqa: E501


        :return: The users of this Users.  # noqa: E501
        :rtype: list[User]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this Users.


        :param users: The users of this Users.  # noqa: E501
        :type: list[User]
        """

        self._users = users
