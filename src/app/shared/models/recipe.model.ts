import { Ingredient } from './ingredient.model';

export class RecipeJson {
  label: string;
  ingredients: string[];
}

export class Recipe {
  constructor(label: string, ingredients: Ingredient[]) {
    this.label = label;
    this.ingredients = ingredients;
  }

  label: string;
  ingredients: Ingredient[];
}

export class RecipeWeight {
  constructor(recipe: Recipe, weight: number) {
    this.recipe = recipe;
    this.weight = weight;
  }

  recipe: Recipe;
  weight: number;
}
