# Generated by Django 2.2.4 on 2020-03-21 05:22

import KiwiAdmin.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.UUIDField(default=KiwiAdmin.utils.UUIDTools.uuid1_hex, editable=False, primary_key=True, serialize=False)),
                ('product_no', models.CharField(default=KiwiAdmin.utils.random_product_no, max_length=13, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('specification', models.SmallIntegerField(choices=[(1, '五斤'), (2, '十斤')])),
                ('image', models.ImageField(max_length=200, null=True, upload_to='images/product')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('status', models.SmallIntegerField(choices=[(-1, '已删除'), (0, '下架'), (1, '上架')], default=1)),
                ('description', models.TextField(null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'product',
                'db_table': 'product',
                'ordering': ['-create_time'],
            },
        ),
    ]
