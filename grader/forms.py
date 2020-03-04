from django import forms

from .models import Solution


class SolutionForm(forms.ModelForm):
    file = forms.FileField(label='File')

    class Meta:
        model = Solution
        fields = ('file',)
