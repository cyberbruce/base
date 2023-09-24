from django.urls  import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("control_center/", views.control_center, name="control_center"),
]
