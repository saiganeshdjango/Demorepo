from django import forms
from testapp.models import Movie
class MovieForm(forms.ModelForm):
    # rdate = forms.DateField()
    # moviename = forms.CharField()
    # hero = forms.CharField()
    # heroine = forms.CharField()
    # rating = forms.IntegerField()
    class Meta:
        model = Movie
        fields='__all__'
