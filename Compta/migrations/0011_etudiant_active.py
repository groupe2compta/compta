# Generated by Django 4.2.4 on 2023-08-18 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compta', '0010_alter_frais_designation'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
