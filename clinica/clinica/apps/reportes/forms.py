from django import forms

class ReporteForm(forms.Form):
	#fecha_ini = forms.DateField(widget = forms.TextInput(), label='Fecha Inicial')
	fecha_ini = forms.DateField(widget = forms.TextInput(attrs={'id':'datepicker'}), label='Fecha Inicial')
	fecha_fin = forms.DateField(widget = forms.TextInput(attrs={'id':'datepicker1'}), label='Fecha Final')
	#reporte1 = forms.BooleanField(widget = forms.CheckboxInput, required=False, initial=True)

class CumpleForm(forms.Form):
	#fecha_ini = forms.DateField(widget = forms.TextInput(), label='Fecha Inicial')
	fecha_cumple = forms.DateField(widget = forms.TextInput(attrs={'id':'datepicker'}), label='Mes del Reporte')	

