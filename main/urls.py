from django.urls import path
from . import views
from .views import contact_form

urlpatterns = [
    path('', views.home, name="index-main"),
    path('blog', views.blog, name="single-blog"),
    path('blog2', views.blog2, name="single-blog2"),
    path('blog3', views.blog3, name="single-blog3"),
    path('blog4', views.blog4, name="single-blog4"),
    path('blog5', views.blog5, name="single-blog5"),
    path('blog6', views.blog6, name="single-blog6"),
    path('error_404', views.error_404, name="error-404"),
    path("submit/", contact_form, name="contact_form"),

]