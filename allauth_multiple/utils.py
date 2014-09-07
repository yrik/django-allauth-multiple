from django.conf import settings


def get_user_models():
    user_models = settings.AUTH_USER_MODELS
    user_models = [__import__(x) for x in user_models]
    return user_models

def get_user_model_by_name(name):
    user_models = settings.AUTH_USER_MODELS
    for user_model in user_models:
        if name.lower() == user_model.split('.')[-1].lower():
            return __import__(user_models)
