from django.conf import settings as django_settings


class Settings:
    """
    Holds default configuration values, the values can be overridden in settings with ``PYNOTIFY_`` prefix.
    """
    PREFIX = 'PYNOTIFY'
    DEFAULTS = {
        'AUTOLOAD_MODULES': None,
        'CELERY_TASK': 'pynotify.tasks.notification_task',
        'ENABLED': True,
        'NOTIFICATION_MODEL': 'pynotify.Notification',
        'RECEIVER': 'pynotify.receivers.SynchronousReceiver',
        'RELATED_OBJECTS_ALLOWED_ATTRIBUTES': {'get_absolute_url', },
        'STRIP_HTML': False,
        'TEMPLATE_CHECK': False,
        'TEMPLATE_PREFIX': '',
        'TEMPLATE_TRANSLATE': False,
    }

    def __getattr__(self, attr):
        if attr not in self.DEFAULTS:
            raise AttributeError('Invalid setting: "{}"').format(attr)

        return getattr(django_settings, '{}_{}'.format(self.PREFIX, attr), self.DEFAULTS[attr])


settings = Settings()
