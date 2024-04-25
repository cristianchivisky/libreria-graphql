# Librería GraphQL

Este proyecto es un back-end para una librería que utiliza GraphQL para interactuar con la base de datos PostgreSQL.

## Tecnologías utilizadas

- Flask: Framework web para Python
- Flask-CORS: Permite solicitudes de origen cruzado
- Flask-SQLAlchemy: ORM para interactuar con la base de datos PostgreSQL

## Configuración

Para ejecutar el proyecto, sigue estos pasos:
1. Crea un entoro virtual (env).
2. Clona el repositorio de GitHub
3. Instala los requisitos: `pip install -r requirements.txt`
4. Crea la base de datos PostgreSQL y el usuario con los permisos adecuados.
5. Actualiza la cadena de conexión de la base de datos en `api_config/__init__.py` con la información de tu base de datos.
4. Ejecuta la aplicación: `python app.py`

## Rutas

- `/graphql`: Punto de entrada para consultas GraphQL

## Contribuciones

¡Nos encantaría recibir tus contribuciones! Aquí hay algunas pautas para ayudarte:

1. Crea una rama nueva para tus cambios.
2. Asegúrate de que tus cambios estén alineados con los objetivos del proyecto.
3. Proporciona una descripción clara y detallada de tus cambios en la solicitud de extracción.
4. Si es necesario, asegúrate de documentar adecuadamente tus cambios.
5. No dudes en comunicarte si necesitas orientación o tienes alguna pregunta.
