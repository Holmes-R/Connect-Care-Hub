import os
import django

# ✅ Set Django settings module before calling django.setup()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Connect_Care_Hub.settings")

# ✅ Initialize Django
django.setup()
from typing import List, Optional
from datetime import date
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from asgiref.sync import sync_to_async
from django.core.exceptions import ObjectDoesNotExist  # ✅ Make sure this is imported

from Myapp.models import Hospital, Doctor  # ✅ Import Django models only after setup

app = FastAPI()


class BloodModel(BaseModel):
    id: int
    BloodType: str
    Qantity: int

    class Config:
        orm_mode = True  
class CylinderModel(BaseModel):
    id: int
    CylinderType: str
    Quantity: int

    class Config:
        orm_mode = True
class OrganModel(BaseModel):
    id: int
    DonatorName: str
    DonarBloodType: str
    Gender: str
    Status: str
    OrganAvailable: str

    class Config:
        orm_mode = True

class HospitalModel(BaseModel):
    id: int
    HospitalName: str
    Admin: str
    Address: str
    Pincode: str
    PhoneNumber: str
    AvailableDoctors: int
    Is_Active: bool
    blood_types: List[BloodModel] = []
    cylinders: List[CylinderModel] = []
    organs: List[OrganModel] = []

    class Config:
        orm_mode = True

class DoctorModel(BaseModel):
    id: int
    DoctorName: str
    Doc_PhoneNumber: str
    Specialization: str
    hospital_id: int  
    class Config:
        orm_mode = True

class AvailabilityModel(BaseModel):
    id: int
    Ambulance_count: Optional[int]
    hospital_id: int 

    class Config:
        orm_mode = True

class AppointmentModel(BaseModel):
    id: int
    PatientName: str
    Age: str
    Description: str
    HospitalName: int 
    date: date

    class Config:
        orm_mode = True

@app.post("/hospitals/", response_model=HospitalModel)
async def create_hospital(hospital: HospitalModel):
    def create_hospital_sync():
        return Hospital.objects.create(
             HospitalName=hospital.HospitalName,
            Admin=hospital.Admin,
            Address=hospital.Address,
            Pincode=hospital.Pincode,
            PhoneNumber=hospital.PhoneNumber,
            AvailableDoctors=hospital.AvailableDoctors,
            Is_Active=hospital.Is_Active
        )
    new_hospital = await sync_to_async(create_hospital_sync)()
    return HospitalModel.from_orm(new_hospital)

@app.get("/hospital/{hospital_id}", response_model=HospitalModel)
async def get_hospital(hospital_id: int):
    try:
        def get_hospital_sync():
            return Hospital.objects.get(id=hospital_id)

        hospital = await sync_to_async(get_hospital_sync)()
        return hospital
    except ObjectDoesNotExist:
        raise HTTPException(status_code=404, detail="Hospital not found")
