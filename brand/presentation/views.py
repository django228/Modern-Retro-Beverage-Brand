from django.views.generic import TemplateView

from brand.application.landing import GetLandingPage


class LandingView(TemplateView):
    template_name = "landing.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        page = GetLandingPage().execute()
        ctx["page"] = page
        return ctx
