# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-16 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StockPicture",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("photo", models.ImageField(upload_to="stock_pictures/")),
                (
                    "photo_credit",
                    models.CharField(
                        help_text="Only use pictures with a <a href='https://creativecommons.org/licenses/'>Creative Commons license</a>.",
                        max_length=200,
                    ),
                ),
                ("photo_link", models.URLField(verbose_name="photo URL")),
                (
                    "kind",
                    models.CharField(
                        choices=[("CO", "Event cover (356 x 210px)"), ("BA", "Section background")], max_length=2
                    ),
                ),
            ],
        ),
    ]
