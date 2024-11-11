Normas, donde se establezcan las normas de seguridad que deben seguir los empleados.
Procedimientos, donde se establezcan los procedimientos de seguridad que deben seguir los
empleados.
Responsabilidades, donde se establezcan las responsabilidades de los empleados en materia de
seguridad.
Sanciones, donde se establezcan las sanciones en caso de incumplimiento de las normas de
seguridad, si las hay.
Revisión y actualización, donde se establezca la periodicidad con la que se revisará y actualizará la
política de seguridad.

# Introducción

La organización que he elegido es una empresa de videojuegos llamada "GameOn". GameOn es una empresa de videojuegos que se dedica a la creación de juegos para consolas y PC desde hace años pero en los últimos meses ha sido víctima de varios ataques DDOS y de malware en la cual se filtraron datos de sus clientes. Por lo tanto, es necesario implementar nuevas políticas de seguridad y prevenir a sus trabajadores de los riesgos a los que están expuestos.

# Objetivos

Los objetivos a establecer son los siguientes:

- Implementar soluciones avanzadas de mitigación de DDOS.
- Reducir el riesgo de ataques de phishing mediante la educación y la implementación de tecnologías de autenticación avanzada.
- Asegurar que los datos sensibles estén cifrados y protegidos.
- Minimizar el riesgo de acceso no autorizado a sistemas internos.
- Reducir las vulnerabilidades mediante actualizaciones y parches constantes.
- Implementar Monitoreo de la Red y de Seguridad

# Alcance

El alcance de estos refuerzos en la politica de seguridad será aplicado a todos los empleados de la organización a excepción de los diseñadores, los cuales por ahora solo deberán estar informados sobre el phishing y el monitoreo de la red.

# Normas

## Prevención de DDOS
- Protección de red perimetral: Todas las conexiones entrantes a la infraestructura deben pasar por un sistema de mitigación de DDoS de alta disponibilidad, como un servicio en la nube especializado (por ejemplo, Cloudflare).
- Escalabilidad dinámica: Los servidores críticos deben estar configurados para escalado automático en caso de picos inusuales de tráfico o de intentos de DDoS.
- Monitoreo de tráfico: Todo el tráfico de red debe ser monitoreado constantemente mediante sistemas de detección de anomalías. Cualquier tráfico sospechoso o inusualmente alto debe generar alertas automáticas para su evaluación inmediata.

La relevancia de estas normas radica en que al tener servidores de juegos online y un sitio web, además de servicios de backend accesibles a usuarios globales, los ataques DDoS representan una amenaza seria. Implementar soluciones avanzadas de mitigación DDoS, monitoreo de tráfico y escalabilidad dinámica protegería a "GameOn" de interrupciones en sus servicios, garantizando la disponibilidad de los servidores para los jugadores. 

## Prevención de Phishing
- Autenticación multifactor: Todos los usuarios, tanto internos como externos (clientes, proveedores, etc.), deben utilizar autenticación multifactor (MFA) para acceder a cualquier sistema que maneje información sensible.
- Educación continua sobre phishing: Todos los empleados deben realizar un curso de capacitación obligatoria sobre ciberseguridad cada seis meses, con un enfoque específico en la identificación de intentos de phishing y la respuesta adecuada ante ellos.
- Filtrado de correo electrónico: El sistema de correo electrónico de la empresa debe estar configurado con filtros para bloquear correos electrónicos con contenido sospechoso, como enlaces o adjuntos maliciosos. Además, se debe aplicar una política de verificación de dominios en los correos electrónicos entrantes.
- Validación de enlaces y correos electrónicos: Los empleados deben verificar siempre la autenticidad de los enlaces en los correos electrónicos antes de hacer clic, utilizando herramientas de análisis de URLs y evitando acceder a enlaces desconocidos o sospechosos.

Los ataques de phishing son comunes en empresas que manejan información privada, y dado que los jugadores y empleados pueden ser blanco de intentos de phishing (por ejemplo, a través de correos electrónicos falsos relacionados con sus cuentas o juegos), es crucial implementar un sistema robusto de MFA y educar a los empleados y usuarios.

## Protección de Datos Sensibles