# Generated by Django 4.0.6 on 2022-08-02 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluasimodel', '0004_alter_datapenduduk_prediksi_bantuan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datapenduduk',
            old_name='jmlanakSMA',
            new_name='jmlanaksma',
        ),
    ]
