from . import views
from django.urls import include, path


urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name='register-user'),
    path('login/', views.LoginUser.as_view(), name='login-user'),
    path('logout/', views.LogoutUser.as_view(), name='logout-user'),
]
