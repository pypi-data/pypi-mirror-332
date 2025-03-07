# Generated by Django 3.1.7 on 2021-04-04 11:16

# Django
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

# AA Bulletin Board
import aa_bulletin_board.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="General",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "verbose_name": "Bulletins",
                "permissions": (
                    ("basic_access", "Can access this app"),
                    ("manage_bulletins", "Can manage (add/change/remove) bulletins"),
                ),
                "managed": False,
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="Bulletin",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("slug", models.CharField(max_length=255)),
                ("content", models.TextField(blank=True)),
                (
                    "created_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("updated_date", models.DateTimeField(blank=True, null=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=models.SET(
                            aa_bulletin_board.models.get_sentinel_user
                        ),
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Bulletin",
                "verbose_name_plural": "Bulletins",
                "default_permissions": (),
            },
        ),
    ]
