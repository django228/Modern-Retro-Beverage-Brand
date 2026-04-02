from django_distill import distill_path

from brand.presentation.views import LandingView

urlpatterns = [
    distill_path(
        "",
        LandingView.as_view(),
        name="landing",
        distill_file="index.html",
    ),
]
