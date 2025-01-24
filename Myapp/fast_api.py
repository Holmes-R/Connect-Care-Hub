import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from asgiref.sync import sync_to_async

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Connect_Care_Hub.settings")

import django
django.setup()

from Myapp.models import Hospital

app = FastAPI()

class HospitalModel(BaseModel):
    HospitalName: str
    Admin: str
    Address: str
    Pincode: str
    PhoneNumber: str
    AvailableDoctors: int

@app.post("/hospital")
async def create_hospital(hospital: HospitalModel):
    new_hospital = await sync_to_async(Hospital.objects.create)(
        HospitalName=hospital.HospitalName,
        Admin=hospital.Admin,
        Address=hospital.Address,
        Pincode=hospital.Pincode,
        PhoneNumber=hospital.PhoneNumber,
        AvailableDoctors=hospital.AvailableDoctors,
    )
    return {"message": f"Hospital {new_hospital.HospitalName} created successfully!"}

@app.get("/")
async def get_hospitals():
    hospitals = await sync_to_async(list)(Hospital.objects.all())
    hospital_list = [
        {
            "HospitalName": h.HospitalName,
            "Admin": h.Admin,
            "Address": h.Address,
            "Pincode": h.Pincode,
            "PhoneNumber": h.PhoneNumber,
            "AvailableDoctors": h.AvailableDoctors,
        }
        for h in hospitals
    ]
    return {"Hospital": hospital_list}