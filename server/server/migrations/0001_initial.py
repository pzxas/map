# Generated by Django 3.0.2 on 2020-01-29 11:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PCI',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('derication', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=200)),
                ('width', models.IntegerField(default=0)),
                ('length', models.IntegerField(default=0)),
                ('alligatorCrackSlightly', models.FloatField(default=0)),
                ('alligatorCrackIntermediate', models.FloatField(default=0)),
                ('alligatorCrackSerious', models.FloatField(default=0)),
                ('netShapedCrackSlightly', models.FloatField(default=0)),
                ('netShapedCrackSerious', models.FloatField(default=0)),
                ('longitudinalCrackSlightly', models.FloatField(default=0)),
                ('longitudinalCrackSerious', models.FloatField(default=0)),
                ('transverseCrackSlightly', models.FloatField(default=0)),
                ('transverseCrackSerious', models.FloatField(default=0)),
                ('pitSlotSlightly', models.FloatField(default=0)),
                ('pitSlotSerious', models.FloatField(default=0)),
                ('looseCrackSlightly', models.FloatField(default=0)),
                ('looseCrackSerious', models.FloatField(default=0)),
                ('subsidenceSlightly', models.FloatField(default=0)),
                ('subsidenceSerious', models.FloatField(default=0)),
                ('rutSlightly', models.FloatField(default=0)),
                ('rutSerious', models.FloatField(default=0)),
                ('wavePackSlightly', models.FloatField(default=0)),
                ('wavePackSerious', models.FloatField(default=0)),
                ('bleed', models.FloatField(default=0)),
                ('repair', models.FloatField(default=0)),
            ],
        ),
    ]
