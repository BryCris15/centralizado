# app/main.py

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import httpx  # Cliente para consumir APIs

app = FastAPI()
templates = Jinja2Templates(directory="./templates")

@app.get("/", response_class=HTMLResponse)
def formulario(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/matricular", response_class=HTMLResponse)
async def matricular(request: Request, nombre: str = Form(...), curso: str = Form(...)):
    # Guardar en archivo
    with open("matriculas.txt", "a") as f:
        f.write(f"{nombre} - {curso}\n")
    
    # Llamada a una API externa (chiste de Chuck Norris)
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get("https://api.chucknorris.io/jokes/random")
            dato_externo = r.json().get("value", "Sin dato")
    except Exception:
        dato_externo = "No se pudo obtener info externa"

    # Renderiza página de confirmación
    return templates.TemplateResponse("confirmacion.html", {
        "request": request,
        "mensaje": f"Matrícula registrada para {nombre} en {curso}",
        "extra": dato_externo
    })