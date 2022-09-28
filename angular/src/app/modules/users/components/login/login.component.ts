import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { HttpServiceService } from '../../http-service.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  formNotValid: boolean = false
  constructor(private http : HttpServiceService) { }

  loginForm : FormGroup = new  FormGroup({
    username : new FormControl('' , Validators.required),
    password : new FormControl("" , Validators.required)
  })

  submitLogin(){
    if (this.loginForm.valid) {
      this.http.loginUser(this.loginForm.value).subscribe((resp) => {
        console.log(resp);
      },
        (error) => {
          console.log(error.error);
        }
)
    }
    else {
      console.log('fill properly ');
      this.formNotValid = true
      console.log(this.loginForm.valid);

    }
  }

  ngOnInit(): void {
  }


}
