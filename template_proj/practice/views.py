from django.views.generic import TemplateView
import datetime

from django.views.generic import TemplateView

class FilterView(TemplateView):
    template_name = 'practice/filters.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = 'Webucator'
        context['url'] = 'https://www.webucator.com'
        context['moon_landing'] = datetime.datetime(
            year=1969, month=7, day=21,
            hour=2, minute=56, second=15,
            tzinfo=datetime.timezone.utc
        )
        context['launch_date'] = datetime.datetime(
    year=1969, month=7, day=16, hour=13, minute=32, second=0,
    tzinfo=datetime.timezone.utc
)
        context['century22'] = datetime.datetime(
    year=2100, month=1, day=1, tzinfo=datetime.timezone.utc
)
        context['inventory'] = {
    'gloves': 0,
    'hats': 51,
    'scarves': 2,
    'socks': 13
}
        
        context['classes'] = {
    'Python': [
        'Introduction to Python', 'Advanced Python',
        'Data Science', 'Django'
    ],
    'Databases': [
        'Introduction to PostgreSQL', 'Introduction to MySQL',
        'Introduction to SQL Server', 'Introduction to Oracle'
    ],
    'Web': [
        'HTML', 'CSS', 'JavaScript'
    ],
    'XML': [
        'Introduction to XML'
    ]
}
        
        context['blurb'] = '<p>You are <em>pretty</em> smart!</p>'

        context['inventory'] = {
    'gloves': 0,
    'hats': 51,
    'scarves': 2,
    'socks': 13
}
        
        context['colors'] = [
    'Red', 'Green', 'Blue', 'Orange', 'Purple', 'Yellow', 'Pink'
]

        context['files'] = [
    {
        'filename': 'macOS 64-bit installer',
        'filesize': 29163525
    },
    {
        'filename': 'Windows x86-64 executable installer',
        'filesize': 26797616
    },
    {
        'filename': 'Windows x86-64 web-based installer',
        'filesize': 1348896
    }
]
        context['user_blurb'] = """Shucks! What a cruddy day I\'ve had.
        I spent the whole darn day with my dirtiest
        friend darning his STINKY socks."""
        return context
    

class HomePageView(TemplateView):
    template_name = 'home.html'

class TagView(TemplateView):
    template_name = 'practice/tags.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['beatles'] = [
            {'firstname': 'Paul', 'lastname': 'McCartney'},
            {'firstname': 'John', 'lastname': 'Lennon'},
            {'firstname': 'George', 'lastname': 'Harrison'},
            {'firstname': 'Ringo', 'lastname': 'Starr'},
        ]
        
        return context