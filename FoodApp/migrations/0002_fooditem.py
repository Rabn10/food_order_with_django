# Generated by Django 4.2.2 on 2023-06-18 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=40)),
                ('description', models.TextField(default='its juicy', max_length=100)),
                ('pimage', models.ImageField(default='', upload_to='restaurant/images')),
                ('price', models.IntegerField()),
                ('totalOrders', models.IntegerField(default=0)),
                ('rating', models.FloatField(default=0.0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FoodApp.category')),
            ],
        ),
    ]
