from django.urls import path
from mainapp import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('sent/', views.send_mail_to_all, name = 'mail')
]
