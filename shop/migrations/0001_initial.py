# Generated by Django 5.0.6 on 2024-07-11 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='images/')),
                ('discount', models.PositiveIntegerField(default=0)),
                ('rating', models.PositiveIntegerField()),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
    ]
