from django.urls import path
from . import views

urlpatterns = [
    path('',views.homee, name="homee"),

    path('booking/',views.list_view, name="booking"),
]
