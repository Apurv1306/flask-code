[app]
title = FaceApp
package.name = faceapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,json,kv
version = 0.1
requirements = python3,kivy,opencv-python,numpy,requests,pandas,fpdf,plyer,pyjnius,pygame,edge-tts
android.permissions = CAMERA,INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,FOREGROUND_SERVICE
android.api = 33
android.minapi = 21
# Declare the service
android.services = SERVICE:service.py
# Enable service on boot
android.service.boot = True
