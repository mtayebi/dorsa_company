from rest_framework.permissions import BasePermission
import base64


class CustomBasePermission(BasePermission):

    message = "the username or password is wrong"

    def has_permission(self, request, view):
        username = None
        password = None

        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if auth_header:
                encoded_credentials = auth_header.split(' ')[1]
                decoded_credentials = base64.b64decode(encoded_credentials).decode("utf-8").split(':')
                username = decoded_credentials[0]
                password = decoded_credentials[1]

        return username == "admin" and password == "admin"
