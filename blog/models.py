from django.db import models
from wagtail.models import Page
from wagtail import blocks
from wagtail import fields
from wagtail.admin.panels import FieldPanel
from core.blocks import ButtonBlock, HighlightBoxBlock
# Create your models here.


class BlogPage(Page):

    body = fields.StreamField([
        ('heading', blocks.RichTextBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('button', ButtonBlock()),
        ('highlight_box', HighlightBoxBlock()),
        ('form_aside', blocks.StreamBlock([
            ('heading1', blocks.RichTextBlock(required=False, help_text="Enter first heading content (big size)")),
            ('heading2', blocks.RichTextBlock(required=False, help_text="Enter second heading content (small size)")),
            ('paragraph', blocks.RichTextBlock(required=False, help_text="Enter paragraph")),
            ('contact_form', blocks.BooleanBlock(required=False, help_text="If it's checked it displays the contact form")),
            ('button', ButtonBlock()),
        ])),
        ('contact_us', HighlightBoxBlock())
    ], null=True, blank=True)

    content_panels = Page.content_panels + [FieldPanel('body')]