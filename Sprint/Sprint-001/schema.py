from pydantic import BaseModel

class SystemConfig(BaseModel):
    project_name: str = 'DroneAI'
