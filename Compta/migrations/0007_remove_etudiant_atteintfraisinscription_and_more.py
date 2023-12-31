# Generated by Django 4.2.4 on 2023-08-16 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compta', '0006_alter_frais_designation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etudiant',
            name='atteintFraisInscription',
        ),
        migrations.RemoveField(
            model_name='etudiant',
            name='atteintFraisReinscription',
        ),
        migrations.RemoveField(
            model_name='etudiant',
            name='atteintFraisSession',
        ),
        migrations.RemoveField(
            model_name='etudiant',
            name='atteintFraisTranche1',
        ),
        migrations.RemoveField(
            model_name='etudiant',
            name='atteintFraisTranche2',
        ),
        migrations.RemoveField(
            model_name='etudiant',
            name='atteintFraisTranche3',
        ),
        migrations.AddField(
            model_name='frais',
            name='atteintFraisInscription',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='frais',
            name='atteintFraisReinscription',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='frais',
            name='atteintFraisSession',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='frais',
            name='atteintFraisTranche1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='frais',
            name='atteintFraisTranche2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='frais',
            name='atteintFraisTranche3',
            field=models.BooleanField(default=False),
        ),
    ]
