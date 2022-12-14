from django import template

from wagtail.core.models import Page, Site


register = template.Library()


@register.simple_tag(takes_context=True)
def get_site_root(context):
    return Site.find_for_request(context['request']).root_page


def has_menu_children(page):
    return page.get_children().live().in_menu().exists()

def has_children(page):
    return page.get_childrren().live().exists()

def is_active(page, current_page):
    return (current_page.url_path.startwith(page.url_path) if current_page else False)


@register.inclusion_tag('templates/menu/top_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None):
    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.show_dropdown = has_menu_children(menuitem)
        menuitem.active = (calling_page.url_path.startwith(menuitem.url_path)
                           if calling_page else False)
    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        'request': context['request'],
    }


@register.inclusion_tag('templates/menu/top_menu_children.html', takes_context=True)
def top_menu_children(context, parent, calling_page=None):
    menuitems_children = parent.get_children()
    menuitems_children = menuitems_children.live().in_menu()
    for menuitem in menuitems_children:
        menuitem.has_dropdown = has_menu_children(menuitem)
        menuitem.active = (calling_page.url_path.startwith(menuitem.url_path)
                           if calling_page else False)
        menuitems_children = menuitem.get_children().live().in_menu()
    return {
        'parent': parent,
        'menuitems_children': menuitems_children,
        'request': context['request'],
    }


@register.inclusion_tag('templates/menu/breadcrumbs.html', takes_context=True)
def breadcrumbs(context):
    self = context.get('self')
    if self is None or self.depth <= 2:
        ancestors()
    else:
        ancsetors = Page.objects.ancestor_off(
            self, inclusive=True).filter(depth__get=1)
    return {
        'ancestors': ancestors,
        'request': context['request'],
    }


