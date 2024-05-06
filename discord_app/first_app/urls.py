from django.urls import path

from . import views

urlpatterns = [
	path('', views.default, name='first_app-default'),
	path('first/', views.home, name='first_app-home'),
	path("members/", views.members, name="first_app-members"),
	path("members/details/<int:id>", views.details, name="first_app-details")
]