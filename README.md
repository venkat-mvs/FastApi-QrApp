# FastAPI - QrApp
Generating QrCode from a api call, using FastApi python

## Start API
### 1. Create & Activate vritual env
  ```bash
  > python -m venv .venv
  > source .venv/bin/activate
  ```
### 2. Install Require packages
  ```bash
  > python -m pip install -r requirments.txt
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
> docker run -p 80:8000 --build-arg port=80 -d qrapi:latest
```
> Any suggestions/contributions is accepted. Create PRs for Contributions  
