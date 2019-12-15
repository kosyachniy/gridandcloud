import {Component, OnInit} from '@angular/core';
import {UserService} from '../user.service';
import {AuthService} from '../auth.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  constructor(private auth: AuthService) {
  }

  ngOnInit() {
    console.log('Yakushkin');
    alert('Yakushkin');
  }


}
