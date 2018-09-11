import { Component } from '@angular/core';
import { Suggestions } from '../shared/services/suggestion.service';
import { Ingredients } from '../shared/services/ingredients.service';
import { Recipes } from '../shared/services/recipes.service';
import { RecipeWeight } from '../shared/models/recipe.model';

@Component({
  selector: 'app-recipes-display',
  templateUrl: './recipes-display.component.html'
})
export class RecipesDisplayComponent {
  constructor(public suggestions: Suggestions,
              public ingredients: Ingredients,
              public recipes: Recipes) { }

  public isSuggested(suggestion: RecipeWeight) {
    return suggestion.weight > 0;
  }
}
