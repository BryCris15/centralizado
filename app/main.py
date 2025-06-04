# app/main.py

from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/matricular")
def matricular(nombre: str = Form(...), curso: str = Form(...)):
    # Guarda la matrícula en el archivo de texto
    with open("app/matriculas.txt", "a") as f:
        f.write(f"{nombre} - {curso}\n")
    
    # Devuelve un mensaje de confirmación
    return JSONResponse(content={"mensaje": f"Matrícula registrada para {nombre} en {curso}"})