import requests
import threading
import time

class HealthCheck:
    def __init__(self, backends, interval=10):
        self.backends = backends
        self.healthy_backends = set(self.backends)
        self.interval = interval
        threading.Thread(target=self.run_health_check, daemon=True).start()

    def run_health_check(self):
        """Periodically check backend health"""
        while True:
            for backend in self.backends:
                try:
                    response = requests.get(backend + "/health", timeout=3)
                    if response.status_code == 200:
                        self.healthy_backends.add(backend)
                    else:
                        self.healthy_backends.discard(backend)
                except requests.RequestException:
                    self.healthy_backends.discard(backend)
            time.sleep(self.interval)

    def get_healthy_backends(self):
        return list(self.healthy_backends)
