import { Component ,inject,OnInit} from '@angular/core';
import { Client } from '../model/class/Client';
import { FormsModule } from "@angular/forms"
import { ClientService } from '../services/client.service';
import { APIResponseModel } from '../model/interface/role';

@Component({
  selector: 'app-client',
  imports: [FormsModule],
  templateUrl: './client.component.html',
  styleUrl: './client.component.css'
})
export class ClientComponent implements OnInit {

  clientObj: Client = new Client()
  clientList: Client[] = [];
  isSave:boolean = true

  clientService = inject(ClientService);

  resetForm() {
    this.clientObj.reset()
}

  loadClient(){
    this.clientService.getAllClients().subscribe((res:APIResponseModel) => {
      this.clientList = res.data
      console.log(this.clientList)
    })
  }

  onDeleteUser(id: number) {
    const isDelete = confirm("Are you sure you wanna delete?")
    if(isDelete){
      this.clientService.deletClientById(id).subscribe((res:APIResponseModel) => {
      if(res.result){
        alert('deleted successfully')
        this.loadClient()
      }
      else{
        alert(res.message)
      }
    
   })
  }
  }

  onEdit(id:number){
      this.clientObj = this.clientList.find(client => client.clientId === id) || this.clientObj
      this.isSave = false
  }

  onSaveClient(){
    this.clientService.addUpdate(this.clientObj).subscribe((res:APIResponseModel) => {
      if(res.result){
        alert('Client Created Successfully')
        this.loadClient()
      }else{
        alert(res.message)
      }
    })
  }

  ngOnInit(): void {
    this.loadClient()
    
  }

}
