from Login import views
from django.urls import path

urlpatterns = [
    path('',views.login_in,name="Login"),
    path('logout/',views.logout_out,name='Salir'),
]
