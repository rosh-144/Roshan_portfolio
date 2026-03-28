from django.urls import path
from . import views

app_name="main"

urlpatterns = [
    path("portfolio/",views.portfolio,name="portfolio"),
]
