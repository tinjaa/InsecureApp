from django.urls import path
from insecureapp import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('admin/', views.admin, name ='admin'),
    path('signup/', views.signup, name='signup',)
]
