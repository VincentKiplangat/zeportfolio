from django.urls import path
from . import views
from .views import contact_form

urlpatterns = [
    path('', views.home, name="index-main"),
    path('blog/Technology', views.blog, name="single-blog"),
    path('blog/Cybersecurity', views.blog2, name="single-blog2"),
    path('blog/Artificial Inteligence', views.blog3, name="single-blog3"),
    path('blog/Sustainability', views.blog4, name="single-blog4"),
    path('blog/Cloud Computing', views.blog5, name="single-blog5"),
    path('blog/Workplace Trend', views.blog6, name="single-blog6"),
    path('error_404', views.error_404, name="error-404"),
    path("contact/submit/", views.contact_form, name="contact_submit"),

]
