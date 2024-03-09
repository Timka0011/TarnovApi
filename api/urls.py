from django.urls import path
from . import views
urlpatterns = [

    path("", views.home.as_view(), name="home"),
    path("branch/", views.BranchList.as_view(), name="branch"),
    path("about/", views.AboutUs.as_view(), name="about"),

]