# Generated by Django 2.0.6 on 2018-06-23 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reward', '0001_initial'),
        ('book', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('current_page_progress', models.PositiveIntegerField(default=0, verbose_name='Current page progress')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='targets', to='book.Book')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('reward', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='targets', to='reward.Reward')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
