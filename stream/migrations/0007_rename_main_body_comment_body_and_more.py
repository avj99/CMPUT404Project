# Generated by Django 4.1.6 on 2023-03-02 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0006_rename_main_date_comment_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='main_body',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='date',
            new_name='main_date',
        ),
    ]
