# main.py
from kivy.app import App
from kivy.uix.widget import Widget
from jnius import autoclass

class RootWidget(Widget):
    pass

class FaceAppAPK(App):
    def build(self):
        return RootWidget()

    def on_start(self):
        # Start the Android service
        service = autoclass('org.kivy.android.PythonService').mService
        if not service:
            from service import service_entry
            service_entry()

if __name__ == '__main__':
    FaceAppAPK().run()
