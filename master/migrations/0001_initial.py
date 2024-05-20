# Generated by Django 4.2 on 2024-04-01 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='partyMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partytype', models.CharField(max_length=50, null=True)),
                ('code', models.CharField(max_length=50, null=True)),
                ('group', models.CharField(max_length=50, null=True)),
                ('expensetype', models.CharField(max_length=50, null=True)),
                ('partyname', models.CharField(max_length=250, null=True, unique=True)),
                ('controllingbranch', models.CharField(max_length=50, null=True)),
                ('parentaccount', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('pin', models.IntegerField(null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('contactperson', models.CharField(max_length=50, null=True)),
                ('mobilenumber', models.IntegerField(null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('registrationtype', models.CharField(max_length=50, null=True)),
                ('servicetype', models.CharField(max_length=50, null=True)),
                ('gstin', models.CharField(max_length=15, null=True)),
                ('pan', models.CharField(max_length=10, null=True)),
                ('tdsdeducation', models.IntegerField(null=True)),
                ('nameco', models.CharField(max_length=50, null=True)),
                ('mobileco', models.CharField(max_length=50, null=True)),
                ('departmentco', models.CharField(max_length=50, null=True)),
                ('branchco', models.CharField(max_length=50, null=True)),
                ('gstinverify', models.CharField(max_length=50, null=True)),
                ('turnoverfivecr', models.CharField(max_length=10, null=True)),
                ('declarationsubmit', models.CharField(max_length=10, null=True)),
                ('einvoiceapli', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]
