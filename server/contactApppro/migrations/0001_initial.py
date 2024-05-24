# Generated by Django 5.0.6 on 2024-05-24 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=200, null=True, unique=True)),
                ('phonenumber', models.IntegerField(unique=True)),
                ('address', models.CharField(blank=True, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
            ],
        ),
    ]