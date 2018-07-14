from django.apps import AppConfig


class MyappConfig(AppConfig):
    name = 'myApp'

    def ready(self):
        from myApp import signals
