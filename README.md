# Librería GraphQL

Este proyecto es un back-end para una librería que utiliza GraphQL para interactuar con la base de datos PostgreSQL.

## Tecnologías utilizadas

- Flask: Framework web para Python

- Flask-CORS: Permite solicitudes de origen cruzado

- Flask-SQLAlchemy: ORM para interactuar con la base de datos PostgreSQL

## Configuración

Para ejecutar el proyecto, sigue estos pasos:

1. Crea un entoro virtual (env).
    ```bash
    python -m venv env
    ```

2. Clona el repositorio de GitHub
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    ```

3. Activa el entorno virtual
- En Windows:
    ```bash
    .\env\Scripts\activate
    ```
- En macOS/Linux:
    ```bash
    source env/bin/activate
    ```

4. Instala los requisitos: 
    ```bash
    pip install -r requirements.txt
    ```

5. Configura las variables de entorno
- Crea un archivo .env en la raíz del proyecto con el siguiente contenido:
    ```bash
    DATABASE_URL=tu_url_de_conexion
    GOOGLE_CLIENT_ID=tu_google_client_id
    GOOGLE_CLIENT_SECRET=tu_google_client_secret
    MICROSOFT_CLIENT_ID=tu_microsoft_client_id
    MICROSOFT_CLIENT_SECRET=tu_microsoft_client_secret
    ```

6. Crea la base de datos PostgreSQL y el usuario con los permisos adecuados.

7. Ejecuta la aplicación: 
    ```bash
    python app.py
    ```

## Rutas

- `/graphql`: Punto de entrada para consultas GraphQL

## Contribuciones

¡Me encantaría recibir contribuciones! Aquí hay algunas pautas para ayudarte:

1. Crea una rama nueva para tus cambios.

2. Asegúrate de que tus cambios estén alineados con los objetivos del proyecto.

3. Proporciona una descripción clara y detallada de tus cambios en la solicitud de extracción.

4. Si es necesario, asegúrate de documentar adecuadamente tus cambios.

5. No dudes en comunicarte si necesitas orientación o tienes alguna pregunta.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.

