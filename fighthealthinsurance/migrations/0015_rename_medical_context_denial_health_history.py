# Generated by Django 5.1.1 on 2024-09-22 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "fighthealthinsurance",
            "0014_alter_denial_appeal_text_alter_denial_denial_text",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="denial",
            old_name="medical_context",
            new_name="health_history",
        ),
    ]