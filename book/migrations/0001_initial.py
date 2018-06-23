# Generated by Django 2.0.6 on 2018-06-23 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name="Author's first name")),
                ('last_name', models.CharField(max_length=255, verbose_name="Author's last name")),
                ('bio', models.TextField(max_length=1024, verbose_name="Author's biography")),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name="Book's name")),
                ('description', models.TextField(max_length=1024, verbose_name="Book's description")),
                ('page_count', models.PositiveIntegerField(default=0, verbose_name='Count of pages')),
                ('authors', models.ManyToManyField(related_name='authors_books', to='book.Author')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Genre title')),
                ('description', models.TextField(max_length=1024, verbose_name='Genre description')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(related_name='books', to='book.Genre'),
        ),
    ]
