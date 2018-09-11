import { PipeTransform, Pipe } from '@angular/core';

@Pipe({
    name: 'shuffle',
    pure: false
})
export class ShufflePipe implements PipeTransform {
  transform(items: any[]): any[] {
    return items.sort(() => Math.random() - 0.5);
  }
}
