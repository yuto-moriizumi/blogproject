# Generated by Django 3.2.5 on 2021-07-17 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0002_alter_blogmodel_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogmodel',
            old_name='post_date',
            new_name='postdate',
        ),
    ]
