from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailcore.blocks import CharBlock, TextBlock, StreamBlock, StructBlock, \
    PageChooserBlock, RichTextBlock

from blog.models import BlogPage, BlogIndexPage
from modelcluster.fields import ParentalKey

class structCardBlock(StructBlock):
    image = ImageChooserBlock()
    heading = CharBlock()
    caption = TextBlock()
    page = PageChooserBlock(required=False)
    class Meta:
        icon = 'image'

class HomePage(Page):
    intro = RichTextField(blank=True)
    showcase_title = RichTextField(blank=True)
    cards = StreamField([
        ('cardblock', structCardBlock()),
        ('tileblock', structCardBlock()),
    ], null=True, blank=False)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super(HomePage, self).get_context(request)

        indexpages = BlogIndexPage.objects.live()  # working
        context['indexpages'] = indexpages
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        MultiFieldPanel([
            FieldPanel('showcase_title', ),
            StreamFieldPanel('cards'),
        ], heading="Project Showcase"),
    ]


class AboutPage(Page):
    name = models.CharField(max_length=250, blank=True)
    bio = RichTextField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    uses = StreamField([
        ('paragraph', RichTextBlock()),
    ], null=True, blank=False)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('name'),
            FieldPanel('bio'),
        ], heading="About Me:"),
        ImageChooserPanel('image'),
        StreamFieldPanel('uses'),
    ]

    parent_page_types = ['home.HomePage']  # only HomePage can create
    subpage_types = []  # no children allowed


#Too lazy to make a contact form...
# from wagtail.wagtailadmin.edit_handlers import FieldRowPanel, InlinePanel
# from wagtail.wagtailforms.edit_handlers import FormSubmissionsPanel
# from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
# class FormField(AbstractFormField):
#     page = ParentalKey('ContactPage', related_name='form_fields')

# class ContactPage(AbstractEmailForm):
#     intro = RichTextField(blank=True)
#     thank_you_text = RichTextField(blank=True)

#     content_panels = AbstractEmailForm.content_panels + [
#         FormSubmissionsPanel(),
#         FieldPanel('intro', classname="full"),
#         InlinePanel('form_fields', label="Form fields"),
#         FieldPanel('thank_you_text', classname="full"),
#         MultiFieldPanel([
#             FieldRowPanel([
#                 FieldPanel('from_address', classname="col6"),
#                 FieldPanel('to_address', classname="col6"),
#             ]),
#             FieldPanel('subject'),
#         ], "Email"),
#     ]

#     ##this over-rides landing page.
#     ## i want to use vue router!
#     #def get_landing_page_template(self, form):
#     #    pass

# #class LandingPage():
# #    pass

# not needed, just a good sample to have on hand
from django.template.defaulttags import register
@register.filter
def order_by(queryset, args):
    args = [x.strip() for x in args.split(',')]
    return queryset.order_by(*args)