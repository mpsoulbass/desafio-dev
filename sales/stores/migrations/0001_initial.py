# Generated by Django 3.2.4 on 2021-06-25 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StoreOwner",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=60, verbose_name="Nome")),
            ],
            options={
                "ordering": ["id", "created_at", "updated_at"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Store",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=60, verbose_name="Nome")),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="stores.storeowner",
                    ),
                ),
            ],
            options={
                "ordering": ["id", "created_at", "updated_at"],
                "abstract": False,
            },
        ),
    ]