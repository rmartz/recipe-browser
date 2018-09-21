import { PipeTransform, Pipe } from '@angular/core';
import { IngredientWeight, Ingredient } from '../models/ingredient.model';

@Pipe({
    name: 'toIngredient',
    pure: false
})
export class ToIngredientPipe implements PipeTransform {
    transform(items: IngredientWeight[]): Ingredient[] {
        return items.map(item => item.ingredient);
    }
}
