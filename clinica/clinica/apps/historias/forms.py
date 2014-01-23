from django import forms
from django.forms.extras import SelectDateWidget
from django.contrib.admin import widgets

#from django.forms.models import inlineformset_factory

#from django import ModelForm
from clinica.apps.historias.models import  Paciente, Persona, Ciudad, Genero, Historia, Evolucion, Profesional, Plan

class addPersonaForm(forms.ModelForm):
	#fecha_nacimiento = forms.DateField(widget=SelectDateWidget(years = range (1900,2014)))
	fecha_nacimiento = forms.DateField(widget=forms.TextInput(attrs={'id':'datepicker'}))
	class Meta:
		model = Persona
		exclude = ('edad',)
		#fields = ('nombres', 'apellido1', 'apellido2', 'fecha_nacimiento','edad','cedula','ciudad',	'genero' )

class addCiudadForm(forms.ModelForm):
	class Meta:
		model = Ciudad
"""	nombre =forms.CharField(widget=forms.TextInput())

	def clean(self):
		return self.cleaned_data
"""
class addProfesionalForm(forms.ModelForm):
	class Meta:
		model  = Profesional
		exclude = ('persona',)


class addPacienteForm(forms.ModelForm):
	class Meta:
		model = Paciente
		exclude = ('persona',)

class showPacienteHistoria(forms.ModelForm):
	class Meta:
		model = Paciente
		#exclude = ('empresa', 'direccion', 'telefono', 'cargo', 'acudiente', 'telefono_acudiente', 'ips', 'tipo', 'carnet')


class addHistoriaForm(forms.ModelForm):
	#fecha = forms.DateField(widget=forms.TextInput(attrs={'id':'datepicker1'}))
	class Meta:
		model = Historia
		exclude = ('paciente','codigo','fecha',)

class addEvolucionForm(forms.ModelForm):
	#fecha = forms.DateField(widget=forms.TextInput(attrs={'id':'datepicker'}))
	class Meta:
		model = Evolucion
		exclude = ('historia','fecha',)

class addPlanForm(forms.ModelForm):
	#fecha = forms.DateField(widget=forms.TextInput(attrs={'id':'datepicker'}))
	class Meta:
		model = Plan
		exclude = ('historia','fecha',)
