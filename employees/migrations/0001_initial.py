# Generated by Django 5.1.3 on 2024-12-04 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.CharField(max_length=10)),
                ('designation', models.CharField(choices=[('HR', 'HR'), ('Manager', 'Manager'), ('Sales', 'Sales')], max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('course', models.CharField(choices=[('MCA', 'MCA'), ('BCA', 'BCA'), ('BSC', 'BSC')], max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
