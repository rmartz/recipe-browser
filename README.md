[![Travis CI status](https://travis-ci.org/rmartz/recipe-browser.svg?branch=develop)](https://travis-ci.org/rmartz/recipe-browser)

# Recipe Browser
Aims to help people find recipes that they may be interested in, by using "Like" to prioritize recipes that include a given recipe and "Nope" to exclude any recipes that do. Recipes that include a higher proportion of "Like"-d ingredients are prioritized more, with a slight focus on recipes that match numerically more matching ingredients (So a recipe that includes 2 selected ingredient out of 4 would rank above a recipe that includes 1 selected ingredient out of 2).

A free-to-use instance is available at https://recipes.reedmartz.com. All changes made to `develop` are deployed to there automatically.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Build

Because some errors can fail during compilation but work under development (Such as private component variables used in the component's template), to test the AOT compiler run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via [Protractor](http://www.protractortest.org/).
