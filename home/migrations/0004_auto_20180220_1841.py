# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-20 18:41
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20180220_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='cards',
            field=wagtail.wagtailcore.fields.StreamField((('cardblock', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('heading', wagtail.wagtailcore.blocks.CharBlock()), ('caption', wagtail.wagtailcore.blocks.RichTextBlock()), ('external_url', wagtail.wagtailcore.blocks.URLBlock())))), ('tileblock', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('heading', wagtail.wagtailcore.blocks.CharBlock()), ('caption', wagtail.wagtailcore.blocks.RichTextBlock()), ('external_url', wagtail.wagtailcore.blocks.URLBlock()))))), null=True),
        ),
    ]
