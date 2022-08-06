# Generated by Django 4.0.6 on 2022-08-06 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('fid', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_pending', models.BooleanField(default=True)),
                ('friendship_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendship_from', to='reader.reader')),
                ('friendship_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendship_to', to='reader.reader')),
            ],
            options={
                'db_table': 'friend',
            },
        ),
    ]
