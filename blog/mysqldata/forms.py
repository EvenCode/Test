from django import forms
from django.db import models

class userform(forms.Form):

	name = forms.CharField(max_length = 50)
	blog_title = forms.CharField(max_length = 200)
	blog_description = forms.CharField(max_length = 2000)