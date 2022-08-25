# Generated by Django 4.0 on 2022-08-25 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
        ('reader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reads',
            fields=[
                ('rsid', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('w', 'Want to Read'), ('r', 'Reading'), ('c', 'Completed')], max_length=1)),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='book.book')),
                ('reader', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reader.reader')),
            ],
            options={
                'db_table': 'reads',
            },
        ),
    ]
