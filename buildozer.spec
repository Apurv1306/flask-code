# buildozer.spec

[app]
# (str) Title of your application
title = FaceApp

# (str) Package name
package.name = faceapp

# (str) Package domain (reverse DNS)
package.domain = org.example

# (str) Source code where the main.py is located
source.dir = .

# (list) List of inclusions using pattern matching
source.include_exts = py,kv,png,jpg,json

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# Use the P4A “recipes” names: kivy, opencv, requests, pyjnius, plyer
requirements = python3,kivy,opencv,requests,pyjnius,plyer

# (str) Kivy entrypoint file
entrypoint = main.py

# (str) Icon of the application
icon.filename = %(source.dir)s/icon.png

# (list) Permissions
android.permissions = CAMERA,INTERNET,FOREGROUND_SERVICE

# (list) Declare an Android service
android.services = SERVICE:service.py

# (bool) Start the service on device boot
android.service.boot = True

# (int) Minimum Android API to support
android.minapi = 21

# (int) Android API level to compile against
android.api = 33

# (int) Target Android SDK
android.sdk = 33

# (str) Java source compatibility
android.java_source = 1.8

# (bool) Copy library instead of symlink (required on some platforms)
android.copy_libs = True

# (str) Android NDK version if needed (optional)
# android.ndk = 23b

# (bool) Enable logcat output when running buildozer android debug
log_level = 2
