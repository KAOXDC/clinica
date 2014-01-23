from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('clinica.apps.historias.views',
	url(r'^add/paciente/$','add_paciente_view', name="vista_agregar_paciente"),
	url(r'^add/ciudad/$','add_ciudad_view', name="vista_agregar_ciudad"),
	url(r'^add/persona/$','add_persona_view', name="vista_agregar_persona"),
	#url(r'^add/historia/(?P<id_pac>.*)/$','add_historia_view', name="vista_agregar_historia"),
	url(r'^add/historia/$','add_historia_view', name="vista_agregar_historia"),
	url(r'^add/evolucion/(?P<id_his>.*)/$','add_evolucion_view', name="vista_agregar_evolucion"),
	url(r'^add/plan/(?P<id_his>.*)/$','add_plan_view', name="vista_agregar_plan"),
	url(r'^add/profesional/$','add_profesional_view', name="vista_agregar_profesional"),
	url(r'^edit/historia/(?P<id_his>.*)$','edit_historia_view', name="vista_editar_historia"),
	url(r'^edit/profesional/(?P<id_pro>.*)$','edit_profesional_view', name="vista_editar_profesional"),
	url(r'^edit/evolucion/(?P<id_evo>.*)$','edit_evolucion_view', name="vista_editar_evolucion"),
	url(r'^edit/plan/(?P<id_pla>.*)$','edit_plan_view', name="vista_editar_plan"),

)