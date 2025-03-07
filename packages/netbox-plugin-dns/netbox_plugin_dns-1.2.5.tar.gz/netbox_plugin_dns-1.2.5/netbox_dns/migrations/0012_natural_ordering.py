# Generated by Django 5.1.3 on 2024-12-02 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("netbox_dns", "0011_rename_related_fields"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nameserver",
            name="name",
            field=models.CharField(
                db_collation="natural_sort", max_length=255, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="record",
            name="fqdn",
            field=models.CharField(
                blank=True,
                db_collation="natural_sort",
                default=None,
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="record",
            name="name",
            field=models.CharField(db_collation="natural_sort", max_length=255),
        ),
        migrations.AlterField(
            model_name="recordtemplate",
            name="name",
            field=models.CharField(
                db_collation="natural_sort", max_length=200, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="recordtemplate",
            name="record_name",
            field=models.CharField(db_collation="natural_sort", max_length=255),
        ),
        migrations.AlterField(
            model_name="registrar",
            name="name",
            field=models.CharField(
                db_collation="natural_sort", max_length=255, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="registrationcontact",
            name="contact_id",
            field=models.CharField(
                db_collation="natural_sort", max_length=50, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="registrationcontact",
            name="name",
            field=models.CharField(
                blank=True, db_collation="natural_sort", max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="view",
            name="name",
            field=models.CharField(
                db_collation="natural_sort", max_length=255, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="zone",
            name="name",
            field=models.CharField(db_collation="natural_sort", max_length=255),
        ),
        migrations.AlterField(
            model_name="zonetemplate",
            name="name",
            field=models.CharField(
                db_collation="natural_sort", max_length=200, unique=True
            ),
        ),
    ]
