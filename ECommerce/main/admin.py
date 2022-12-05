from django.contrib import admin
from .models import Banner,Category,Brand,Color,Size,Product,ProductAttribute,CartOrder,CartOrderItems,ProductReview,Wishlist,UserAddressBook

""" Registro en admin de Marcas """
admin.site.register(Brand)
""" Registro en admin de Tallas """
admin.site.register(Size)

""" Registro en admin de los Banners """
class BannerAdmin(admin.ModelAdmin):
	list_display=('alt_text','image_tag')
admin.site.register(Banner,BannerAdmin)

""" Registro en admin de las Categorías """
class CategoryAdmin(admin.ModelAdmin):
	list_display=('title','image_tag')
admin.site.register(Category,CategoryAdmin)

""" Registro en admin de los colores """
class ColorAdmin(admin.ModelAdmin):
	list_display=('title','color_bg')
admin.site.register(Color,ColorAdmin)

""" Registro en admin de los Productos """
class ProductAdmin(admin.ModelAdmin):
    list_display=('id','title','category','brand','status','is_featured')
    list_editable=('status','is_featured')
admin.site.register(Product,ProductAdmin)

""" Registro en admin de los Atributos de los Productos """
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display=('id','image_tag','product','price','color','size')
admin.site.register(ProductAttribute,ProductAttributeAdmin)

""" Registro en admin de las Ordenes """
class CartOrderAdmin(admin.ModelAdmin):
	list_editable=('paid_status','order_status')
	list_display=('user','total_amt','paid_status','order_dt','order_status')
admin.site.register(CartOrder,CartOrderAdmin)

""" Registro en admin de Artículos del Carrito """
class CartOrderItemsAdmin(admin.ModelAdmin):
	list_display=('invoice_no','item','image_tag','qty','price','total')
admin.site.register(CartOrderItems,CartOrderItemsAdmin)

""" Registro en admin de las Reviews """
class ProductReviewAdmin(admin.ModelAdmin):
	list_display=('user','product','review_text','get_review_rating')
admin.site.register(ProductReview,ProductReviewAdmin)

""" Registro en admin de Listas de Deseos """
admin.site.register(Wishlist)

""" Registro en admin de Direcciones """
class UserAddressBookAdmin(admin.ModelAdmin):
	list_display=('user','address','status')
admin.site.register(UserAddressBook,UserAddressBookAdmin)