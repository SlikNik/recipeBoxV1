from django import forms
from recipes.models import Author, Recipe


class SignupForm(forms.Form):
    firstname = forms.CharField(max_length=240)
    lastname = forms.CharField(max_length=240)
    bio = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)
class AddAuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('name', 'bio', 'user')

class AddRecipeAdminForm(forms.ModelForm):

   class Meta:
        model = Recipe
        fields = ('title', 'author', 'description', 'time_required', 'instructions')

        # def __init__(self, *args, **kwargs):
        #     author = kwargs.pop('author', None)
        #     super(ArticleForm, self).__init__(*args, **kwargs)
        #     if not request.user.is_staff:
        #         del self.fields['author']

class AddRecipeForm(forms.ModelForm):

   class Meta:
        model = Recipe
        fields = ('title', 'description', 'time_required', 'instructions')
