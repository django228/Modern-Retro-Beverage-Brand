from django.conf import settings


def site_base(_request):
    return {"SITE_BASE_PATH": getattr(settings, "SITE_BASE_PATH", "")}
