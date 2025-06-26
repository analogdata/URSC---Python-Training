# Save this code as fastapi_app.py

from fastapi import FastAPI                # FastAPI is a high-performance web framework for building APIs
from pydantic import BaseModel             # Used to define and validate data models for input
from typing import Optional                # Lets us mark fields as optional (e.g., pressure can be None)

# Create a FastAPI application instance
app = FastAPI()

# ----------------------------------------------------------------------
# Define a data model (schema) for incoming POST requests using Pydantic
# This is how you tell FastAPI what kind of data to expect
# ----------------------------------------------------------------------
class SensorData(BaseModel):
    sensor_id: str                         # Required: Sensor ID (e.g., "TEMP_001")
    temperature: float                     # Required: Temperature reading
    pressure: Optional[float] = None       # Optional: Pressure value, can be left out

# ----------------------------------------------------------------------
# ROUTES / ENDPOINTS
# ----------------------------------------------------------------------

# Basic root endpoint to verify API is running
# Access: http://127.0.0.1:8000/
@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI!"}


# Health check or status endpoint
# Access: http://127.0.0.1:8000/status
@app.get("/status")
async def get_status():
    return {"system_status": "Operational", "uptime_hours": 125.5}


# Endpoint to fetch details of a sensor by its ID (path parameter)
# Access: http://127.0.0.1:8000/sensor/TEMP_001
@app.get("/sensor/{sensor_id}")
async def get_sensor_info(sensor_id: str):
    """
    Returns mock metadata for a sensor ID.
    If 'TEMP_001' is requested, it returns hardcoded sensor details.
    """
    if sensor_id == "TEMP_001":
        return {
            "sensor_id": sensor_id,
            "type": "Temperature",
            "location": "Engine Bay"
        }
    else:
        # Return a 404 status with a custom message
        return {"sensor_id": sensor_id, "message": "Sensor not found"}, 404


# Endpoint to accept new sensor data using a POST request
# Access: http://127.0.0.1:8000/new_sensor_reading/
@app.post("/new_sensor_reading/")
async def create_sensor_reading(data: SensorData):
    """
    Accepts and parses JSON data into a SensorData object automatically.
    FastAPI validates the data format and types.
    """
    # You could store this data into a database or log it
    print(f"Received new reading: ID={data.sensor_id}, Temp={data.temperature}, Pres={data.pressure}")

    return {
        "status": "Reading received successfully",
        "data_received": data
    }

# ----------------------------------------------------------------------
# This block is needed only if you're running this file directly with Python
# Normally, you run FastAPI using: `uvicorn fastapi_app:app --reload`
# ----------------------------------------------------------------------
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)