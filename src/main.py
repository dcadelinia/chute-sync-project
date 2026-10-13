from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.telemetry import generate_arena_telemetry

app = FastAPI(title="Chute Sync Telemetry System")
templates = Jinja2Templates(directory="templates")

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
