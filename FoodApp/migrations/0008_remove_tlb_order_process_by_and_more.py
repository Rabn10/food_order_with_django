# Generated by Django 4.2.2 on 2023-09-30 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FoodApp', '0007_tbl_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tlb_order',
            name='process_by',
        ),
        migrations.AlterField(
            model_name='tbl_rating',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tlb_order',
            name='Customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]