# Generated by Django 4.2.3 on 2023-10-01 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
