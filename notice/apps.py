from django.apps import AppConfig


class NoticeConfig(AppConfig):
    name = 'notice'

    def ready(self):
        try:
            import notice.signals 
        except ImportError:
            pass