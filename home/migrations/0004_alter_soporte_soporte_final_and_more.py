# Generated by Django 4.0.4 on 2022-05-29 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_soporte_soporte_final_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soporte',
            name='Soporte_Final',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='soporte',
            name='Soporte_Inicio',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='soporte',
            name='Soporte_Solucionado',
            field=models.BooleanField(default=False),
        ),
    ]