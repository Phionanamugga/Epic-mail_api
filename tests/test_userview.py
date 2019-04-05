import unittest
from api.models.user_model import User


class Test_user(unittest.TestCase):
    def setUp(self):
        kwargs = {
            "user_id": 1,
            "first_name": "Phiona",
            "last_name": "Namugga",
            "email": "phionanamugga@gmail.com",
            "password": "123K4567M",
        }
        self.user = User(**kwargs)

    def test_user_id(self):
        # Tests that the user_id is equal to the given id
        self.assertEqual(self.user.user_id, 1, "user_id must be 1")
        self.user.user_id = 2
        self.assertEqual(self.user.user_id, 2, "user_id is now 2")

    def test_user_email(self):
        # Tests that the email is equal to the given email
        self.assertEqual(self.user.email, "phionanamugga@gmail.com")

    def test_email_type(self):
        # Tests the datatype of the email
        self.assertIsInstance(self.user.email, str)
        self.assertNotIsInstance(self.user.email, int)

    def test_password(self):
        # Tests that the password is equal to the given password
        self.assertEqual(self.user.password, "123K4567M")
        self.user.password = "567wxQ84"
        self.assertEqual(self.user.password, "567wxQ84",
                         "password is now 567wxQ84")

    def test_class_instance(self):
        # Tests that the defined object is an instance of the User class
        self.assertIsInstance(self.user, User)