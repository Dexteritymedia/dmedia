from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import StreamFieldPanel, InlinePanel, FieldPanel, MultiFieldPanel, FieldRowPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

from home import blocks


class HomePage(Page):

    max_count = 1
    template = 'index.html'
    
    main_menu = StreamField(
        [
            
            ('page_header', blocks.HeadingBlock()),
            ('menu', blocks.HomePageMenuBlock()),
            ('service', blocks.ServiceMainBlock()),
            ('work', blocks.FeatureBlock()),
            ('testimony', blocks.TestimonialBlock()),
            ('fact', blocks.FactBlock()),
        ],
        null=True,
        blank=True,
    )


    content_panels = Page.content_panels + [
        StreamFieldPanel('main_menu'),
    ]


    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Home'
        

class AboutIndex(Page):

    
    subpage_types = [
        
        'home.AboutPage',
    ]

    template = 'about_index.html'
    max_count = 1
    
    intro = RichTextField(blank=True)

    class Meta:
        verbose_name = 'About'



class AboutPage(Page):
    parent_page_types = [
        
        'home.AboutIndex',
    ]

    subpage_types = [
        
        'home.AboutPage',
    ]

    template = 'about_page.html'


    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]


class ServiceIndex(Page):


    subpage_types = [
        
        'home.ServicePage',
    ]

    template = 'service_index.html'
    max_count = 1

    image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )
    
    intro = RichTextField(blank=True)

    service_page = StreamField(
        [
            ('service_list', blocks.ServiceIndexListBlock()),
            ('client', blocks.ClientBlock()),
            ('service_main', blocks.ServiceMainBlock()),
        ], null=True, blank=True,
    )
    


    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('image'),
            FieldPanel('intro'),
            ],),
        StreamFieldPanel('service_page'),
    ]

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'



class ServicePage(Page):
    parent_page_types = [
        
        'home.ServiceIndex',
    ]

    template = 'service_page.html'

    
    service_contact = StreamField(
        [
            ('image', blocks.ImageBlock()),
            ('service_contact', blocks.ServiceContactBlock()),
            ('faq', blocks.FAQBlock()),
            ('service_testimony', blocks.ServiceTestimonyBlock()),
            ('service_list', blocks.ServiceListBlock()),
        ], null=True, blank=True,
    )


    content_panels = Page.content_panels + [
        MultiFieldPanel([
            StreamFieldPanel('service_contact'),
            ],),
    ]





class FormField(AbstractFormField):
    page = ParentalKey('FormPage', related_name='form_fields', on_delete=models.CASCADE)

class FormPage(AbstractEmailForm):

    template = 'contact_page.html'


    max_count = 1

    heading = RichTextField(blank=True, null=True)
    thank_you_text = RichTextField(blank=True, null=True)


    content_panels = AbstractEmailForm.content_panels + [
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('heading', classname='full'),
        FieldPanel('thank_you_text', classname='full'),
    ]

