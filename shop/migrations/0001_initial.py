# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-24 00:54
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Active',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u6d3b\u52a8\u540d\u79f0')),
                ('shoptype', models.CharField(choices=[('product', '\u4ea7\u54c1'), ('category', '\u5206\u7c7b'), ('tribe', '\u90e8\u843d'), ('rank', '\u7528\u6237\u7b49\u7ea7'), ('limit', '\u9650\u65f6\u62a2\u8d2d'), ('group', '\u56e2\u8d2d'), ('newer', '\u65b0\u4eba\u793c\u5305'), ('article', '\u6587\u7ae0'), ('speed', '\u52a0\u901f\u5ea6'), ('crowd', '\u4f17\u7b79'), ('coupon', '\u4f18\u60e0\u5238')], default='product', max_length=32, verbose_name='\u4ea4\u6613\u7c7b\u578b')),
                ('description', models.CharField(max_length=32, verbose_name='\u7b80\u4ecb')),
                ('starttime', models.DateTimeField(verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('endtime', models.DateTimeField(verbose_name='\u7ed3\u675f\u65f6\u95f4')),
                ('sale', models.BooleanField(default=False, verbose_name='\u4e0a\u67b6')),
                ('complete', models.IntegerField(verbose_name='\u5b8c\u6210\u6570')),
                ('count', models.IntegerField(verbose_name='\u603b\u6570')),
                ('meanwhile', models.BooleanField(default=False, verbose_name='\u662f\u5426\u53ef\u540c\u65f6\u53c2\u4e0e\u5176\u4ed6\u6d3b\u52a8')),
                ('appendtime', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u6d3b\u52a8',
            },
        ),
        migrations.CreateModel(
            name='ActiveRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u6d3b\u52a8\u8303\u56f4\u540d\u79f0')),
                ('rank', models.CharField(choices=[('PT', '\u666e\u901a\u7528\u6237'), ('HJ', '\u9ec4\u91d1\u7528\u6237'), ('BJ', '\u767d\u91d1\u7528\u6237'), ('ZS', '\u94bb\u77f3\u7528\u6237')], default='PT', max_length=32, verbose_name='\u7528\u6237\u7b49\u7ea7')),
                ('appendtime', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u6d3b\u52a8\u8303\u56f4',
                'verbose_name_plural': '\u6d3b\u52a8\u8303\u56f4',
            },
        ),
        migrations.CreateModel(
            name='Activeship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Activeuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isparticipation', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5df2\u53c2\u4e0e')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u6536\u8d27\u4eba')),
                ('mobile', models.CharField(max_length=32, verbose_name='\u624b\u673a\u53f7')),
                ('detail', models.CharField(max_length=32, verbose_name='\u8be6\u7ec6\u6536\u8d27\u5730\u5740')),
                ('isdefault', models.BooleanField(default=False, verbose_name='\u662f\u5426\u9ed8\u8ba4')),
                ('usable', models.BooleanField(default=True, verbose_name='\u662f\u5426\u53ef\u7528')),
                ('appendtime', models.DateField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u9001\u8d27\u5730\u5740',
                'verbose_name_plural': '\u9001\u8d27\u5730\u5740',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u5206\u7c7b')),
                ('sale', models.BooleanField(default=False, verbose_name='\u4e0a\u67b6')),
                ('appendtime', models.DateField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Category', verbose_name='\u7236\u5206\u7c7b')),
            ],
            options={
                'verbose_name': '\u4ea7\u54c1\u5206\u7c7b',
                'verbose_name_plural': '\u4ea7\u54c1\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u540d\u79f0')),
                ('price', models.CharField(max_length=32, verbose_name='\u4ef7\u683c')),
                ('thumb', models.ImageField(upload_to='products', verbose_name='\u7f29\u7565\u56fe')),
                ('url', models.CharField(max_length=32, verbose_name='\u94fe\u63a5')),
                ('orderby', models.IntegerField(verbose_name='\u6392\u5e8f')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u5e02\u540d')),
                ('code', models.CharField(blank=True, max_length=12, null=True, verbose_name='\u90ae\u653f\u7f16\u7801')),
            ],
            options={
                'verbose_name': '\u5e02',
                'verbose_name_plural': '\u5e02',
            },
        ),
        migrations.CreateModel(
            name='CoinItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change', models.IntegerField(verbose_name='\u6539\u53d8\u6570')),
                ('typename', models.CharField(choices=[('GWFH', '\u8d2d\u7269\u8fd4\u8fd8'), ('GWZC', '\u8d2d\u7269\u652f\u51fa'), ('TGSD', '\u63a8\u5e7f\u6240\u5f97')], max_length=32, verbose_name='\u83b7\u5f97\u65b9\u5f0f')),
                ('detail', models.CharField(max_length=32, verbose_name='\u83b7\u5f97\u8be6\u60c5')),
                ('changetime', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u679c\u5e01\u8be6\u7ec6',
                'verbose_name_plural': '\u679c\u5e01\u8be6\u7ec6',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appendtime', models.DateField(auto_now_add=True, verbose_name='\u6536\u85cf\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u6536\u85cf',
                'verbose_name_plural': '\u6536\u85cf',
            },
        ),
        migrations.CreateModel(
            name='Commet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=256, verbose_name='\u8bc4\u8bba\u5185\u5bb9')),
                ('recommend', models.BooleanField(default=False, verbose_name='\u662f\u5426\u63a8\u8350')),
                ('appendtime', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u4ea7\u54c1\u8bc4\u8bba',
                'verbose_name_plural': '\u4ea7\u54c1\u8bc4\u8bba',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u4e61')),
            ],
            options={
                'verbose_name': '\u4e61',
                'verbose_name_plural': '\u4e61',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='provice', chained_model_field='provice', null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.City')),
                ('country', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='region', chained_model_field='region', null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Country')),
            ],
            options={
                'verbose_name': '\u5730\u7406\u6570\u636e',
                'verbose_name_plural': '\u5730\u7406\u6570\u636e',
            },
        ),
        migrations.CreateModel(
            name='MyCoupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('useStatus', models.CharField(choices=[('KY', '\u53ef\u7528'), ('BKY', '\u4e0d\u53ef\u7528'), ('YSY', '\u5df2\u4f7f\u7528')], default='KY', max_length=4, verbose_name='\u53ef\u7528\u72b6\u6001')),
                ('appendtime', models.DateField(auto_now_add=True, verbose_name='\u83b7\u5f97\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u6211\u7684\u4f18\u60e0\u5238',
                'verbose_name_plural': '\u6211\u7684\u4f18\u60e0\u5238',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderNumber', models.CharField(max_length=128, verbose_name='\u8ba2\u5355\u7f16\u53f7')),
                ('receive_name', models.CharField(max_length=32, verbose_name='\u6536\u8d27\u4eba')),
                ('coin', models.IntegerField(default=0, verbose_name='\u4f7f\u7528\u679c\u5e01')),
                ('mobile', models.CharField(max_length=32, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('detail', models.CharField(max_length=32, verbose_name='\u8be6\u7ec6\u6536\u8d27\u5730\u5740')),
                ('totalMoney', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='\u8ba2\u5355\u91d1\u989d')),
                ('appendtime', models.DateField(auto_now_add=True)),
                ('orderStatusOption', models.CharField(choices=[('CANCEL', '\u53d6\u6d88'), ('WAITING', '\u7b49\u5f85\u652f\u4ed8'), ('PAYSUCCESS', '\u652f\u4ed8\u6210\u529f'), ('PACKAGE', '\u6b63\u5728\u51fa\u5e93'), ('INDELIVERY', '\u6b63\u5728\u914d\u9001'), ('COMPLETE', '\u8ba2\u5355\u5b8c\u6210')], max_length=32, verbose_name='\u8ba2\u5355\u72b6\u6001')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Location', verbose_name='\u5730\u7406\u4f4d\u7f6e')),
                ('mycoupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.MyCoupon', verbose_name='\u4f7f\u7528\u4f18\u60e0\u5238')),
            ],
            options={
                'verbose_name': '\u8ba2\u5355',
                'verbose_name_plural': '\u8ba2\u5355',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoptype', models.CharField(choices=[('product', '\u4ea7\u54c1'), ('category', '\u5206\u7c7b'), ('tribe', '\u90e8\u843d'), ('rank', '\u7528\u6237\u7b49\u7ea7'), ('limit', '\u9650\u65f6\u62a2\u8d2d'), ('group', '\u56e2\u8d2d'), ('newer', '\u65b0\u4eba\u793c\u5305'), ('article', '\u6587\u7ae0'), ('speed', '\u52a0\u901f\u5ea6'), ('crowd', '\u4f17\u7b79'), ('coupon', '\u4f18\u60e0\u5238')], default='product', max_length=32, verbose_name='\u4ea4\u6613\u7c7b\u578b')),
                ('shoptypeID', models.IntegerField(verbose_name='\u4ea4\u6613\u7c7b\u578b\u5355\u53f7')),
                ('product_name', models.CharField(max_length=32, verbose_name='\u4ea7\u54c1\u540d\u79f0')),
                ('optionName', models.CharField(max_length=32, verbose_name='')),
                ('thumb', models.ImageField(blank=True, upload_to='article', verbose_name='\u4ea7\u54c1\u7f29\u7565\u56fe')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='\u6210\u4ea4\u4ef7')),
                ('count', models.IntegerField(verbose_name='\u4ea4\u6613\u6570')),
                ('appendtime', models.DateField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Order')),
            ],
            options={
                'verbose_name': '\u8ba2\u5355\u8be6\u60c5',
                'verbose_name_plural': '\u8ba2\u5355\u8be6\u60c5',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='\u6807\u9898')),
                ('showTitle', models.BooleanField(default=False, verbose_name='\u663e\u793a\u6807\u9898')),
                ('type', models.CharField(choices=[('4', '\u5355\u884c\u56db\u5217'), ('2', '\u5355\u884c\u4e24\u5217'), ('1', '\u5355\u884c\u5355\u5217')], default='1', max_length=32)),
                ('orderby', models.IntegerField(verbose_name='\u6392\u5e8f')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u4ea7\u54c1\u540d\u79f0')),
                ('thumb', models.ImageField(upload_to='products', verbose_name='\u7f29\u7565\u56fe')),
                ('number', models.IntegerField(verbose_name='\u603b\u6570')),
                ('description', models.TextField(verbose_name='\u4ea7\u54c1\u63cf\u8ff0')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u4ea7\u54c1\u8be6\u60c5')),
                ('package', models.CharField(max_length=32, verbose_name='\u5305\u88c5')),
                ('service', models.CharField(max_length=32, verbose_name='\u552e\u540e')),
                ('coin', models.IntegerField(verbose_name='\u8fd4\u5e01')),
                ('recommend', models.BooleanField(default=False, verbose_name='\u63a8\u8350')),
                ('sale', models.BooleanField(default=False, verbose_name='\u4e0a\u67b6')),
                ('freight', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='\u8fd0\u8d39')),
                ('appendtime', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category', verbose_name='\u5206\u7c7b')),
            ],
            options={
                'verbose_name': '\u4ea7\u54c1',
                'verbose_name_plural': '\u4ea7\u54c1',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(blank=True, upload_to='product', verbose_name='\u4ea7\u54c1\u56fe\u50cf')),
                ('isdefault', models.BooleanField(default=False, verbose_name='\u9ed8\u8ba4')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product', verbose_name='\u4ea7\u54c1')),
            ],
        ),
        migrations.CreateModel(
            name='ProductOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='')),
                ('avator', models.ImageField(blank=True, upload_to='product/option', verbose_name='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='\u4ef7\u683c')),
                ('shoptype', models.CharField(choices=[('product', '\u4ea7\u54c1'), ('category', '\u5206\u7c7b'), ('tribe', '\u90e8\u843d'), ('rank', '\u7528\u6237\u7b49\u7ea7'), ('limit', '\u9650\u65f6\u62a2\u8d2d'), ('group', '\u56e2\u8d2d'), ('newer', '\u65b0\u4eba\u793c\u5305'), ('article', '\u6587\u7ae0'), ('speed', '\u52a0\u901f\u5ea6'), ('crowd', '\u4f17\u7b79'), ('coupon', '\u4f18\u60e0\u5238')], default='product', max_length=32, verbose_name='\u4ea4\u6613\u7c7b\u578b')),
                ('count', models.IntegerField(verbose_name='\u5e93\u5b58')),
                ('effective', models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548')),
                ('isdefault', models.BooleanField(default=False, verbose_name='\u9ed8\u8ba4')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product', verbose_name='\u4ea7\u54c1')),
            ],
            options={
                'verbose_name': '\u4ea7\u54c1\u79cd\u7c7b',
                'verbose_name_plural': '\u4ea7\u54c1\u79cd\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Promote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoptype', models.CharField(choices=[('product', '\u4ea7\u54c1'), ('category', '\u5206\u7c7b'), ('tribe', '\u90e8\u843d'), ('rank', '\u7528\u6237\u7b49\u7ea7'), ('limit', '\u9650\u65f6\u62a2\u8d2d'), ('group', '\u56e2\u8d2d'), ('newer', '\u65b0\u4eba\u793c\u5305'), ('article', '\u6587\u7ae0'), ('speed', '\u52a0\u901f\u5ea6'), ('crowd', '\u4f17\u7b79'), ('coupon', '\u4f18\u60e0\u5238')], default='product', max_length=32, verbose_name='\u4ea4\u6613\u7c7b\u578b')),
                ('promoteType', models.CharField(choices=[('POST', '\u6d77\u62a5'), ('FRIEND', '\u597d\u53cb'), ('CIRCLE', '\u670b\u53cb\u5708')], max_length=32, verbose_name='\u63a8\u5e7f\u7c7b\u578b')),
                ('appendtime', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u63a8\u5e7f',
                'verbose_name_plural': '\u63a8\u5e7f',
            },
        ),
        migrations.CreateModel(
            name='PromoteDeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealtime', models.DateField(auto_now_add=True)),
                ('promote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Promote')),
            ],
            options={
                'verbose_name': '\u63a8\u5e7f\u6210\u4ea4',
                'verbose_name_plural': '\u63a8\u5e7f\u6210\u4ea4',
            },
        ),
        migrations.CreateModel(
            name='Provice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u7701\u540d')),
            ],
            options={
                'verbose_name': '\u7701',
                'verbose_name_plural': '\u7701',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u533a\u540d')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.City')),
            ],
            options={
                'verbose_name': '\u533a',
                'verbose_name_plural': '\u533a',
            },
        ),
        migrations.CreateModel(
            name='ShopCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('useCoin', models.BooleanField(default=False, verbose_name='\u4f7f\u7528\u679c\u5e01')),
                ('mycoupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.MyCoupon', verbose_name='\u6211\u7684\u53ef\u7528\u4f18\u60e0\u5238')),
            ],
            options={
                'verbose_name': '\u8d2d\u7269\u8f66',
                'verbose_name_plural': '\u8d2d\u7269\u8f66',
            },
        ),
        migrations.CreateModel(
            name='ShopCartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoptype', models.CharField(choices=[('product', '\u4ea7\u54c1'), ('category', '\u5206\u7c7b'), ('tribe', '\u90e8\u843d'), ('rank', '\u7528\u6237\u7b49\u7ea7'), ('limit', '\u9650\u65f6\u62a2\u8d2d'), ('group', '\u56e2\u8d2d'), ('newer', '\u65b0\u4eba\u793c\u5305'), ('article', '\u6587\u7ae0'), ('speed', '\u52a0\u901f\u5ea6'), ('crowd', '\u4f17\u7b79'), ('coupon', '\u4f18\u60e0\u5238')], default='product', max_length=32, verbose_name='\u4ea4\u6613\u7c7b\u578b')),
                ('shoptypeID', models.IntegerField(verbose_name='\u8d2d\u7269\u7c7b\u578b\u7f16\u7801')),
                ('count', models.IntegerField(verbose_name='\u4ea7\u54c1\u6570')),
                ('check', models.BooleanField(default=True)),
                ('appendtime', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product', verbose_name='\u4ea7\u54c1')),
                ('productOption', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.ProductOption', verbose_name='\u4ea7\u54c1\u89c4\u683c')),
                ('shopcart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.ShopCart', verbose_name='\u8d2d\u7269\u8f66')),
            ],
            options={
                'verbose_name': '\u8d2d\u7269\u8f66\u9879',
                'verbose_name_plural': '\u8d2d\u7269\u8f66\u9879',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products', verbose_name='\u7f29\u7565\u56fe')),
                ('name', models.CharField(max_length=32, verbose_name='\u6807\u9898')),
                ('url', models.CharField(max_length=32, verbose_name='\u94fe\u63a5')),
                ('orderby', models.IntegerField(verbose_name='\u6392\u5e8f')),
            ],
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u540d\u79f0')),
                ('value', models.CharField(max_length=32, verbose_name='\u503c')),
                ('istitle', models.BooleanField(default=False, verbose_name='\u662f\u5426\u4f5c\u4e3a\u6807\u9898')),
                ('appendtime', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
            ],
            options={
                'verbose_name': '\u4ea7\u54c1\u89c4\u683c',
                'verbose_name_plural': '\u4ea7\u54c1\u89c4\u683c',
            },
        ),
        migrations.CreateModel(
            name='Tribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='\u5927\u9646', max_length=32, verbose_name='\u90e8\u843d\u540d\u79f0')),
                ('body', models.TextField(verbose_name='\u90e8\u843d\u8be6\u60c5')),
                ('tribeType', models.CharField(choices=[('PTBL', '\u666e\u901a\u90e8\u843d'), ('DLBL', '\u4f4d\u7f6e\u90e8\u843d')], default='PTBL', max_length=16, verbose_name='\u90e8\u843d\u7c7b\u578b')),
                ('appendtime', models.DateField(auto_now_add=True)),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Location')),
            ],
            options={
                'verbose_name': '\u90e8\u843d',
                'verbose_name_plural': '\u90e8\u843d',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u59d3\u540d')),
                ('openid', models.CharField(max_length=32, verbose_name='\u5fae\u4fe1\u516c\u4f17\u53f7OpenID')),
                ('avator_url', models.URLField(verbose_name='\u516c\u4f17\u53f7\u5934\u50cf\u5730\u5740')),
                ('rank', models.CharField(choices=[('PT', '\u666e\u901a\u7528\u6237'), ('HJ', '\u9ec4\u91d1\u7528\u6237'), ('BJ', '\u767d\u91d1\u7528\u6237'), ('ZS', '\u94bb\u77f3\u7528\u6237')], default='PT', max_length=32, verbose_name='\u7528\u6237\u7b49\u7ea7')),
                ('coinCount', models.IntegerField(default=0, verbose_name='\u679c\u5e01')),
                ('avator', models.ImageField(blank=True, null=True, upload_to='article', verbose_name='\u5934\u50cf')),
                ('mobile', models.CharField(max_length=32, null=True, verbose_name='\u624b\u673a\u53f7')),
                ('password', models.CharField(max_length=32, null=True, verbose_name='\u5bc6\u7801')),
                ('gender', models.CharField(choices=[('f', '\u5973\u751f'), ('m', '\u7537\u751f')], default='m', max_length=2, verbose_name='\u6027\u522b')),
                ('appendtime', models.DateField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.User')),
                ('tribes', models.ManyToManyField(blank=True, null=True, to='shop.Tribe', verbose_name='\u90e8\u843d')),
            ],
            options={
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
        ),
        migrations.CreateModel(
            name='UserRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u59d3\u540d')),
                ('thumb', models.ImageField(blank=True, upload_to='article', verbose_name='\u7b49\u7ea7\u6807\u5fd7')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u7b49\u7ea7',
                'verbose_name_plural': '\u7528\u6237\u7b49\u7ea7',
            },
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('active_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.Active')),
                ('couponOption', models.CharField(choices=[('YH', '\u6ee1\u51cf\u5238'), ('YF', '\u8fd0\u8d39\u5238'), ('DJQ', '\u4ee3\u91d1\u5238')], max_length=32, verbose_name='\u4f18\u60e0\u5238\u7c7b\u522b')),
                ('over', models.IntegerField(verbose_name='\u8d2d\u7269\u6ee1\u591a\u5c11')),
                ('reduce', models.IntegerField(verbose_name='\u51cf\u591a\u5c11')),
                ('mailReduce', models.IntegerField(verbose_name='\u51cf\u591a\u5c11\u90ae\u8d39')),
            ],
            options={
                'verbose_name': '\u8d2d\u7269\u5238',
                'verbose_name_plural': '\u8d2d\u7269\u5238',
            },
            bases=('shop.active',),
        ),
        migrations.CreateModel(
            name='Crowd',
            fields=[
                ('active_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.Active')),
                ('market_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='\u5e02\u573a\u4ef7')),
            ],
            options={
                'verbose_name': '\u4f17\u7b79',
                'verbose_name_plural': '\u4f17\u7b79',
            },
            bases=('shop.active',),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('active_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.Active')),
                ('market_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='\u5e02\u573a\u4ef7')),
            ],
            options={
                'verbose_name': '\u56e2\u8d2d\u6d3b\u52a8',
                'verbose_name_plural': '\u56e2\u8d2d\u6d3b\u52a8',
            },
            bases=('shop.active',),
        ),
        migrations.CreateModel(
            name='Limit',
            fields=[
                ('active_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.Active')),
                ('market_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='\u5e02\u573a\u4ef7')),
            ],
            options={
                'verbose_name': '\u9650\u65f6\u62a2\u8d2d',
                'verbose_name_plural': '\u9650\u65f6\u62a2\u8d2d',
            },
            bases=('shop.active',),
        ),
        migrations.CreateModel(
            name='Newer',
            fields=[
                ('active_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.Active')),
                ('newer_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='\u65b0\u4eba\u4ef7')),
            ],
            options={
                'verbose_name': '\u65b0\u624b\u793c\u5305',
                'verbose_name_plural': '\u65b0\u624b\u793c\u5305',
            },
            bases=('shop.active',),
        ),
        migrations.CreateModel(
            name='Speed',
            fields=[
                ('active_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.Active')),
            ],
            options={
                'verbose_name': '\u52a0\u901f\u5ea6',
                'verbose_name_plural': '\u52a0\u901f\u5ea6',
            },
            bases=('shop.active',),
        ),
        migrations.AddField(
            model_name='shopcart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.User', verbose_name='\u7528\u6237'),
        ),
        migrations.AddField(
            model_name='promotedeal',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.User'),
        ),
        migrations.AddField(
            model_name='promote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.User'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product', verbose_name='\u76f8\u5173\u4ea7\u54c1'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='productOption',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.ProductOption', verbose_name='\u4ea7\u54c1\u7c7b\u578b'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.User', verbose_name='\u7528\u6237'),
        ),
        migrations.AddField(
            model_name='mycoupon',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.User', verbose_name='\u4f1a\u5458'),
        ),
        migrations.AddField(
            model_name='location',
            name='provice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Provice'),
        ),
        migrations.AddField(
            model_name='location',
            name='region',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='city', chained_model_field='city', null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Region'),
        ),
        migrations.AddField(
            model_name='country',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Region'),
        ),
        migrations.AddField(
            model_name='commet',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product', verbose_name='\u5206\u7c7b'),
        ),
        migrations.AddField(
            model_name='commet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.User', verbose_name='\u7528\u6237'),
        ),
        migrations.AddField(
            model_name='collection',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product', verbose_name='\u4ea7\u54c1'),
        ),
        migrations.AddField(
            model_name='collection',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.User', verbose_name='\u4f1a\u5458'),
        ),
        migrations.AddField(
            model_name='coinitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.User', verbose_name='\u7528\u6237'),
        ),
        migrations.AddField(
            model_name='city',
            name='provice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Provice'),
        ),
        migrations.AddField(
            model_name='cell',
            name='Page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Page'),
        ),
        migrations.AddField(
            model_name='address',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Location', verbose_name='\u5730\u7406\u4f4d\u7f6e'),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.User', verbose_name='\u4f1a\u5458'),
        ),
        migrations.AddField(
            model_name='activeuser',
            name='active',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Active'),
        ),
        migrations.AddField(
            model_name='activeuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.User', verbose_name='\u6d3b\u52a8\u53c2\u4e0e\u4eba'),
        ),
        migrations.AddField(
            model_name='activeship',
            name='active',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Active'),
        ),
        migrations.AddField(
            model_name='activeship',
            name='activerange',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.ActiveRange', verbose_name='\u6d3b\u52a8\u8303\u56f4'),
        ),
        migrations.AddField(
            model_name='activerange',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Category', verbose_name='\u5206\u7c7b'),
        ),
        migrations.AddField(
            model_name='activerange',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Location', verbose_name='\u5730\u7406\u4f4d\u7f6e'),
        ),
        migrations.AddField(
            model_name='activerange',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Product', verbose_name='\u4ea7\u54c1'),
        ),
        migrations.AddField(
            model_name='activerange',
            name='tribe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Tribe', verbose_name='\u90e8\u843d'),
        ),
        migrations.AddField(
            model_name='active',
            name='activerange',
            field=models.ManyToManyField(through='shop.Activeship', to='shop.ActiveRange', verbose_name='\u53c2\u4e0e\u8303\u56f4'),
        ),
        migrations.AddField(
            model_name='active',
            name='users',
            field=models.ManyToManyField(through='shop.Activeuser', to='shop.User', verbose_name='\u6d3b\u52a8\u53c2\u4e0e\u4eba'),
        ),
        migrations.AddField(
            model_name='mycoupon',
            name='coupon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Coupon', verbose_name='\u4f18\u60e0\u5238'),
        ),
    ]
