BEGIN;
CREATE TABLE `historias_genero` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `nombre` varchar(20) NOT NULL
)
;
CREATE TABLE `historias_ciudad` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `nombre` varchar(200) NOT NULL
)
;
CREATE TABLE `historias_tipoidentificacion` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `abreviacion` varchar(20) NOT NULL,
    `nombre` varchar(200) NOT NULL
)
;
CREATE TABLE `historias_persona` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `nombres` varchar(200) NOT NULL,
    `apellido1` varchar(200) NOT NULL,
    `apellido2` varchar(200) NOT NULL,
    `fecha_nacimiento` date NOT NULL,
    `edad` varchar(20) NOT NULL,
    `identificacion_id` integer NOT NULL,
    `cedula` varchar(20) NOT NULL UNIQUE,
    `direccion` varchar(200) NOT NULL,
    `telefono` varchar(200) NOT NULL,
    `email` varchar(200) NOT NULL,
    `ciudad_id` integer NOT NULL,
    `genero_id` integer NOT NULL
)
;
ALTER TABLE `historias_persona` ADD CONSTRAINT `genero_id_refs_id_e880165d` FOREIGN KEY (`genero_id`) REFERENCES `historias_genero` (`id`);
ALTER TABLE `historias_persona` ADD CONSTRAINT `ciudad_id_refs_id_87240a54` FOREIGN KEY (`ciudad_id`) REFERENCES `historias_ciudad` (`id`);
ALTER TABLE `historias_persona` ADD CONSTRAINT `identificacion_id_refs_id_9c9038fe` FOREIGN KEY (`identificacion_id`) REFERENCES `historias_tipoidentificacion` (`id`);
CREATE TABLE `historias_ips` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `ips_nombre` varchar(500) NOT NULL
)
;
CREATE TABLE `historias_tipousuario` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `tipo_usuario` varchar(200) NOT NULL
)
;
CREATE TABLE `historias_paciente` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `persona_id` integer NOT NULL,
    `empresa` varchar(200) NOT NULL,
    `direccion` varchar(200) NOT NULL,
    `telefono` varchar(20) NOT NULL,
    `cargo` varchar(200) NOT NULL,
    `acudiente` varchar(200) NOT NULL,
    `telefono_acudiente` varchar(20) NOT NULL,
    `ips_id` integer NOT NULL,
    `tipo_id` integer NOT NULL,
    `carnet` varchar(200) NOT NULL
)
;
ALTER TABLE `historias_paciente` ADD CONSTRAINT `persona_id_refs_id_9eb9ff2b` FOREIGN KEY (`persona_id`) REFERENCES `historias_persona` (`id`);
ALTER TABLE `historias_paciente` ADD CONSTRAINT `ips_id_refs_id_8139beec` FOREIGN KEY (`ips_id`) REFERENCES `historias_ips` (`id`);
ALTER TABLE `historias_paciente` ADD CONSTRAINT `tipo_id_refs_id_f884d125` FOREIGN KEY (`tipo_id`) REFERENCES `historias_tipousuario` (`id`);
CREATE TABLE `historias_profesional` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `profesion` varchar(200) NOT NULL,
    `codigo` varchar(20) NOT NULL,
    `persona_id` integer NOT NULL
)
;
ALTER TABLE `historias_profesional` ADD CONSTRAINT `persona_id_refs_id_a7471a3d` FOREIGN KEY (`persona_id`) REFERENCES `historias_persona` (`id`);
CREATE TABLE `historias_historia` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `codigo` varchar(200) NOT NULL UNIQUE,
    `fecha` date NOT NULL,
    `paciente_id` integer NOT NULL,
    `doctor_id` integer NOT NULL
)
;
ALTER TABLE `historias_historia` ADD CONSTRAINT `paciente_id_refs_id_28cc8a96` FOREIGN KEY (`paciente_id`) REFERENCES `historias_paciente` (`id`);
ALTER TABLE `historias_historia` ADD CONSTRAINT `doctor_id_refs_id_cc0cf04f` FOREIGN KEY (`doctor_id`) REFERENCES `historias_profesional` (`id`);
CREATE TABLE `historias_evolucion` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `historia_id` integer NOT NULL,
    `doctor_id` integer NOT NULL,
    `fecha` date NOT NULL,
    `diente` varchar(200) NOT NULL,
    `superficie` varchar(200) NOT NULL,
    `descripcion` longtext NOT NULL
)
;
ALTER TABLE `historias_evolucion` ADD CONSTRAINT `doctor_id_refs_id_c3ad6cb5` FOREIGN KEY (`doctor_id`) REFERENCES `historias_profesional` (`id`);
ALTER TABLE `historias_evolucion` ADD CONSTRAINT `historia_id_refs_id_0dbd43d6` FOREIGN KEY (`historia_id`) REFERENCES `historias_historia` (`id`);
CREATE TABLE `historias_plan` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `historia_id` integer NOT NULL,
    `doctor_id` integer NOT NULL,
    `fecha` date NOT NULL,
    `diente` varchar(200) NOT NULL,
    `superficie` varchar(200) NOT NULL,
    `diagnostico` longtext NOT NULL,
    `plan_de_tratamiento` longtext NOT NULL
)
;
ALTER TABLE `historias_plan` ADD CONSTRAINT `doctor_id_refs_id_70f7d987` FOREIGN KEY (`doctor_id`) REFERENCES `historias_profesional` (`id`);
ALTER TABLE `historias_plan` ADD CONSTRAINT `historia_id_refs_id_0b13d026` FOREIGN KEY (`historia_id`) REFERENCES `historias_historia` (`id`);
CREATE INDEX `historias_persona_0a74282e` ON `historias_persona` (`identificacion_id`);
CREATE INDEX `historias_persona_67a22d87` ON `historias_persona` (`ciudad_id`);
CREATE INDEX `historias_persona_7bcc6f63` ON `historias_persona` (`genero_id`);
CREATE INDEX `historias_paciente_0b03659e` ON `historias_paciente` (`persona_id`);
CREATE INDEX `historias_paciente_b38e2a5d` ON `historias_paciente` (`ips_id`);
CREATE INDEX `historias_paciente_acf1eac4` ON `historias_paciente` (`tipo_id`);
CREATE INDEX `historias_profesional_0b03659e` ON `historias_profesional` (`persona_id`);
CREATE INDEX `historias_historia_e922f925` ON `historias_historia` (`paciente_id`);
CREATE INDEX `historias_historia_72821be1` ON `historias_historia` (`doctor_id`);
CREATE INDEX `historias_evolucion_03a3cf99` ON `historias_evolucion` (`historia_id`);
CREATE INDEX `historias_evolucion_72821be1` ON `historias_evolucion` (`doctor_id`);
CREATE INDEX `historias_plan_03a3cf99` ON `historias_plan` (`historia_id`);
CREATE INDEX `historias_plan_72821be1` ON `historias_plan` (`doctor_id`);

COMMIT;
