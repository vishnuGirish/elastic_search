# Generated by Django 4.2.4 on 2023-08-02 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="is_deleted",
            field=models.BooleanField(default=False),
        ),
    ]
