from django.shortcuts import render, redirect
from .models import Category, FoodItem
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from .forms import CategoryForm, FoodItemForm

def home_view(request):
    # ดึงข้อมูลวัตถุดิบที่หมดอายุแล้ว
    today = timezone.now().date()
    expired_items = FoodItem.objects.filter(expiry_date__lt=today)
    expired_count = expired_items.count()

    return render(request, 'home.html', {
        'expired_count': expired_count,
        'expired_items': expired_items,
    })

def manage_food(request):
    categories = Category.objects.all()
    food_items = FoodItem.objects.all()
    return render(request, 'manage_food.html', {
        'categories': categories,
        'food_items': food_items
    })

# ฟังก์ชันเพิ่ม Category
def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            category, created = Category.objects.get_or_create(name=name)
            if created:
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': 'Category already exists'})
    return JsonResponse({'success': False, 'error': 'Invalid request'})

# ฟังก์ชันเพิ่ม Food Item
def add_food_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category_id = request.POST.get('category')
        expiry_date = request.POST.get('expiry_date')

        try:
            category = Category.objects.get(id=category_id)
            FoodItem.objects.create(name=name, category=category, expiry_date=expiry_date)
            return JsonResponse({'success': True})
        except Category.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Category does not exist'})
    return JsonResponse({'success': False, 'error': 'Invalid request'})

# ฟังก์ชันลบ Food Item
def delete_food_item(request, pk):
    try:
        item = FoodItem.objects.get(pk=pk)
        item.delete()
        return JsonResponse({'success': True})
    except FoodItem.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Item does not exist'})


