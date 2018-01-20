from collections import Counter
from itertools import chain, combinations
from operator import itemgetter

from django.core.management.base import BaseCommand

from recipes.models import Recipe, Ingredient


def remainder(iterator):
    # Iterate through a sequence emitting each item with all subsequent items
    l = list(iterator)
    for pos, val in enumerate(l):
        yield val, l[pos + 1:]


def find_optimal_subset(size, sets):
    def parse_subsets(prefix, innersets):
        for subset, rest in remainder(innersets):
            combined = prefix | subset
            if len(combined) > size:
                continue
            yield combined, 1

            for subset, count in parse_subsets(combined, rest):
                yield subset, count + 1

    # Remove any sets that trivially can not match
    filtered_counts = [set(subset) for subset in sets if len(subset) <= size]
    if not filtered_counts:
        raise Exception("No results found")

    subsets = parse_subsets(set([]), filtered_counts)

    return max(subsets, key=itemgetter(1))


class Command(BaseCommand):
    def handle(self, *args, **options):
        recipes = Recipe.objects.all().prefetch_related('ingredients')
        sets = [set(recipe.ingredients.all().values_list('id', flat=True)
                    .order_by('id'))
                for recipe in recipes]

        for size in range(2, 11):
            try:
                ingredients, count = find_optimal_subset(size, sets)

                print size, count, ', '.join(Ingredient.objects.filter(id__in=ingredients).values_list('label', flat=True))
            except Exception as e:
                print size, e
