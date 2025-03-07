# Django Utility Suite

## Description
`django_utility_suite` is a set of utilities to enhance Django development


## Installation

You can install this package with:

```bash
pip install django-utility-suite
```

Or if you use Poetry:

```bash
poetry add django-utility-suite
```

## Usage

### Django Configuration
Add `django_utility_suite` to `INSTALLED_APPS` in your `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'django_utility_suite',
]
```

## Package utils
### 1. Performance optimization and cache management.

#### Using `ReadOnlyViewSetMixin`
This mixin provides an optimized way to handle caching in read-only views.

```python
from django_utility_suite.api.mixins import ReadOnlyViewSetMixin
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelViewSet(ReadOnlyViewSetMixin, ReadOnlyModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    
    def get_cache_key(self):
        if self.action == "retrieve":
            return f"mimodel-retrieve-{self.lookup_field}"
        elif self.action == "list":
            return f"mimodel-list"
    
    @property
    def cache_prefix(self):
        return "my_model"
```

## Development
If you want to contribute, clone the repository and use Poetry to manage dependencies:

```bash
git clone https://github.com/yourusername/django-utility-suite.git
cd django-utility-suite
poetry install
```

## License
This project is licensed under the MIT license.
