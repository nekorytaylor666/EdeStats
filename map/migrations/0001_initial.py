# Generated by Django 2.0.7 on 2018-11-13 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=200)),
                ('lat', models.FloatField(default=0)),
                ('lng', models.FloatField(default=0)),
                ('ent', models.FloatField(default=0)),
            ],
        ),
    ]