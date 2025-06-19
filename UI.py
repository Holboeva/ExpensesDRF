from http.client import responses

from django.contrib.sites import requests


class AuthUI:

    def register(self):
        register_api_url = "https://10.10.3.127:8000/api/v1/auth/register"
        data = {
            "first_name" : input("First name : "),
            "email" : input("Email : "),
            "password" : input("Password : "),
        }
        response = request.post(register_api_url, json=data)
        print(response)
    def main(self):
        menu = """
            1) Register
            2) Login
            3) Logout
            >>> """

        key = input(menu)
        match key:
            case '1':
                self.register()
            case '2':
                self.login()
            case '3':
                self.logout()

AuthUI.main()