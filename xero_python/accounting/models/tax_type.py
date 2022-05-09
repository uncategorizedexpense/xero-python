# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from enum import Enum


class TaxType(Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    allowed enum values
    """

    OUTPUT = "OUTPUT"
    INPUT = "INPUT"
    CAPEXINPUT = "CAPEXINPUT"
    EXEMPTEXPORT = "EXEMPTEXPORT"
    EXEMPTEXPENSES = "EXEMPTEXPENSES"
    EXEMPTCAPITAL = "EXEMPTCAPITAL"
    EXEMPTOUTPUT = "EXEMPTOUTPUT"
    INPUTTAXED = "INPUTTAXED"
    BASEXCLUDED = "BASEXCLUDED"
    GSTONCAPIMPORTS = "GSTONCAPIMPORTS"
    GSTONIMPORTS = "GSTONIMPORTS"
    NONE = "NONE"
    INPUT2 = "INPUT2"
    ZERORATED = "ZERORATED"
    OUTPUT2 = "OUTPUT2"
    CAPEXINPUT2 = "CAPEXINPUT2"
    CAPEXOUTPUT = "CAPEXOUTPUT"
    CAPEXOUTPUT2 = "CAPEXOUTPUT2"
    CAPEXSRINPUT = "CAPEXSRINPUT"
    CAPEXSROUTPUT = "CAPEXSROUTPUT"
    ECACQUISITIONS = "ECACQUISITIONS"
    ECZRINPUT = "ECZRINPUT"
    ECZROUTPUT = "ECZROUTPUT"
    ECZROUTPUTSERVICES = "ECZROUTPUTSERVICES"
    EXEMPTINPUT = "EXEMPTINPUT"
    REVERSECHARGES = "REVERSECHARGES"
    RRINPUT = "RRINPUT"
    RROUTPUT = "RROUTPUT"
    SRINPUT = "SRINPUT"
    SROUTPUT = "SROUTPUT"
    ZERORATEDINPUT = "ZERORATEDINPUT"
    ZERORATEDOUTPUT = "ZERORATEDOUTPUT"
    BLINPUT = "BLINPUT"
    DSOUTPUT = "DSOUTPUT"
    EPINPUT = "EPINPUT"
    ES33OUTPUT = "ES33OUTPUT"
    ESN33OUTPUT = "ESN33OUTPUT"
    IGDSINPUT2 = "IGDSINPUT2"
    IMINPUT2 = "IMINPUT2"
    MEINPUT = "MEINPUT"
    NRINPUT = "NRINPUT"
    OPINPUT = "OPINPUT"
    OSOUTPUT = "OSOUTPUT"
    TXESSINPUT = "TXESSINPUT"
    TXN33INPUT = "TXN33INPUT"
    TXPETINPUT = "TXPETINPUT"
    TXREINPUT = "TXREINPUT"
    INPUT3 = "INPUT3"
    INPUT4 = "INPUT4"
    OUTPUT3 = "OUTPUT3"
    OUTPUT4 = "OUTPUT4"
    SROUTPUT2 = "SROUTPUT2"
    TXCA = "TXCA"
    SRCAS = "SRCAS"
    BLINPUT2 = "BLINPUT2"
    DRCHARGESUPPLY20 = "DRCHARGESUPPLY20"
    DRCHARGE20 = "DRCHARGE20"
    DRCHARGESUPPLY5 = "DRCHARGESUPPLY5"
    DRCHARGE5 = "DRCHARGE5"
    BADDEBTRELIEF = "BADDEBTRELIEF"
    IGDSINPUT3 = "IGDSINPUT3"
    SROVR = "SROVR"
    TOURISTREFUND = "TOURISTREFUND"
    TXRCN33INPUT = "TXRCN33INPUT"
    TXRCREINPUT = "TXRCREINPUT"
    TXRCESSINPUT = "TXRCESSINPUT"
