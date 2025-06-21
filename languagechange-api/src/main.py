from fastapi import FastAPI, HTTPException, Depends, Header
from pydantic import BaseModel
from googletrans import Translator
from src.utils import translate_text

app = FastAPI()
translator = Translator()

API_KEY = "8d93f7a1b6e74f3bb92d4a6a47e29c6c10bfa2ee4ed0a9b09a3cf58e1f2c44c7"  # Set your API key here

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API Key")

class TranslationRequest(BaseModel):
    from_lang: str
    to_lang: str
    text: str

@app.post("/translate/")
async def translate(
    request: TranslationRequest,
     api_key: str = Depends(verify_api_key)
    ):
    try:
        translated_text = translate_text(request.from_lang, request.to_lang, request.text)
        return {"translated_text": translated_text}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Welcome to the Language Translation API. Use the /translate endpoint to translate text."}