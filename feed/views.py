from django.shortcuts import render, redirect
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostForm,YorumForm
from .models import Post, Yorum,Tags

@login_required(login_url="login_page")
def home_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)    
            post.user = request.user 
            tags = Tags.objects.get_or_create(title = post.title)
            post.save()
            
            
            print(post.tags.add(tags[0]))
            return redirect('home_page')

    else:
        form = PostForm()

    # Tüm postları çek
    posts = Post.objects.all()
    hashtags = Post.objects.values('title','slug').annotate(title_count=Count('title')).order_by('-title_count')
    deneme = Tags.objects.all()
    return render(request, 'feed/home.html', {
        "form": form,
        "posts": posts,
        'hashtags':deneme
    })


def post_detay_view(request, post_slug):
    print(post_slug)
    post = get_object_or_404(Post, slug=post_slug)

    if request.method == 'POST':
        yorum_form = YorumForm(request.POST)

        if yorum_form.is_valid():
            yorum = yorum_form.save(commit=False)
            yorum.post = post
            yorum.author = request.user 
            yorum.save()
            return redirect('post_detay_page', post_slug=post.slug)
    else:
        yorum_form = YorumForm()


    yorumlar = Yorum.objects.filter(post = post)
    hashtags = Post.objects.values('title').annotate(title_count=Count('title')).order_by('-title_count')
    deneme = Tags.objects.all()

    # print(hashtags)
    # print(tags_counts)
    return render(request, 'feed/post-detay.html', {'post': post, 'yorum_form': yorum_form, 'yorumlar': yorumlar,'hashtags':deneme})



def hashtag_detay_view(request,hashtag_slug):
    
    tag = Tags.objects.get(slug = hashtag_slug)
    posts = posts = Post.objects.filter(tags = tag)
    all_tags = Tags.objects.all()

    return render(request,'feed/hashtags-detay.html',{'posts':posts,"hashtags":all_tags})


def post_edit_view(request,post_slug):
    post = Post.objects.get(slug = post_slug)

    if(request.method == 'POST'):
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home_page')
        else:
            return render(request,'feed/post-edit.html',{
                'form':form,
                'post':post
            })
        
    form = PostForm(instance = post)
    return render(request,'feed/post-edit.html',{
        'form':form,
        'post':post
    })



def yorum_detay_view(request,yorum_slug):
    yorum = get_object_or_404(Yorum, slug=yorum_slug)
    return render(request, 'feed/yorum-detay.html', {'yorum': yorum})


def yorum_edit_view(request,yorum_slug):
    yorum = Yorum.objects.get(slug = yorum_slug)
    if request.method == 'POST':
        form = YorumForm(request.POST,request.FILES, instance = yorum)
        if form.is_valid():
            yorum = form.save(commit=False)
            yorum.author = request.user
            yorum.save()
            return redirect('home_page')
        else:
            return render(request,'feed/yorum-edit.html',{
                'form':form,
                'yorum':yorum
            })
    
    form = YorumForm(instance=yorum)

    return render(request,'feed/yorum-edit.html',{
        'form':form,
        'yorum':yorum
    })


def post_delete_view(request,post_slug):
    post = Post.objects.get(slug = post_slug)
    if request.method == 'POST':
        post.delete()
        return redirect('home_page')
    else:
        return render(request,'feed/post-delete.html',{'post':post})
    



def yorum_delete_view(request,yorum_slug):
    yorum = Yorum.objects.get(slug = yorum_slug)
    if request.method == 'POST':
        yorum.delete()
        return redirect('home_page')
    else:
        return render(request,'feed/yorum-delete.html',{'yorum':yorum})