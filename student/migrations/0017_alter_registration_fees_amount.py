# Generated by Django 4.2.6 on 2023-11-05 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0016_semesters_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration_fees',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
