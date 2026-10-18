from fastapi import FastAPI
from src.controllers.user_controller import router as user_router


app = FastAPI(title="Gerstock API", version="1.0.0")


app.include_router(user_router)

# Tu ruta principal original
@app.get("/")
def home():
    return {"message": "gerstock-system"}