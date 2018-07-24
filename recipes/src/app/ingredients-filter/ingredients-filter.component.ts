import { Component } from '@angular/core';
import { Ingredients } from '../shared/services/ingredients.service';

@Component({
  selector: 'app-ingredients-filter',
  templateUrl: './ingredients-filter.component.html'
})
export class IngredientsFilterComponent {
  constructor(public ingredients: Ingredients) { }
}
