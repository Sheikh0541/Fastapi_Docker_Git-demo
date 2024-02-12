
from fastapi import FastAPI 
from fastapi import UploadFile, File 
from model import model_prediction, read_image
import uvicorn

app = FastAPI()

# @app.get("/hello")
# def read_root():
#     return {"hello": "world"} 

# @app.get("/")
# def hello_user(name: str):
#     return f"Hello: {name}"

dir = "Images/"

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

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)