from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.templatetags.wagtailcore_tags import richtext



class LinkStructValue(blocks.StructValue):

    def url(self):
        button_page = self.get('button_page')
        button_url = self.get('button_url')
        if button_page:
            return button_page.url
        elif button_url:
            return button_url

        return None


#1
class HeadingBlock(blocks.StructBlock):

    jumbotron = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('image', ImageChooserBlock(required=False)),
                ('title', blocks.CharBlock(required=False, max_length=40)),
                ('description', blocks.RichTextBlock(required=False, features=['h1','h2','h3','h4','h5','h6','hr','bold','italic','link','code','superscript','subscript','strikethrough','blockquote',],)),
                ('color', blocks.CharBlock(required=False, default='#000000', max_length=40, help_text="Enter a hexdecimal color for the background e.g #000000")),
                ('text_color', blocks.CharBlock(required=False, default='#ffffff', max_length=40, help_text="Enter a hexdecimal color for the text e.g #000000 or red")),
                ('button_page', blocks.PageChooserBlock(required=False)),
                ('button_url', blocks.URLBlock(required=False)),
                ('button_text', blocks.CharBlock(required=False, default='Read More', max_length=40)),
            ]
        )
    )


    class Meta:
        template = "blocks/jumbotron_text_block.html"
        icon = "list-ul"
        label = "Heading"
        max_num = 1


class HomePageMenuBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.RichTextBlock(required=True, features=['bold','italic'])
    button_page = blocks.PageChooserBlock(required=False, target_model=['home.ServicePage'])
    button_text = blocks.CharBlock(required=False, default='Read More', max_length=40)


    class Meta:
        template = "blocks/menu_block.html"
        icon = "plus"
        label = "Menu"


class ServiceMainBlock(blocks.StructBlock):

    image = ImageChooserBlock(required=False)
    second_image = ImageChooserBlock(required=False)
    heading = blocks.CharBlock(required=True, max_length=60)
    description  = blocks.RichTextBlock(required=False, features=['h1','h2','h3','h4','h5','h6','hr','bold','italic','link',],)
    button_page = blocks.PageChooserBlock(required=False, target_model=['home.ServicePage'])
    button_text = blocks.CharBlock(required=False, default='Read More', max_length=40)
    


    class Meta:
        template = "blocks/about.html"
        label = "Main Service"
        max_num = 1


class FeatureBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.RichTextBlock(required=True, features=['bold','italic'])

    card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('title', blocks.CharBlock(required=False, max_length=40)),
                ('text', blocks.RichTextBlock(required=False, features=['h1','h2','h3','h4','h5','h6','hr','bold','italic','link','code','superscript','subscript','strikethrough','blockquote',],)),   
            ]
        )
    )

    image = ImageChooserBlock(required=False)
    second_image = ImageChooserBlock(required=False)


    class Meta:
        template = "blocks/feature.html"
        icon = "list-ul"
        label = "Work"
        max_num = 1



class TestimonialBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    title = blocks.CharBlock(required=False, max_length=60)
    text = blocks.RichTextBlock(required=True, features=['bold','italic'])
    name = blocks.CharBlock(required=False, max_length=60)


    class Meta:
        template = "blocks/testimony.html"
        icon = "plus"
        label = "Testimony"
        


class FactBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    description = blocks.RichTextBlock(required=True, features=['bold','italic'])


    class Meta:
        template = "blocks/fact.html"
        icon = "plus"
        label = "Fact"



#service index page
class ServiceIndexListBlock(blocks.StructBlock):

    jumbotron_color = blocks.CharBlock(required=False, max_length=40, help_text="Enter a hexdecimal color for the background e.g #000000")

    service_index = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('image_icon', ImageChooserBlock(required=False)),
                ('title', blocks.CharBlock(required=False, max_length=40)),
            ]
        )
    )


    class Meta:
        template = "blocks/service_index_block.html"
        icon = "list-ul"
        label = "Service"
        max_num = 1


class ClientBlock(blocks.StructBlock):

    image = ImageChooserBlock(required=False)
    heading = blocks.CharBlock(required=False, max_length=60)


    class Meta:
        template = "blocks/client_block.html"
        label = "Client"
        max_num = 1


#service page
class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    caption = blocks.CharBlock(required=False, max_length=60)


    class Meta:
        template = "blocks/image_block.html"
        icon = "plus"
        label = "Image"



class ServiceContactBlock(blocks.StructBlock):
    contact_link = blocks.PageChooserBlock(required=False, target_model=['home.FormPage'])
    text = blocks.CharBlock(required=False, default='Lets talk', max_length=60)


    class Meta:
        template = "blocks/service_contact_block.html"
        icon = "plus"
        label = "Service Contact"
        


class FAQBlock(blocks.StructBlock):
    question = blocks.CharBlock(required=True)
    answer = blocks.CharBlock(required=True, max_length=60)


    class Meta:
        template = "blocks/faq_block.html"
        icon = "plus"
        label = "FAQ"


class ServiceTestimonyBlock(blocks.StructBlock):

    jumbotron_color = blocks.CharBlock(required=False, max_length=40, default='#000000', help_text="Enter a hexdecimal color for the background e.g #000000")
    heading = blocks.CharBlock(required=True, max_length=60)
    description  = blocks.RichTextBlock(required=False, features=['h1','h2','h3','h4','h5','h6','hr','bold','italic','link',],)

    service_testimony = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('name', blocks.CharBlock(required=False, max_length=40)),
                ('description', blocks.RichTextBlock(required=False, features=['h1','h2','h3','h4','h5','h6','hr','bold','italic','link',],)),
            ]
        )
    )


    class Meta:
        template = "blocks/service_testimony_block.html"
        icon = "list-ul"
        label = "Service Testimony"
        max_num = 1



class ServiceListBlock(blocks.StructBlock):

    heading = blocks.CharBlock(required=True, default='Our Services', max_length=60)
    description  = blocks.RichTextBlock(required=False, features=['h1','h2','h3','h4','h5','h6','hr','bold','italic','link',],)
    list_item = blocks.CharBlock(required=False, max_length=40)
    image = ImageChooserBlock(required=False)


    class Meta:
        template = "blocks/service_list_block.html"
        label = "Service List"
        max_num = 1
