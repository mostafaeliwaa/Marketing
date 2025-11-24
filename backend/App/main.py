from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Insightify AI is running!"}

@app.post("/predict")
def predict(data: dict):
    
    return {"result": "This is a dummy prediction", "input": data}