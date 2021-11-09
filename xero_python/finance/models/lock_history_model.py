# coding: utf-8

"""
    Xero Finance API

    The Finance API is a collection of endpoints which customers can use in the course of a loan application, which may assist lenders to gain the confidence they need to provide capital.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class LockHistoryModel(BaseModel):
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
        "hard_lock_date": "date",
        "soft_lock_date": "date",
        "updated_date_utc": "datetime",
    }

    attribute_map = {
        "hard_lock_date": "hardLockDate",
        "soft_lock_date": "softLockDate",
        "updated_date_utc": "updatedDateUtc",
    }

    def __init__(
        self, hard_lock_date=None, soft_lock_date=None, updated_date_utc=None
    ):  # noqa: E501
        """LockHistoryModel - a model defined in OpenAPI"""  # noqa: E501

        self._hard_lock_date = None
        self._soft_lock_date = None
        self._updated_date_utc = None
        self.discriminator = None

        if hard_lock_date is not None:
            self.hard_lock_date = hard_lock_date
        if soft_lock_date is not None:
            self.soft_lock_date = soft_lock_date
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc

    @property
    def hard_lock_date(self):
        """Gets the hard_lock_date of this LockHistoryModel.  # noqa: E501

        Date the account hard lock was set  # noqa: E501

        :return: The hard_lock_date of this LockHistoryModel.  # noqa: E501
        :rtype: date
        """
        return self._hard_lock_date

    @hard_lock_date.setter
    def hard_lock_date(self, hard_lock_date):
        """Sets the hard_lock_date of this LockHistoryModel.

        Date the account hard lock was set  # noqa: E501

        :param hard_lock_date: The hard_lock_date of this LockHistoryModel.  # noqa: E501
        :type: date
        """

        self._hard_lock_date = hard_lock_date

    @property
    def soft_lock_date(self):
        """Gets the soft_lock_date of this LockHistoryModel.  # noqa: E501

        Date the account soft lock was set  # noqa: E501

        :return: The soft_lock_date of this LockHistoryModel.  # noqa: E501
        :rtype: date
        """
        return self._soft_lock_date

    @soft_lock_date.setter
    def soft_lock_date(self, soft_lock_date):
        """Sets the soft_lock_date of this LockHistoryModel.

        Date the account soft lock was set  # noqa: E501

        :param soft_lock_date: The soft_lock_date of this LockHistoryModel.  # noqa: E501
        :type: date
        """

        self._soft_lock_date = soft_lock_date

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this LockHistoryModel.  # noqa: E501

        The system date time that the lock was updated  # noqa: E501

        :return: The updated_date_utc of this LockHistoryModel.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this LockHistoryModel.

        The system date time that the lock was updated  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this LockHistoryModel.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc
