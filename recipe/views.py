import json
from django.http import JsonResponse
import os
from django.conf import settings

def get_recipe_intro(request):
    data = None
    with open(os.path.join(settings.BASE_DIR, 'static/data/recipeintro.json')) as file:
        data = json.load(file)
    return JsonResponse(data)

def get_recipe_details(request):
    id = request.GET.get('id', None)
    data = None
    with open(os.path.join(settings.BASE_DIR, 'static/data/recipedetails.json')) as file:
        data = json.load(file)
    # data = JsonResponse(data)
    for recipe in data["data"]:
        if recipe["id"] == int(id):
            return JsonResponse(recipe)
    return None