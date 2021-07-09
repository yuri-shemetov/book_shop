from . import models
from shop import models as shop_models
from django.views.generic import RedirectView, DetailView
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages

class CartView(DetailView):
    model = models.Cart
    template_name = 'carts/cart-edit.html'

    def get_object(self, queryset=None):
        # get cart
        cart_id = self.request.session.get('cart_id')
        cart, created = models.Cart.objects.get_or_create(
            pk=cart_id,
            defaults={}
        )
        if created:
            self.request.session['cart_id'] = cart.pk

        # get book_in_cart
        book_id = self.request.GET.get('book_id')
        if book_id:
            book = shop_models.Book.objects.get(pk=int(book_id))
            if book.quantity > 0:
                book_in_cart, book_created = models.BookInCart.objects.get_or_create(
                    cart=cart,
                    book=book,
                    defaults={
                        'unit_price': book.price
                    },
                )
                book.quantity -= 1
                book.save()
                if not book_created:
                    # prod position in the cart
                    q = book_in_cart.quantity + 1
                    book_in_cart.quantity = q
                    book_in_cart.save()
            else:
                messages.add_message(self.request, messages.INFO, f'К сожалению, книги {str(book)}, нет сейчас в наличии')

        return cart

class DeleteBook(RedirectView):
    model = models.BookInCart
    success_url = reverse_lazy('carts:cart-edit')

    def get_redirect_url(self, *args, **kwargs):
        book_id = self.request.GET.get('filter')
        book_in_cart = models.BookInCart.objects.get(pk=int(book_id))
        books = shop_models.Book.objects.all()
        for book in books:
            if book.name == book_in_cart.book.name:
                book.quantity += book_in_cart.quantity
                book.save()

        self.model.objects.get(pk=self.kwargs.get('pk')).delete()
        return self.success_url

class CartUpdate(View):
    def post(self, request):
        action = request.POST.get('submit')

        cart_id = self.request.session.get('cart_id')
        cart, created = models.Cart.objects.get_or_create(
            pk=cart_id,
            defaults={},
        )
        if created:
            self.request.session['cart_id'] = cart.pk
        books = cart.books.all()
        if books:
            for key, value in request.POST.items():
                if 'quantityforgood_' in key:
                    pk = int(key.split('_')[1])
                    book = books.get(pk=pk)
                    books_main = shop_models.Book.objects.all()
                    for book_main in books_main:
                        if book_main.name == book.book.name:
                            quantity = book_main.quantity
                            for_massage_quantity = book_main.quantity + book.quantity
                            new_quantity = quantity + book.quantity - int(value)
                            if new_quantity >= 0:
                                book_main.quantity = new_quantity
                                book_main.save()
                                book.quantity = int(value)
                                book.save()
                            else:
                                messages.add_message(self.request, messages.INFO, f'Количество книг {str(book_main)} - ограничено. Введите не более {str(for_massage_quantity)} шт. ')
        if action == 'save_cart':
            return HttpResponseRedirect(reverse_lazy('carts:cart-edit'))
        elif action == 'create_order':
            return HttpResponseRedirect(reverse_lazy('orders:create-order'))
        else:
            return HttpResponseRedirect(reverse_lazy('carts:cart-edit'))