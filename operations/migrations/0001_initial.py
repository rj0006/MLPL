# Generated by Django 4.2 on 2024-02-06 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consignment',
            fields=[
                ('consignment_no', models.AutoField(primary_key=True, serialize=False)),
                ('consignment_date', models.DateField()),
                ('source', models.CharField(max_length=100, null=True)),
                ('destination', models.CharField(max_length=100, null=True)),
                ('mode', models.CharField(max_length=100, null=True)),
                ('billing_at', models.CharField(max_length=100, null=True)),
                ('consignor', models.CharField(max_length=100, null=True)),
                ('consignee', models.CharField(max_length=100, null=True)),
                ('billing_party', models.CharField(max_length=100, null=True)),
                ('delivery_at', models.CharField(max_length=100, null=True)),
                ('load_type', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.CharField(max_length=100)),
                ('invoice_date', models.DateField()),
                ('invoice_description', models.CharField(max_length=100)),
                ('part_code', models.CharField(max_length=100)),
                ('invoice_value', models.CharField(max_length=100)),
                ('consignment_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.consignment')),
            ],
        ),
    ]