# Generated by Django 5.0.6 on 2024-06-06 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=999)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='banner_images/%Y/%m/%d/')),
            ],
        ),
    ]
