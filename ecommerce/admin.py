from django.contrib import admin

# Register your models here.
from .models import Product, Member, ProductCompany, Cart, ProductCatergory, UserSession 

admin.site.register(Product)
admin.site.register(Member)
admin.site.register(ProductCompany)
admin.site.register(Cart)
admin.site.register(ProductCatergory)
admin.site.register(UserSession)








