import { Component } from '@angular/core';
import { Suggestions } from '../shared/services/suggestion.service';
import { IngredientWeight } from '../shared/models/ingredient.model';

@Component({
  selector: 'app-ingredients-filter',
  templateUrl: './ingredients-filter.component.html'
})
export class IngredientsFilterComponent {
  constructor(public suggestions: Suggestions) { }

  public isRated(suggestion: IngredientWeight) {
    return suggestion.ingredient.blacklisted || suggestion.ingredient.favorited;
  }

  public isSuggestion(suggestion: IngredientWeight) {
    return (!suggestion.ingredient.favorited
            && (suggestion.occurrences > 0));
  }
}
