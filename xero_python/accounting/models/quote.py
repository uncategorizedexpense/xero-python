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


class Quote(BaseModel):
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
        "quote_id": "str",
        "quote_number": "str",
        "reference": "str",
        "terms": "str",
        "contact": "Contact",
        "line_items": "list[LineItem]",
        "date": "date[ms-format]",
        "date_string": "str",
        "expiry_date": "date[ms-format]",
        "expiry_date_string": "str",
        "status": "QuoteStatusCodes",
        "currency_code": "CurrencyCode",
        "currency_rate": "float",
        "sub_total": "float",
        "total_tax": "float",
        "total": "float",
        "total_discount": "float",
        "title": "str",
        "summary": "str",
        "branding_theme_id": "str",
        "updated_date_utc": "datetime[ms-format]",
        "line_amount_types": "QuoteLineAmountTypes",
        "status_attribute_string": "str",
        "validation_errors": "list[ValidationError]",
    }

    attribute_map = {
        "quote_id": "QuoteID",
        "quote_number": "QuoteNumber",
        "reference": "Reference",
        "terms": "Terms",
        "contact": "Contact",
        "line_items": "LineItems",
        "date": "Date",
        "date_string": "DateString",
        "expiry_date": "ExpiryDate",
        "expiry_date_string": "ExpiryDateString",
        "status": "Status",
        "currency_code": "CurrencyCode",
        "currency_rate": "CurrencyRate",
        "sub_total": "SubTotal",
        "total_tax": "TotalTax",
        "total": "Total",
        "total_discount": "TotalDiscount",
        "title": "Title",
        "summary": "Summary",
        "branding_theme_id": "BrandingThemeID",
        "updated_date_utc": "UpdatedDateUTC",
        "line_amount_types": "LineAmountTypes",
        "status_attribute_string": "StatusAttributeString",
        "validation_errors": "ValidationErrors",
    }

    def __init__(
        self,
        quote_id=None,
        quote_number=None,
        reference=None,
        terms=None,
        contact=None,
        line_items=None,
        date=None,
        date_string=None,
        expiry_date=None,
        expiry_date_string=None,
        status=None,
        currency_code=None,
        currency_rate=None,
        sub_total=None,
        total_tax=None,
        total=None,
        total_discount=None,
        title=None,
        summary=None,
        branding_theme_id=None,
        updated_date_utc=None,
        line_amount_types=None,
        status_attribute_string=None,
        validation_errors=None,
    ):  # noqa: E501
        """Quote - a model defined in OpenAPI"""  # noqa: E501

        self._quote_id = None
        self._quote_number = None
        self._reference = None
        self._terms = None
        self._contact = None
        self._line_items = None
        self._date = None
        self._date_string = None
        self._expiry_date = None
        self._expiry_date_string = None
        self._status = None
        self._currency_code = None
        self._currency_rate = None
        self._sub_total = None
        self._total_tax = None
        self._total = None
        self._total_discount = None
        self._title = None
        self._summary = None
        self._branding_theme_id = None
        self._updated_date_utc = None
        self._line_amount_types = None
        self._status_attribute_string = None
        self._validation_errors = None
        self.discriminator = None

        if quote_id is not None:
            self.quote_id = quote_id
        if quote_number is not None:
            self.quote_number = quote_number
        if reference is not None:
            self.reference = reference
        if terms is not None:
            self.terms = terms
        if contact is not None:
            self.contact = contact
        if line_items is not None:
            self.line_items = line_items
        if date is not None:
            self.date = date
        if date_string is not None:
            self.date_string = date_string
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if expiry_date_string is not None:
            self.expiry_date_string = expiry_date_string
        if status is not None:
            self.status = status
        if currency_code is not None:
            self.currency_code = currency_code
        if currency_rate is not None:
            self.currency_rate = currency_rate
        if sub_total is not None:
            self.sub_total = sub_total
        if total_tax is not None:
            self.total_tax = total_tax
        if total is not None:
            self.total = total
        if total_discount is not None:
            self.total_discount = total_discount
        if title is not None:
            self.title = title
        if summary is not None:
            self.summary = summary
        if branding_theme_id is not None:
            self.branding_theme_id = branding_theme_id
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if line_amount_types is not None:
            self.line_amount_types = line_amount_types
        if status_attribute_string is not None:
            self.status_attribute_string = status_attribute_string
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def quote_id(self):
        """Gets the quote_id of this Quote.  # noqa: E501

        QuoteID GUID is automatically generated and is returned after create or GET.  # noqa: E501

        :return: The quote_id of this Quote.  # noqa: E501
        :rtype: str
        """
        return self._quote_id

    @quote_id.setter
    def quote_id(self, quote_id):
        """Sets the quote_id of this Quote.

        QuoteID GUID is automatically generated and is returned after create or GET.  # noqa: E501

        :param quote_id: The quote_id of this Quote.  # noqa: E501
        :type: str
        """

        self._quote_id = quote_id

    @property
    def quote_number(self):
        """Gets the quote_number of this Quote.  # noqa: E501

        Unique alpha numeric code identifying a quote (Max Length = 255)  # noqa: E501

        :return: The quote_number of this Quote.  # noqa: E501
        :rtype: str
        """
        return self._quote_number

    @quote_number.setter
    def quote_number(self, quote_number):
        """Sets the quote_number of this Quote.

        Unique alpha numeric code identifying a quote (Max Length = 255)  # noqa: E501

        :param quote_number: The quote_number of this Quote.  # noqa: E501
        :type: str
        """
        if quote_number is not None and len(quote_number) > 255:
            raise ValueError(
                "Invalid value for `quote_number`, "
                "length must be less than or equal to `255`"
            )  # noqa: E501

        self._quote_number = quote_number

    @property
    def reference(self):
        """Gets the reference of this Quote.  # noqa: E501

        Additional reference number  # noqa: E501

        :return: The reference of this Quote.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this Quote.

        Additional reference number  # noqa: E501

        :param reference: The reference of this Quote.  # noqa: E501
        :type: str
        """
        if reference is not None and len(reference) > 4000:
            raise ValueError(
                "Invalid value for `reference`, "
                "length must be less than or equal to `4000`"
            )  # noqa: E501

        self._reference = reference

    @property
    def terms(self):
        """Gets the terms of this Quote.  # noqa: E501

        Terms of the quote  # noqa: E501

        :return: The terms of this Quote.  # noqa: E501
        :rtype: str
        """
        return self._terms

    @terms.setter
    def terms(self, terms):
        """Sets the terms of this Quote.

        Terms of the quote  # noqa: E501

        :param terms: The terms of this Quote.  # noqa: E501
        :type: str
        """
        if terms is not None and len(terms) > 4000:
            raise ValueError(
                "Invalid value for `terms`, "
                "length must be less than or equal to `4000`"
            )  # noqa: E501

        self._terms = terms

    @property
    def contact(self):
        """Gets the contact of this Quote.  # noqa: E501


        :return: The contact of this Quote.  # noqa: E501
        :rtype: Contact
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this Quote.


        :param contact: The contact of this Quote.  # noqa: E501
        :type: Contact
        """

        self._contact = contact

    @property
    def line_items(self):
        """Gets the line_items of this Quote.  # noqa: E501

        See LineItems  # noqa: E501

        :return: The line_items of this Quote.  # noqa: E501
        :rtype: list[LineItem]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this Quote.

        See LineItems  # noqa: E501

        :param line_items: The line_items of this Quote.  # noqa: E501
        :type: list[LineItem]
        """

        self._line_items = line_items

    @property
    def date(self):
        """Gets the date of this Quote.  # noqa: E501

        Date quote was issued – YYYY-MM-DD. If the Date element is not specified it will default to the current date based on the timezone setting of the organisation  # noqa: E501

        :return: The date of this Quote.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Quote.

        Date quote was issued – YYYY-MM-DD. If the Date element is not specified it will default to the current date based on the timezone setting of the organisation  # noqa: E501

        :param date: The date of this Quote.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def date_string(self):
        """Gets the date_string of this Quote.  # noqa: E501

        Date the quote was issued (YYYY-MM-DD)  # noqa: E501

        :return: The date_string of this Quote.  # noqa: E501
        :rtype: str
        """
        return self._date_string

    @date_string.setter
    def date_string(self, date_string):
        """Sets the date_string of this Quote.

        Date the quote was issued (YYYY-MM-DD)  # noqa: E501

        :param date_string: The date_string of this Quote.  # noqa: E501
        :type: str
        """

        self._date_string = date_string

    @property
    def expiry_date(self):
        """Gets the expiry_date of this Quote.  # noqa: E501

        Date the quote expires – YYYY-MM-DD.  # noqa: E501

        :return: The expiry_date of this Quote.  # noqa: E501
        :rtype: date
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this Quote.

        Date the quote expires – YYYY-MM-DD.  # noqa: E501

        :param expiry_date: The expiry_date of this Quote.  # noqa: E501
        :type: date
        """

        self._expiry_date = expiry_date

    @property
    def expiry_date_string(self):
        """Gets the expiry_date_string of this Quote.  # noqa: E501

        Date the quote expires – YYYY-MM-DD.  # noqa: E501

        :return: The expiry_date_string of this Quote.  # noqa: E501
        :rtype: str
        """
        return self._expiry_date_string

    @expiry_date_string.setter
    def expiry_date_string(self, expiry_date_string):
        """Sets the expiry_date_string of this Quote.

        Date the quote expires – YYYY-MM-DD.  # noqa: E501

        :param expiry_date_string: The expiry_date_string of this Quote.  # noqa: E501
        :type: str
        """

        self._expiry_date_string = expiry_date_string

    @property
    def status(self):
        """Gets the status of this Quote.  # noqa: E501


        :return: The status of this Quote.  # noqa: E501
        :rtype: QuoteStatusCodes
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Quote.


        :param status: The status of this Quote.  # noqa: E501
        :type: QuoteStatusCodes
        """

        self._status = status

    @property
    def currency_code(self):
        """Gets the currency_code of this Quote.  # noqa: E501


        :return: The currency_code of this Quote.  # noqa: E501
        :rtype: CurrencyCode
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this Quote.


        :param currency_code: The currency_code of this Quote.  # noqa: E501
        :type: CurrencyCode
        """

        self._currency_code = currency_code

    @property
    def currency_rate(self):
        """Gets the currency_rate of this Quote.  # noqa: E501

        The currency rate for a multicurrency quote  # noqa: E501

        :return: The currency_rate of this Quote.  # noqa: E501
        :rtype: float
        """
        return self._currency_rate

    @currency_rate.setter
    def currency_rate(self, currency_rate):
        """Sets the currency_rate of this Quote.

        The currency rate for a multicurrency quote  # noqa: E501

        :param currency_rate: The currency_rate of this Quote.  # noqa: E501
        :type: float
        """

        self._currency_rate = currency_rate

    @property
    def sub_total(self):
        """Gets the sub_total of this Quote.  # noqa: E501

        Total of quote excluding taxes.  # noqa: E501

        :return: The sub_total of this Quote.  # noqa: E501
        :rtype: float
        """
        return self._sub_total

    @sub_total.setter
    def sub_total(self, sub_total):
        """Sets the sub_total of this Quote.

        Total of quote excluding taxes.  # noqa: E501

        :param sub_total: The sub_total of this Quote.  # noqa: E501
        :type: float
        """

        self._sub_total = sub_total

    @property
    def total_tax(self):
        """Gets the total_tax of this Quote.  # noqa: E501

        Total tax on quote  # noqa: E501

        :return: The total_tax of this Quote.  # noqa: E501
        :rtype: float
        """
        return self._total_tax

    @total_tax.setter
    def total_tax(self, total_tax):
        """Sets the total_tax of this Quote.

        Total tax on quote  # noqa: E501

        :param total_tax: The total_tax of this Quote.  # noqa: E501
        :type: float
        """

        self._total_tax = total_tax

    @property
    def total(self):
        """Gets the total of this Quote.  # noqa: E501

        Total of Quote tax inclusive (i.e. SubTotal + TotalTax). This will be ignored if it doesn’t equal the sum of the LineAmounts  # noqa: E501

        :return: The total of this Quote.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Quote.

        Total of Quote tax inclusive (i.e. SubTotal + TotalTax). This will be ignored if it doesn’t equal the sum of the LineAmounts  # noqa: E501

        :param total: The total of this Quote.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def total_discount(self):
        """Gets the total_discount of this Quote.  # noqa: E501

        Total of discounts applied on the quote line items  # noqa: E501

        :return: The total_discount of this Quote.  # noqa: E501
        :rtype: float
        """
        return self._total_discount

    @total_discount.setter
    def total_discount(self, total_discount):
        """Sets the total_discount of this Quote.

        Total of discounts applied on the quote line items  # noqa: E501

        :param total_discount: The total_discount of this Quote.  # noqa: E501
        :type: float
        """

        self._total_discount = total_discount

    @property
    def title(self):
        """Gets the title of this Quote.  # noqa: E501

        Title text for the quote  # noqa: E501

        :return: The title of this Quote.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Quote.

        Title text for the quote  # noqa: E501

        :param title: The title of this Quote.  # noqa: E501
        :type: str
        """
        if title is not None and len(title) > 100:
            raise ValueError(
                "Invalid value for `title`, "
                "length must be less than or equal to `100`"
            )  # noqa: E501

        self._title = title

    @property
    def summary(self):
        """Gets the summary of this Quote.  # noqa: E501

        Summary text for the quote  # noqa: E501

        :return: The summary of this Quote.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this Quote.

        Summary text for the quote  # noqa: E501

        :param summary: The summary of this Quote.  # noqa: E501
        :type: str
        """
        if summary is not None and len(summary) > 3000:
            raise ValueError(
                "Invalid value for `summary`, "
                "length must be less than or equal to `3000`"
            )  # noqa: E501

        self._summary = summary

    @property
    def branding_theme_id(self):
        """Gets the branding_theme_id of this Quote.  # noqa: E501

        See BrandingThemes  # noqa: E501

        :return: The branding_theme_id of this Quote.  # noqa: E501
        :rtype: str
        """
        return self._branding_theme_id

    @branding_theme_id.setter
    def branding_theme_id(self, branding_theme_id):
        """Sets the branding_theme_id of this Quote.

        See BrandingThemes  # noqa: E501

        :param branding_theme_id: The branding_theme_id of this Quote.  # noqa: E501
        :type: str
        """

        self._branding_theme_id = branding_theme_id

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this Quote.  # noqa: E501

        Last modified date UTC format  # noqa: E501

        :return: The updated_date_utc of this Quote.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this Quote.

        Last modified date UTC format  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this Quote.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc

    @property
    def line_amount_types(self):
        """Gets the line_amount_types of this Quote.  # noqa: E501


        :return: The line_amount_types of this Quote.  # noqa: E501
        :rtype: QuoteLineAmountTypes
        """
        return self._line_amount_types

    @line_amount_types.setter
    def line_amount_types(self, line_amount_types):
        """Sets the line_amount_types of this Quote.


        :param line_amount_types: The line_amount_types of this Quote.  # noqa: E501
        :type: QuoteLineAmountTypes
        """

        self._line_amount_types = line_amount_types

    @property
    def status_attribute_string(self):
        """Gets the status_attribute_string of this Quote.  # noqa: E501

        A string to indicate if a invoice status  # noqa: E501

        :return: The status_attribute_string of this Quote.  # noqa: E501
        :rtype: str
        """
        return self._status_attribute_string

    @status_attribute_string.setter
    def status_attribute_string(self, status_attribute_string):
        """Sets the status_attribute_string of this Quote.

        A string to indicate if a invoice status  # noqa: E501

        :param status_attribute_string: The status_attribute_string of this Quote.  # noqa: E501
        :type: str
        """

        self._status_attribute_string = status_attribute_string

    @property
    def validation_errors(self):
        """Gets the validation_errors of this Quote.  # noqa: E501

        Displays array of validation error messages from the API  # noqa: E501

        :return: The validation_errors of this Quote.  # noqa: E501
        :rtype: list[ValidationError]
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """Sets the validation_errors of this Quote.

        Displays array of validation error messages from the API  # noqa: E501

        :param validation_errors: The validation_errors of this Quote.  # noqa: E501
        :type: list[ValidationError]
        """

        self._validation_errors = validation_errors
