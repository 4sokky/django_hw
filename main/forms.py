from django import forms
from . import models


class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Articles
        fields = ('title', 'body', 'article_subject', 'image', 'created_by')     # TODO: Don't need to choose user
        # TODO: Fix img upload with form