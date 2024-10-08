from wagtail import blocks


class ButtonBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(required=False, help_text="Enter the button value")
    link = blocks.URLBlock(required=False, help_text="Enter the url of this button")
    bg_color = blocks.ChoiceBlock(required=False, choices=[
        ('darkblue', 'Dark Blue'),
        ('green', 'Green'),
        ('white', 'White')
    ],
    help_text="Choose a button type"
    )
            


class HighlightBoxBlock(blocks.StructBlock):
    heading = blocks.RichTextBlock(required=False, help_text="Enter the heading")
    subheading = blocks.RichTextBlock(required=False, help_text="Enter the subheading")
    text = blocks.RichTextBlock(required=False, help_text="Enter the text")
    button = ButtonBlock(required=False, help_text="Enter the button")
    contact_us = blocks.BooleanBlock(required=False, help_text="Check if you want to show contact us button")
    bg_color = blocks.ChoiceBlock(required=False, choices=[
        ('darkblue', 'Dark Blue'),
        ('green', 'Green'),
        ('white', 'White'),
        ('gray', 'Gray')
    ])


