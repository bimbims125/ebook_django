# Generated by Django 3.2.9 on 2022-01-01 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0003_alter_book_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_author', models.CharField(max_length=100)),
            ],
        ),
    ]
