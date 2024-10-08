from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.panels import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel
)
from wagtail.fields import RichTextField
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField
)
from wagtail import fields
from wagtail import blocks
from core.blocks import HighlightBoxBlock, ButtonBlock


class FormField(AbstractFormField):
    page = ParentalKey(
        'ContactPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )


class ContactPage(AbstractEmailForm):

    template = "contact/contact_page.html"
    # This is the default path.
    # If ignored, Wagtail adds _landing.html to your template name
    landing_page_template = "contact/contact_page_landing.html"

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

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

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel("subject"),
        ], heading="Email Settings"),
    ]  + [FieldPanel('body')]