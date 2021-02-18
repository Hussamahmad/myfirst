from django.forms import Form, ModelForm, TextInput, Textarea, Select
from .models import Book, Review

class BookForm(ModelForm):

    class Meta:
        model = Book
        fields = ("name", "company", "number", "price")
        widgets = {
            "name": TextInput(attrs={'class': 'form-control'}),
            "company": TextInput(attrs={'class': 'form-control'}),
            "number": TextInput(attrs={'class': 'form-control'}),
            "price": Textarea(attrs={'class': 'form-control'})
            }

class ReviewForm(ModelForm):

    class Meta:
        model = Review
        fields = ('stars', 'thoughts')
        widgets = {
            'thoughts': Textarea(attrs={'class': 'form-control'})
        }

class StarForm(ModelForm):

    class Meta:
        model = Review
        fields = ('stars',)
        labels = {
            'stars': 'by Review',
        }
        widgets = {
            'stars': Select(attrs={'class': 'search-form'})
        }
