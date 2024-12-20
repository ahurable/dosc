# Generated by Django 5.0.10 on 2024-12-08 20:35

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_alter_homepage_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "hero",
                        wagtail.blocks.StreamBlock(
                            [
                                (
                                    "heading",
                                    wagtail.blocks.RichTextBlock(
                                        help_text="Enter heading size text for your hero section",
                                        required=True,
                                    ),
                                ),
                                (
                                    "text",
                                    wagtail.blocks.RichTextBlock(
                                        help_text="Enter text for your hero section",
                                        required=True,
                                    ),
                                ),
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        help_text="Choose a image related to your bussiness",
                                        required=True,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "about",
                        wagtail.blocks.StreamBlock(
                            [
                                (
                                    "text",
                                    wagtail.blocks.RichTextBlock(
                                        help_text="Enter Description for your about section",
                                        required=True,
                                    ),
                                ),
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        help_text="Choose related images to your bussiness",
                                        required=True,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "highlight_text",
                        wagtail.blocks.RichTextBlock(
                            help_text="The text inside this section will displayed with a different background in home page. For example you can mention what you will buy as a buyer or what you sell as a seller.",
                            required=False,
                        ),
                    ),
                    (
                        "guid",
                        wagtail.blocks.StreamBlock(
                            [
                                (
                                    "text",
                                    wagtail.blocks.RichTextBlock(
                                        help_text="Make it clear, tell the customers or sellers about the rules, if and else",
                                        required=True,
                                    ),
                                ),
                                (
                                    "steps",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            (
                                                "step",
                                                wagtail.blocks.TextBlock(
                                                    help_text="Enter the name of the space"
                                                ),
                                            ),
                                            (
                                                "image",
                                                wagtail.images.blocks.ImageChooserBlock(
                                                    help_text="Enter a image related to this step (it can be a symbol or a emoji transparented for better output)"
                                                ),
                                            ),
                                            (
                                                "text",
                                                wagtail.blocks.TextBlock(
                                                    help_text="What in this step costs for consumer"
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "advantages",
                        wagtail.blocks.StreamBlock(
                            [
                                (
                                    "bonus",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            (
                                                "text",
                                                wagtail.blocks.RichTextBlock(
                                                    help_text="why customer have to choose you? explain with dotted and short phrases",
                                                    required=False,
                                                ),
                                            ),
                                            (
                                                "image",
                                                wagtail.images.blocks.ImageChooserBlock(
                                                    help_text="Choose a related image",
                                                    required=False,
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                                (
                                    "text",
                                    wagtail.blocks.RichTextBlock(
                                        help_text="This text will shown under bonus section",
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "contact_us",
                        wagtail.blocks.StreamBlock(
                            [
                                (
                                    "heading",
                                    wagtail.blocks.RichTextBlock(
                                        help_text="this is the big text for upper section of contact us",
                                        required=False,
                                    ),
                                ),
                                (
                                    "text",
                                    wagtail.blocks.RichTextBlock(
                                        help_text="this is the smaller text shown under the heading of contact us",
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "last_speech",
                        wagtail.blocks.RichTextBlock(
                            help_text="If there is things that you have to mention about it",
                            required=False,
                        ),
                    ),
                ]
            ),
        ),
    ]
