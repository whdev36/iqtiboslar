from django.contrib import admin
from .models import Quote, Author

# Register
admin.site.register(Author)
admin.site.register(Quote)
