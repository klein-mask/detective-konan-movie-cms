from django import forms
from app.models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'release_date', 'income', )

class SampleChoiceForm(forms.Form):
	CHOICE = (
		('release_date', '公開日'),
		('income', '興行収入'),
	)
	select = forms.fields.ChoiceField(required=True,
									choices=CHOICE,
									initial=['release_date'],
									widget=forms.widgets.Select(attrs={
										'class': 'round',
										'placeholder': 'Sort'
									}))