# Generated by Django 2.2.10 on 2020-03-20 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mercury", "0012_gfconfig"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gfconfig",
            name="gf_current",
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
