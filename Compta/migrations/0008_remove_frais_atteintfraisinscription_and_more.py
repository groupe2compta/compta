# Generated by Django 4.2.4 on 2023-08-16 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Compta', '0007_remove_etudiant_atteintfraisinscription_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frais',
            name='atteintFraisInscription',
        ),
        migrations.RemoveField(
            model_name='frais',
            name='atteintFraisReinscription',
        ),
        migrations.RemoveField(
            model_name='frais',
            name='atteintFraisSession',
        ),
        migrations.RemoveField(
            model_name='frais',
            name='atteintFraisTranche1',
        ),
        migrations.RemoveField(
            model_name='frais',
            name='atteintFraisTranche2',
        ),
        migrations.RemoveField(
            model_name='frais',
            name='atteintFraisTranche3',
        ),
    ]
