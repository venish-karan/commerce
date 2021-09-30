from django.contrib import admin

# Register your models here.

from .models import Auction

class AuctionAdmin(admin.ModelAdmin):
    model = Auction
    list_display = ("id","title", "image", "bid", "comment","created_at","updated_at")


admin.site.register(Auction, AuctionAdmin)
