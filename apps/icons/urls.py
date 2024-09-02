from django.urls import path
from .views import IconsView


urlpatterns = [
    path(
        "icons/ri/",
        IconsView.as_view(template_name="icons_ri.html"),
        name="icons-ri",
    ),
]
