from allauth.account.auth_backends import AuthenticationBackend

from .utils import get_user_models


class MultipleAuthenticationBackend(AuthenticationBackend):

    def _authenticate_by_email(self, **credentials):
        email = credentials.get('email', credentials.get('username'))
        if email:

            for user_model in get_user_models():
                try:
                    user = user_model.objects.get(email=email)
                    if user.check_password(credentials["password"]):
                        return user
                except user_model.DoesNotExist:
                    pass

        return None

    def get_user(self, user_id):
        for user_model in get_user_models():
            try:
                user_model.objects.get(pk=user_id)
            except user_model.DoesNotExist:
                pass
        return None
