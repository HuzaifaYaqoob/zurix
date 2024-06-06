from django.shortcuts import render, redirect

from django.http import HttpResponse

from Product.models import Category, Product, BannerImage, Brand
# Create your views here.


def HomePage(request):
    context = {}

    context['categories'] = Category.objects.all()
    prods = Product.objects.all()
    context['products'] = prods
    context['recent_products'] = prods.order_by('-created_at')
    context['banners'] = BannerImage.objects.filter(is_special=False)
    context['special_banners'] = BannerImage.objects.filter(is_special=True)
    context['brands'] = Brand.objects.all()
    return render(request, 'index.html', context)


def ProductViewPage(request, slug):
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        return redirect('/')

    context = {
        'product' : product,
        'suggested_products' : Product.objects.filter(category=product.category)
    }
    return render(request, 'detail.html', context)