from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(
        max_length=150,
        null=False,
        blank=False
    )
    name_abbreviation = models.CharField(
        max_length=8,
        null=False,
        blank=False
    )
    class Meta:
        db_table = "country"
class State(models.Model):
    name = models.CharField(
        max_length=150,
        null=False,
        blank=False
    )
    country = models.ForeignKey(
        Country,
        null=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        db_table = "address_state"

class City(models.Model):
    name = models.CharField(
        max_length=150,
        null=False,
        blank=False
    )
    state = models.ForeignKey(
        State,
        null = True,
        on_delete=models.SET_NULL
    )

    class Meta:
        db_table = "city"