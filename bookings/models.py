from django.db import models
from doctors.models import Doctor
from patients.models import Patient

class Appointment(models.Model):
    patient = models.ForeignKey(
        Patient, related_name='appointments', on_delete=models.CASCADE
        )
    doctor = models.ForeignKey(
        Doctor, related_name='appointments', on_delete=models.CASCADE
        )
    appointment_date = models.DateTimeField()
    appointment_time = models.TextField()
    notes = models.TextField()
    status = models.CharField(max_length=10)

class MedicalNote(models.Model):
    appointment = models.ForeignKey(
        Appointment, related_name='medical_notes', on_delete=models.CASCADE
        )
    note = models.TextField()
    date = models.DateTimeField()