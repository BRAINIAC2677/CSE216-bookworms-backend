# Generated by Django 4.0 on 2022-08-28 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('lid', models.AutoField(primary_key=True, serialize=False)),
                ('library_name', models.CharField(max_length=200)),
                ('photo_url', models.CharField(blank=True, max_length=200, null=True)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'db_table': 'library',
            },
        ),
    ]
