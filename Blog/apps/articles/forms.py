from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
from .models import Post
from django.utils import timezone

class ArticleForm(ModelForm):
     class Meta:
         model = Post
         fields = ['title', 'text', 'published_date']
         widgets = {
            'title': TextInput(attrs={'class': 'title-input', 'placeholder': 'Blog Heading..'}),
            'text': Textarea(attrs={'id': 'markdown-input', 'placeholder': 'Once upon a time...'}),
            'published_date': DateTimeInput(attrs={
                'class': 'form-control datetime-picker', 
                'placeholder': 'Select publish date and time (optional)',
                'type': 'datetime-local'
            }),
        }

     def clean_published_date(self):
        published_date = self.cleaned_data.get('published_date')
        if not published_date:
            return timezone.now()  # Set current time if no date is provided
        return published_date
