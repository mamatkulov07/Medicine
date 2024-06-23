from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='img/', null=True, blank=False)
    date_of_birth = models.SmallIntegerField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)


class Doctor(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    license_number = models.IntegerField()
    years_of_experience = models.SmallIntegerField()
    education = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)


class MedicalRecord(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    record_type = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)


class Appointment(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    reason = models.TextField()


class Medication(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dosage = models.TextField()


class FitnessProgram(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField


class Notification(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateField()


