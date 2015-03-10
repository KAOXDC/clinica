from django.contrib	import admin
from clinica.apps.historias.models import *

admin.site.register(Genero)
admin.site.register(Ciudad)
admin.site.register(Persona)

admin.site.register(TipoIdentificacion)
admin.site.register(Ips)
admin.site.register(Profesional)
admin.site.register(Paciente)
admin.site.register(Evolucion)
admin.site.register(Historia)
admin.site.register(TipoUsuario)
admin.site.register(Plan)
admin.site.register(Estado)

