# Generated by Django 4.2.4 on 2023-08-14 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Compta', '0004_etudiant_atteintfraisinscription_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=155)),
                ('date_creation', models.DateField(auto_now_add=True)),
                ('date_modification', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='frais',
            name='annee',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Compta.annee'),
            preserve_default=False,
        ),
    ]
