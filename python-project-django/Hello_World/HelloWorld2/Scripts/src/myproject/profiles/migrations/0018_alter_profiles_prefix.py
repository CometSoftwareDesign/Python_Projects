# Generated by Django 3.2.9 on 2021-11-06 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0017_alter_profiles_prefix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='Prefix',
            field=models.CharField(choices=[('Mr. ', 'Mr. '), ('Ms. ', 'Ms. '), ('Mrs. ', 'Mrs. ')], default='', max_length=60),
        ),
    ]