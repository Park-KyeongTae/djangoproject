# Generated by Django 4.2.3 on 2023-08-09 02:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="category",
            field=models.CharField(
                choices=[
                    ("FR", "일상의글"),
                    ("SO", "유머"),
                    ("JR", "Junior"),
                    ("SR", "Senior"),
                    ("GR", "Graduate"),
                ],
                default="FR",
                max_length=2,
            ),
        ),
    ]