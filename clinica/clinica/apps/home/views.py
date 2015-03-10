# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from clinica.apps.historias.models import Paciente, Historia, Evolucion, Profesional, Persona, Plan
from clinica.apps.home.forms import ContactoFrm, LoginForm
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect


def index_view(request):
	return render_to_response('home/index.html',context_instance=RequestContext(request))

def buscar_view(request):
	busqueda = request.POST['buscalo']
	historias = Historia.objects.all()
	
	his = []
	nombres = Persona.objects.filter(nombres__contains = busqueda)
	apellidos1 = Persona.objects.filter(apellido1__contains = busqueda)
	apellidos2 = Persona.objects.filter(apellido2__contains = busqueda)
	
	#pacientes = Paciente.objects.filter(persona__contains = busqueda)
	#historias = Historia.objects.filter(codigo__contains = busqueda)
	info = "vacio"

	for h in historias:
		if busqueda == h.codigo:
			info ="se encontro una historia"
			his.append(h) 
			break

	for h in historias:
		for p in nombres:
			if p.cedula == h.codigo:
				his.append(h)
		for p in apellidos1:
			if p.cedula == h.codigo:
				his.append(h)
		for p in apellidos2:
			if p.cedula == h.codigo:
				his.append(h)



	ctx = {'info':info, 'his':his}

	print his
	return render_to_response('home/buscar.html',ctx,context_instance=RequestContext(request))


def about_view(request):
	mensaje = "este es un mensaje desde mi vista"
	ctx = {'msg':mensaje}
	return render_to_response('home/about.html', ctx, context_instance=RequestContext(request))

def profesionales_view(request, pagina):
	lista_pro = Profesional.objects.filter()
	paginator = Paginator(lista_pro,5)
	try:
		page = int (pagina)
	except:
		page = 1
	try:
		profesionales = paginator.page(page)
	except(Emptypage, Invalidpage):
		profesionales = paginator.page(paginator)

	ctx = {'profesionales':profesionales}
	return render_to_response('home/profesionales.html', ctx, context_instance=RequestContext(request))

def pacientes_view(request, pagina):
	lista_pac = Paciente.objects.filter()
	paginator = Paginator(lista_pac,5)
	try:
		page = int (pagina)
	except:
		page = 1
	try:
		pacientes = paginator.page(page)
	except(Emptypage, Invalidpage):
		pacientes = paginator.page(paginator)

	ctx = {'pacientes':pacientes}
	return render_to_response('home/pacientes.html', ctx, context_instance=RequestContext(request))

def historia_view(request, pagina):
	lista_his = Historia.objects.filter()
	paginator = Paginator(lista_his,5)
	try:
		page = int (pagina)
	except:
		page = 1
	try:
		historias = paginator.page(page)
	except(Emptypage, Invalidpage):
		historias = paginator.page(paginator)

	ctx = {'historias':historias}
	return render_to_response('home/historias.html', ctx, context_instance=RequestContext(request))	

def contacto_view(request):
	info_enviado = False # definir si se envio informacion o no se envio
	email = ""
	titulo = ""
	texto = ""

	if request.method == "POST":
		formulario = ContactoFrm(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['email']
			titulo = formulario.cleaned_data['titulo']
			texto = formulario.cleaned_data['texto']
	else:
		formulario = ContactoFrm()
	ctx = {'form':formulario, 'email':email, 'titulo':titulo, 'texto':texto, 'info_enviado':info_enviado}
	return render_to_response('home/contacto.html',ctx, context_instance = RequestContext(request)) 


def singlePaciente_view(request, id_pac):
	pac = Paciente.objects.get(id=id_pac)
	lista_his = Historia.objects.all()
	info = 3

	for h in lista_his:
		if h.paciente.id == pac.id:
			info = 1 # YA tiene Historia
			break
		else:
			info = 2 # NO TIENE historia
			#break
	ctx = {'paciente':pac, 'info':info, 'h':h}
	return render_to_response('home/singlepaciente.html', ctx, context_instance = RequestContext(request))

def singleProfesional_view(request, id_pro):
	pro = Profesional.objects.get(id=id_pro)
	ctx = {'profesional':pro}
	return render_to_response('home/singleprofesional.html', ctx, context_instance = RequestContext(request))


def singleHistoria_view(request, id_his):
	his = Historia.objects.get(id=id_his)
	aux = 0
	evoluciones = []
	planes = []
	#pac =Paciente.objects.get(id = id_his)
	
	lista_his = Historia.objects.all()
	lista_evo = Evolucion.objects.all()
	lista_pla = Plan.objects.all()

	for h in lista_his:
		if h.id == his.id:
			aux = h

	#his = Historia.objects.get(id=id_his)
	for e in lista_evo:
		if e.historia.id == aux.id:
			evoluciones.append(e)

	for p in lista_pla:
		if p.historia.id == aux.id:
			planes.append(p)


	ctx = {'historia':his, 'aux':aux, 'evoluciones':evoluciones, 'planes':planes}
	return render_to_response('home/singlehistoria.html', ctx, context_instance = RequestContext(request))

def evoluciones_view (request, id_pac):
	pac = Historia.objects.get(id=id_pac)
	
	lista_his = Historia.objects.all()
	lista_evo = Evolucion.objects.all()

	for h in lista_his:
		if h.paciente == pac.id:
			#aux = h
			for e in lista_evo:
				if h.id == e.historia:
					evoluciones = append(e)

	ctx = {'evoluciones':evoluciones}
	return render_to_response('home/evoluciones.html', ctx, context_instance = RequestContext(request))

def planes_view (request, id_pac):
	pac = Historia.objects.get(id=id_pac)
	
	lista_his = Historia.objects.all()
	lista_pla = Plan.objects.all()

	for h in lista_his:
		if h.paciente == pac.id:
			#aux = h
			for e in lista_pla:
				if h.id == e.historia:
					planes = append(e)

	ctx = {'planes':planes}
	return render_to_response('home/plan.html', ctx, context_instance = RequestContext(request))


def login_view(request):
	mensaje =""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				usuario = authenticate(username=username, password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect('/')
				else:
					mensaje = "usuario y/o password incorrecto"
		form =LoginForm()
		ctx = {'form':form, 'mensaje':mensaje}
		return render_to_response('home/login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

