# Generated by Django 3.2.6 on 2022-04-30 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metaverse', '0005_rename_new_file_content_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='file',
            field=models.FileField(blank=True, upload_to='', verbose_name=''),
        ),
    ]