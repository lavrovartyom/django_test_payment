# Generated by Django 4.1.3 on 2022-11-20 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='product name')),
                ('description', models.TextField(verbose_name='product description')),
                ('price', models.IntegerField(default=0, verbose_name='the price of the product')),
            ],
        ),
    ]
