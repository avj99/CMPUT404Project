# Generated by Django 4.1.6 on 2023-03-02 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0004_rename_main_body_comment_body_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='main_body',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='main_name',
        ),
    ]
