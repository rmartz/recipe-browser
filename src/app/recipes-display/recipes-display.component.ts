import { Component } from '@angular/core';
import { Suggestions } from '../shared/services/suggestion.service';

@Component({
  selector: 'app-recipes-display',
  templateUrl: './recipes-display.component.html'
})
export class RecipesDisplayComponent {
  constructor(public suggestions: Suggestions) { }
}
