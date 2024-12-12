from django.db import models
from wagtail.models import Page
from wagtail import blocks
from wagtail import fields
from wagtail.admin.panels import FieldPanel
from core.blocks import ButtonBlock, HighlightBoxBlock
from wagtail.contrib.table_block.blocks import TableBlock
# Create your models here.

default_table_options = {
    'minSpareRows': 0,
    'startRows': 6,
    'startCols': 3,
    'colHeaders': False,
    'rowHeaders': False,
    'contextMenu': True,
    'editor': 'text',
    'stretchH': 'all',
    'height': 108,
    'languege': 'en',
    'renderer': 'text',
    'autoColumnSize': False,
}

class ComparePage(Page):

    body = fields.StreamField([
        ('heading', blocks.RichTextBlock(classname="full title")),
        ('subheading', blocks.RichTextBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('table', TableBlock(table_options=default_table_options)),
        ('highlight_box', HighlightBoxBlock()),
        ('button', ButtonBlock())
    ], null=True, blank=True)

    content_panels = Page.content_panels + [FieldPanel('body')]