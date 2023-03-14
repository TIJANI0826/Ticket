# Generated by Django 3.1.7 on 2021-04-26 03:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=50, null=True, validators=[django.core.validators.RegexValidator(message='Invalid first name entered', regex="^[A-Za-z]([a-zA-Z ,\\'\\.]*)$")])),
                ('last_name', models.CharField(max_length=50, null=True, validators=[django.core.validators.RegexValidator(message='Invalid last name entered', regex='^[a-zA-Z]+$')])),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Please enter a valid phone number. Only 10 digits allowed.', regex='^\\d{10,10}$')])),
                ('address', models.TextField(null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='Profile Picture')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('nationality', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=30)),
                ('date_of_birth', models.DateTimeField(verbose_name='Closing Date')),
                ('reason_for_registering', models.TextField(null=True)),
                ('start_date', models.DateTimeField(verbose_name='Occasion Date')),
                ('exp_date', models.DateTimeField(verbose_name='Closing Date')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_event', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(verbose_name='Occasion Date')),
                ('closing_date', models.DateTimeField(verbose_name='Closing Date')),
                ('event_banner', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d')),
                ('is_approved', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Reservation',
                'ordering': ['start_date'],
            },
        ),
        migrations.CreateModel(
            name='TicketNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_number', models.CharField(editable=False, max_length=120)),
                ('expired', models.BooleanField(default=False)),
                ('ticket', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='account.member')),
            ],
            options={
                'verbose_name': 'Ticket Number ',
            },
        ),
        migrations.AddField(
            model_name='member',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.package'),
        ),
        migrations.CreateModel(
            name='DailySchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('security', models.CharField(max_length=200)),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.package')),
            ],
        ),
    ]
