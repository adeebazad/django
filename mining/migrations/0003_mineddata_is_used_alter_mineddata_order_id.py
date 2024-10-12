# Generated by Django 5.1.1 on 2024-09-28 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mining', '0002_mineddata_delete_miningdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='mineddata',
            name='is_used',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mineddata',
            name='order_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]