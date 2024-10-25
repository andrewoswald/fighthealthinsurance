# Generated by Django 5.1.2 on 2024-10-25 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "fighthealthinsurance",
            "0041_rename_pubquerymeddata_pubmedquerydata_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="pubmedarticlesummarized",
            name="basic_summary",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="pubmedarticlesummarized",
            name="publication_date",
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="pubmedarticlesummarized",
            name="says_effective",
            field=models.BooleanField(null=True),
        ),
    ]
