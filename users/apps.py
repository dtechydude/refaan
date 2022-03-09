from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'




    #working on the signal
    def ready(self):
        import users.signals
