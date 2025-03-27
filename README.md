# ThreatEye

ThreatEye is a cybersecurity tool that scans a system for vulnerabilities, provides historical incident data related to those vulnerabilities, and assists users in mitigating security threats. It also integrates with the Shodan API to cross-check findings with publicly available security data.

## Features
- Scan a system for known vulnerabilities
- Retrieve historical incidents linked to detected vulnerabilities
- Provide potential impact and financial loss details from past security incidents
- Integrate with the Shodan API for real-world vulnerability verification
- Expose a REST API with FastAPI for easy integration

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.10+
- pip (Python package manager)
- Virtual environment (optional but recommended)

### Clone the Repository
```bash
git clone https://github.com/kushalsharma0702/ThreatEye.git
cd ThreatEye/Backend
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Configuration
### Set Up Environment Variables
Create a `.env` file in the `Backend` directory and add the following:
```env
SHODAN_API_KEY=your_shodan_api_key
```

## Running the Application
### Start the Backend Server
Run the FastAPI server using Uvicorn:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Once started, visit Swagger UI for API documentation:
- Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.

## API Endpoints
### 1. User Registration
**Endpoint:** `/auth/register`
- **Method:** `POST`
- **Payload:**
  ```json
  {
    "username": "testuser",
    "password": "testpass"
  }
  ```
- **Response:**
  ```json
  {
    "message": "User registered successfully"
  }
  ```

### 2. Start System Scan
**Endpoint:** `/scan/start?username={username}`
- **Method:** `POST`
- **Response:**
  ```json
  {
    "username": "kush",
    "status": "Scan completed",
    "vulnerabilities": [
      "CVE-2023-1234",
      "CVE-2024-5678"
    ],
    "incident_history": [
      {
        "CVE": "CVE-2023-1234",
        "impact": "Data breach",
        "loss": "$500K"
      },
      {
        "CVE": "CVE-2024-5678",
        "impact": "Ransomware attack",
        "loss": "$1M"
      }
    ]
  }
  ```

### 3. Verify Vulnerabilities with Shodan
**Script:** `shodan_checker.py`
- **Usage:**
  ```bash
  python shodan_checker.py <PUBLIC_IP>
  ```
- **Example Output:**
  ```bash
  [+] Searching Shodan for 8.8.8.8...
  --- Device Information ---
  IP: 8.8.8.8
  Organization: Google LLC
  Operating System: None
  --- Open Ports ---
  Port: 443
  Port: 53
  --- Vulnerabilities (CVEs) ---
  ```

## Troubleshooting
### API Not Working?
- Ensure your FastAPI server is running (`uvicorn main:app --host 0.0.0.0 --port 8000 --reload`).
- Check Swagger UI at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
- If Shodan script fails:
  - Ensure `SHODAN_API_KEY` is correctly set.
  - Test with a known public IP like `8.8.8.8`.

## License
MIT License

## Contact
For issues or contributions, open a GitHub issue or reach out at `sharmakushal7417@gmail.com`.

