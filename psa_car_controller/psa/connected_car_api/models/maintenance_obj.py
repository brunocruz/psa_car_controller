# coding: utf-8

"""
    Groupe PSA Connected Car - WEB API B2C

    *PSA B2C Connected Car API*  # Introduction This is the description of the *Groupe PSA Connected Car V2 API*. The speccification is  is based on **OpenAPI Specification version 3** and can be displayed via [ReDoc](https://github.com/Rebilly/ReDoc)a or [Swagger](http://swagger.io).   This API allows applications to fetch data from the connected Vehicles data platform. # Authentication PSA Connected Car APIs uses the [OAuth 2.0](https://tools.ietf.org/html/rfc6749) protocol for authentication and Authorization. any application require a valid [Access Token](https://tools.ietf.org/html/rfc6749#section-1.4) to access to user data. # Errors   Error codes returned by all REST APIs comply with the standard. Nevertheless, PSA Services (callers) need to have more complete data structures (even when the answer is not Http-OK) to better detail the type of error by providing application code, message and a debugging code(for investigation purposes). The http code of the response is managed by the protocol itself (in the header).      **Errors are  returned as a generic error response:**    * ```xError``` object model.       # noqa: E501

    OpenAPI spec version: 4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MaintenanceObj(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'created_at': 'datetime',
        'days_before_maintenace': 'int',
        'mileage_before_maintenance': 'int'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'days_before_maintenace': 'daysBeforeMaintenace',
        'mileage_before_maintenance': 'mileageBeforeMaintenance'
    }

    def __init__(self, created_at=None, days_before_maintenace=None, mileage_before_maintenance=None):  # noqa: E501
        """MaintenanceObj - a model defined in Swagger"""  # noqa: E501

        self._created_at = None
        self._days_before_maintenace = None
        self._mileage_before_maintenance = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if days_before_maintenace is not None:
            self.days_before_maintenace = days_before_maintenace
        if mileage_before_maintenance is not None:
            self.mileage_before_maintenance = mileage_before_maintenance

    @property
    def created_at(self):
        """Gets the created_at of this MaintenanceObj.  # noqa: E501

        Date when the resource has been created.  # noqa: E501

        :return: The created_at of this MaintenanceObj.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this MaintenanceObj.

        Date when the resource has been created.  # noqa: E501

        :param created_at: The created_at of this MaintenanceObj.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def days_before_maintenace(self):
        """Gets the days_before_maintenace of this MaintenanceObj.  # noqa: E501


        :return: The days_before_maintenace of this MaintenanceObj.  # noqa: E501
        :rtype: int
        """
        return self._days_before_maintenace

    @days_before_maintenace.setter
    def days_before_maintenace(self, days_before_maintenace):
        """Sets the days_before_maintenace of this MaintenanceObj.


        :param days_before_maintenace: The days_before_maintenace of this MaintenanceObj.  # noqa: E501
        :type: int
        """

        self._days_before_maintenace = days_before_maintenace

    @property
    def mileage_before_maintenance(self):
        """Gets the mileage_before_maintenance of this MaintenanceObj.  # noqa: E501


        :return: The mileage_before_maintenance of this MaintenanceObj.  # noqa: E501
        :rtype: int
        """
        return self._mileage_before_maintenance

    @mileage_before_maintenance.setter
    def mileage_before_maintenance(self, mileage_before_maintenance):
        """Sets the mileage_before_maintenance of this MaintenanceObj.


        :param mileage_before_maintenance: The mileage_before_maintenance of this MaintenanceObj.  # noqa: E501
        :type: int
        """

        self._mileage_before_maintenance = mileage_before_maintenance

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MaintenanceObj, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MaintenanceObj):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other