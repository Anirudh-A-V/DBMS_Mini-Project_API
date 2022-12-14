# Generated by Django 4.1.4 on 2022-12-11 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bill",
            fields=[
                ("bill_id", models.AutoField(primary_key=True, serialize=False)),
                ("units", models.IntegerField()),
                ("amount", models.IntegerField()),
                ("date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Consumer",
            fields=[
                ("consumer_id", models.AutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=300)),
                ("phone", models.CharField(max_length=20)),
                ("password", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Complaint",
            fields=[
                ("complaint_id", models.AutoField(primary_key=True, serialize=False)),
                ("description", models.CharField(max_length=1000)),
                ("date", models.DateField()),
                (
                    "consumer_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="consumer.consumer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BillStatus",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status", models.CharField(max_length=100)),
                (
                    "bill_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="consumer.bill",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="bill",
            name="consumer_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="consumer.consumer"
            ),
        ),
    ]
