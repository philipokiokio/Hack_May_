# Generated by Django 3.2.3 on 2021-05-27 05:23

import autoslug.fields
from django.db import migrations
import shortuuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0004_alter_carddetail_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='carddetail',
            name='uuid',
            field=shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22),
        ),
        migrations.AlterField(
            model_name='carddetail',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='first_name', unique_with=('last_name',)),
        ),
    ]
