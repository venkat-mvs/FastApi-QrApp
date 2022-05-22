# FastAPI - QrApp
Generating QrCode from a api call, using FastApi python

## Start API
### 1. Create & Activate vritual env
  ```bash
  > python -m venv .
  > source ./bin/activate
  ```
### 2. Install Require packages
  ```bash
  > python -m pip install -r requirments.py.txt
  ```
### 3. Run Module
  ```bash
  > cd API
  > python main.py
  ```
## Docker Setup
### 1. Create Docker Image
```bash
> docker build -t qrapi:latest .
```
### 2. Start Container
```bash
> docker run -p 80:8000 -e HOST=0.0.0.0 -e PORT=8000 -e API_TITLE=API -e API_VERSION=0.1.1 -d qrapi:latest
```
> Any suggestions/contributions is accepted. Create PRs for Contributions  
