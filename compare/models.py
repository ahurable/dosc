from django.db import models
from wagtail.models import Page
from wagtail import blocks
from wagtail import fields
from wagtail.admin.panels import FieldPanel
from core.blocks import ButtonBlock, HighlightBoxBlock
from wagtail.contrib.table_block.blocks import TableBlock
# Create your models here.


class ComparePage(Page):

    body = fields.StreamField([
        ('heading', blocks.RichTextBlock(classname="full title")),
        ('subheading', blocks.RichTextBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('table', TableBlock()),
        ('highlight_box', HighlightBoxBlock()),
        ('button', ButtonBlock())
    ], null=True, blank=True)

    content_panels = Page.content_panels + [FieldPanel('body')]