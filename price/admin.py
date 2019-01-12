from django.contrib import admin
from .models import PriceList, shortDescription

class allPriceList(admin.ModelAdmin):
    list_display = ('id', 'name_of_service', 'price', 'number_of_photos', 'visible')
    ordering = ('id',)

class shortDescriptionMethod(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not shortDescription.objects.exists()

admin.site.register(PriceList, allPriceList)
admin.site.register(shortDescription, shortDescriptionMethod)
