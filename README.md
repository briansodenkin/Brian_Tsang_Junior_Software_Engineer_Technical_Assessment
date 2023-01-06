# Backend_Engineer_Test

## Choice of Framework & Library
In this project, I used `Django` for development. 
### Benefits & drawbacks
*Benefits*
- Reusability
  - In python, there are mainly three framworks Django, Flask, and FastAPI. 
  - Most packages in Django
  - Full-stack web development framework, unlike others.

- MVC(model-view-controller) architecture
  - Have modifications that doest not affect the model.
  - Sepearate components for backend projects

- Conveinence to development
  - Necessary tools are provided
  - Provided ORM(object-relational mapper), admin, relational database, web templating system, and URL dispatchers

*Drawbacks*
- No conventions on development:
  - Configure many things for other packages, like DRF.
  - Override mehtods/ class while developing
  - Deep understanding for the documentatios are required

- Monolithic
  - Certain set of files and pre-defined variables. 
  - Mandatory file structure that we can’t use our own.

### Assumptions underlying that choice

- Scalable in the future
  - Scale up with hardware additions.
  - More complex model design, more API provided

## Potential Improvement
- Model design
  - Further splitting for the models, address, phone fields are very commonly changed
  - Some models can be splitted to handle popular CRUD operations
  - E.g. clinic/

- API design
  - More API endpoints should be provided for conveinient CRUD operations
  - E.g. doctor/availability/
 
- Testing
  - CRUD operations for `Clinic`, `Phone` are not tested rigorously 
  - Validation testing for the fields should be tested

- Localisation
  - CRUD operations based on `locale` are not supported  

## Production consideration
- Recoverability: 
  - Ability to recover an application environment in the event of system failure or data loss
  - Backup database
  - Backup server
  - Recover the data

- Availablitiy
  - Ability to provide services when user request
  - Regular checking on the server status
  - Cloud hosting

- Correctness
  - Provide the most up-to-date response
  - Handle async update, create
  - Data lock for async operations

## Assumptions
- `Phone` and `District` are related to where the doctor worked in, namely `Clinic`
- `Doctor` availability should be in Json format
- `Doctor` availability should have specific field
- `Doctor` can work in multiple `Clinic`
- `Doctor` can has many `Category`
- No async operations on the database
- Json provided by response from the GET request will give all info required by the sample UI

## Database design

* ER diagram:

![ER diagram](https://github.com/briansodenkin/backend_api_test/blob/main/Doctor_model-17.drawio.png)

* Takeaway:
- `Doctor` & `Clinic` are seperated:
    - Thinner model design for `Doctor`(too many fields)
    - Some fields like `address` should be used to record a `Clinic` instead of `Doctor`

- Models can be decoupled to three groups:
  - `Doctor` 
  - `Clinic`
  - `District` (Seperated model as `District` is One-to-Many related to `Doctor` & `Clinic`)

- `Doctor` & `Clinic` are in Many-to-Many relations, implicit table will be generate by `Django`

- Each groups represent a seperated app

## Getting Started

This is a section to show you how to set up the project environment

### Prerequisites

* python
  * version > 3.6+ 
  ```sh
  brew install python
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/briansodenkin/backend_engineer_test.git
   ```
2. Install all python packages
   ```sh
   pip install -n requirements.txt
   ```

### Database Migrations & Admin setup

1. Remoe the local `.sqlite3` file
   ```sh
   rm *.sqlite3
   ```
2. Run migrations for the database
   ```sh
   python manage.py migrate
   ```
3. Set admin to monitor the database
   ```sh
   python manage.py createsuperuser
   ```
   ```sh
   Email: `Enter customised email`
   Password: `Enter customised password`
   ```

## Usage

After successfully set up the environment according to `Getting Started`.
This is a section to show you run the project

### Run server
   
   ```sh
   python manage.py runserver
   ```
After running the above command, development server will be avaliable at
   ```sh
   http://127.0.0.1:8000
   ```
   
### Testing
   
   ```sh
   python manage.py test
   ```
Testing based on the CREATE, RETRIEVE, UPDATE operations of the `Doctor` related endpoints
   
### API Endpoints

For detailed documentations for the API, it is available at

   ```sh
   http://127.0.0.1:8000/api/docs
   ```
   
| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| GET | /api/admin/ | To login as admin to monitor database |
| GET | /api/docs | To retrieve the detailed api documents page |
| POST | /api/user/create | To create a new user |
| GET | /doctor | To retrieve all doctors |
| GET | /doctor/?catgeory=`category_id` or `category_name` | To retrieve all doctors based on `Category` |
| GET | /doctor/?language=`English` or `Chinese` | To retrieve all doctors based on language |
| GET | /doctor/?district=`district_id` or `district_name` | To retrieve all doctors based on `District` |
| GET | /doctor/?min_price=`price`&max_price=`price` | To retrieve all doctors based on price range |
| GET | /doctor/:id | To retrieve details of a single doctor |
| PUT | /doctor/:id | To update details of a single doctor |
| PATCH | /doctor/:id | To update partial details of a single doctor |
| POST | /doctor/ | To create a new doctor |

### Technologies Used
* [Django](https://www.djangoproject.com/)
