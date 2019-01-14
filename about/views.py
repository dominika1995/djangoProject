from django.shortcuts import render
from .models import DescriptionAbout
from gallery.models import PortfolioCatalog, Image


def about_view(request):
    text = DescriptionAbout.objects.all()[0].text

    all_catalog = PortfolioCatalog.objects.all().order_by('-data')[:3]
    catalogs = []
    for catalog in all_catalog:
        image_source = Image.objects.filter(catalog__id=catalog.id)[:1].values()
        catalogs.append({
            'title': catalog.name,
            'image': image_source[0],
            'id': catalog.id
        })

    return render(request, "../templates/about.html",
                  {'text': text, 'gallery': catalogs})
