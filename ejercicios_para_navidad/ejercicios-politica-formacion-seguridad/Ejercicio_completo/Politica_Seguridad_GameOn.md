# Política de Seguridad de GameOn

## Introducción

La organización que he elegido es una empresa de videojuegos llamada "GameOn". GameOn es una empresa que se dedica a la creación de juegos para consolas y PC desde hace años, pero en los últimos meses ha sido víctima de varios ataques DDoS y de malware, lo que resultó en la filtración de datos de sus clientes. Por lo tanto, es necesario implementar nuevas políticas de seguridad y preparar a sus trabajadores para enfrentar los riesgos a los que están expuestos.

## Objetivos

- Implementar soluciones avanzadas de mitigación de DDoS.
- Reducir el riesgo de ataques de phishing mediante la educación y la implementación de tecnologías de autenticación avanzada.
- Asegurar que los datos sensibles estén cifrados y protegidos.
- Minimizar el riesgo de acceso no autorizado a sistemas internos.
- Reducir las vulnerabilidades mediante actualizaciones y parches constantes.
- Implementar monitoreo de la red y de seguridad.

## Alcance

El alcance de esta política de seguridad se aplica a todos los empleados de la organización, a excepción de los diseñadores, quienes, por ahora, solo deben estar informados sobre el phishing y el monitoreo de la red.

## Normas

### Prevención de DDoS
- **Protección de red perimetral:** Todas las conexiones entrantes a la infraestructura deben pasar por un sistema de mitigación de DDoS de alta disponibilidad, como un servicio en la nube especializado (por ejemplo, Cloudflare).
- **Escalabilidad dinámica:** Los servidores críticos deben estar configurados para escalado automático en caso de picos inusuales de tráfico o intentos de DDoS.
- **Monitoreo de tráfico:** Todo el tráfico de red debe ser monitoreado constantemente mediante sistemas de detección de anomalías. Cualquier tráfico sospechoso o inusualmente alto debe generar alertas automáticas para su evaluación inmediata.

### Prevención de Phishing
- **Autenticación multifactor (MFA):** Todos los usuarios deben utilizar MFA para acceder a cualquier sistema que maneje información sensible.
- **Educación continua:** Los empleados deben realizar un curso de capacitación obligatorio sobre ciberseguridad cada seis meses, con énfasis en la identificación de intentos de phishing.
- **Filtrado de correo electrónico:** El sistema de correo debe incluir filtros para bloquear correos sospechosos con enlaces o adjuntos maliciosos.
- **Validación de enlaces:** Los empleados deben verificar siempre la autenticidad de los enlaces antes de hacer clic, utilizando herramientas de análisis de URLs.

### Protección de Datos Sensibles
- **Cifrado de datos:** Todo dato sensible debe estar cifrado tanto en tránsito como en reposo, usando protocolos como AES-256 y TLS 1.2 o superior.
- **Encriptación de backups:** Los backups deben ser cifrados y almacenados de forma segura. No se deben almacenar copias sin cifrar en ningún sistema, ya sea local o en la nube.
- **Acceso restringido:** Solo personal autorizado puede acceder a datos sensibles, basado en el principio de menor privilegio. El acceso debe ser monitorizado y auditado regularmente.
- **Eliminación segura:** Los datos sensibles deben eliminarse mediante métodos certificados de borrado seguro, como sobreescritura de datos o destrucción física de discos.

### Control de Acceso a Sistemas Internos
- **Gestión de privilegios:** Cada empleado debe tener acceso únicamente a las herramientas y sistemas necesarios para su rol.
- **Revisión de accesos:** Los accesos deben ser revisados trimestralmente para garantizar que no existan permisos innecesarios.
- **Bloqueo automático:** Implementar bloqueos automáticos en cuentas tras varios intentos fallidos de inicio de sesión.

### Actualizaciones y Parches
- **Actualización automática:** Configurar sistemas para aplicar actualizaciones automáticas de seguridad cuando sea posible.
- **Auditorías regulares:** El equipo de IT debe realizar auditorías mensuales para verificar que todos los sistemas y aplicaciones estén actualizados.
- **Gestión de vulnerabilidades:** Priorizar e implementar parches para vulnerabilidades críticas dentro de las 48 horas posteriores a su identificación.

### Monitoreo de la Red y de Seguridad
- **Sistemas de detección de intrusos (IDS/IPS):** Implementar sistemas que analicen el tráfico en tiempo real y bloqueen actividades sospechosas.
- **Alertas de seguridad:** Configurar notificaciones automáticas para eventos anómalos detectados en la red.
- **Análisis de registros:** Realizar análisis periódicos de registros para identificar patrones de comportamiento inusuales.

## Procedimientos

1. **Gestión de incidentes:**
   - Los incidentes de seguridad deben ser reportados de inmediato al equipo de IT a través del sistema interno de tickets.
   - Un equipo de respuesta debe analizar el incidente y aplicar las medidas correctivas necesarias en un plazo máximo de 24 horas.
   - Se debe mantener un registro detallado de todos los incidentes, incluyendo su naturaleza, impacto y las medidas implementadas.

2. **Actualizaciones y parches:**
   - Todos los sistemas deben estar configurados para aplicar actualizaciones automáticas siempre que sea posible.
   - El equipo de IT debe realizar auditorías mensuales para verificar que todos los sistemas estén actualizados.
   - Las actualizaciones críticas deben ser priorizadas y aplicadas inmediatamente tras su lanzamiento.

3. **Accesos y contraseñas:**
   - Los empleados deben cambiar sus contraseñas cada 90 días.
   - Las contraseñas deben cumplir con requisitos de longitud y complejidad, incluyendo mínimo 12 caracteres, mayúsculas, números y símbolos especiales.
   - Los accesos deben ser revocados inmediatamente cuando un empleado deja la organización o cambia de rol.

4. **Auditorías internas:**
   - Se realizarán auditorías trimestrales para revisar el cumplimiento de las políticas de seguridad.
   - Cualquier desviación o incumplimiento detectado deberá ser subsanado en un plazo de 15 días.

## Responsabilidades

- **Empleados:** Cumplir con las normas establecidas, reportar incidentes de seguridad y asistir a las capacitaciones obligatorias.
- **Equipo de IT:** Implementar y supervisar las políticas de seguridad, realizar auditorías periódicas y responder a incidentes.
- **Directivos:** Promover la cultura de seguridad dentro de la organización, garantizar la asignación de recursos y aprobar cambios en las políticas.
- **Líderes de equipo:** Asegurarse de que sus equipos cumplan con las políticas y reportar cualquier anomalía o problema de seguridad.

## Sanciones

- **Infracciones leves:** Una advertencia escrita para el empleado, seguida de una sesión obligatoria de recapacitación.
- **Infracciones graves:** Suspensión temporal del acceso a sistemas y revisión disciplinaria. Incluye compartir contraseñas, ignorar actualizaciones o no reportar incidentes de seguridad.
- **Infracciones reiteradas o críticas:** Despido inmediato y, si corresponde, acción legal. Por ejemplo, la manipulación o divulgación intencional de datos sensibles.

## Revisión y Actualización

La política de seguridad será revisada y actualizada cada seis meses por el equipo de IT, en colaboración con el departamento legal y los directivos. Además, se realizarán revisiones extraordinarias tras cualquier incidente grave que revele vulnerabilidades en las medidas actuales.
