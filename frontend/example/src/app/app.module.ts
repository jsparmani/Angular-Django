import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import { ShowDataComponent } from './show-data/show-data.component';
import { PagenotfoundComponent } from './pagenotfound/pagenotfound.component';


import { RouterModule } from '@angular/router';
import { AppRoutingModule } from './app-routing.module';
import { HelloComponent } from './hello/hello.component';

@NgModule({
  declarations: [
    AppComponent,
    ShowDataComponent,
    PagenotfoundComponent,
    HelloComponent
  ],
  imports: [
    HttpModule,
    AppRoutingModule,
    BrowserModule,
    RouterModule.forRoot([
    {path: '',component: AppComponent},
    {path: 'show',component: ShowDataComponent},
    {path: 'hello',component: HelloComponent},


    ])
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
