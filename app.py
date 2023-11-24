from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from config import get_settings
from langchain.chat_models import ChatOpenAI
from prompts import LINKEDIN_MESSAGE_PROMPT

SETTINGS = get_settings()

app = FastAPI(title=SETTINGS.api_name, version=SETTINGS.revision)

# Modelos Pydantic para los requests
class PromptRequest(BaseModel):
    prompt: str

class MessageRequest(BaseModel):
    nombre: str
    rol_actual: str
    rol_a_postular: str
    nombre_de_la_empresa: str

# Modelos Pydantic para las respuestas
class PromptResponse(BaseModel):
    response: str

class MessageResponse(BaseModel):
    message: str

class StatusResponse(BaseModel):
    message: str
    status: str
    api_name: str
    revision: str
    model_version: str
    log_level: str
    api_url: str

# Endpoint de status
@app.get("/status", response_model=StatusResponse, 
         description="Devuelve el estado actual del servicio, incluyendo la versión del modelo GPT, la versión de la API, y otros detalles de configuración.")
def get_status():
    settings = get_settings()
    return StatusResponse(
        message="Endpoint de status del servicio de LanchChain usando FastAPI",
        status="OK",
        api_name=settings.api_name,
        revision=settings.revision,
        model_version=settings.gpt,
        log_level=settings.log_level,
        api_url=settings.api_url
    )

# Endpoint para obtener respuesta a un prompt
@app.post("/prompt", response_model=PromptResponse, 
          description="Recibe un prompt textual y devuelve una respuesta generada por el modelo GPT. Útil para obtener respuestas generales basadas en el input proporcionado.")
def get_prompt_response(request: PromptRequest):
    try:
        llm = ChatOpenAI(model_name=SETTINGS.gpt, openai_api_key=SETTINGS.api_key)
        prediction = llm.predict(request.prompt)
        return PromptResponse(response=prediction)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint para generar un mensaje personalizado
@app.post("/generate_message", response_model=MessageResponse, 
          description="Genera un mensaje personalizado para solicitar una entrevista en LinkedIn. El usuario debe proporcionar su nombre, el rol actual, el rol a postular y el nombre de la empresa.")
def generate_message(request: MessageRequest):
    try:
        formatted_prompt = LINKEDIN_MESSAGE_PROMPT.format(
            nombre_de_la_empresa=request.nombre_de_la_empresa,
            nombre=request.nombre,
            rol_actual=request.rol_actual,
            rol_a_postular=request.rol_a_postular
        )
        llm = ChatOpenAI(model_name=SETTINGS.gpt, openai_api_key=SETTINGS.api_key)
        gpt_response = llm.predict(formatted_prompt)
        return MessageResponse(message=gpt_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", reload=True)
