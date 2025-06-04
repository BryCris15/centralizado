# Usamos una imagen base liviana con Python
FROM python:3.10-slim

# Creamos y nos movemos a la carpeta de trabajo
WORKDIR /app

# Copiamos el contenido de la carpeta app al contenedor
COPY app/ /app

# Instalamos FastAPI y Uvicorn
RUN pip install fastapi uvicorn

# Exponemos el puerto que usará la app (3009)
EXPOSE 3009

# Comando para correr la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3009"]