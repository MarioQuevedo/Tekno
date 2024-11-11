class Cart():
    def __init__(self,request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart
        

    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True
        
    def add(self,product):
        if str(product.id_producto) not in self.cart.keys():
            self.cart[product.id_producto] = {
                "product_id" : product.id_producto,
                "name" : product.nombre,
                "quantity" : 1,
                "price" : float(product.precio),
                "image" : product.imagen.url
            }
        else:
            for key, value in self.cart.items():
                if key == str(product.id_producto):
                    value["quantity"] = value["quantity"] + 1
                    break
        self.save()
        
    
    def remove(self, product):
        product_id = str(product.id_producto)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    def decrement(self,product):
        for key, value in self.cart.items():
            if key == str(product.id_producto):
                value["quantity"] = value["quantity"] - 1
                if value["quantity"] < 1:
                    self.remove(product)
                else:
                    self.save()
                break
            else:
                print("El producto no existe en el carrito")

    def clear(self):
        self.session["cart"] = {}
        self.session.modified = True