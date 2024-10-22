from store.models import Product,Profile

class Cart():
    def __init__(self,request):
        self.session = request.session
        # Get request
        self.request = request
        # Get the current session if it exists
        cart = self.session.get('session_key')

        # If the user is new,no session key,create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] ={}
        
        # make sure cart is available on all pages of site
        self.cart = cart

    def db_add(self,product,quantity):
        product_id = str(product)
        product_qty = str(quantity)
        #Logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price':str(product.price)}
            self.cart[product_id] = int(product_qty)
        self.session.modified = True

        #Deal with logged in user
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            #{'3':1,'4':2} -> {"3":1,"4":2}
            carty = str(self.cart) # "{'3':1,'4':2}"
            carty = carty.replace("\'","\"")

            #save carty to the profile model
            current_user.update(old_cart=str(carty))

    def add(self,product,quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        #Logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price':str(product.price)}
            self.cart[product_id] = int(product_qty)
        self.session.modified = True

        #Deal with logged in user
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            #{'3':1,'4':2} -> {"3":1,"4":2}
            carty = str(self.cart) # "{'3':1,'4':2}"
            carty = carty.replace("\'","\"")

            #save carty to the profile model
            current_user.update(old_cart=str(carty))




    def __len__(self):
        return len(self.cart)
    

    def get_prods(self):
        # Get ids from cart
        product_ids = self.cart.keys()
        # Use ids to lookup products in database model
        products = Product.objects.filter(id__in=product_ids)

        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self,product,quantity):
        product_id = str(product)
        product_qty = int(quantity)

        #get cart
        ourcart = self.cart
        #update Dictionary/cart
        ourcart[product_id] = product_qty

        self.session.modified = True

        

        # Deal with logged in user
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            #{'3':1,'4':2} -> {"3":1,"4":2}
            carty = str(self.cart) # "{'3':1,'4':2}"
            carty = carty.replace("\'","\"")

            #save carty to the profile model
            current_user.update(old_cart=str(carty))


        thing = self.cart
        return thing
    
    def delete(self,product):
        # {'4':3,'1':2}
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True
        # Deal with logged in user
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            #{'3':1,'4':2} -> {"3":1,"4":2}
            carty = str(self.cart) # "{'3':1,'4':2}"
            carty = carty.replace("\'","\"")

            #save carty to the profile model
            current_user.update(old_cart=str(carty))

    def cart_total(self):
        # Get product ids
        product_ids = self.cart.keys()
        # looking for those keys in our product model
        products = Product.objects.filter(id__in=product_ids)
        quantities = self.cart
        #start counting from 0
        total = 0
        for key,value in quantities.items():
            # Convert the key string into int so we do math operations
            key=int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)
        return total
