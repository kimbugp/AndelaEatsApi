from app.utils.handled_exceptions import BaseModelValidationError
from tests.base_test_case import BaseTestCase
from tests.base_test_utils import BaseTestUtils
from factories import MenuTemplateItemFactory, MenuTemplateWeekDayFactory, LocationFactory, MealItemFactory


class TestMenuTemplateItem(BaseTestCase, BaseTestUtils):

    def setUp(self):
        self.BaseSetUp()
        self.meal_items = MealItemFactory.create_batch(5)
        [item.save() for item in self.meal_items]

    def tearDown(self):
        self.BaseTearDown()

    def test_create_menu_template_item_with_no_permission_fails(self):
        day = MenuTemplateWeekDayFactory()
        day.save()
        data = {
            "mainMealId": 1,
            "allowedSide": 1,
            "allowedProtein": 1,
            "dayId": day.id
        }
        response = self.client().post(
            self.make_url("/menu_template_items/"), headers=self.headers(),
            data=self.encode_to_json_string(data))
        response_json = self.decode_from_json_string(
            response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response_json['msg'],
                         'Access Error - No Role Granted')

    def test_create_menu_template_item_with_permission_succeeds(self):
        self.create_admin()
        day = MenuTemplateWeekDayFactory()
        day.save()
        data = {
            "mainMealId": self.meal_items[0].id,
            "allowedSide": 1,
            "allowedProtein": 1,
            "proteinItems": [i.id for i in self.meal_items],
            "sideItems": [i.id for i in self.meal_items],
            "dayId": day.id
        }
        response = self.client().post(
            self.make_url("/menu_template_items/"), headers=self.headers(),
            json=data)
        response_json = self.decode_from_json_string(
            response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_json['msg'], 'OK')
        self.assertJSONKeysPresent(response_json['payload'], 'mainMealId')
        self.assertJSONKeysPresent(response_json['payload'], 'dayId')

    def test_create_menu_template_item_with_no_data_fails(self):
        self.create_admin()
        data = {}
        response = self.client().post(
            self.make_url("/menu_template_items/"), headers=self.headers(),
            data=self.encode_to_json_string(data))
        response_json = self.decode_from_json_string(
            response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response_json['msg'], 'Bad Request - Request Must be JSON Formatted')

    def test_create_menu_template_item_with_missing_fields_fails(self):
        self.create_admin()
        day = MenuTemplateWeekDayFactory()
        day.save()
        data = {
            "allowedSide": 1,
            "allowedProtein": 1,
            "dayId": day.id
        }
        response = self.client().post(
            self.make_url("/menu_template_items/"), headers=self.headers(),
            data=self.encode_to_json_string(data))
        response_json = self.decode_from_json_string(
            response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response_json['msg'], 'Bad Request - mainMealId is required')

    def test_create_menu_template_item_invalid_side_and_protein_item_ids_fails(self):
        self.create_admin()
        day = MenuTemplateWeekDayFactory()
        day.save()
        data = {
            "mainMealId": self.meal_items[0].id,
            "allowedSide": 1,
            "allowedProtein": 1,
            "proteinItems": [123],
            "sideItems": [233],
            "dayId": day.id
        }

        response_ = self.client().post(
            self.make_url("/menu_template_items/"), headers=self.headers(),
            data=self.encode_to_json_string(data))
        response = self.client().post(
            self.make_url("/menu_template_items/"), headers=self.headers(),
            data=self.encode_to_json_string(data))
        response_json = self.decode_from_json_string(
            response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertJSONKeysPresent(response_json, 'msg')
        self.assertEqual(response_json['msg'],
                         "Bad Request - sideItems contains invalid id(s) for meal_item table ")

    def test_create_same_exact_menu_template_item_fails(self):
        self.create_admin()
        day = MenuTemplateWeekDayFactory()
        day.save()
        data = {
            "mainMealId": self.meal_items[0].id,
            "allowedSide": 1,
            "allowedProtein": 1,
            "proteinItems": [i.id for i in self.meal_items],
            "sideItems": [i.id for i in self.meal_items],
            "dayId": day.id
        }

        response_ = self.client().post(
            self.make_url("/menu_template_items/"), headers=self.headers(),
            data=self.encode_to_json_string(data))
        response = self.client().post(
            self.make_url("/menu_template_items/"), headers=self.headers(),
            data=self.encode_to_json_string(data))
        response_json = self.decode_from_json_string(
            response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertJSONKeysPresent(response_json['payload'], 'message')
        self.assertEqual(response_json['payload']['message'],
                         'Menu Template Item already exists')