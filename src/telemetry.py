import time
import random
from pydantic import BaseModel

class TeamPerformance(BaseModel):
    team_id: str = "TEAM 04"
    sync_accuracy: float
    crew_efficiency: float
    time_to_release: float
    gate_lock_secure: bool
    horse_motion_active: bool
    rider_ready_standby: bool

def generate_arena_telemetry() -> TeamPerformance:
    """Simulates real-time EdgeAI stream from the 10-foot bucking chute box."""
    return TeamPerformance(
        team_id="TEAM 04",
        sync_accuracy=round(random.uniform(95.0, 99.9), 1),
        crew_efficiency=round(random.uniform(92.0, 98.5), 1),
        time_to_release=round(random.uniform(0.0, 1.5), 2),
        gate_lock_secure=True,
        horse_motion_active=True,
        rider_ready_standby=False
   )
