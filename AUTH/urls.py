from django.urls import path
from . import views 

urlpatterns = [
    path('reg/',views.registratiomform,name="registration_url"),
    path('login/',views.loginUser,name="login_url"),
    path('logout/',views.logoutView,name="logout_url"),
]