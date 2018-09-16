import { PipeTransform, Pipe } from '@angular/core';

@Pipe({
    name: 'sortBy',
    pure: false
})
export class SortByPipe implements PipeTransform {
  private get_sort(keys: string[]) {
    function sort(a, b) {
      for (let key of keys) {
        let direction = 1;
        if (key.charAt(0) === '-') {
          direction = -1;
          key = key.substr(1);
        }
        const diff = a[key] - b[key];
        if (diff !== 0) {
          return direction * diff;
        }
      }
      return 0;
    }
    return sort;
  }

  transform(items: any[], keys: string[]): any[] {
    const sort = this.get_sort(keys);
    return items.sort(sort);
  }
}
