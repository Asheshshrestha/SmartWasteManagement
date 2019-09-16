from django import forms
from blogs.models import Blogs


class BlogCreationForm(forms.ModelForm):
    cover_image = forms.ImageField(required=False)
    class Meta:
        model = Blogs
        fields = ("title", "article","cover_image")


