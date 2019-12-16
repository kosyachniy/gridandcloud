import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { MainComponent } from './main/main.component';
import {RouterModule} from '@angular/router';
import {AppRoutingModule} from './app-routing.module';

import {HttpClientModule} from '@angular/common/http';
import {ReactiveFormsModule} from "@angular/forms";
import { registerLocaleData } from '@angular/common';
import localeRu from '@angular/common/locales/ru';
import { StatusPipe } from './status.pipe';
registerLocaleData(localeRu, 'ru');
@NgModule({
  declarations: [
    AppComponent,
    MainComponent,
    StatusPipe,
  ],
  imports: [
    BrowserModule,
    RouterModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
