from django import forms
from .models import user_comment

class CommentForm(forms.ModelForm):
	class Meta:
		model = user_comment
		fields = ('user_name', 'comment')