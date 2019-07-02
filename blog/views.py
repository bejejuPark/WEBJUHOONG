from django.shortcuts import render
from .models import Post, Category
from django.views.generic import ListView, DetailView

class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)  # 왜 쓰는 진 모르지만 써야하는 형식적인 함수
        context['category_list'] = Category.objects.all()  # 카테고리를 다 가져옴
        context['posts_without_category'] = Post.objects.filter(category=None).count()  # 가려서 context[]에 넣어줌

        return context

    # def index(request):
    #     posts = Post.objects.all()
    #
    #     return render(
    #         request,
    #         'blog/index.html',
    #         {
    #             'posts':posts,
    #         }
    #     )

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)  # 왜 쓰는 진 모르지만 써야하는 형식적인 함수
        context['category_list'] = Category.objects.all()  # 카테고리를 다 가져옴
        context['posts_without_category'] = Post.objects.filter(category=None).count()  # 가려서 context[]에 넣어줌

        return context

    # def post_detail(requset, pk):
    #     blog_post = Post.objects.get(pk=pk)
    #
    #     return render(
    #         requset,
    #         'blog/post_detail.html',
    #         {
    #             'blog_post':blog_post
    #         }
    #     )


class PostListByCategory(ListView):

    def get_queryset(self):
        slug = self.kwargs['slug']

        if slug == '_none':
            category = None
        else:
            category = Category.objects.get(slug=slug)

        return Post.objects.filter(category=category).order_by('-created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(type(self), self).get_context_data(**kwargs)  # 왜 쓰는 진 모르지만 써야하는 형식적인 함수
        context['category_list'] = Category.objects.all()  # 카테고리를 다 가져옴
        context['posts_without_category'] = Post.objects.filter(category=None).count()  # 가려서 context[]에 넣어줌

        slug = self.kwargs['slug']

        if slug == '_none':
            context['category'] = '미분류'
        else:
            category = Category.objects.get(slug=slug)
            context['category'] = category

        # context['title'] = 'Blog - {}'.format(category.name)
        return context

