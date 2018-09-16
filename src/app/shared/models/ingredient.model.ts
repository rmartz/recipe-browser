export enum Rating {
  Unrated = 0,
  Liked = 1,
  Disliked = 2,
  Neutral = 3
}

export class Ingredient {
  constructor(label: string) {
    this.label = label;
    this._rating = Rating.Unrated;
  }

  label: string;
  _rating: Rating;

  get rating(): Rating {
    return this._rating;
  }

  set rating(rating: Rating) {
    if (rating === Rating.Liked) {
      this.favorited = true;
    } else if (rating === Rating.Disliked) {
      this.blacklisted = true;
    } else {
      if (this.blacklisted) {
        this.blacklisted = false;
      }
      if (this.favorited) {
        this.favorited = false;
      }
      this._rating = rating;
    }
  }

  get blacklisted(): boolean {
    return this._rating === Rating.Disliked;
  }

  set blacklisted(blacklisted: boolean) {
    if (blacklisted === this.blacklisted) {
      // No action needed
      return;
    }
    if (blacklisted) {
      this._rating = Rating.Disliked;
    } else {
      this._rating = Rating.Unrated;
    }

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
    return this._rating === Rating.Liked;
  }

  set favorited(favorited: boolean) {
    if (favorited === this.favorited) {
      // No action needed
      return;
    }
    if (favorited) {
      this._rating = Rating.Liked;
    } else {
      this._rating = Rating.Unrated;
    }

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
