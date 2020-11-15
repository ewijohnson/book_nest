from django.contrib import admin
from .models import MainEntry, Work, Series, Subject, AddedEntry, Book, Location, \
    Collection, Holding, Item


admin.site.register(MainEntry)
admin.site.register(Work)
admin.site.register(Series)
admin.site.register(Subject)
admin.site.register(AddedEntry)
admin.site.register(Book)
admin.site.register(Location)
admin.site.register(Collection)
admin.site.register(Holding)
admin.site.register(Item)
