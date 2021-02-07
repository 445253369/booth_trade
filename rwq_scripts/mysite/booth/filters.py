import django_filters
from .models import *


class BoothFilter(django_filters.FilterSet):
    """
    摊位过滤器
    """

    class Meta:
        model = Booth
        # fields = ['name', 'location', 'price', 'area']
        fields = {
            'name': ['contains'],
            'position': ['contains', ],
            'area': ['lt', 'gt'],
            'price': ['lt', 'gt'],

        }

        @property
        def qs(self):
            parent = super().qs
            # author = getattr(self.request, 'user', None)
            return parent.exclude(status='rented')