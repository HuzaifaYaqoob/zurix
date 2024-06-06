from django.db import models

# Create your models here.


class BannerImage(models.Model):
    title = models.CharField(max_length=999, default='')
    description = models.TextField()
    image = models.ImageField(upload_to='banner_images/%Y/%m/%d/')

    is_special = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Brand(models.Model):
    name = models.CharField(max_length=999, default='')
    image = models.ImageField(upload_to='brand_images/%Y/%m/%d/')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=999, default='')
    slug = models.CharField(max_length=999, default='')
    image = models.ImageField(upload_to='category_images/%Y/%m/%d/')

    @property
    def products(self):
        return Product.objects.filter(category=self)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='category_products')
    name = models.CharField(max_length=999, default='')
    price = models.FloatField(default=0)
    discount_price = models.FloatField(default=0)

    slug = models.CharField(max_length=999, default='')

    short_description = models.TextField()
    description = models.TextField()
    aditional_information = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def image(self):
        return ProductImage.objects.filter(product=self)[0].image
    
    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='product_images/%Y/%m/%d/')

    def __str__(self):
        return self.product.name


class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_sizes')
    name = models.CharField(default='', max_length=999)
    value = models.CharField(max_length=999, default='')

    def __str__(self):
        return self.name

class ProductColor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_colors')
    name = models.CharField(default='', max_length=999)
    value = models.CharField(max_length=999, default='')

    def __str__(self):
        return self.name