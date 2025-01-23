import { Component, inject } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import { MasterComponent } from "./master/master.component";
import { HttpClient } from '@angular/common/http';
import { Irole } from './model/interface/role';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, MasterComponent,RouterLink],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {

  title = 'angular_lean_partner';

}
