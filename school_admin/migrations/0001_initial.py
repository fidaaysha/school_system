# Generated by Django 4.1.6 on 2023-02-11 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Staffname', models.CharField(max_length=20)),
                ('Staff_email', models.CharField(max_length=20, unique=True)),
                ('Staff_dob', models.CharField(max_length=20)),
                ('Staff_mobile', models.BigIntegerField()),
                ('Staff_qualification', models.CharField(max_length=20)),
                ('Staff_address', models.CharField(max_length=50)),
                ('Staff_experience', models.CharField(max_length=20)),
                ('Staff_type', models.CharField(max_length=20)),
                ('Staff_gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject', models.CharField(max_length=20)),
                ('authorize', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='common.login')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_admin.addstaff')),
            ],
        ),
    ]
