from django.shortcuts import render
from fastapi import FastAPI,Depends,HTTPException
from django.db import transaction
from Myapp.models import Appointment, Hospital
from pydantic import BaseModel
from datetime import date

# Create your views here.

app = FastAPI()
