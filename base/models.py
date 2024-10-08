from django.db import models
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel, TabbedInterface, ObjectList
)
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting
)
from wagtail.models import Orderable
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
# Create your models here.



class HeaderMenu(Orderable):

    setting = ParentalKey(
        "base.SiteSettings",
        related_name="header_menu",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    panels = [
                FieldPanel('title'),
                FieldPanel('url')
            ]
    
class Footer(Orderable):
    setting = ParentalKey(
        'base.SiteSettings',
        related_name="footer",
        on_delete=models.CASCADE
    )
    heading = models.TextField(help_text="This text displays in a large size into the footer")
    text = models.TextField(help_text="Enter the main text it fits into the footer (like license or copyright content)")

    panels = [
        FieldPanel('heading'),
        FieldPanel('text')
    ]



@register_setting
class SiteSettings(BaseGenericSetting, ClusterableModel):


    company_number = models.CharField( help_text="Enter your company phone number", default="09123456789", max_length=15)
    motivate_text = models.CharField( help_text="Something to make user motivated like : Get A Cash Offer Today", default="09123456789", max_length=250)
    motivate_url = models.CharField( help_text="When user cliked on motivate text, where shall he go? enter the url.", default="Enter motivation url", max_length=100)
   
    company_name = models.CharField( help_text="Enter name of your company (it'll displayed below the logo)", default="09123456789", max_length=200)
    company_claims = models.CharField( help_text="Enter your company claims", default="09123456789", max_length=300)

    main_tab = [
        MultiFieldPanel(
            [
                FieldPanel("company_number"),
                FieldPanel("motivate_text"),
                FieldPanel("motivate_url")
            ],
            "Top header settings"
        ),
        MultiFieldPanel(
            [
                FieldPanel("company_name"),
                FieldPanel("company_claims")
            ],
            "Present your company"
        ),
    ]

    header_tab = [
        MultiFieldPanel([
            InlinePanel('header_menu'),
        ],
        "Menu Items"
        )
    ]

    footer_tab = [
        MultiFieldPanel([
            InlinePanel('footer')
        ],
        "Footer Options"
        )
    ]

    edit_handler = TabbedInterface([
        ObjectList(header_tab, heading="header"),
        ObjectList(footer_tab, heading="Footer Options"),
        ObjectList(main_tab, heading="main")
    ])


