# Generated by Django 3.2 on 2022-08-09 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20220804_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliation',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliations', to='course.course'),
        ),
    ]