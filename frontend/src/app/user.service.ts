import {Injectable} from '@angular/core';
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

  sendFile(fileToUpload: File, token: string) {
    const endpoint = `${this.baseUrl}/upload`;
    const formdata: FormData = new FormData();
    formdata.append('file', fileToUpload);
    formdata.append('token', token);
    const req = new HttpRequest('POST', endpoint, formdata, {
      responseType: 'json'
    });
    return this.http.request(req);
  }

  logIn(password: string, login: string) {
    const endpoint = `${this.baseUrl}/`;
    const formdata: FormData = new FormData();
    // formdata.append('params', new Blob([JSON.stringify({
    //   login,
    //   password
    // })], {
    //   type: 'application/json'
    // }));
    // }
    const sendData = {
      method: 'account.auth',
      params: {
        login,
        password
      }
    }
    return this.http.post(endpoint, sendData);
    // const req = new HttpRequest('POST', endpoint, sendData, {
    //     responseType: 'json',
    //   }
    // );
    // return this.http.request(req);
  }

  logout(token: string) {
    const endpoint = `${this.baseUrl}/`;
    const sendData = {
      method: 'account.exit',
      params: {
        token,
      }
    }
    return this.http.post(endpoint, sendData);
  }

  getStory(token: string) {
    const endpoint = `${this.baseUrl}/`;
    console.log(token);
    const sendData = {
      method: 'tasks.get',
      token
  }
  return this.http.post(endpoint, sendData);
  }

}
