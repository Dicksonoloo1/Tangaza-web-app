# Generated by Django 3.1.6 on 2021-02-22 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='user_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
