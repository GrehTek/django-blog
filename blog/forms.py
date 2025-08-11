from django import forms
from .models import BlogPost, BlogComment, BlogLike

class BlogPostForm(forms.ModelForm):
  class Meta:
    model = BlogPost
    fields = '__all__'
    exclude = ['blogpost_created_at', 'blogpost_user', 'blogpost_likes', 'blogpost_comments', 'blogpost_shares']

class BlogCommentForm(forms.ModelForm):
  class Meta:
    model = BlogComment
    fields = ['post_id', 'comment']

class BlogLikesForm(forms.ModelForm):
  class Meta:
    model = BlogLike
    fields = ['post_id']