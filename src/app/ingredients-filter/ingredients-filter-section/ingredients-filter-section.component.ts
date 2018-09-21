import { Component, Input } from '@angular/core';
import { Ingredient } from '../../shared/models/ingredient.model';

@Component({
  selector: 'app-ingredients-filter-section',
  templateUrl: './ingredients-filter-section.component.html'
})
export class IngredientsFilterSectionComponent {
  @Input() ingredients: Ingredient[];

  public viewport = 5;

  constructor() { }

  public expand() {
    this.viewport = undefined;
  }

  public shrink() {
    this.viewport = 5;
  }
}
