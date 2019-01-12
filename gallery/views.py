from django.shortcuts import render
from .models import PortfolioCatalog, Image, ShortDescription


def all_gallery_view(request):
    all_catalog = PortfolioCatalog.objects.all()
    catalogs = []
    for catalog in all_catalog:
        image_source = Image.objects.filter(catalog__id=catalog.id)[:1].values()
        catalogs.append({
            'title': catalog.name,
            'image': image_source[0],
            'id': catalog.id
        })
    text = ShortDescription.objects.all()[0].text
    return render(request, "../templates/gallery.html", {'catalog': catalogs, 'text': text})


def detail_gallery_view(request, id):
    all_catalog = PortfolioCatalog.objects.filter(id=id)[:1]
    catalogs = []
    for catalog in all_catalog:
        image_source = Image.objects.filter(catalog__id=catalog.id).values()
        images = []
        for image in image_source:
            images.append(image['image'])
        catalogs.append({
            'title': catalog.name,
            'image': images,
            'id': catalog.id
        })
    return render(request, "../templates/galleryDetail.html", {'catalog': catalogs})
