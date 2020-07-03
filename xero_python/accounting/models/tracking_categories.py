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


class TrackingCategories(BaseModel):
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
    openapi_types = {"tracking_categories": "list[TrackingCategory]"}

    attribute_map = {"tracking_categories": "TrackingCategories"}

    def __init__(self, tracking_categories=None):  # noqa: E501
        """TrackingCategories - a model defined in OpenAPI"""  # noqa: E501

        self._tracking_categories = None
        self.discriminator = None

        if tracking_categories is not None:
            self.tracking_categories = tracking_categories

    @property
    def tracking_categories(self):
        """Gets the tracking_categories of this TrackingCategories.  # noqa: E501


        :return: The tracking_categories of this TrackingCategories.  # noqa: E501
        :rtype: list[TrackingCategory]
        """
        return self._tracking_categories

    @tracking_categories.setter
    def tracking_categories(self, tracking_categories):
        """Sets the tracking_categories of this TrackingCategories.


        :param tracking_categories: The tracking_categories of this TrackingCategories.  # noqa: E501
        :type: list[TrackingCategory]
        """

        self._tracking_categories = tracking_categories
