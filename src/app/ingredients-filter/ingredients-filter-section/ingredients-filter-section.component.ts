import { Component, Input } from '@angular/core';
import { IngredientWeight } from '../../shared/models/ingredient.model';

@Component({
  selector: 'app-ingredients-filter-section',
  templateUrl: './ingredients-filter-section.component.html'
})
export class IngredientsFilterSectionComponent {
  @Input() suggestions: IngredientWeight[];
  @Input() sortKey: String;
  @Input() heading: String;

  constructor() { }
}