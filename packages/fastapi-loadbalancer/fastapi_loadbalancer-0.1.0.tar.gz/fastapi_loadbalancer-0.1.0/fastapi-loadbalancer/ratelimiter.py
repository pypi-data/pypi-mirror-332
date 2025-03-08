import time

class RateLimiter:
    def __init__(self, limit=10, window=60):
        self.limit = limit
        self.window = window
        self.requests = {}

    def allow_request(self, client_ip):
        """Check if request is within rate limit"""
        now = time.time()
        if client_ip not in self.requests:
            self.requests[client_ip] = []
        
        self.requests[client_ip] = [t for t in self.requests[client_ip] if now - t < self.window]
        
        if len(self.requests[client_ip]) < self.limit:
            self.requests[client_ip].append(now)
            return True
        return False
