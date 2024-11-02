# Generated by Django 5.1.2 on 2024-10-31 03:51

import uuid

import django.core.files.storage
import django.db.models.deletion
from django.db import migrations, models

import fighthealthinsurance.combined_storage


class Migration(migrations.Migration):

    dependencies = [
        ("fighthealthinsurance", "0043_faxestosend_denial_appeal_fax_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="faxestosend",
            name="combined_document",
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
        migrations.AddField(
            model_name="faxestosend",
            name="denial_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="fighthealthinsurance.denial",
            ),
        ),
        migrations.AddField(
            model_name="faxestosend",
            name="destination",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="faxestosend",
            name="name",
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name="faxestosend",
            name="sent",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="faxestosend",
            name="uuid",
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=300),
        ),
        migrations.AddField(
            model_name="pubmedquerydata",
            name="denial_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="fighthealthinsurance.denial",
            ),
        ),
        migrations.AlterField(
            model_name="faxestosend",
            name="health_history",
            field=models.TextField(null=True),
        ),
    ]
