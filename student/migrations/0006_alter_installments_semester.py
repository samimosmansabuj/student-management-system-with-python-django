# Generated by Django 4.2.6 on 2023-10-24 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_installments_is_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installments',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.semesters'),
        ),
    ]
