# Generated by Django 4.1.4 on 2023-01-19 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_alter_psychotest_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='psychotest',
            name='test_file',
            field=models.FileField(blank=True, db_column='test_file', null=True, upload_to='blog/static/blog/files/'),
        ),
    ]