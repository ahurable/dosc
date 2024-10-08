# Generated by Django 5.0.7 on 2024-08-08 14:37

import django.db.models.deletion
import wagtail.blocks
import wagtail.contrib.table_block.blocks
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0093_uploadedfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComparePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.fields.StreamField([('heading', wagtail.blocks.RichTextBlock(form_classname='full title')), ('subheading', wagtail.blocks.RichTextBlock(form_classname='full title')), ('paragraph', wagtail.blocks.RichTextBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock()), ('highlight_box', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(help_text='Enter the heading', required=False)), ('subheading', wagtail.blocks.RichTextBlock(help_text='Enter the subheading', required=False)), ('text', wagtail.blocks.RichTextBlock(help_text='Enter the text', required=False)), ('button', wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock(help_text='Enter the button value', required=False)), ('link', wagtail.blocks.URLBlock(help_text='Enter the url of this button', required=False)), ('bg_color', wagtail.blocks.ChoiceBlock(choices=[('darkblue', 'Dark Blue'), ('green', 'Green'), ('white', 'White')], help_text='Choose a button type', required=False))], help_text='Enter the button', required=False)), ('contact_us', wagtail.blocks.BooleanBlock(help_text='Check if you want to show contact us button', required=False)), ('bg_color', wagtail.blocks.ChoiceBlock(choices=[('darkblue', 'Dark Blue'), ('green', 'Green'), ('white', 'White'), ('gray', 'Gray')], required=False))])), ('button', wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock(help_text='Enter the button value', required=False)), ('link', wagtail.blocks.URLBlock(help_text='Enter the url of this button', required=False)), ('bg_color', wagtail.blocks.ChoiceBlock(choices=[('darkblue', 'Dark Blue'), ('green', 'Green'), ('white', 'White')], help_text='Choose a button type', required=False))]))], blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
