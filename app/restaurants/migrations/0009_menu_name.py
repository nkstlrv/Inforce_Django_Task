# Generated by Django 4.2.3 on 2023-07-12 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0008_alter_menu_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='name',
            field=models.CharField(default='Unknown Menu', max_length=50),
        ),
    ]
