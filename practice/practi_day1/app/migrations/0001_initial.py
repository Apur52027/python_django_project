# Generated by Django 5.1.4 on 2025-02-11 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adminform',
            fields=[
                ('auto_field', models.AutoField(primary_key=True, serialize=False)),
                ('char_field', models.CharField(max_length=255)),
                ('boolean_field', models.BooleanField()),
                ('date_field', models.DateField()),
                ('decimal_field', models.DecimalField(decimal_places=2, max_digits=5)),
                ('duration_field', models.DurationField()),
                ('email_field', models.EmailField(max_length=254)),
                ('file_field', models.FileField(upload_to='files/')),
                ('date_time_field', models.DateTimeField()),
            ],
        ),
    ]
