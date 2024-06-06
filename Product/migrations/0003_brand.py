# Generated by Django 5.0.6 on 2024-06-06 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=999)),
                ('image', models.ImageField(upload_to='brand_images/%Y/%m/%d/')),
            ],
        ),
    ]
