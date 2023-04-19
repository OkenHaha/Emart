# Generated by Django 3.2.12 on 2022-05-20 02:32

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_rename_product_img_userprofile_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager_account',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, default=None, editable=False, null=True, populate_from=['user', 'Email'], unique=True),
        ),
    ]
