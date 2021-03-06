import re
from flask import jsonify

name_regex = r"[a-zA-Z]"
password_regex = r"(?=.*[0-9])"


class Validate:
    """This class contains validators for the different entries"""
    def validate_user(self, data):
        # Validates user fields
        user_fields = ['first_name', 'last_name', 'email', 'password']
        try:
            if len(data.keys()) == 0:
                return "No user added"
            for user_field in user_fields:
                if data[user_field] == "":
                    return user_field + " cannot be blank"

            if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)",
                            data['email']):
                return "Invalid email format"

            if not re.match(r"([a-zA-Z ]*$)", data['first_name']):
                return "Only alphanumerics allowed in first name"

            if not re.match(r"([a-zA-Z ]*$)", data['last_name']):
                return "Only alphanumerics allowed in last_name" 
                
            if len(data['password']) < 8:
                return "Password too short"

            else:
                return "is_valid"
        except KeyError:
            return "Invalid, Key fields missing"

    def validate_login(self, data):
        try:
            if len(data.keys()) == 0 or len(data.keys()) > 2:
                return "Only email and password for login"
            if 'email' not in data.keys():
                return "Email is missing"
            if 'password' not in data.keys():
                return "Missing password"
            if data['email'] == "" or data['password'] == "":
                return "Input email or password"
            else:
                return "Credentials valid"
        except KeyError:
            return "Invalid fields"

    def validate_message(self, data):
        # Validates the message fields
        message_fields = ['subject', 'message']
        try:
            for message_field in message_fields:
                if data[message_field] == "":
                    return message_field + " cannot be blank"
            else:
                return "Valid"
        except KeyError:
            return "Invalid Key Fields"

    def validate_id(self, item_id, item_list):
        if item_id != 0 and item_id <= len(item_list):
            return True
        return False