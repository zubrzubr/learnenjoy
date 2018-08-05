# Generated by Django 2.0.6 on 2018-08-04 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('target', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='reward',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='targets', to='reward.Reward'),
        ),
    ]
