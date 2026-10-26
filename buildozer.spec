[app]
title = ThreeInRow
package.name = threeinrow
package.domain = org.zaur

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3==3.11.9, hostpython3==3.11.9, kivy==2.3.0

orientation = portrait
fullscreen = 1

# --- Настройки Android ---
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# --- Настройки сборки ---
android.accept_sdk_license = True
android.debug_artifact = apk
