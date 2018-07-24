import { Component } from '@angular/core';
import { Recipes } from '../shared/services/recipes.service';

@Component({
  selector: 'app-recipes-display',
  templateUrl: './recipes-display.component.html'
})
export class RecipesDisplayComponent {
  constructor(public recipes: Recipes) { }
}
