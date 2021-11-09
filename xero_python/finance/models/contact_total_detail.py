# coding: utf-8

"""
    Xero Finance API

    The Finance API is a collection of endpoints which customers can use in the course of a loan application, which may assist lenders to gain the confidence they need to provide capital.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class ContactTotalDetail(BaseModel):
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
    openapi_types = {
        "total_paid": "float",
        "total_outstanding": "float",
        "total_credited_un_applied": "float",
    }

    attribute_map = {
        "total_paid": "totalPaid",
        "total_outstanding": "totalOutstanding",
        "total_credited_un_applied": "totalCreditedUnApplied",
    }

    def __init__(
        self, total_paid=None, total_outstanding=None, total_credited_un_applied=None
    ):  # noqa: E501
        """ContactTotalDetail - a model defined in OpenAPI"""  # noqa: E501

        self._total_paid = None
        self._total_outstanding = None
        self._total_credited_un_applied = None
        self.discriminator = None

        if total_paid is not None:
            self.total_paid = total_paid
        if total_outstanding is not None:
            self.total_outstanding = total_outstanding
        if total_credited_un_applied is not None:
            self.total_credited_un_applied = total_credited_un_applied

    @property
    def total_paid(self):
        """Gets the total_paid of this ContactTotalDetail.  # noqa: E501

        Total paid invoice and cash value for the contact within the period.  # noqa: E501

        :return: The total_paid of this ContactTotalDetail.  # noqa: E501
        :rtype: float
        """
        return self._total_paid

    @total_paid.setter
    def total_paid(self, total_paid):
        """Sets the total_paid of this ContactTotalDetail.

        Total paid invoice and cash value for the contact within the period.  # noqa: E501

        :param total_paid: The total_paid of this ContactTotalDetail.  # noqa: E501
        :type: float
        """

        self._total_paid = total_paid

    @property
    def total_outstanding(self):
        """Gets the total_outstanding of this ContactTotalDetail.  # noqa: E501

        Total outstanding invoice value for the contact within the period.  # noqa: E501

        :return: The total_outstanding of this ContactTotalDetail.  # noqa: E501
        :rtype: float
        """
        return self._total_outstanding

    @total_outstanding.setter
    def total_outstanding(self, total_outstanding):
        """Sets the total_outstanding of this ContactTotalDetail.

        Total outstanding invoice value for the contact within the period.  # noqa: E501

        :param total_outstanding: The total_outstanding of this ContactTotalDetail.  # noqa: E501
        :type: float
        """

        self._total_outstanding = total_outstanding

    @property
    def total_credited_un_applied(self):
        """Gets the total_credited_un_applied of this ContactTotalDetail.  # noqa: E501

        Total unapplied credited value for the contact within the period.  # noqa: E501

        :return: The total_credited_un_applied of this ContactTotalDetail.  # noqa: E501
        :rtype: float
        """
        return self._total_credited_un_applied

    @total_credited_un_applied.setter
    def total_credited_un_applied(self, total_credited_un_applied):
        """Sets the total_credited_un_applied of this ContactTotalDetail.

        Total unapplied credited value for the contact within the period.  # noqa: E501

        :param total_credited_un_applied: The total_credited_un_applied of this ContactTotalDetail.  # noqa: E501
        :type: float
        """

        self._total_credited_un_applied = total_credited_un_applied
