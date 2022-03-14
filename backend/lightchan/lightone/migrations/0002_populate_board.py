# Generated by Django 4.0.2 on 2022-03-13 22:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [("lightone", "0001_initial")
    ]

    def insertData(apps, scheme_editor):
        Board = apps.get_model('lightone', 'Board')
        board = Board(id = "man", board_name="main", board_description="General Discussion", nsfw=False, mnemonic="man")
        board.save()
        board2 = Board(id = "mus", board_name="music", board_description="Music, Bands, Concerts", nsfw=False, mnemonic="mus")
        board2.save()
        board3 = Board(id = "art", board_name="art", board_description="Art and Artists", nsfw=False, mnemonic="art")
        board3.save()
        board4 = Board(id = "lit", board_name="literature", board_description="All Things Literature", nsfw=False, mnemonic="lit")
        board4.save()
        board5 = Board(id = "tec", board_name="technology", board_description="Technology Discussion", nsfw=False, mnemonic="tec")
        board5.save()

    operations = [
        migrations.RunPython(insertData)
    ]