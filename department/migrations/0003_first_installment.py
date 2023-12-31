# Generated by Django 4.2.6 on 2023-10-21 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0002_alter_department_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='first_installment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('is_paid', models.BooleanField(default=False)),
                ('paid_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
