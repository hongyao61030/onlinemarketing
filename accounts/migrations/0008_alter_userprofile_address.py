# Generated by Django 4.1.6 on 2023-03-02 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_rename_longtitude_userprofile_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
