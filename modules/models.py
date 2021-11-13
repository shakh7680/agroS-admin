from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.base import Model
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

class Fertilizer(models.Model):
    name_of_fertilizer = models.CharField(max_length=20)
    used_for_what = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=10,decimal_places=3)
    how_much_available = models.DecimalField(max_digits=10,decimal_places=3)
    def __str__(self):
        return self.name_of_fertilizer

class DeliveryOfGoods(models.Model):
    name_of_good = models.CharField(max_length=50)
    how_amount = models.DecimalField(max_digits=10,decimal_places=3)
    where_to_deliver = models.CharField(max_length=50)
    status = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)]) 
    deadline_to_delivery = models.DateTimeField()

class LocalGlobalMarket(models.Model):
    name_of_good = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=10,decimal_places=3)
    how_much_available = models.DecimalField(max_digits=10,decimal_places=3)
    local_global = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)
    def __str__(self):
        return self.name_of_good

# Machine Renting
class MachineOwners(models.Model):
    FullName = models.CharField(max_length=100)
    TypeOfMachine = models.CharField(max_length=50)
    Cost_Machine_day = models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.TypeOfMachine

class Machines(models.Model):
    TypeOfMachine = models.CharField(max_length=50)
    status = models.CharField(max_length=30)
    who_rent = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.TypeOfMachine

