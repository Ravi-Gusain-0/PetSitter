# Generated by Django 3.2.6 on 2022-02-27 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userManagement', '0003_doggydetails_sitterreq'),
    ]

    operations = [
        migrations.CreateModel(
            name='SitterDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('location', models.CharField(max_length=200)),
                ('intro', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='pics')),
                ('usermodel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userManagement.usermodel')),
            ],
        ),
        migrations.DeleteModel(
            name='SitterReq',
        ),
    ]
