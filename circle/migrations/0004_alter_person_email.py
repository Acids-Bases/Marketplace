# Generated by Django 3.2.5 on 2021-07-05 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circle', '0003_alter_person_ph_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
