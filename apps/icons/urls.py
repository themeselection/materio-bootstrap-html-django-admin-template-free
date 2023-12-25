from django.urls import path
from .views import IconsView


urlpatterns = [
    path(
        "icons/mdi/",
        IconsView.as_view(template_name="icons_mdi.html"),
        name="icons-mdi",
    ),
]
