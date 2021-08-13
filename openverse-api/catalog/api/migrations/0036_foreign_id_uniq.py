# Generated by Django 3.2.5 on 2021-08-13 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_view_count_null'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='audio',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterField(
            model_name='audio',
            name='foreign_identifier',
            field=models.CharField(blank=True, db_index=True, help_text='The identifier provided by the upstream source.', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='audioset',
            name='foreign_identifier',
            field=models.CharField(blank=True, db_index=True, help_text='The identifier provided by the upstream source.', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='foreign_identifier',
            field=models.CharField(blank=True, db_index=True, help_text='The identifier provided by the upstream source.', max_length=1000, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='audio',
            unique_together={('foreign_identifier', 'provider')},
        ),
        migrations.AlterUniqueTogether(
            name='image',
            unique_together={('foreign_identifier', 'provider')},
        ),
    ]
