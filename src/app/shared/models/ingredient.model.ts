export class Ingredient {
  constructor(label: string) {
    this.label = label;
    this._blacklisted = false;
  }

  label: string;
  _blacklisted: boolean;
  _favorited: boolean;

  get blacklisted(): boolean {
    return this._blacklisted;
  }

  set blacklisted(blacklisted: boolean) {
    if (blacklisted === this._blacklisted) {
      // No action needed
      return;
    }
    this._blacklisted = blacklisted;

    const event = new CustomEvent('blacklistChange', {
      detail: {
        ingredient: this
      }
    });
    document.dispatchEvent(event);

    if (blacklisted) {
      this.favorited = false;
    }
  }

  get favorited(): boolean {
    return this._favorited;
  }

  set favorited(favorited: boolean) {
    if (favorited === this._favorited) {
      // No action needed
      return;
    }
    this._favorited = favorited;

    const event = new CustomEvent('favoriteChange', {
      detail: {
        ingredient: this
      }
    });
    document.dispatchEvent(event);

    if (favorited) {
      this.blacklisted = false;
    }
  }
}

export class IngredientWeight {
  constructor(ingredient: Ingredient, weight: number, occurrences: number, additions: number) {
    this.ingredient = ingredient;
    this.weight = weight;
    this.occurrences = occurrences;
    this.additions = additions;
  }

  ingredient: Ingredient;
  weight: number;
  occurrences: number;
  additions: number;
}
