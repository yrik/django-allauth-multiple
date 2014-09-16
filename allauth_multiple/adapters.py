from allauth.account.models import EmailAddress
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.adapter import DefaultAccountAdapter

from .utils import get_user_models, get_user_model_by_name


class MultipleUserSocialAccountAdapter(DefaultSocialAccountAdapter):

    def new_user(self, request, sociallogin):
        """
        Instantiate a new User instance in case user signups.
        """
        # choose usertype based on GET params
        user_model = get_user_model_by_name(request.GET['user_type'])
        user = user_model()
        return user


class MultipleUserAccountAdapter(DefaultAccountAdapter):

    def new_user(self, request):
        """
        Instantiate a new User instance in case user signups.
        """
        # choose usertype based on GET params
        user_model = get_user_model_by_name(request.GET['user_type'])
        user = user_model()
        return user

    def login(self, request, user):
        from django.contrib.auth import login
        # HACK: This is not nice. The proper Django way is to use an
        # authentication backend
        if not hasattr(user, 'backend'):
            user.backend = "allauth_multiple.auth_backends.MultipleAuthenticationBackend"
        login(request, user)


    def save_user(self, request, user, form, commit=True):
        user = super(MultipleUserAccountAdapter, self).save_user(
            request, user, form, commit=False
        )

        if hasattr(user, 'email'):
            user.email = form.cleaned_data.get('email')
        
        if commit:
            user.save()

