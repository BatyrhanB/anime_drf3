from django.conf import settings
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from .models import User

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def get_recipes_without_cache():
    return list(User.objects.prefetch_related('ingredient_set__food'))


def get_recipes_with_cache():
    if 'recipes' in cache:
        recipes = cache.get('recipes')
    else:
        recipes = list(User.objects.prefetch_related('ingredient_set__food'))
        cache.set('recipes', recipes, timeout=CACHE_TTL)
    return recipes  