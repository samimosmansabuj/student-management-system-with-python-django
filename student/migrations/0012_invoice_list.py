# Generated by Django 4.2.6 on 2023-11-04 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_remove_student_admision_id'),
        ('student', '0011_installments_payment_method'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Invoice_id', models.CharField(max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.student')),
            ],
        ),
    ]
