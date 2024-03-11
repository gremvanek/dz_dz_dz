from django.shortcuts import render, get_object_or_404

from config.models import Product


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(
            f"Новая заявка на обратную связь:\nИмя: {name}\nТелефон: {phone}\nСообщение: {message}"
        )
    return render(request, 'contacts.html')


def product_detail(request, pk):
    # Используем get_object_or_404 для загрузки продукта по PK или возвращения 404 ошибки, если продукт не найден
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'app_name/product_detail.html', context)
