import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';

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
import { ShufflePipe } from './shared/pipes/shuffle.pipe';
import { IngredientsSearchComponent } from './ingredients-filter/ingredients-search/ingredients-search.component';
import { ToIngredientPipe } from './shared/pipes/toingredient.pipe';

@NgModule({
  declarations: [
    AppComponent,
    CallbackPipe,
    SortByPipe,
    ShufflePipe,
    ToIngredientPipe,
    IngredientsFilterComponent,
    IngredientsFilterSectionComponent,
    IngredientsSearchComponent,
    IngredientItemComponent,
    RecipesDisplayComponent,
    RecipeItemComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [
    Ingredients,
    Recipes,
    Suggestions
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
