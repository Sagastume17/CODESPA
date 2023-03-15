from user import views
from django.urls import path
from django.conf import settings#para agregar la ruta de la imagen 
from django.conf.urls.static import static#para agregar la ruta de la imagen 

urlpatterns = [
    path('nuevousuario/',views.nuevousuario,name="NuevoUser"),
    path('registrousuario/',views.usuarioindividual,name="UserIndividual"),
    path('listausuario/',views.listausuario,name="ListaUser"),
    path('updateusuario/<str:id>',views.updateusuario,name="UpdateUser"),
    path('deleteusuario/<str:id>',views.deleteusuario,name="DeleteUser"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)