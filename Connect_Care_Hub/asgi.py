import os
import django
from django.core.asgi import get_asgi_application
from fastapi import FastAPI
from starlette.middleware.wsgi import WSGIMiddleware
from fast_api import app as fastapi_app  # Import FastAPI app

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Connect_Care_Hub.settings")
django_app = get_asgi_application()

