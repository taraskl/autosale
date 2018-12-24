from django.db import models

# Create your models here.
class Autos(models.Model):
    mark = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    year = models.IntegerField()
    CATEGORIES = (
        ('<1990', 'До 1990 года выпуска'),
        ('1990-2000', 'От 1990 до 2000 года выпуска'),
        ('2000-2010', 'От 2000 до 2010 года выпуска'),
        ('>2010', 'После 2010 года выпуска'),
    )
    price = models.IntegerField()
    owner = models.CharField(max_length=128)
    category = models.CharField(max_length=128)


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
        super().save(*args, **kwargs)  # Call the "real" save() method.
   
    def __str__(self):
        return f"{self.mark} ({self.model})"
# def utomatically_insert_category():
#     last_auto = Autos.objects.all().order_by('id').last()
#     year = last_auto.year
#     print(year)
#     if year < 1990:
#         return last_auto.category = 'defore 1990'

#     # elif year >= 1990 and year < 2000:
#     #     return 'От 1990 до 2000 года выпуска'
#     # elif year >= 2000 and year < 2010:
#     #     return 'От 2000 до 2010 года выпуска'
#     # elif year >= 2010:
#     #     return 'После 2010 года выпуска'
#     else:
#         pass
            # return (
            #     ('<1990', 'До 1990 года выпуска'),
            #     ('1990-2000', 'От 1990 до 2000 года выпуска'),
            #     ('2000-2010', 'От 2000 до 2010 года выпуска'),
            #     ('>2010', 'После 2010 года выпуска'),
            #     )                    

        # if self.year < 1990:
        #     self.year = '<1990'
        # if self.year < 1990:
        #     self.year = '<1990'  





    # def __str__(self):
    #     return f"{self.mark} ({self.model})"