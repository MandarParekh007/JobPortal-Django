import { Component, inject, OnInit } from '@angular/core';
import { MasterService } from '../services/master.service';
import { IDesignation } from '../model/interface/designation';
import { APIResponseModel } from '../model/interface/role';

@Component({
  selector: 'app-designation',
  imports: [],
  templateUrl: './designation.component.html',
  styleUrl: './designation.component.css'
})
export class DesignationComponent implements OnInit {
  masterService = inject(MasterService);

  designationList: IDesignation[] = []
  isLoader:boolean = true

  ngOnInit(): void {
     this.masterService.getDesignations().subscribe((result:APIResponseModel) => {
        this.designationList = result.data
        this.isLoader = false
     })
  }


}
