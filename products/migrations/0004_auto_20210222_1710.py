# Generated by Django 3.1.6 on 2021-02-22 17:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_upload_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='upload',
            name='image',
            field=models.FileField(upload_to='pics/'),
        ),
    ]
