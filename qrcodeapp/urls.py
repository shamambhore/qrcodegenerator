from django.urls import path
from . import views
urlpatterns = [
    path('', views.qr_generate, name='qr_generate'),
]