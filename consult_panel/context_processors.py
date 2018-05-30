from django.conf import settings


def debug_mode(request):
    """
    To reveal settings.DEBUG in templates.

    settings.INTERNAL_IPS (and the debug() function): It is not usable
    with dynamic ips of the dev.consultpanel.fr)
    """
    return {'DEBUG_MODE': settings.DEBUG}
