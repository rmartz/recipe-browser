import { Component } from '@angular/core';
import { Suggestion } from '../shared/services/suggestion.service';

@Component({
  selector: 'app-recipes-display',
  templateUrl: './recipes-display.component.html'
})
export class RecipesDisplayComponent {
  constructor(public suggestion: Suggestion) { }
}
