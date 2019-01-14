from django.contrib import admin
from .models import DescriptionAbout
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)

    def has_add_permission(self, request):
        return not DescriptionAbout.objects.exists()


admin.site.register(DescriptionAbout, PostAdmin)
