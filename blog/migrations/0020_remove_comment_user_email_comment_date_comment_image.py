# Generated by Django 4.0 on 2022-01-03 16:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_alter_post_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user_email',
        ),
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 3, 16, 10, 8, 307540, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads'),
        ),
    ]
