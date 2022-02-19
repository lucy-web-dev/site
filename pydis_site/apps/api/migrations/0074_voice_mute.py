# Generated by Django 3.0.14 on 2021-10-09 18:52
from django.apps.registry import Apps
from django.db import migrations, models
from django.db.backends.base.schema import BaseDatabaseSchemaEditor


def migrate_infractions(apps: Apps, schema_editor: BaseDatabaseSchemaEditor) -> None:
    Infraction = apps.get_model("api", "Infraction")

    for infraction in Infraction.objects.filter(type="voice_ban"):
        infraction.type = "voice_mute"
        infraction.save()


def unmigrate_infractions(apps: Apps, schema_editor: BaseDatabaseSchemaEditor) -> None:
    Infraction = apps.get_model("api", "Infraction")

    for infraction in Infraction.objects.filter(type="voice_mute"):
        infraction.type = "voice_ban"
        infraction.save()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0073_otn_allow_GT_and_LT'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infraction',
            name='type',
            field=models.CharField(choices=[('note', 'Note'), ('warning', 'Warning'), ('watch', 'Watch'), ('mute', 'Mute'), ('kick', 'Kick'), ('ban', 'Ban'), ('superstar', 'Superstar'), ('voice_ban', 'Voice Ban'), ('voice_mute', 'Voice Mute')], help_text='The type of the infraction.', max_length=10),
        ),
        migrations.RunPython(migrate_infractions, unmigrate_infractions)
    ]