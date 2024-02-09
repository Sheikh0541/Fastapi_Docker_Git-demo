
from fastapi import FastAPI 
from fastapi import UploadFile, File 
import uvicorn

app = FastAPI()

@app.get("/hello")
def read_root():
    return {"hello": "world"} 

@app.get("/")
def hello_user(name: str):
    return f"Hello: {name}"

@app.post("/predict")
def predict_image():
    return f"Predicted type =" 

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)