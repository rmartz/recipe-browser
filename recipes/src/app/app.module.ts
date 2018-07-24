import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { IngredientsFilterComponent } from './ingredients-filter/ingredients-filter.component';
import { Ingredients } from './shared/services/ingredients.service';
import { Recipes } from './shared/services/recipes.service';
import { RecipesDisplayComponent } from './recipes-display/recipes-display.component';

@NgModule({
  declarations: [
    AppComponent,
    IngredientsFilterComponent,
    RecipesDisplayComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [
    Ingredients,
    Recipes
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
