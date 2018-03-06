# Generated by Django 2.0.2 on 2018-03-06 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
        ('reward', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name="Target's name")),
                ('description', models.TextField(max_length=1024, verbose_name="Target's description")),
                ('start_date', models.DateField(verbose_name="Target's start date")),
                ('end_date', models.DateField(verbose_name="Target's end date")),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='targets', to='book.Book')),
                ('reward', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rewards', to='reward.Reward')),
            ],
        ),
    ]
