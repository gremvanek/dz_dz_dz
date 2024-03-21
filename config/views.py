from django.db.models import Model
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import ListView

from config.models import Product, Post


def home(request):
    products = Product.objects.all()
    context = {'object_list': products}
    return render(request, 'home.html', context)


class ContactView(TemplateView):
    template_name = 'contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(
            f"Новая заявка на обратную связь:\nИмя: {name}\nТелефон: {phone}\nСообщение: {message}"
        )
        return render(request, self.template_name)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class PostView(TemplateView):
    template_name = 'create_post.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(
            f"Новая заявка на обратную связь:\nИмя: {name}\nТелефон: {phone}\nСообщение: {message}"
        )
        return render(request, self.template_name)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    template_name = 'create_view.html'
    fields = ['title', 'slug', 'content', 'preview', 'is_published']
    success_url = reverse_lazy('post_list')


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'slug', 'content', 'preview', 'is_published']
    context_object_name = 'post'
    slug_field = 'slug'
    success_url = reverse_lazy('post_list')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('post_list')


def product_detail(request, pk):
    product = get_object_or_404(Product, **{'pk': pk})
    product.increment_views()  # increment для добавления просмотров
    context = {'product': product}
    return render(request, 'product_details.html', context)
