# Generated by Django 3.0.8 on 2020-09-09 04:15

from django.db import migrations, models
import myapp1.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0003_auto_20200909_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='name',
            field=models.CharField(max_length=100, unique=True, validators=[myapp1.models.validate_name]),
        ),
    ]
