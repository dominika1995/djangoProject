from django.contrib import admin
from .models import PortfolioCatalog, Image, ShortDescription


class InlineImage(admin.TabularInline):
    model = Image


class CatalogAdmin(admin.ModelAdmin):
    inlines = [InlineImage]


class ShortDescriptionMethod(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not ShortDescription.objects.exists()


admin.site.register(PortfolioCatalog, CatalogAdmin)
admin.site.register(ShortDescription, ShortDescriptionMethod)
