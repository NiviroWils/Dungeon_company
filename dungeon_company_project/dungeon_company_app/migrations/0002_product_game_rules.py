# Generated by Django 5.0 on 2023-12-26 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dungeon_company_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='game_rules',
            field=models.TextField(blank=True, null=True),
        ),
    ]