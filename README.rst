== Allauth with multiple usertypes


* Installation

- install `django-allauth` and add all needed settings for it

- add `allauth_multiple` to `INSTALLED_APPS`

- add `AUTH_USER_MODELS` (note `S` in the end). It's list of user models allowed to signup.
  ```
  AUTH_USER_MODELS = ['core.User', 'core.Expert']
  ```

- adjust `AUTHENTICATION_BACKENDS`

    ```
    AUTHENTICATION_BACKENDS = (
        # Needed to login by username in Django admin, regardless of `allauth`
        "django.contrib.auth.backends.ModelBackend",
        # Multitype auth backend
        "allauth_multiple.auth_backends.MultipleAuthenticationBackend",
    )
    ```

- adjust `SOCIALACCOUNT_ADAPTER`

    ```
    SOCIALACCOUNT_ADAPTER ='allauth_multiple.adapters.MultipleUserSocialAccountAdapter'
    ```

- adjust `ACCOUNT_ADAPTER`

    ```
    ACCOUNT_ADAPTER ='allauth_multiple.adapters.MultipleUserAccountAdapter'
    ```

- pass `user_type` GET paramenter for each form of user registration.
  Allowed values are names of user models. For example `?user-type=Expert`.
