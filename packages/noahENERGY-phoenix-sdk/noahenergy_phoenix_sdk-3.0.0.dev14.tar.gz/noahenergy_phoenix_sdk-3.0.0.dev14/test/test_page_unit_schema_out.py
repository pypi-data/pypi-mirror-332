# coding: utf-8

"""
    Phoenix API

    Base API for Glumanda and other services.

    The version of the OpenAPI document: Alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from phoenix_sdk.models.page_unit_schema_out import PageUnitSchemaOut

class TestPageUnitSchemaOut(unittest.TestCase):
    """PageUnitSchemaOut unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PageUnitSchemaOut:
        """Test PageUnitSchemaOut
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageUnitSchemaOut`
        """
        model = PageUnitSchemaOut()
        if include_optional:
            return PageUnitSchemaOut(
                results = [
                    phoenix_sdk.models.unit_schema_out.UnitSchemaOut(
                        created_by_id = '', 
                        id = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '', 
                        conf = phoenix_sdk.models.conf.Conf(), 
                        address_id = '', 
                        parent_id = '', 
                        company_id = '', 
                        unit_group_id = '', 
                        unit_platform = 'ems', 
                        unit_group = phoenix_sdk.models.unit_group_schema_out.UnitGroupSchemaOut(
                            created_by_id = '', 
                            id = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            name = '', 
                            company_id = '', ), )
                    ],
                page = 1.0,
                size = 1.0,
                pages = 0.0,
                total = 0.0,
                has_next = True,
                has_prev = True
            )
        else:
            return PageUnitSchemaOut(
                results = [
                    phoenix_sdk.models.unit_schema_out.UnitSchemaOut(
                        created_by_id = '', 
                        id = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '', 
                        conf = phoenix_sdk.models.conf.Conf(), 
                        address_id = '', 
                        parent_id = '', 
                        company_id = '', 
                        unit_group_id = '', 
                        unit_platform = 'ems', 
                        unit_group = phoenix_sdk.models.unit_group_schema_out.UnitGroupSchemaOut(
                            created_by_id = '', 
                            id = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            name = '', 
                            company_id = '', ), )
                    ],
                total = 0.0,
        )
        """

    def testPageUnitSchemaOut(self):
        """Test PageUnitSchemaOut"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
