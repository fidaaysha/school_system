# Generated by Django 4.1.6 on 2023-02-12 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_admin', '0007_alter_salary_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='classdivision',
            name='teacher',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='school_admin.teachers'),
        ),
    ]
