from fastapi import FastAPI
from .database import Base, engine
from .routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Secure API User Service",
    description="FastAPI backend with authentication and secure endpoints",
)

app.include_router(router)


@app.get("/")
def root():
    return {"message": "API is running"}
