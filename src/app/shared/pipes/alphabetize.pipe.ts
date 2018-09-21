import { PipeTransform, Pipe } from '@angular/core';

@Pipe({
    name: 'alphabetize',
    pure: false
})
export class AlphabetizePipe implements PipeTransform {
  transform(items: any[], key: string): any[] {
      return items.sort((a, b) => a[key].localeCompare(b[key]));
  }
}
