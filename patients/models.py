from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)

class Insurance(models.Model):
    patient = models.ForeignKey(
        Patient,related_name='insurances', on_delete=models.CASCADE
        )
    provider = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=100)
    expiration_date = models.DateField()

class MedicalRecord(models.Model):
    patient = models.ForeignKey(
        Patient, related_name='medical_records', on_delete=models.CASCADE
        )
    date = models.DateField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    follow_up_date = models.DateField()
    
