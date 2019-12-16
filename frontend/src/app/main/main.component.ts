import {Component, OnInit} from '@angular/core';
import {UserService} from '../user.service';
import {AuthService} from '../auth.service';
import {UserModel} from "../userModel";
import {FormBuilder, Validators} from "@angular/forms";

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  fileToUpload: File;
  loader = false;
  user: UserModel = {
    token: null,
    history: null
  };
  historyUser;
  isAuth = false;
  form = this.fb.group({
    login: [null, Validators.required],
    password: [null, Validators.required]
  });
  constructor(private userService: UserService, public auth: AuthService, private fb: FormBuilder) {
  }

  ngOnInit() {
    this.checkIsAuth();
  }
  login() {
   this.isAuth = true;
  }
  logout() {
    localStorage.clear();
    this.user.token = null;
    this.user.history = null;
  }
  checkIsAuth() {
    const token = localStorage.getItem('token');
    if (token) {
      console.log('auth', token);
      this.user.token = token;
    }
  }
  getHistory(token: string) {
    this.userService.getStory(token).subscribe((res:any) => {
      if (res.result) {
        this.user.history = res.result.tasks;
      }
      console.log(this.user);
    })
  }
  reload() {
    this.getHistory(this.user.token);
  }
  changeFile(event) {
    if (event.target.files && event.target.files.length) {
      const file = event.target.files[0];
      this.fileToUpload = file;
    }
  }
  onSubmit(){
   this.userService.logIn(this.form.value.login, this.form.value.password).subscribe((res:any) => {
     if (res.result) {
       this.isAuth = false;
       this.form.reset();
       this.user.token = res.result.token;
       localStorage.setItem('token', res.result.token );
       this.getHistory(res.result.token);
     }
   })
  }
  sendFile() {
    this.loader = true;
    this.userService.sendFile(this.fileToUpload, this.user.token).subscribe((res: any) => {
      console.log(res);
      if (res.status === 200) {
        this.loader = false;
        this.fileToUpload = null;
      }
    });
  }
}
