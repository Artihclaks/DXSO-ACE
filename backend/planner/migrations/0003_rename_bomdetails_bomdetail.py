# Generated by Django 4.2.1 on 2023-05-29 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_rename__93e_100kva_int_o_p_trx_al_o_s_bomdetails_801032569_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BomDetails',
            new_name='BomDetail',
        ),
    ]
