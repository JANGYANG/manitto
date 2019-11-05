# Generated by Django 2.2.7 on 2019-11-05 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apple',
            fields=[
                ('appleId', models.AutoField(db_column='loId', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='loName', max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('manittoId', models.ForeignKey(blank=True, db_column='id', db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='manitto.Apple')),
            ],
        ),
    ]
