from django import forms

class ExampleForm(forms.Form):

   name= forms.CharField(max_length=20)
   comment = forms.CharField(widget=forms.Textarea)
   
