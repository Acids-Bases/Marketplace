# Generated by Django 3.2.4 on 2021-06-28 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circle', '0004_alter_person_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='sold',
            field=models.ManyToManyField(blank=True, related_name='sold', to='circle.Article'),
        ),
    ]
