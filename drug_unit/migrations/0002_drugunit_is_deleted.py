# Generated by Django 2.0.6 on 2020-10-16 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drug_unit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drugunit',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
