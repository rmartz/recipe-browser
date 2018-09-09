import { PipeTransform, Pipe } from '@angular/core';

@Pipe({
    name: 'sortBy',
    pure: false
})
export class SortByPipe implements PipeTransform {
  transform(items: any[], key: string): any[] {
    return items.sort((a, b) => b[key] - a[key]);
  }
}
