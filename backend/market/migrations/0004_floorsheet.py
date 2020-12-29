# Generated by Django 3.1.4 on 2020-12-29 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_companylist'),
    ]

    operations = [
        migrations.CreateModel(
            name='FloorSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractnum', models.IntegerField()),
                ('symbol', models.CharField(max_length=25)),
                ('buyerbroker', models.IntegerField()),
                ('sellerbroker', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('amount', models.FloatField()),
                ('date_saved', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]