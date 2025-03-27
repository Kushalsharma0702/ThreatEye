from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import uuid

app = FastAPI(title="ThreatEye - Cybersecurity Scanner")

# Simulated database for users
users_db = {}

# Simulated scan results
scan_results = {}

# User model for registration
class User(BaseModel):
    username: str
    password: str

# Scan result model
class ScanResult(BaseModel):
    username: str
    status: str
    vulnerabilities: list
    incident_history: list

@app.post("/auth/register")
async def register_user(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    users_db[user.username] = user.password
    return {"message": "User registered successfully", "username": user.username}

@app.post("/scan/start")
async def start_scan(username: str = Query(..., description="Username to scan system for vulnerabilities")):
    if username not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Simulated scan results
    vulnerabilities = ["CVE-2023-1234", "CVE-2024-5678"]
    incident_history = [
        {"CVE": "CVE-2023-1234", "impact": "Data breach", "loss": "$500K"},
        {"CVE": "CVE-2024-5678", "impact": "Ransomware attack", "loss": "$1M"}
    ]
    
    scan_results[username] = ScanResult(
        username=username,
        status="Scan completed",
        vulnerabilities=vulnerabilities,
        incident_history=incident_history
    ).dict()

    return scan_results[username]

@app.get("/scan/results")
async def get_scan_results(username: str = Query(..., description="Username to fetch scan results")):
    if username not in scan_results:
        raise HTTPException(status_code=404, detail="No scan results found for this user")
    
    return scan_results[username]
