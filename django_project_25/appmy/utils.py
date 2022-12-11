main_menu = [
    {'title': 'About site', 'url_name': 'about'},
    {'title': 'Feedback', 'url_name': 'feedback'},
    {'title': 'Add your post', 'url_name': 'add_post'},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['main_menu'] = main_menu
        return context
