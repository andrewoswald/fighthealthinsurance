# Generated by Django 5.0.8 on 2024-09-28 23:18

import regex_field.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("fighthealthinsurance", "0025_denial_employer_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="denialtypes",
            name="diagnosis_regex",
            field=regex_field.fields.RegexField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name="denialtypes",
            name="procedure_regex",
            field=regex_field.fields.RegexField(max_length=400, null=True),
        ),
    ]
