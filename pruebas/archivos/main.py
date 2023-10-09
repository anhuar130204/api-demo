import os
import shutil
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Monta el directorio de imágenes estáticas
app.mount("/static/imagenes", StaticFiles(directory="static/imagenes"), name="static_imagenes")

def get_upload_dir(file_extension: str):
    if file_extension.lower() in (".jpg", ".jpeg", ".png", ".gif"):
        return "static/imagenes"
    elif file_extension.lower() == ".pdf":
        return "static/pdf"
    else:
        return "static"

@app.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):
    uploaded_filenames = []

    for file in files:
        # Genera la ruta de destino dentro del directorio correspondiente
        file_extension = os.path.splitext(file.filename)[1]
        upload_dir = get_upload_dir(file_extension)

        # Crea el directorio si no existe
        os.makedirs(upload_dir, exist_ok=True)

        # Genera la ruta de destino dentro del directorio correspondiente
        destination_path = os.path.join(upload_dir, file.filename)

        # Abre el archivo en modo binario y lo copia al destino
        with open(destination_path, "wb") as dest_file:
            shutil.copyfileobj(file.file, dest_file)

        uploaded_filenames.append(file.filename)

    return {"uploaded_filenames": uploaded_filenames}

@app.get("/")
async def main():
    content = """
<body>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
