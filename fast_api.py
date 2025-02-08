import os
import django
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from asgiref.sync import sync_to_async
from django.core.exceptions import ObjectDoesNotExist

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Connect_Care_Hub.settings")
django.setup()

from Myapp.models import Hospital, Doctor

app = FastAPI()

class HospitalModel(BaseModel):
    HospitalName: str
    Admin: str
    Address: str
    Pincode: str
    PhoneNumber: str
    AvailableDoctors: int
    Is_Active: bool = True

class DoctorModel(BaseModel):
    DoctorName: str
    Doc_PhoneNumber: str
    Specialization: str
    hospital_id: int 

