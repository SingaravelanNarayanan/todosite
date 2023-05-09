from django import forms
from .models import Todo
# from todo.forms import TodoForm

class TodoForm(forms.ModelForm):
	class Meta:
		model = Todo
		fields = "__all__"
