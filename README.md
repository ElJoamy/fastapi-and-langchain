# LangChain usando FastAPI

## Descripción
Este proyecto es una API implementada con FastAPI que utiliza el modelo GPT de OpenAI para dos funcionalidades principales:
1. Generar respuestas basadas en prompts textuales.
2. Crear mensajes personalizados para solicitudes de entrevistas en LinkedIn.

## Configuración

### Pre-requisitos
- Python 3.8 o superior
- Dependencias listadas en `requirements.txt`

### Instalación
Primero, clona el repositorio e instala las dependencias:
```bash
git clone [URL del repositorio]
cd [Nombre del directorio]
pip install -r requirements.txt
```

### Configuración del Entorno
Crea un archivo `.env` basado en `.env.example` y actualiza las variables de entorno:
```
API_NAME="LangChain usando FastAPIPRUEBA"
REVISION="debug"
GPT="gpt-3.5-turbo-1106"
LOG_LEVEL="CRITICAL"
API_URL="http://127.0.0.1:8000/"
API_KEY="[TU CLAVE DE API DE OPENAI]"
```

## Ejecución
Para iniciar el servidor, ejecuta:
```bash
uvicorn app:app --reload
```
El servidor estará disponible en `http://127.0.0.1:8000/`.

## Endpoints

### GET /status
Devuelve el estado actual del servicio, incluyendo la versión del modelo GPT, la versión de la API, y otros detalles de configuración.

**Respuesta:**
```json
{
  "message": "string",
  "status": "string",
  "api_name": "string",
  "revision": "string",
  "model_version": "string",
  "log_level": "string",
  "api_url": "string"
}
```

### POST /prompt
Recibe un prompt textual y devuelve una respuesta generada por el modelo GPT.

**Solicitud:**
```json
{
  "prompt": "string"
}
```

**Respuesta:**
```json
{
  "response": "string"
}
```

### POST /generate_message
Genera un mensaje personalizado para solicitar una entrevista en LinkedIn.

**Solicitud:**
```json
{
  "nombre": "string",
  "rol_actual": "string",
  "rol_a_postular": "string",
  "nombre_de_la_empresa": "string"
}
```

**Respuesta:**
```json
{
  "message": "string"
}
```

## Manejo de Errores
La API retorna un error 500 con un mensaje detallado en caso de fallo en la generación de respuestas.
