# Generated by Django 3.2.9 on 2022-01-04 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamapp', '0003_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='post_user',
            field=models.TextField(default=0, max_length=150),
        ),
    ]