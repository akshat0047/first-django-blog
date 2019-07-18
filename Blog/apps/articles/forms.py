from django.forms import ModelForm
from .models import Post

# Create the form class.
class ArticleForm(ModelForm):
     class Meta:
         model = Post
         fields = [ 'title', 'text', 'created_date']

     def clean(self):
        cleaned_data = super(ArticleForm, self).clean()
