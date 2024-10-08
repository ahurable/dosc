from django.db import models

from wagtail.models import Page
from wagtail import fields, blocks
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageChooserBlock

class HomePage(Page):
    
    body = fields.StreamField([
        (
            "hero", 
            blocks.StreamBlock([
                ("text", blocks.RichTextBlock(required=True, help_text="Enter Description for your hero section")),
                ("image", ImageChooserBlock(required=True, help_text="Choose a image related to your bussiness"))
            ])
        ),
        (
            "about", 
            blocks.StreamBlock([
                ("text", blocks.RichTextBlock(required=True, help_text="Enter Description for your about section")),
                ("image", ImageChooserBlock(required=True, help_text="Choose related images to your bussiness"))
            ])    
        ),
        (
            "highlight_text", 
            blocks.RichTextBlock(required=False, help_text="The text inside this section will displayed with a different background in home page. For example you can mention what you will buy as a buyer or what you sell as a seller.")
        ),
        (
            "guid",
            blocks.StreamBlock(
                [
                    ("text", blocks.RichTextBlock(required=True, help_text="Make it clear, tell the customers or sellers about the rules, if and else")),
                    ("steps",
                        blocks.StreamBlock([
                            ('step', blocks.TextBlock( help_text="Enter the name of the space")),
                            ('image', ImageChooserBlock(help_text="Enter a image related to this step (it can be a symbol or a emoji transparented for better output)")),
                            ('text', blocks.TextBlock( help_text="What in this step costs for consumer"))
                        ])
                    )
                ]
            )
        ),
        (
            "advantages",
            blocks.StreamBlock([
                (
                    "bonus", 
                    blocks.StreamBlock([
                        ("text", blocks.RichTextBlock(required=False, help_text="why customer have to choose you? explain with dotted and short phrases")),
                        ("image", ImageChooserBlock(required=False, help_text="Choose a related image"))
                    ]),
                ),
                (
                    "text",
                    blocks.RichTextBlock(required=False, help_text="This text will shown under bonus section")
                )
            ], True)
        ),
        (
            "contact_us",
            blocks.StreamBlock([
                (
                    'heading', 
                    blocks.RichTextBlock(required=False, help_text="this is the big text for upper section of contact us") 
                ),
                (
                    'text',
                    blocks.RichTextBlock(required=False, help_text="this is the smaller text shown under the heading of contact us")
                )
            ])
        ),
        (
            "last_speech",
            blocks.RichTextBlock(required=False, help_text="If there is things that you have to mention about it")
        )
    ])

    content_panels = Page.content_panels + [ FieldPanel('body') ]
