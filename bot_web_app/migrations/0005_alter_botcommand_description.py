# Generated by Django 4.2.3 on 2023-07-25 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bot_web_app", "0004_alter_botcommand_description_alter_user_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="botcommand",
            name="description",
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
    ]
