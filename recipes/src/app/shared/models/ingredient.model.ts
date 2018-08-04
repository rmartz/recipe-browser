export class Ingredient {
  constructor(label: string) {
    this.label = label;
    this.blacklisted = false;
  }

  label: string;
  blacklisted: boolean;
}
