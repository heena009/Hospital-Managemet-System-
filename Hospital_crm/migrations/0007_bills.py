# Generated by Django 3.1.6 on 2021-05-14 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital_crm', '0006_doctor_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('amount', models.IntegerField(null=True)),
                ('type', models.CharField(choices=[('Lab Test', 'Lab Test'), ('Room Charges', 'Room Charges'), ('Doctor Visits', 'Doctor Visits'), ('Lunch', 'Lunch'), ('Medicines', 'Medicines'), ('First Visit', 'First Visit'), ('Followup Visit', 'Followup Visit'), ('In Comments', 'In Comments')], max_length=200)),
                ('Comments', models.TextField(max_length=500)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital_crm.patient')),
            ],
        ),
    ]
