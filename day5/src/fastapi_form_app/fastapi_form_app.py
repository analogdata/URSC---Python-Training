# Save this code as fastapi_form_app.py

from fastapi import FastAPI, Request, Form                   # Import FastAPI core and tools for form handling
from fastapi.responses import HTMLResponse                   # Used to indicate HTML output
from fastapi.templating import Jinja2Templates               # For rendering Jinja2 HTML templates
from typing import Optional                                  # To mark pressure as optional

# Create the FastAPI app instance
app = FastAPI()

# Tell FastAPI where to find your HTML templates (create a folder named 'templates')
templates = Jinja2Templates(directory="templates")

# ============================
# ROUTE 1: Display HTML form
# ============================
# Access this route at: http://127.0.0.1:8001/sensor_form
@app.get("/", response_class=HTMLResponse)
async def get_sensor_form(request: Request, result: Optional[str] = None):
    """
    Display the sensor input form. The `result` (if any) is passed to the template to show a message after form submission.
    """
    return templates.TemplateResponse("sensor_form.html", {
        "request": request,
        "result": result
    })

# ============================
# ROUTE 2: Process submitted form
# ============================
# This route is hit when the user clicks "Submit" on the form
@app.post("/process_form", response_class=HTMLResponse)
async def post_sensor_form(
    request: Request,                                 # Required to re-render the form with result
    sensor_id: str = Form(...),                       # Required text input from form
    temperature: float = Form(...),                   # Required number input, auto-converted to float
    pressure: Optional[float] = Form(None)            # Optional number input, will be None if left blank
):
    # Process received data
    processed_message = (
        f"Sensor ID: {sensor_id}, Temp: {temperature}°C, "
        f"Pressure: {pressure if pressure is not None else 'N/A'} kPa"
    )

    # Print for server logs
    print("✅ Received:", processed_message)

    # Re-render the form page with result
    return templates.TemplateResponse("sensor_form.html", {
        "request": request,
        "result": processed_message
    })

# ============================
# HOW TO RUN THIS APP:
# ============================
# Run the server with:
#   uvicorn fastapi_form_app:app --reload --port 8001
#
# Make sure your folder has this structure:
#   fastapi_form_app.py
#   templates/
#     └── sensor_form.html
#
# The HTML file content is provided below.