import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {HttpRequest} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  baseUrl = 'https://grid.kosyachniy.com/api';

  constructor(private http: HttpClient) {
  }

  sendFile(fileToUpload: File) {
    const endpoint = `${this.baseUrl}/upload`;
    const formdata: FormData = new FormData();
    formdata.append('file', fileToUpload);
    const req = new HttpRequest('POST', endpoint, formdata, {
      responseType: 'json'
    });
    return this.http.request(req);
  }
}
