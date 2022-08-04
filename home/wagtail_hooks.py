from wagtail.core import hooks
from wagtail.contrib.modeladmin.options import ( ModelAdmin, ModelAdminGroup, modeladmin_register)
from .models import AboutPage, ServicePage, FormPage

class AboutAdmin(ModelAdmin):
    model = AboutPage
    menu_label = 'About'
    menu_icon = 'group'
    menu_order = 150
    add_to_settings_menu = False
    exclude_from_explorer = False

modeladmin_register(AboutAdmin)


class ServiceAdmin(ModelAdmin):
    model = ServicePage
    menu_label = 'Services'
    menu_order = 130
    add_to_settings_menu = False
    exclude_from_explorer = False

modeladmin_register(ServiceAdmin)



class FormAdmin(ModelAdmin):
    model = FormPage
    menu_label = 'Contact Forms'
    menu_icon = 'list-ul'
    menu_order = 160
    add_to_settings_menu = False
    exclude_from_explorer = False

modeladmin_register(FormAdmin)
