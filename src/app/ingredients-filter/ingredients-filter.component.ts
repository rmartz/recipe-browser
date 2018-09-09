import { Component } from '@angular/core';
import { Suggestions } from '../shared/services/suggestion.service';
import { IngredientWeight } from '../shared/models/ingredient.model';

@Component({
  selector: 'app-ingredients-filter',
  templateUrl: './ingredients-filter.component.html'
})
export class IngredientsFilterComponent {
  constructor(public suggestions: Suggestions) { }

  public isBlacklisted(suggestion: IngredientWeight) {
    return suggestion.ingredient.blacklisted;
  }

  public isFavorited(suggestion: IngredientWeight) {
    return suggestion.ingredient.favorited;
  }

  public isCommon(suggestion: IngredientWeight) {
    return !suggestion.ingredient.favorited && (suggestion.weight === 0) && (suggestion.occurrences > 0);
  }

  public isSuggestion(suggestion: IngredientWeight) {
    return !suggestion.ingredient.favorited && suggestion.weight > 0;
  }

}
