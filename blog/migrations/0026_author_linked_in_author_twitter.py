# Generated by Django 4.0 on 2022-01-04 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_alter_comment_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='linked_in',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='twitter',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
