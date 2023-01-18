# Generated by Django 4.1.5 on 2023-01-18 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_remove_sous_category_category_id_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="sous_category_id",
        ),
        migrations.AddField(
            model_name="sous_category",
            name="category_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="home.category",
            ),
        ),
    ]