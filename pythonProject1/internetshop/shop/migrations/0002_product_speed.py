# Generated by Django 5.0.6 on 2024-07-06 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='speed',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
