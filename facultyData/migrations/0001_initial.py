# Generated by Django 5.0.6 on 2024-09-15 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=10)),
                ('fDept', models.CharField(max_length=10)),
                ('fSal', models.IntegerField()),
            ],
        ),
    ]
