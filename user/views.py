from django.shortcuts import render,redirect
from user.models import User
from user.forms import RegistroForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password


def nuevousuario(request):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        form = RegistroForm()
        if request.method == "POST":
            form = RegistroForm(request.POST)
            if form.is_valid():
                try:
                    u = User()
                    u.username = form.cleaned_data["username"]
                    u.password = make_password(form.cleaned_data["password"])
                    u.first_name = form.cleaned_data["first_name"]
                    u.last_name = form.cleaned_data["last_name"]
                    u.email = form.cleaned_data["email"]
                    u.rol = form.cleaned_data["rol"]
                    u.is_staff = form.cleaned_data["is_staff"]
                    u.is_active = form.cleaned_data["is_active"]
                    u.is_superuser = form.cleaned_data["is_superuser"]
                    u.save()
                    messages.success(request,'Registro de Usuario Exitoso')
                    return redirect('NuevoUser')
                except:
                    messages.error(request,'Registro de Usuario Fallido')
                    return redirect('NuevoUser')

            else:
                messages.error(request,"Formulario Corrupto")
                return redirect('NuevoUser')


        return render(request,"user/nuevousuario.html",{'form':form})





def usuarioindividual(request):
        form = RegistroIndividualForm()
        if request.method == "POST":
            form = RegistroIndividualForm(request.POST)
            if form.is_valid():
                try:
                    u = User()
                    u.username = form.cleaned_data["username"]
                    u.password = make_password(form.cleaned_data["password"])
                    u.first_name = form.cleaned_data["first_name"]
                    u.last_name = form.cleaned_data["last_name"]
                    u.email = form.cleaned_data["email"]
                    u.rol = "normal"
                    u.is_staff = 0
                    u.is_active = 1
                    u.is_superuser = 0
                    u.direccion = form.cleaned_data["direccion"]
                    u.direccion2 = form.cleaned_data["direccion2"]
                    u.tel = form.cleaned_data["tel"]
                    u.ciudad = form.cleaned_data["ciudad"]
                    u.departamento = form.cleaned_data["departamento"]
                    u.save()
                    messages.success(request,'Registro de Usuario Exitoso')
                    return redirect('UserIndividual')
                except:
                    messages.error(request,'Registro de Usuario Fallido')
                    return redirect('UserIndividual')

            else:
                messages.error(request,"Formulario Corrupto")
                return redirect('UserIndividual')


        return render(request,"user/registro.html",{'form':form})



def listausuario(request):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        usuarios = User.objects.all()
        return render(request,"user/todousuario.html",{'usuarios':usuarios})




def updateusuario(request,id):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
         usuarios = User.objects.get(username=id)
         if request.method == 'GET':
            form = RegistroForm(instance=usuarios)
         else:
            form = RegistroForm(request.POST,request.FILES,instance = usuarios)
     
            if form.is_valid():
                try:
                    form.save()
                    messages.success(request, 'Usuario Modificado Exitosamente!.')
                    return redirect('ListaUser')#la redireccion es en name del path en la url  path('',views.compras,name="Compras"),
                except:
                    messages.error(request, 'Modificacion de Usuario Fallido!.')
                    return redirect('ListaUser') # path('error/',views.error,name="Error"),

    
    return render(request,"user/updateusuario.html",{'form':form,'d':id})






def deleteusuario(request,id):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        usuarios = User.objects.get(username=id)
        print(usuarios.username)
        if usuarios.username == request.user:
            messages.error(request, 'No Puedes Eliminar Tu Propio Usuario!.')
            return redirect('ListaUser')          
         
        else:
            if request.method == 'GET':
                try:
                    usuarios.delete() 
                    messages.success(request, 'Usuario Eliminado Exitosamente!.')
                    return redirect('ListaUser')#la redireccion es en name del path en la url  path('',views.compras,name="Compras"),
                except:
                    messages.error(request, 'Eliminacion de Usuario Fallido!.')
                    return redirect('ListaUser') # path('error/',views.error,name="Error"),
            else:
              pass           
  




