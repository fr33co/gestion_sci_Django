# Create your views here.
#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render,  get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from BoletinAvances.apps.login.forms import LoginForm, RegisterForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from BoletinAvances.apps.boletines.models import Boletines
from BoletinAvances.apps.avances.models import Avances
from BoletinAvances.apps.listas.models import Listas
from BoletinAvances.apps.contactos.models import Contactos
from django.views.generic import ListView, FormView, UpdateView, DetailView, DeleteView


#VISTA DE LOGIN
def login_view(request):
    mensaje = ""
    if request.user.is_authenticated():
        return HttpResponseRedirect('/tablero/')
    else:
        if request.method == "POST":

            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username, password=password)
                if usuario is not None and usuario.is_active:
                    login(request, usuario)
                    return HttpResponseRedirect('/tablero/')
                else:
                    mensaje = "Usuario y/o password incorrectos"
        form = LoginForm()
        ctx = {'form': form, 'mensaje': mensaje}
    return render_to_response('login/login.html', ctx, context_instance=RequestContext(request))


#VISTA DE LOGOUT
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/?next=%s' % request.path)


#GRAFICOS
@login_required(login_url='/') 
def graph_view(request):
    usuarios = User.objects.count()
    listas = Listas.objects.count()
    boletines = Boletines.objects.count()
    avances = Avances.objects.count()
    contactos = Contactos.objects.count()
    lboletines = Boletines.objects.order_by('id')
    ctx = {'boletines': boletines, 'lboletines': lboletines, 'avances': avances, 'usuarios': usuarios, 'listas': listas,
           'contactos': contactos,}
    return render_to_response('dashboard/dashboard.html', ctx, context_instance=RequestContext(request))


#CREAR USUARIOS
@login_required(login_url='/') 
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            usuario = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password_one = form.cleaned_data['password_one']
            password_two = form.cleaned_data['password_two']
            u = User.objects.create_user(first_name=first_name,last_name=last_name,username=usuario,email=email,password=password_one)
            u.save()
            return HttpResponseRedirect("/administracion/usuarios")
        else:
            form = RegisterForm()
        return render_to_response('usuarios/addUsuario.html', {'form': form}, context_instance=RequestContext(request))


#VISUALIZAR LISTA DE USUARIOS
@login_required(login_url='/') 
def usuarios_view(request):
    usuarios = User.objects.all().order_by('-is_superuser', 'id')
    return render_to_response('usuarios/listUsuarios.html', {"usuarios": usuarios}, context_instance=RequestContext(request))


#VISTA PARA VISUALIZAR USUARIOS INDIVIDUALES
@login_required(login_url='/') 
def singleusuarios_view(request, id): 
    usuarios = User.objects.get(id=id)
    ctx = {'usuarios': usuarios}
    return render_to_response('usuarios/singleUsuarios.html', ctx, context_instance=RequestContext(request))


#VISTA PARA ELIMINAR USUARIOS INDIVIDUALES
@login_required(login_url='/') 
def singleusuarios_delete(request, id): 
    usuarios = User.objects.get(id=id).delete()
    return HttpResponseRedirect("/administracion/usuarios")
    
    
#VISTA PARA MODIFICAR USUARIOS INDIVIDUALES
#ACTUALIZAR
class UsuariosUpdate(UpdateView):
    model = User
    fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password']
    slug_field = 'id'
    template_name = 'usuarios/usuarios_update_form.html'
    success_url = '/administracion/usuarios'