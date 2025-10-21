from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=100, null=False)
    type = models.CharField(max_length=40, null=False)
    weigth = models.IntegerField(null=False)
    Heigth= models.IntegerField(null=False)
    
    def __str__(self):
        return self.name
    

    
    
    
    
    
    
    
    
    ##Trainer 
    #name:
    #age:
    #level: