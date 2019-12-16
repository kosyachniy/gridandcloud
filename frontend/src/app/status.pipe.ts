import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'status'
})
export class StatusPipe implements PipeTransform {

  transform(value: any, ...args: any[]): any {
    if (value === 1) {
      return 'В обработке'
    }
    if (value === 2) {
      return 'Обработано'
    }
    if (value === true) {
      return 'Обнаружено селфи'
    }
    if (value === false) {
      return 'Не обнаружено селфи'
    }
    return null;
  }

}
