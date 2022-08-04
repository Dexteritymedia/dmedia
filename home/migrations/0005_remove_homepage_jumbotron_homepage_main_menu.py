# Generated by Django 4.0.2 on 2022-07-31 16:53

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homepage_fact_alter_homepage_service_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='jumbotron',
        ),
        migrations.AddField(
            model_name='homepage',
            name='main_menu',
            field=wagtail.core.fields.StreamField([('jumbotron', wagtail.core.blocks.StructBlock([('jumbotron', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(max_length=40, required=False)), ('description', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'bold', 'italic', 'link', 'code', 'superscript', 'subscript', 'strikethrough', 'blockquote'], required=False)), ('color', wagtail.core.blocks.CharBlock(default='#000000', help_text='Enter a hexdecimal color for the background e.g #000000', max_length=40, required=False)), ('text_color', wagtail.core.blocks.CharBlock(default='#ffffff', help_text='Enter a hexdecimal color for the text e.g #000000 or red', max_length=40, required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(default='Read More', max_length=40, required=False))])))])), ('menu', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=60, required=True)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic'], required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(page_type=['home.ServicePage'], required=False)), ('button_text', wagtail.core.blocks.CharBlock(default='Read More', max_length=40, required=False))])), ('service', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('second_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('heading', wagtail.core.blocks.CharBlock(max_length=60, required=True)), ('description', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'bold', 'italic', 'link'], required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(page_type=['home.ServicePage'], required=False)), ('button_text', wagtail.core.blocks.CharBlock(default='Read More', max_length=40, required=False))])), ('work', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=60, required=True)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic'], required=True)), ('card', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=40, required=False)), ('text', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'bold', 'italic', 'link', 'code', 'superscript', 'subscript', 'strikethrough', 'blockquote'], required=False))]))), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('second_image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('testimony', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(max_length=60, required=False)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic'], required=True)), ('name', wagtail.core.blocks.CharBlock(max_length=60, required=False))])), ('fact', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('description', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic'], required=True))]))], blank=True, null=True),
        ),
    ]
