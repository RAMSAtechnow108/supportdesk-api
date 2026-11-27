from fastapi.testclient import TestClient
from sqlalchemy.exc import SQLAlchemyError
from app.main import app

from unittest.mock import MagicMock
from fastapi import HTTPException
from app.database.session import get_db


client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "successful"


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    
    
    
def test_database_health_success():
    db = MagicMock()

    def override_get_db():
        yield db
        
    app.dependency_overrides[get_db] = override_get_db
    try: 
        response = client.get("/health/database")
        assert response.status_code ==200
        assert response.json()["status"]=="healthy"
        assert response.json()["database"] == "connected"

        db.execute.assert_called_once()

        
    finally:
        app.dependency_overrides.clear()



def test_database_health_failure():
    db = MagicMock()

    db.execute.side_effect = SQLAlchemyError("database unavailable")

    def override_get_up():
        yield db
        
    app.dependency_overrides[get_db] = override_get_up
    
    try:
        
        response = client.get("/health/database")

        assert response.status_code == 503
        assert response.json()["detail"]["status"] == "unhealthy"
        assert response.json()["detail"]["database"] == "disconnected"

    finally:
        app.dependency_overrides.clear()
