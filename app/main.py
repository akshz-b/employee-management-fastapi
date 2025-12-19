from fastapi import FastAPI
from .database import engine
from .models import Base
from .routes.employees import router as employee_router


app = FastAPI(title="Employee Management API")
app.include_router(employee_router)


Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"status": "API running"}
