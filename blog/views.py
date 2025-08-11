from django.shortcuts import render, redirect
from .models import BlogPost, BlogComment, BlogLike
from .forms import BlogPostForm, BlogCommentForm
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse
import json

# Create your views here.
def home(request):

  blogposts = BlogPost.objects.all().order_by('-blogpost_created_at')

  current_user = request.user

  if request.method == 'POST':
    pk = request.POST['pk']
    post = BlogPost.objects.get(pk=pk)

    post.delete()
    messages.success(request, "Post deleted")
    return redirect('bloghome')  

  return render(request, 'index.html', {'timestamp': timezone.now().timestamp(),'current_user': current_user, 'blogposts':blogposts})

def edit_blogpost(request, pk):
  blogpost = BlogPost.objects.get(pk=pk)

  if request.method == 'POST':
    form = BlogPostForm(request.POST, instance=blogpost)
    if form.is_valid():
      form.save()
      messages.success(request, 'Blog post updated successfully!')
      return redirect('bloghome')
    else:
      messages.warning(request, "Unable to update post")
      return redirect('edit_blogpost')
  else:
    form = BlogPostForm(instance=blogpost)

  return render(request, 'edit-post.html', {'form': form, 'blogpost': blogpost})


def delete_blogpost(request, pk):
  post = BlogPost.objects.get(pk=pk)

  if request.method == 'POST':
    post.delete()
    messages.success(request, "Post Deleted Successfully")
    return redirect('bloghome')
  else:
    message.error(request, "Unable to delete blog post")
  
  return render(request, 'bloghome')


def receive_data(request):
  if request.method == 'POST':
    data = json.loads(request.body)
    avatar = data.get('avatar')

    # check if current user already liked post
    current_user = request.user
    blog_likes = BlogLike.objects.filter(user=current_user, post_id=avatar)

    print(current_user)

    # unlike if current user already liked post

    # get current likes count

    # update avatar
    if not blog_likes:
      blog_likes_add = BlogLike(post_id=avatar)
      blog_likes_add.save()

      likes = BlogPost.objects.get(id=avatar)    
      likes.blogpost_likes += 1
      likes.save()  
      return JsonResponse({'new_avatar': f"{likes.blogpost_likes}"})
      return redirect('bloghome')
    else:
      # unlike post
      blog_likes.delete()
  return JsonResponse({'error: invalid'}, status=400)


def blog_comment(request, pk):

  post = BlogPost.objects.get(pk=pk)
  # fetch all comments previously made on post
  comments = BlogComment.objects.all()

  if request.method == 'POST':
    comment = request.POST.get('comment')
    post_id = request.POST.get('post_id')
    
    form = BlogCommentForm(request.POST)

    if form.is_valid():
      form.save()
      messages.success(request, "Comment added")
      return redirect('blog_comment', pk=pk)

    # blogcomment = BlogComment(post_id=post_id, comment=comment)
    # blogcomment.save()
    # messages.success(request, "Comment added!!!")
    # return redirect('bloghome')    

  return render(request, 'blog-comment.html', {'post': post, 'comments':comments})