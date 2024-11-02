# Generated by Django 5.1.2 on 2024-10-10 02:01

import django.core.files.storage
from django.db import migrations, models

import fighthealthinsurance.combined_storage


class Migration(migrations.Migration):

    dependencies = [
        ("fighthealthinsurance", "0033_pubmedarticlesummarized_pubquerymeddata"),
    ]

    operations = [
        migrations.AlterField(
            model_name="followupdocuments",
            name="followup_document",
            field=models.FileField(
                null=True,
                storage=fighthealthinsurance.combined_storage.CombinedStorage(
                    django.core.files.storage.FileSystemStorage(
                        location="localish_data"
                    ),
                    django.core.files.storage.FileSystemStorage(
                        location="external_data"
                    ),
                    django.core.files.storage.FileSystemStorage(
                        location="external_data_b"
                    ),
                ),
                upload_to="",
            ),
        ),
        migrations.AlterField(
            model_name="plandocuments",
            name="plan_document",
            field=models.FileField(
                null=True,
                storage=fighthealthinsurance.combined_storage.CombinedStorage(
                    django.core.files.storage.FileSystemStorage(
                        location="localish_data"
                    ),
                    django.core.files.storage.FileSystemStorage(
                        location="external_data"
                    ),
                    django.core.files.storage.FileSystemStorage(
                        location="external_data_b"
                    ),
                ),
                upload_to="",
            ),
        ),
    ]
