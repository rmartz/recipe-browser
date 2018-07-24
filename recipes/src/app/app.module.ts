import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { IngredientsFilterComponent } from './ingredients-filter/ingredients-filter.component';
import { Ingredients } from './shared/services/ingredients.service';

@NgModule({
  declarations: [
    AppComponent,
    IngredientsFilterComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [
    Ingredients
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
