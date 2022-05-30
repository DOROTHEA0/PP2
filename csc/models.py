from django.db import models


# Create your models here.
class CSCUser(models.Model):
    email = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    full_name = models.CharField(max_length=32)
    occupation = models.CharField(max_length=32)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'CSCUser'


class Animal(models.Model):
    class CatChoice(models.TextChoices):
        reptiles = 'Reptiles'
        flying_avian_animals = 'Flying Avian Animals'
        mammals = 'Mammals'
        insects = 'Insects'
        poultry = 'Poultry'
        fishes = 'Fishes'
        carnivores = 'Carnivores'
        other = 'Other'

    discoverer = models.ForeignKey('CSCUser', on_delete=models.CASCADE)
    animal_name = models.CharField(max_length=32)
    discover_data = models.DateField(auto_now=True)
    picture = models.ImageField(upload_to='img', default='img/default.jpg')
    catgories = models.CharField(max_length=32, choices=CatChoice.choices, default=CatChoice.other)

    def __str__(self):
        return self.animal_name

    class Meta:
        db_table = 'Animal'
