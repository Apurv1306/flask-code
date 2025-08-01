# service.py
from jnius import autoclass
from plyer import notification
from core import FaceAppService

class FaceAppAndroidService:
    def __init__(self):
        self.service = FaceAppService()

    def start(self):
        # Run in background thread
        threading.Thread(target=self.service.run_periodic_recognition, daemon=True).start()

# Entry point for Buildozer
def service_entry():
    FaceAppAndroidService().start()
