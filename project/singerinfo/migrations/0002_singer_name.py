# Generated by Django 5.0.6 on 2024-06-30 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singerinfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='singer',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
