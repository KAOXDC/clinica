from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from clinica.apps.historias.forms import *
from clinica.apps.historias.models import *
from django.http import HttpResponseRedirect
from django.forms.models import inlineformset_factory
from datetime import date 
def calculate_age(born):
    today = date.today()
    try: 
        birthday = born.replace(year=today.year)
    except ValueError: # raised when birth date is February 29 and the current year is not a leap year
        birthday = born.replace(year=today.year, day=born.day-1)
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year

def add_persona_view(request):
	if request.user.is_authenticated():
		now = date.today()
		if request.method == "POST":
			form_a = addCiudadForm(request.POST, prefix = "a")
			form_b = addPersonaForm(request.POST, prefix = "b")
			if form_a.is_valid() and form_b.is_valid():
				a = form_a.save()
				b = form_b.save(commit=False)

				b.edad = calculate_age(b.fecha_nacimiento)

				b.ciudad = a
				b.save()
				return HttpResponseRedirect("/add/persona/")
			else:
				info = "fallo"	
		else:
			form_a = addCiudadForm(prefix = "a")
			form_b = addPersonaForm(prefix = "b")
		ctx = {'form_a':form_a, 'form_b':form_b, 'now':now}	
		return render_to_response ('historias/addpersona.html',ctx, context_instance= RequestContext(request) )	
	else:
		return HttpResponseRedirect('/')

#Agregar un nuevo Profesional
def add_profesional_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			form_per = addPersonaForm(request.POST, prefix = "per")
			form_pro = addProfesionalForm(request.POST, prefix = "pro")
			if form_per.is_valid() and form_pro.is_valid():
				per = form_per.save(commit=False)
				per.edad = calculate_age(per.fecha_nacimiento)
				per.save()
				pro = form_pro.save(commit=False)
				pro.persona = per
				pro.save()
				info = "Profesional Guardado Satisfactoriamente"
				return HttpResponseRedirect ("/profesionales/page/1")

			else:
				info = "Fallo el Registro del Profesional"
		else:
			form_per = addPersonaForm(prefix = "per")
			form_pro = addProfesionalForm(prefix = "pro")
		ctx = {'form_pro':form_pro,'form_per':form_per}
		return render_to_response ('historias/addprofesional.html',ctx,context_instance = RequestContext(request))
	else:
		return HttpResponseRedirect('/')

#Agregar un nuevo Paciente
def add_paciente_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			form_per = addPersonaForm(request.POST, prefix = "per")
			form_pac = addPacienteForm(request.POST, prefix = "pac")
			if form_per.is_valid() and form_pac.is_valid():
				per = form_per.save()
				pac = form_pac.save(commit=False)
				pac.persona = per
				pac.save()
				info = "Paciente Guardado Satisfactoriamente"
				return HttpResponseRedirect ("/pacientes/page/1")

			else:
				info = "Fallo el Registro de Paciente"
		else:
			form_per = addPersonaForm(prefix = "per")
			form_pac = addPacienteForm(prefix = "pac")
		ctx = {'form_pac':form_pac,'form_per':form_per}
		return render_to_response ('historias/addpaciente.html',ctx,context_instance = RequestContext(request))
	else:
		return HttpResponseRedirect('/')

#Agregar Historia
def add_historia_view(request):
	if request.user.is_authenticated():
		now = date.today()
		if request.method == "POST":
			form_per = addPersonaForm(request.POST, prefix = "per")
			form_pac = addPacienteForm(request.POST, prefix = "pac")
			form_his = addHistoriaForm(request.POST, prefix = "his")
			if form_per.is_valid() and form_pac.is_valid() and form_his.is_valid():
				per = form_per.save(commit=False)
				per.edad = calculate_age(per.fecha_nacimiento)
				per.save()
				pac = form_pac.save(commit=False)
				his = form_his.save(commit=False)
				pac.persona = per
				pac.save()
				his.paciente = pac
				his.codigo = pac.persona.cedula
				his.fecha = now
				his.save()
				info = "Paciente Guardado Satisfactoriamente"
				return HttpResponseRedirect ('/historia/%s'%his.id)
			else:
				info = "Error Registro Historia"
		else:
			form_per = addPersonaForm(prefix = "per")
			form_pac = addPacienteForm(prefix = "pac")
			form_his = addHistoriaForm(prefix = "his")
		ctx =  {'form_his':form_his, 'form_per':form_per, 'form_pac':form_pac ,'now':now }
		return render_to_response ('historias/addhistoria.html', ctx,  context_instance = RequestContext(request))
	else:
		return HttpResponseRedirect('/')		

def add_plan_view(request, id_his):
	if request.user.is_authenticated():
		now = date.today()
		his = Historia.objects.get(id= id_his)
		if request.method == "POST":
			form_pla = addPlanForm(request.POST, prefix = "pla")
			if form_pla.is_valid():
				pla = form_pla.save(commit = False)
				pla.historia = his
				pla.fecha = now
				pla.save()
				info = "Evolucion Guardado Satisfactoriamente"
				return HttpResponseRedirect ('/historia/%s'%his.id)
			else:
				info = "Fallo el Registro de Evolucion"
		else:
			form_pla = addPlanForm(prefix = "pla")
		ctx =  {'form_pla':form_pla, 'his':his}
		return render_to_response ('historias/addplan.html', ctx,  context_instance = RequestContext(request))
	else:
		return HttpResponseRedirect('/')
	

def add_evolucion_view(request, id_his):
	if request.user.is_authenticated():
		now = date.today()
		his = Historia.objects.get(id= id_his)
		if request.method == "POST":
			form_evo = addEvolucionForm(request.POST, prefix = "evo")
			if form_evo.is_valid():
				evo = form_evo.save(commit = False)
				evo.historia = his
				evo.fecha = now
				evo.save()
				info = "Evolucion Guardado Satisfactoriamente"
				return HttpResponseRedirect ('/historia/%s'%his.id)
			else:
				info = "Fallo el Registro de Evolucion"
		else:
			form_evo = addEvolucionForm(prefix = "evo")
		ctx =  {'form_evo':form_evo, 'his':his}
		return render_to_response ('historias/addevolucion.html', ctx,  context_instance = RequestContext(request))
	else:
		return HttpResponseRedirect('/')
		

def add_ciudad_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			form = addCiudadForm(request.POST)
			info = "inicializando"
			if form.is_valid():
				nombre = form.cleaned_data['nombre']
				c = Ciudad()
				c.ciu_nombre = nombre
				c.save()
				info = "Guardado Satisfactoriamente"
			else:
				info = "Datos Incorrectos"
			form = addCiudadForm()
			ctx = {'form':form , 'informacion':info}
			return render_to_response('historias/addciudad.html',ctx, context_instance= RequestContext(request))

		else: #GET
			form = addCiudadForm()
			ctx = {'form':form} 
			return render_to_response('historias/addciudad.html',ctx ,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')


'''
EDITAR 
'''

def edit_plan_view(request, id_pla):
	now = date.today()
	if request.user.is_authenticated():
		pla = Plan.objects.get(id= id_pla)
		old = pla.fecha 
		his = Historia.objects.get( id= pla.historia.id)
		if request.method == "POST":
			form_pla = addPlanForm(request.POST, instance = pla)
			if form_pla.is_valid():
				pla = form_pla.save(commit = False)
				pla.historia = his
				pla.fecha = old
				pla.save()
				info = "Evolucion Guardado Satisfactoriamente"
				return HttpResponseRedirect ('/historia/%s'%his.id)
			else:
				info = "Fallo el Registro de Evolucion"
		else:
			form_pla = addPlanForm(instance = pla)
		ctx =  {'form_pla':form_pla, 'pla':pla, 'his':his}
		return render_to_response ('historias/editplan.html', ctx,  context_instance = RequestContext(request))
	else:
		return HttpResponseRedirect('/')


def edit_evolucion_view(request, id_evo):
	now = date.today()
	if request.user.is_authenticated():
		evo = Evolucion.objects.get(id= id_evo)
		old = evo.fecha 
		his = Historia.objects.get( id= evo.historia.id)
		if request.method == "POST":
			form_evo = addEvolucionForm(request.POST, instance = evo)
			if form_evo.is_valid():
				evo = form_evo.save(commit = False)
				evo.historia = his
				evo.fecha = old
				evo.save()
				info = "Evolucion Guardado Satisfactoriamente"
				return HttpResponseRedirect ('/historia/%s'%his.id)
			else:
				info = "Fallo el Registro de Evolucion"
		else:
			form_evo = addEvolucionForm(instance = evo)
		ctx =  {'form_evo':form_evo, 'evo':evo, 'his':his}
		return render_to_response ('historias/editevolucion.html', ctx,  context_instance = RequestContext(request))
	else:
		return HttpResponseRedirect('/')


def edit_historia_view(request, id_his):
	now = date.today()
	
	his = Historia.objects.get(id = id_his)
	pac = Paciente.objects.get(id = his.paciente.id )
	per = Persona.objects.get(id = pac.persona.id )
	if request.method == "POST":
		form_per = addPersonaForm(request.POST,instance =per)
		form_pac = addPacienteForm(request.POST,instance =pac)
		form_his = addHistoriaForm(request.POST,instance =his)
		if form_per.is_valid() and form_pac.is_valid() and form_his.is_valid():
			per = form_per.save(commit=False)
			per.edad = calculate_age(per.fecha_nacimiento)
			per.save()
			pac = form_pac.save(commit=False)
			his = form_his.save(commit=False)
			pac.persona = per
			pac.save()
			his.paciente = pac
			his.codigo = pac.persona.cedula
			his.save()
			info = "Paciente Guardado Satisfactoriamente"
			return HttpResponseRedirect ("/historia/%s"%his.id)
		else:
			info = "Error Registro Historia"
	else:
		form_per = addPersonaForm(instance  = per)
		form_pac = addPacienteForm(instance = pac)
		form_his = addHistoriaForm(instance = his)
	ctx = {'form_his':form_his, 'form_per':form_per , 'form_pac':form_pac ,'now':now , 'his':his} 
	return render_to_response('historias/edithistoria.html', ctx,  context_instance= RequestContext(request))

def edit_profesional_view(request, id_pro):
	pro = Profesional.objects.get(id=id_pro)
	per = Persona.objects.get(id=pro.persona.id)
	if request.method == "POST":
		form_per = addPersonaForm(request.POST, instance = per)
		form_pro = addProfesionalForm(request.POST, instance = pro)
		if form_per.is_valid() and form_pro.is_valid():
			per = form_per.save(commit=False)
			per.edad = calculate_age(per.fecha_nacimiento)
			per.save()
			pro = form_pro.save(commit=False)
			pro.persona = per
			pro.save()
			info = "Profesional Guardado Satisfactoriamente"
			return HttpResponseRedirect ("/profesionales/page/1")
		else:
			info = "Fallo el Registro del Profesional"
	else:
		form_per = addPersonaForm(instance = per)
		form_pro = addProfesionalForm(instance = pro)
	ctx = {'form_pro':form_pro,'form_per':form_per, 'pro':pro}
	return render_to_response('historias/editprofesional.html', ctx,  context_instance= RequestContext(request))