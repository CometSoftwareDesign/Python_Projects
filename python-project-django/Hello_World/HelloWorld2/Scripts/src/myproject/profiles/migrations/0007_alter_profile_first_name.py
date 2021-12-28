# Generated by Django 3.2.9 on 2021-11-05 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_alter_profile_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='First_Name',
            field=models.CharField(blank=True, choices=[('Mr. ', 'Mr. '), ('Mrs. ', 'Mrs. '), ('Ms. ', 'Ms. ')], default='', max_length=60),
        ),
    ]