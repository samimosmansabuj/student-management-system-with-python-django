# Generated by Django 4.2.7 on 2023-12-19 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_alter_student_student_image'),
        ('student', '0021_invoice_registration_fees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration_fees',
            name='Student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Student', to='account.student'),
        ),
    ]
