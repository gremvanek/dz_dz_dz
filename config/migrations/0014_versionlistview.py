# Generated by Django 3.2.24 on 2024-04-05 12:29

from django.db import migrations, models
import django.db.models.deletion
import django.views.generic.list


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0013_alter_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='VersionListView',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='config.product')),
            ],
            bases=(django.views.generic.list.ListView, 'config.product'),
        ),
    ]