from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.database.connection import engine


def test_database_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            value = result.scalar()

            print("Database connection successful!")
            print(f"Test query result: {value}")
        
    except SQLAlchemyError as error:
        print("Database connection failed!")
        print(f"Error: {error}")

    finally:
        engine.dispose()

if __name__=="__main__":
    test_database_connection()