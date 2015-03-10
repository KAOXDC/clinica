from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('clinica.apps.reportes.views',
#	url(r'^historia/(?P<id_his>.*)/$','singleHistoria_view',name='vista_single_historia'),
	url(r'^reportes/cumple/$', 'reporte_cumple_view', name = 'vista_reporte_cumple'),
	url(r'^reportes/genero/$', 'reporte_genero_view', name = 'vista_reporte_genero'),
	url(r'^reportes/diagvstrat/$', 'reporte_diag_vs_trat_view', name = 'vista_reporte_diag_vs_trat'),
	url(r'^reportes/diagincompleto/$', 'reporte_diag_incompleto_view', name = 'vista_reporte_diag_incompleto'),
	url(r'^reportes/$', 'reportes_view', name = 'vista_reportes'),

)