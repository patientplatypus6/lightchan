# Generated by Django 4.0.2 on 2022-03-13 22:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False, unique=True)),
                ('board_name', models.TextField()),
                ('board_description', models.TextField()),
                ('nsfw', models.BooleanField()),
                ('mnemonic', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('clean_id', models.TextField(default=0)),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('file_name', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('votes', models.IntegerField(default=1)),
                ('mnemonic', models.TextField()),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lightone.board', to_field='mnemonic')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('clean_id', models.TextField(default=0)),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('file_name', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('votes', models.IntegerField(default=1)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lightone.comment')),
            ],
        )
    ]
