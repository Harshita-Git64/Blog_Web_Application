# Generated by Django 4.0.2 on 2022-04-08 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_profile_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='author',
            field=models.CharField(max_length=14),
        ),
    ]
