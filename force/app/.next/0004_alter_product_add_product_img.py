# Generated by Django 3.2.10 on 2022-02-06 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_manager_account_slug_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_add',
            name='Product_Img',
            field=models.ImageField(upload_to='image/'),
        ),
    ]
