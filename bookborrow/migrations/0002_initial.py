# Generated by Django 4.0 on 2022-08-28 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('library', '0001_initial'),
        ('bookborrow', '0001_initial'),
        ('reader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookborrow',
            name='borrowed_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reader.reader'),
        ),
        migrations.AddField(
            model_name='bookborrow',
            name='borrowed_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.library'),
        ),
    ]
