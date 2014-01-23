from django.db import models

superficies = (
	('incisal', 'Incisal'),
	('oclusal', 'Oclusal'),
	('vestibular', 'Vestibular'),
	('mesial','Mesial'),
	('distal','Distal'),
	('palatina','Palatina'),
	('lingual','Lingual'),
	('angulo mesial','Angulo Mesial'),
	('angulo distal','Angulo Distal'),
)

dientes =(
	('11','11'),
	('12','12'),
	('13','13'),
	('14','14'),
	('15','15'),
	('16','16'),
	('17','17'),
	('18','18'),
	
	('21','21'),
	('22','22'),
	('23','23'),
	('24','24'),
	('25','25'),
	('26','26'),
	('27','27'),
	('28','28'),

	('31','31'),
	('32','32'),
	('33','33'),
	('34','13'),
	('35','35'),
	('36','36'),
	('37','37'),
	('38','38'),
	
	('41','41'),
	('42','42'),
	('43','43'),
	('44','44'),
	('45','45'),
	('46','46'),
	('47','47'),
	('48','48'),
	
	('51','51'),
	('52','52'),
	('53','53'),
	('54','54'),
	('55','55'),

	('61','61'),
	('62','62'),
	('63','63'),
	('64','64'),
	('65','65'),

	('71','71'),
	('72','72'),
	('73','73'),
	('74','74'),
	('75','75'),
	
	('81','81'),
	('82','82'),
	('83','83'),
	('84','84'),
	('85','85'),

)

class Genero(models.Model):
	nombre			=models.CharField(max_length=20)
	def __unicode__(self):
		return self.nombre

class Ciudad(models.Model):
	nombre			=models.CharField(max_length=200)
	def __unicode__(self):
		return self.nombre	

class TipoIdentificacion(models.Model):
	abreviacion				= models.CharField(max_length=20)
	nombre 					= models.CharField(max_length=200)
	def __unicode__ (self):
		return self.abreviacion

class Persona(models.Model):
	nombres					=models.CharField(max_length=200)
	apellido1				=models.CharField(max_length=200)
	apellido2				=models.CharField(max_length=200)
	fecha_nacimiento		=models.DateField()
	edad					=models.CharField(max_length=20)
	identificacion 			=models.ForeignKey(TipoIdentificacion)
	cedula					=models.CharField(max_length=20, unique=True)
	direccion				=models.CharField(max_length=200, blank=True)
	telefono				=models.CharField(max_length=200, blank=True)
	email					=models.EmailField(max_length=200, blank=True)
	ciudad					=models.ForeignKey(Ciudad)
	genero 					=models.ForeignKey(Genero)
	def __unicode__ (self):
		nombre_completo = "%s %s %s"% (self.nombres, self.apellido1, self.apellido2)
		return nombre_completo

class Ips(models.Model):
	ips_nombre 				=models.CharField(max_length=500)
	def __unicode__ (self):
		return self.ips_nombre

class TipoUsuario(models.Model):
	tipo_usuario 			=models.CharField(max_length=200)#tabla de tipo de usuario
	def __unicode__(self):
		return self.tipo_usuario

class Paciente(models.Model):
	persona					=models.ForeignKey(Persona)
	# Trabajo de la Persona
	empresa					=models.CharField(max_length=200, blank=True)
	direccion				=models.CharField(max_length=200, blank=True)
	telefono				=models.CharField(max_length=20,  blank=True)
	cargo					=models.CharField(max_length=200, blank=True)
	# En caso de Emergencia  Avisar  a:
	acudiente				=models.CharField(max_length=200, blank=True)
	telefono_acudiente		=models.CharField(max_length=20,  blank=True)
	# Nombre IPS
	ips						=models.ForeignKey(Ips)
	tipo 					=models.ForeignKey(TipoUsuario)
	carnet					=models.CharField(max_length=200, blank=True)
	def __unicode__ (self):
		nombre_completo = "%s %s %s"% (self.persona.nombres, self.persona.apellido1, self.persona.apellido2)
		return nombre_completo

class Profesional(models.Model):
	profesion 				=models.CharField(max_length=200)
	codigo					=models.CharField(max_length=20)
	persona					=models.ForeignKey(Persona)
	def __unicode__ (self):
		return self.persona

class Historia (models.Model):
	codigo					=models.CharField(max_length=200, unique=True)
	fecha 					=models.DateField() 
	paciente				=models.ForeignKey(Paciente)
	doctor					=models.ForeignKey(Profesional)
	def __unicode__(self):
		return self.codigo

class Evolucion(models.Model):
	historia				=models.ForeignKey(Historia)
	doctor					=models.ForeignKey(Profesional)
	fecha					=models.DateField()
	diente					=models.CharField(max_length=200, choices=dientes)
	superficie				=models.CharField(max_length=200, choices=superficies)
	descripcion				=models.TextField(max_length=1000)
	def __unicode__ (self):
		return self.descripcion
		
class Plan(models.Model):
	historia				=models.ForeignKey(Historia)
	doctor					=models.ForeignKey(Profesional)
	fecha					=models.DateField()
	diente					=models.CharField(max_length=200, choices=dientes)
	superficie				=models.CharField(max_length=200, choices=superficies)
	diagnostico				=models.TextField(max_length=1000)
	plan_de_tratamiento		=models.TextField(max_length=1000)
	def __unicode__ (self):
		return self.diagnostico