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
class Seminar(models.Model):
    name_of_seminar = models.CharField(max_length=50)
    tutor = models.CharField(max_length= 100)
    cost = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name_of_seminar

class Event(models.Model):
    name_of_event = models.CharField(max_length=50)
    tutor = models.CharField(max_length=50)
    cost = models.IntegerField()
    date = models.DateTimeField()
    deadline = models.DateTimeField() 
    def __str__(self):
        return self.name_of_event

class New(models.Model):
    name_of_news = models.CharField(max_length=50)
    definition = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name_of_news

class Tips(models.Model):
    name_of_tip = models.CharField(max_length=50)
    author_of_tip = models.CharField(max_length=50)
    definition = models.TextField()
    def __str__(self):
        return self.name_of_tip

class Experts(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length= 100)
    phone_number = models.CharField(max_length=20)
    experience = models.IntegerField()
    activity_type = models.CharField(max_length=20)
    def __str__(self):
        return self.first_name