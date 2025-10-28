from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=100, null=False)
    type = models.CharField(max_length=40, null=False)
    weigth = models.IntegerField(null=False)
    Heigth= models.IntegerField(null=False)
    picture= models.ImageField(upload_to='pokemon_pictures/', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Trainer(models.Model):
        name_trainer = models.CharField(max_length=40, null=False)
        lastname = models.CharField(max_length=40, null=False)
        level = models.IntegerField(null=False)
        birthdate = models.DateField(null=False)
        
        def __str__(self):
            return self.name_trainer
    
        
    
    
    
    
    
    
    
    
    
    ##Trainer 
    #name:
    #age:
    #level: