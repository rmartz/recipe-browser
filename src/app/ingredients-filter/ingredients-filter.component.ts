import { Component } from '@angular/core';
import { Suggestions } from '../shared/services/suggestion.service';

@Component({
  selector: 'app-ingredients-filter',
  templateUrl: './ingredients-filter.component.html'
})
export class IngredientsFilterComponent {
  constructor(public suggestions: Suggestions) { }
}
