from django.conf import settings


def add_models(x):
    l = x.split(".")
    l.insert(1, 'models')
    return ".".join(l)


def import_class(cl):
    d = cl.rfind(".")
    classname = cl[d+1:len(cl)]
    m = __import__(cl[0:d], globals(), locals(), [classname])
    return getattr(m, classname)


def get_user_models():

    user_models = settings.AUTH_USER_MODELS
    user_models = [add_models(x) for x in user_models]
    user_models = [import_class(x) for x in user_models]
    return user_models


def get_user_model_by_name(name):

    user_models = settings.AUTH_USER_MODELS
    user_models = [add_models(x) for x in user_models]
    for user_model in user_models:
        if name.lower() == user_model.split('.')[-1].lower():
            return import_class(user_model)
