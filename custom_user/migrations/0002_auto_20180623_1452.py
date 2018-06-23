# Generated by Django 2.0.6 on 2018-06-23 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('custom_user', '0001_initial'),
        ('auth', '0009_alter_user_last_name_max_length'),
        ('target', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='targets',
            field=models.ManyToManyField(blank=True, related_name='users_targets', to='target.Target'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterUniqueTogether(
            name='customuser',
            unique_together={('email', 'username')},
        ),
    ]
