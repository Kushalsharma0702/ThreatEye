# ThreatEye

## Overview
ThreatEye is an automated cybersecurity tool designed to detect and analyze vulnerabilities in an organization's system. It collects real-time attack data, compares it with known vulnerabilities, and scans systems for potential security risks. The project aims to help businesses identify and mitigate threats before they lead to security breaches.

## Features
- **Real-Time Attack Data Collection**: Fetches data from APIs like CVE, MITRE ATT&CK, and Shodan.
- **Vulnerability Analysis**: Extracts key details and matches attacks with known CVEs.
- **System Scanning**: Uses tools like Nmap, OWASP Dependency-Check, and Nikto to analyze company systems.
- **Reporting & Alerts**: Generates reports in JSON, PDF, and CSV formats, with optional email/Slack alerts.
- **Web Dashboard (Optional)**: Provides an interactive UI using React and Tailwind CSS.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- PostgreSQL/MongoDB (or SQLite for small-scale testing)
- Required Python libraries (listed in `requirements.txt`)

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/Kushalsharma0702/ThreatEye.git
   cd threateye
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up the database:
   ```sh
   python setup_db.py
   ```
4. Run the system scanner:
   ```sh
   python scanner.py
   ```
5. (Optional) Start the web dashboard:
   ```sh
   cd frontend
   npm install
   npm start
   ```

## Usage
1. Run the attack data fetcher:
   ```sh
   python fetch_attack_data.py
   ```
2. Analyze the vulnerabilities:
   ```sh
   python analyze_vulnerabilities.py
   ```
3. Scan a system for potential threats:
   ```sh
   python system_scanner.py --target your-domain.com
   ```
4. Generate a security report:
   ```sh
   python generate_report.py --format pdf
   ```

## Technologies Used
- **Backend:** Python (Flask/Django)
- **Database:** PostgreSQL/MongoDB/SQLite
- **Security Tools:** Nmap, OWASP Dependency-Check, Nikto
- **Frontend (Optional):** React, Tailwind CSS
- **Reporting:** ReportLab (PDF), Pandas (CSV)

## Future Enhancements
- AI-driven threat prediction
- Integration with more security APIs
- Real-time monitoring dashboard

## Contributors
- **Kushal Sharma** (Project Lead)
- Open for contributions! Feel free to submit PRs or raise issues.

## License
This project is licensed under the MIT License. See `LICENSE` for details.
