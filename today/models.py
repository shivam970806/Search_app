from django.db import models

# Create your models here.
 
class Emp(models.Model): 
    first_name = models.CharField(max_length=30,blank = False) 
    last_name = models.CharField(max_length=30,blank = False) 
    email = models.EmailField(blank = False) 
    designation = models.CharField(max_length=50,blank = False)
    def __str__(self):
        return self.first_name


class Benefit(models.Model): 
    Employee = models.ForeignKey(Emp,on_delete=models.CASCADE)
    benefit_type = models.CharField(max_length=100,blank = False) 
    benefit_ammount = models.CharField(max_length=20,blank = False) 
    
    def __str__(self): 
        return self.benefit_type 
 
