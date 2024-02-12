
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

dir = "Images/"

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
        image = await file.read() 
        file_name = "new.jpg" 
        with open(f"{dir}{file_name}", "wb") as f:
             f.write(image) 

        return  

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)