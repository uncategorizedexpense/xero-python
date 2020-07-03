# coding: utf-8

"""
    Xero Projects API

    This is the Xero Projects API  # noqa: E501

    OpenAPI spec version: 2.2.6
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Projects(BaseModel):
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
    openapi_types = {"pagination": "Pagination", "items": "list[Project]"}

    attribute_map = {"pagination": "pagination", "items": "items"}

    def __init__(self, pagination=None, items=None):  # noqa: E501
        """Projects - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._items = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if items is not None:
            self.items = items

    @property
    def pagination(self):
        """Gets the pagination of this Projects.  # noqa: E501


        :return: The pagination of this Projects.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this Projects.


        :param pagination: The pagination of this Projects.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def items(self):
        """Gets the items of this Projects.  # noqa: E501


        :return: The items of this Projects.  # noqa: E501
        :rtype: list[Project]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this Projects.


        :param items: The items of this Projects.  # noqa: E501
        :type: list[Project]
        """

        self._items = items
