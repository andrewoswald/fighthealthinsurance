# Generated by Django 5.0.8 on 2024-09-27 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fighthealthinsurance", "0017_remove_denial_plan_documents_plandocuments"),
    ]

    operations = [
        migrations.CreateModel(
            name="InterestedProfessional",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(default="", max_length=300)),
                ("business_name", models.CharField(default="", max_length=300)),
                ("phone_number", models.CharField(default="", max_length=300)),
                ("address", models.CharField(default="", max_length=1000)),
                ("email", models.EmailField(max_length=254)),
                ("comments", models.CharField(default="", max_length=30000)),
                ("clicked_for_paid", models.BooleanField(default=True)),
                ("paid", models.BooleanField(default=False)),
                ("signup_date", models.DateField(auto_now=True)),
            ],
        ),
    ]
