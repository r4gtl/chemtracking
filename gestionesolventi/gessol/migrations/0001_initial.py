# Generated by Django 3.1.1 on 2020-09-29 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnaSupp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('cap', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=100)),
                ('prov', models.CharField(max_length=10)),
                ('gg_valuta', models.IntegerField()),
                ('sds_path', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
