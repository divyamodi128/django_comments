from django.shortcuts import render
from django.apps import apps
from django.contrib.auth import get_user_model
from django.core.signals import setting_changed
from django.dispatch import receiver


# @receiver(setting_changed)
# def user_model_swapped(**kwargs):
#     if kwargs['setting'] == 'AUTH_USER_MODEL':
#         apps.clear_cache()
#         from myapp import some_module
#         some_module.UserModel = get_user_model()
# Create your views here.
