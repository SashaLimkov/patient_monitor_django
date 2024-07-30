# Generated by Django 5.0.7 on 2024-07-29 09:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("medical", "0002_alter_condition_options_condition_condition_type_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="deviations",
            options={"verbose_name": "Показатель", "verbose_name_plural": "Показатели"},
        ),
        migrations.AlterModelOptions(
            name="marker",
            options={
                "ordering": ["-name"],
                "verbose_name": "Маркер",
                "verbose_name_plural": "Маркеры",
            },
        ),
        migrations.RemoveField(
            model_name="marker",
            name="deviations",
        ),
        migrations.RemoveField(
            model_name="marker",
            name="measurement",
        ),
        migrations.CreateModel(
            name="MarkerCondition",
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
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Обновлено"),
                ),
                (
                    "deviations",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="medical.deviations",
                    ),
                ),
                (
                    "measurement",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="medical.measurement",
                    ),
                ),
                (
                    "name",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="medical.marker",
                    ),
                ),
            ],
            options={
                "verbose_name": "Марке",
                "verbose_name_plural": "Маркеры",
                "ordering": ["-name"],
            },
        ),
    ]