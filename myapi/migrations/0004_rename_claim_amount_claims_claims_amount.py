# Generated by Django 3.2.5 on 2021-07-25 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_claims_claim_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='claims',
            old_name='claim_amount',
            new_name='claims_amount',
        ),
    ]
