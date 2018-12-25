from django.db import models

# Create your models here.
class Autos(models.Model):
    mark = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    year = models.IntegerField()
    price = models.IntegerField()
    owner = models.CharField(max_length=128)
    category = models.CharField(max_length=128, editable=False)

    def save(self, *args, **kwargs):
        if self.year < 1990:
            self.category = 'До 1990 года выпуска'
        elif self.year >= 1990 and self.year < 2000:
            self.category = 'От 1990 до 2000 года выпуска'
        elif self.year >= 2000 and self.year < 2010:
            self.category = 'От 2000 до 2010 года выпуска'
        elif self.year >= 2010:
            self.category = 'После 2010 года выпуска'
        else:
            pass
        super().save(*args, **kwargs)  
   
    def __str__(self):
        return f"{self.mark}  {self.model} ({self.year})"
