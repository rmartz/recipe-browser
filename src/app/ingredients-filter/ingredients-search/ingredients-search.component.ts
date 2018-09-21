import { Component, Input } from '@angular/core';
import { Ingredients } from '../../shared/services/ingredients.service';

@Component({
  selector: 'app-ingredients-search',
  templateUrl: './ingredients-search.component.html'
})
export class IngredientsSearchComponent {

  public search_string = '';

  constructor(public ingredients: Ingredients) { }
}
