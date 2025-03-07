# Generated by Django 5.0.9 on 2024-11-11 08:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("netbox_dns", "0010_view_ip_address_filter"),
    ]

    operations = [
        migrations.AlterField(
            model_name="record",
            name="zone",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="records",
                to="netbox_dns.zone",
            ),
        ),
        migrations.AlterField(
            model_name="zone",
            name="registrant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="registrant_zones",
                to="netbox_dns.registrationcontact",
            ),
        ),
        migrations.AlterField(
            model_name="zone",
            name="registrar",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="zones",
                to="netbox_dns.registrar",
            ),
        ),
        migrations.AlterField(
            model_name="zone",
            name="soa_mname",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="soa_zones",
                to="netbox_dns.nameserver",
            ),
        ),
        migrations.AlterField(
            model_name="zone",
            name="view",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="zones",
                to="netbox_dns.view",
            ),
        ),
    ]
