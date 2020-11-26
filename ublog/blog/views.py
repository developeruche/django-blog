from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditPostForm, MakeCommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# def home(request):
#     return render(request, 'home.html', {

#     })


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context


class ArticleDetailViews(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(ArticleDetailViews,
                        self).get_context_data(*args, **kwargs)
        tl = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = tl.total_likes()

        liked = False
        if tl.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['category_menu'] = category_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'


class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_catergory.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = EditPostForm


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


def CategoryView(request, categorys):
    category_posts = Post.objects.filter(category=categorys.replace('-', ' '))
    return render(request, 'catergories.html', {
        'categorys': categorys.title().replace('-', ' '),
        'category_posts': category_posts
    })


def CategoryListView(request):
    category_menu_list = Category.objects.all()
    return render(request, 'catergories_list.html', {
        'category_menu_list': category_menu_list
    })


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))


class AddCommentView(CreateView):
    model = Comment
    form_class = MakeCommentForm
    template_name = 'add_comments.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)
