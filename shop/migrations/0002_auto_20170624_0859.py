# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-24 00:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopcart',
            name='mycoupon',
            field=models.ForeignKey(blank=None, default=None, on_delete=django.db.models.deletion.CASCADE, to='shop.MyCoupon', verbose_name='\u6211\u7684\u53ef\u7528\u4f18\u60e0\u5238'),
        ),
    ]
