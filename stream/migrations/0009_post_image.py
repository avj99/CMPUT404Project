# Generated by Django 4.1.7 on 2023-03-08 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0008_alter_post_howmanylike'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/post_photo'),
        ),
    ]
