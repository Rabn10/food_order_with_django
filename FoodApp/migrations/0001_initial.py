# Generated by Django 4.2.2 on 2023-06-18 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cname', models.TextField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
    ]