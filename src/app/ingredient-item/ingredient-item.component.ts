import { Component, Input } from '@angular/core';
import { Ingredient } from '../shared/models/ingredient.model';

@Component({
  selector: 'app-ingredient-item',
  templateUrl: './ingredient-item.component.html'
})
export class IngredientItemComponent {
  @Input() ingredient: Ingredient;

  constructor() { }
}
