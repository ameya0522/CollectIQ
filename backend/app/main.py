
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine, check_database_connection
from app import models
from app.routers.customer import router as customer_router

# Create database tables for initial development
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CollectIQ API",
    description="Invoice and payment management platform",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(customer_router)


@app.get("/")
def home():
    return {"message": "Welcome to CollectIQ!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/health/db")
def database_health():
    try:
        result = check_database_connection()

        return {
            "status": "connected",
            "database": result[0],
            "user": result[1]
        }

    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Database connection failed"
        )
