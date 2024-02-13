from fastapi import FastAPI, UploadFile
from model import model_prediction, read_image

app = FastAPI()

dir = "Images/"


@app.get("/")
async def read_root():
    return {"message": "Hello, World from a Dockerized fastAPI APP!"}


@app.post("/predict")
def predict_image(image: UploadFile):
    object_image = image.file.read()
    image = read_image(object_image)

    # Making prediction result
    result = model_prediction(image)

    # File Saving
    file_name = "new.jpg"
    with open(f"{dir}{file_name}", "wb") as f:
        f.write(object_image)

    return f"This is a {result}"
