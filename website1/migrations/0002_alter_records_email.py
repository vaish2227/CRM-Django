# Generated by Django 5.0.6 on 2024-06-17 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='Records',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
