# Generated by Django 4.0 on 2022-01-02 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, height_field='200', null=True, upload_to='uploads', width_field='200'),
        ),
    ]
