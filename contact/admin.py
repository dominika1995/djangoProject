from django.contrib import admin
from .models import MyEmailAddress, ShortDescription


class Description(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not ShortDescription.objects.exists()


class EmailAddress(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not MyEmailAddress.objects.exists()


admin.site.register(MyEmailAddress, EmailAddress)
admin.site.register(ShortDescription, Description)
