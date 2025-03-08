import random
import requests
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .healthcheck import HealthCheck
from .ratelimiter import RateLimiter
from .cache import ResponseCache

class LoadBalancer:
    def __init__(self, backend_urls, cache_enabled=True, rate_limit=10):
        self.backends = backend_urls
        self.current_backend = 0
        self.health_checker = HealthCheck(self.backends)
        self.cache = ResponseCache() if cache_enabled else None
        self.rate_limiter = RateLimiter(rate_limit)

    def get_next_backend(self):
        """Round-robin selection of the next backend"""
        self.current_backend = (self.current_backend + 1) % len(self.backends)
        return self.backends[self.current_backend]

    async def proxy_request(self, request: Request):
        """Forward the request to the backend"""
        if not self.health_checker.get_healthy_backends():
            return JSONResponse(content={"error": "No healthy backends available"}, status_code=503)

        if not self.rate_limiter.allow_request(request.client.host):
            return JSONResponse(content={"error": "Too many requests"}, status_code=429)

        backend_url = self.get_next_backend()

        if self.cache:
            cached_response = self.cache.get(backend_url + request.url.path)
            if cached_response:
                return JSONResponse(content=cached_response, status_code=200)

        try:
            response = requests.request(
                method=request.method,
                url=backend_url + request.url.path,
                headers=dict(request.headers),
                data=await request.body()
            )

            if self.cache:
                self.cache.set(backend_url + request.url.path, response.json())

            return JSONResponse(content=response.json(), status_code=response.status_code)
        except Exception as e:
            return JSONResponse(content={"error": str(e)}, status_code=500)
