from django.db import models

#makemigrations - create changes store in file
#migrate - apply the pending changes created by makemigrations
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=125)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    #iss function se db me contact object 1 ki jagaha direct user ka enter kiya hua naam aaega
    
        
    
       