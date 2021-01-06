# Generated by Django 3.1.5 on 2021-01-05 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0003_auto_20210105_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='event',
            field=models.ForeignKey(default='', limit_choices_to={'event.iscompleted': False}, on_delete=django.db.models.deletion.CASCADE, to='Events.event'),
        ),
    ]