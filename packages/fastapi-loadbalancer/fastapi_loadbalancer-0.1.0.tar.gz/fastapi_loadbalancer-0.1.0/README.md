# 🚀 FastAPI Load Balancer

A lightweight **load balancer** for FastAPI applications that distributes traffic across multiple backend services.  
It provides **round-robin request distribution, automatic failover, caching, and rate limiting**.

## 🌟 Features
✅ **Round-robin Load Balancing** - Distributes requests evenly across backends.  
✅ **Health Checks** - Automatically detects and removes unhealthy backends.  
✅ **Auto-Retry & Failover** - If a backend is down, the request is retried on another backend.  
✅ **Rate Limiting** (Optional) - Prevent API abuse.  
✅ **Caching** (Optional) - Improve performance by caching responses.  

---

## 📦 Installation
Install via `pip`:
```sh
pip install fastapi-loadbalancer
```

---

## 🚀 **Usage**
### 1️⃣ **Run Backend Services**
You need at least two backend FastAPI servers running.  
Example: `backend1.py`
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/data")
def get_data():
    return {"backend": "Backend 1", "message": "Hello from Backend 1"}
```
Run it with:
```sh
uvicorn backend1:app --port 8001 --reload
```

Create another backend (`backend2.py`) with:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/data")
def get_data():
    return {"backend": "Backend 2", "message": "Hello from Backend 2"}
```
Run it with:
```sh
uvicorn backend2:app --port 8002 --reload
```

---

### 2️⃣ **Create the Load Balancer**
Now, create a `gateway.py` file that will act as the **load balancer**:
```python
from fastapi import FastAPI, Request
from fastapi_loadbalancer import LoadBalancer

app = FastAPI()

# List of backend servers
backend_servers = [
    "http://127.0.0.1:8001",
    "http://127.0.0.1:8002"
]

# Initialize Load Balancer
load_balancer = LoadBalancer(backend_servers)

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def handle_request(request: Request, path: str):
    return await load_balancer.proxy_request(request)
```

---

### 3️⃣ **Run the Load Balancer**
Now, start the **load balancer**:
```sh
uvicorn gateway:app --port 8000 --reload
```

---

### 4️⃣ **Test the Load Balancer**
Send a request to the load balancer:
```sh
curl http://127.0.0.1:8000/data
```
The response will alternate between:
```json
{"backend": "Backend 1", "message": "Hello from Backend 1"}
```
or
```json
{"backend": "Backend 2", "message": "Hello from Backend 2"}
```

---

## ⚙️ **Advanced Features**
### 🛠 **Health Check**
The package automatically removes **unhealthy backends** from the rotation.

### 🚀 **Rate Limiting** (Optional)
To prevent abuse, you can enable **rate limiting** in `loadbalancer.py`.

### ⚡ **Caching** (Optional)
If you enable **caching**, the load balancer will **store responses** to reduce backend load.

---

## 🎯 **Why Use This?**
- **Easily distribute requests** between multiple FastAPI backends.
- **Automatic failover** ensures high availability.
- **Lightweight & easy to integrate** with any FastAPI project.

---

## 📜 **License**
This project is licensed under the **MIT License**.

---

## 🤝 **Contributing**
1. Fork the repository.
2. Create a new branch (`feature-new`).
3. Commit changes and open a PR.

---

## 📬 **Need Help?**
For issues, please open a GitHub **Issue**.

---

## ⭐ **Star this project if you find it useful!** ⭐
