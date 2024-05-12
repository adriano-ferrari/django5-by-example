
from django.urls import include, path

from . import views

urlpatterns = [
    # previous login view
    path('login/', views.user_login, name='login'),
]