from django.conf.urls.defaults import patterns,url


urlpatterns = patterns('clinica.apps.home.views',
	url(r'^$','index_view',name='vista_principal'),
	url(r'^about/$','about_view',name='vista_about'),
	url(r'^contacto/$','contacto_view',name='vista_contacto'),
	url(r'^pacientes/page/(?P<pagina>.*)/$','pacientes_view',name='vista_pacientes'),
	url(r'^historias/page/(?P<pagina>.*)/$','historia_view',name='vista_historias'),
	url(r'^profesionales/page/(?P<pagina>.*)/$','profesionales_view',name='vista_profesionales'),
	url(r'^paciente/(?P<id_pac>.*)/$','singlePaciente_view',name='vista_single_paciente'),
	url(r'^profesional/(?P<id_pro>.*)/$','singleProfesional_view',name='vista_single_profesional'),
	url(r'^historia/(?P<id_his>.*)/$','singleHistoria_view',name='vista_single_historia'),
	url(r'^evoluciones/','evoluciones_view',name='vista_evolucion'),
	url(r'^buscar/$','buscar_view', name= 'vista_buscar'),
	url(r'^login/$', 'login_view', name= 'vista_login'),
	url(r'^logout/$', 'logout_view', name= 'vista_logout'),
)