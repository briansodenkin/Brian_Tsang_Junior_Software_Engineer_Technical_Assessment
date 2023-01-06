# backend_api_test

## Database design

ER diagram

![ER diagram](https://github.com/briansodenkin/backend_api_test/blob/main/Doctor_model-17.drawio.png)

Takeaway:
- Models can be decoupled to three groups:
  - `Doctor`
  - `Clinic`
  - `District` (Seperated as `District` is One-to-Many related to `Doctor` & `Clinic`)
- Each groups represent a seperated `app`
- Doctor & Clinic are in Many-to-Many relations, implicit table will be generate by `Django`


 

