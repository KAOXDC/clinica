# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from clinica.apps.reportes.forms import ReporteForm, CumpleForm
from django.forms import extras
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from datetime import *
import datetime
from clinica.apps.historias.forms import *
from clinica.apps.historias.models import *
from datetime import date 

def reportes_view(request):
	return render_to_response('home/reportes.html',context_instance = RequestContext(request)) 
	

def reporte_diag_vs_trat_view(request):
	info_enviado = False
	fecha_ini = ""
	fecha_fin = ""
	num_diag = 0
	num_trat = 0
	#num_diag = Plan.objects.count()
	
	if request.method == "POST":
		reportes = ReporteForm(request.POST)
		if reportes.is_valid():
			info_enviado = True
			fecha_ini = reportes.cleaned_data['fecha_ini']
			fecha_fin = reportes.cleaned_data['fecha_fin']
			num_diag = Plan.objects.filter(fecha__range=(fecha_ini, fecha_fin)).count()
			num_trat = Evolucion.objects.filter(fecha__range=(fecha_ini, fecha_fin)).count()
	else:
		reportes = ReporteForm()
	ctx = {'reporte1':reportes, 'num_diag':num_diag, 'num_trat':num_trat ,'info_enviado':info_enviado, 'fecha_ini':fecha_ini, 'fecha_fin':fecha_fin}
	return render_to_response('reportes/diag_vs_trat.html',ctx, context_instance = RequestContext(request)) 

def reporte_diag_incompleto_view(request):
	info_enviado = False
	fecha_ini = ""
	fecha_fin = ""
	num_diag_inc = 0
	num_diag_com = 0
	num_diag_can = 0
	num_diag_pro = 0
	plan_inc = []
	plan_pro = []

	if request.method == "POST":
		reportes = ReporteForm(request.POST)
		if reportes.is_valid():
			info_enviado = True
			fecha_ini = reportes.cleaned_data['fecha_ini']
			fecha_fin = reportes.cleaned_data['fecha_fin']
			num_diag_inc = Plan.objects.filter(fecha__range=(fecha_ini, fecha_fin), estado='1').count()
			num_diag_com = Plan.objects.filter(fecha__range=(fecha_ini, fecha_fin), estado='2').count()
			num_diag_can = Plan.objects.filter(fecha__range=(fecha_ini, fecha_fin), estado='3').count()
			num_diag_pro = Plan.objects.filter(fecha__range=(fecha_ini, fecha_fin), estado='4').count()
			plan_inc = Plan.objects.filter(fecha__range=(fecha_ini, fecha_fin), estado='1')
			plan_pro = Plan.objects.filter(fecha__range=(fecha_ini, fecha_fin), estado='4')
	else:
		reportes = ReporteForm()
	ctx = {'reporte2':reportes,'plan_inc':plan_inc, 'plan_pro':plan_pro, 'num_diag_inc':num_diag_inc, 'info_enviado':info_enviado, 'fecha_ini':fecha_ini, 'fecha_fin':fecha_fin, 'num_diag_com':num_diag_com, 'num_diag_can':num_diag_can, 'num_diag_pro':num_diag_pro}
	return render_to_response('reportes/diag_incompletos.html',ctx, context_instance = RequestContext(request)) 

def reporte_genero_view(request):
	hom_mayores = 0
	muj_mayores = 0
	hom_menores = 0
	muj_menores = 0
	hom_total = 0
	muj_total = 0
	info_enviado = True
	#num_mayores = Plan.objects.filter(historia__paciente__persona__edad__range=('18','120'), fecha__range=(fecha_ini, fecha_fin) ).count()# ).count()
	hom_mayores = Paciente.objects.filter(persona__edad__range=('18','120'), persona__genero__nombre='Masculino').count()
	muj_mayores = Paciente.objects.filter(persona__edad__range=('18','120'), persona__genero__nombre='Femenino').count()
	hom_menores = Paciente.objects.filter(persona__edad__range=('0','17'), persona__genero__nombre='Masculino').count()
	muj_menores = Paciente.objects.filter(persona__edad__range=('0','17'), persona__genero__nombre='Femenino').count()
	hom_total = hom_menores + hom_mayores
	muj_total = muj_menores + muj_mayores
	
	ctx = {'hom_total':hom_total, 'muj_total':muj_total, 'hom_mayores':hom_mayores, 'muj_mayores':muj_mayores, 'hom_menores':hom_menores, 'muj_menores':muj_menores,'info_enviado':info_enviado}
	return render_to_response('reportes/reporte_genero.html', ctx, context_instance = RequestContext(request)) 

def reporte_cumple_view(request):
	info_enviado = False
	fecha_cumple = ""
	#hoy = date.today()
	#mes = hoy.month
	mes = 0
	mes_str = ""
	pac_cumple = []


	if request.method == "POST":
		reportes = CumpleForm(request.POST)
		if reportes.is_valid():
			info_enviado = True
			fecha_cumple = reportes.cleaned_data['fecha_cumple']
			mes = fecha_cumple.month
			pac_cumple = Historia.objects.filter(paciente__persona__fecha_nacimiento__month = mes)
			mes_str=fecha_cumple.strftime('%B')
	else:
		reportes = CumpleForm()
	ctx = {'mes_str':mes_str,'reporte_cumple':reportes, 'pac_cumple':pac_cumple, 'info_enviado':info_enviado, 'fecha_cumple':fecha_cumple }
	return render_to_response('reportes/cumple.html',ctx, context_instance = RequestContext(request)) 

