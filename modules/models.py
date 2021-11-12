from django.db import models

# Create your models here.
# Sponsorship
class Farmer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length= 100)
    phone_number = models.CharField(max_length=20)
    experience = models.IntegerField()
    business_type = models.CharField(max_length=1)
    activity_type = models.CharField(max_length=20)
    def __str__(self):
        return self.first_name

class Investor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length= 100)
    phone_number = models.CharField(max_length=20)
    def __str__(self):
        return self.first_name
        
class Service(models.Model):
    farmer_id = models.ManyToManyField(Farmer, related_name='service')
    service_type = models.CharField(max_length=50)
    serive_definition = models.TextField()
    def __str__(self):
        return self.farmer_id

class Contract(models.Model):
    farmer_id = models.ManyToManyField(Farmer, related_name='farmer')
    investor_id = models.ManyToManyField(Investor, related_name='investor')
    amount = models.IntegerField()
    def __str__(self):
        return self.amount

# Collabration
