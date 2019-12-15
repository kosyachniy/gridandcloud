import { Component, OnInit } from '@angular/core';
import {UserService} from "../user.service";
import {AuthService} from "../auth.service";

@Component({
  selector: 'app-start',
  templateUrl: './start.component.html',
  styleUrls: ['./start.component.css']
})
export class StartComponent implements OnInit {
  fileToUpload: File;
  loader = false;
  constructor(public auth: AuthService, private userService: UserService) { }

  ngOnInit() {
  }
  changeFile(event) {
    if (event.target.files && event.target.files.length) {
      const file = event.target.files[0];
      this.fileToUpload = file;
    }
  }

  sendFile() {
    this.loader = true;
    this.userService.sendFile(this.fileToUpload).subscribe((res: any) => {
      console.log(res);
      if (res.status === 200) {
        this.loader = false;
      }
    });
  }

}
