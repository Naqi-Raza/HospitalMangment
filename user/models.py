from django.db import models

# Create your models here.

class Drsadia(models.Model):
    petient_name = models.CharField(max_length=100,default='Unknown')
    Adress = models.CharField(max_length=200, null=True, blank=True)
        # ✅ fixed here, not in terminal
    Cell_no = models.CharField(max_length=15, null=True, blank=True)
    Dr_name = models.CharField(max_length=100, default='Unknown')

    

    def __str__(self):
        return str(self.petient_name)
