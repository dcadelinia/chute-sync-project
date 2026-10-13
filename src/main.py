from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.telemetry import generate_arena_telemetry
from src.monitoring.health_check import monitor_router  # Integrated monitor router

app = FastAPI(title="Chute Sync Telemetry System")
templates = Jinja2Templates(directory="templates")

# Mount monitoring router paths
app.include_router(monitor_router)

@app.get("/", response_class=HTMLResponse)
async def live_dashboard(request: Request):
    telemetry_data = generate_arena_telemetry()
    return templates.TemplateResponse(
        "index.html", 
        {"request": request, "telemetry": telemetry_data}
    )

@app.get("/api/telemetry")
async def get_telemetry():
    return generate_arena_telemetry()
