# Generated by Django 4.2.3 on 2023-08-09 03:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_post_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="category",
            field=models.CharField(
                choices=[("0", "일상"), ("1", "유머"), ("2", "정보")],
                default="0",
                max_length=1,
            ),
        ),
    ]
