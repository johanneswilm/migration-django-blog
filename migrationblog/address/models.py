from django.db import models

class AddressBook(models.Model):
    name = models.CharField(max_length=200)
    telephone = models.CharField(max_length=25)
    postcode = models.CharField(max_length=25, default="00000")
