# Generated by Django 3.1.1 on 2020-09-30 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gessol', '0008_auto_20200930_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='cap',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='company',
            name='prov',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
