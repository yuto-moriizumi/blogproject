# Generated by Django 3.2.5 on 2021-07-17 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='category',
            field=models.CharField(choices=[('bussiness', 'ビジネス'), ('life', '生活'), ('other', 'その他')], max_length=50),
        ),
    ]
