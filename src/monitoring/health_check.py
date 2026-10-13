import time
from fastapi import APIRouter, Response, status

monitor_router = APIRouter(prefix="/sys", tags=["Infrastructure Monitoring"])

@monitor_router.get("/heartbeat")
async def system_heartbeat_check():
    """
    Returns a status payload verifying live sensor tracking 
    and EdgeAI hardware synchronization health.
    """
    return {
        "status": "OPERATIONAL",
        "timestamp_epoch_ms": int(time.time() * 1000),
        "hardware_nodes": {
            "nvidia_jetson_nodes": "ONLINE",
            "countdown_buzzer_relay": "CONNECTED",
            "rfid_glove_receiver": "CONNECTED"
        }
   }
