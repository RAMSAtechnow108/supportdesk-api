from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.config.settings import settings
from app.database.session import get_db


app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.app_version,
    debug=settings.debug
)

@app.get("/")
def home():
    return {
        "status":"successful",
        "status_code": 200,
        "message":"Welcome Back!"
    }

@app.get("/health")
def health_check():
    return {
        "status":"healthy",
        "message": "SupportDesk API is running"
    }
    

@app.get("/health/database")
def database_health_check(db: Session = Depends(get_db)):

    try:
        db.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected",
            "message": "Database connection is working"
        }

    except SQLAlchemyError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={
                "status": "unhealthy",
                "database": "disconnected",
                "message": "Database connection failed"
            }
        )