import os
from django.core.asgi import get_asgi_application
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from Myapp.fast_api import app as fastapi_app  # Correct import for FastAPI app
import django
django.setup()
# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Connect_Care_Hub.settings')


# Get Django ASGI application
django_asgi_app = get_asgi_application()

# Create FastAPI app instance
app = FastAPI()

# Mount the FastAPI app onto specific paths
app.mount('/api', WSGIMiddleware(fastapi_app))  # Correct usage of FastAPI app instance
app.mount("/", fastapi_app)  # FastAPI app mounted at /fastapi
app.mount("/admin", WSGIMiddleware(django_asgi_app))