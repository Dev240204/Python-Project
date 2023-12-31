# Generated by Django 4.2.3 on 2023-09-29 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=200, null=True)),
                ('product_original_price', models.IntegerField(blank=True, null=True)),
                ('product_discounted_price', models.IntegerField(blank=True, null=True)),
                ('product_category', models.CharField(blank=True, choices=[('shoes', 'Shoes'), ('clothes', 'Clothes'), ('mobile', 'Mobile')], max_length=200, null=True)),
                ('product_image_link', models.ImageField(blank=True, max_length=1000, null=True, upload_to='')),
                ('product_checkout_link', models.CharField(blank=True, max_length=1000, null=True)),
                ('product_description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
