# Generated by Django 4.1 on 2022-08-20 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_alter_notes_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Notes'},
        ),
    ]