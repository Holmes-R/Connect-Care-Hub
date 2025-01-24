import os
from django.core.asgi import get_asgi_application
from fastapi.middleware.wsgi import WSGIMiddleware
from fast_api import app as fastapi_app

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django_asgi_app = get_asgi_application()

# Combine Django and FastAPI apps
from fastapi import FastAPI
app = FastAPI()
app.mount('/api', WSGIMiddleware(fastapi_app))
