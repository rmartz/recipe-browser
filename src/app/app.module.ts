import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { IngredientsFilterComponent } from './ingredients-filter/ingredients-filter.component';
import { Ingredients } from './shared/services/ingredients.service';
import { Recipes } from './shared/services/recipes.service';
import { RecipesDisplayComponent } from './recipes-display/recipes-display.component';
import { IngredientItemComponent } from './ingredient-item/ingredient-item.component';
import { RecipeItemComponent } from './recipe-item/recipe-item.component';
import { Suggestions } from './shared/services/suggestion.service';
import { CallbackPipe } from './shared/pipes/callback.pipe';
import { SortByPipe } from './shared/pipes/sort-by.pipe';
import { IngredientsFilterSectionComponent } from './ingredients-filter/ingredients-filter-section/ingredients-filter-section.component';

@NgModule({
  declarations: [
    AppComponent,
    CallbackPipe,
    SortByPipe,
    IngredientsFilterComponent,
    IngredientsFilterSectionComponent,
    IngredientItemComponent,
    RecipesDisplayComponent,
    RecipeItemComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  providers: [
    Ingredients,
    Recipes,
    Suggestions
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
