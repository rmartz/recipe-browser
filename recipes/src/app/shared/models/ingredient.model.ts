

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
    this._blacklisted = blacklisted;

    const event = new CustomEvent('blacklistChange', {
      detail: {
        ingredient: this
      }
    });
    document.dispatchEvent(event);
  }

  get favorited(): boolean {
    return this._favorited;
  }

  set favorited(favorited: boolean) {
    this._favorited = favorited;

    const event = new CustomEvent('favoriteChange', {
      detail: {
        ingredient: this
      }
    });
    document.dispatchEvent(event);
  }
}
