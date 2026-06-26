from django.contrib import admin
from .models import Category, Expense , User
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "amount",
        "date",
        "category"
    ]
    search_fields = [
        "title",
        "description"
    ]
    list_filter = [
        "category",
        "date"
    ]
    ordering = [
        "-date"
    ]


admin.site.register(User)