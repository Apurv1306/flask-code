# service.py

from android.storage import primary_external_storage_path
from pathlib import Path
import threading, time
from core import FaceAppService

class FaceAppAndroidService:
    def __init__(self):
        # Create known_faces on external storage
        ext = primary_external_storage_path()
        self.known_faces_dir = Path(ext) / "FaceApp" / "known_faces"
        self.known_faces_dir.mkdir(parents=True, exist_ok=True)

        # Point backend at that directory
        self.service = FaceAppService(known_faces_dir=str(self.known_faces_dir))

    def start(self):
        # Run recognition loop in background
        threading.Thread(target=self.service.run_periodic_recognition, daemon=True).start()

def service_entry():
    FaceAppAndroidService().start()
