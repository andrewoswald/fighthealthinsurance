# Generated by Django 5.0.8 on 2024-10-04 05:11

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fighthealthinsurance", "0028_denial_appeal_result"),
    ]

    operations = [
        migrations.AddField(
            model_name="denial",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
