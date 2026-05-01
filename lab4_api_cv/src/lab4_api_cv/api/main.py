from fastapi import FastAPI, UploadFile, File
import shutil
import os
from lab4_api_cv.services.image_service import analizar_imagen

app = FastAPI()

# Crear carpeta data si no existe
os.makedirs("data", exist_ok=True)

@app.post("/analyze-image")
def analyze_image(file: UploadFile = File(...)):
    path = f"data/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resultado = analizar_imagen(path)

    return {
        "mensaje": "Procesamiento exitoso",
        "resultado": resultado
    }