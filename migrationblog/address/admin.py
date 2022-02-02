from django.contrib import admin

from . import models

class AddressBookAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.AddressBook, AddressBookAdmin)
