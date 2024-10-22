from .cart import Cart

# create context processors so our cart  can work on all pages
def cart(request):
    # Return the default data from the cart
    return {'cart':Cart(request)}