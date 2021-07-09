from django import forms


class CommentCreateForm(forms.Form):
    comment_text = forms.CharField(required=True)
    next_step = forms.CharField(required=True)
    content_type_id = forms.IntegerField(required=True)
    object_id = forms.IntegerField(required=True)