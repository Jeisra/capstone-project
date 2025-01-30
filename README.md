# capstone-project
Back-end developer capstone project

*****OVERVIEW OF GRADING CRITERIA*****

# Has the student committed the project to a Git repository?

https://github.com/Jeisra/capstone-project.git

http://127.0.0.1:8000/admin/ 

user: admin
pass: lemonadmin
email admin@littlelemon.com

user: John
pass: continental
email john@littlelemon.com

***API routes***
http://127.0.0.1:8000/api/ ***api root***
http://127.0.0.1:8000/api/booking/ ***genera reserva***
http://127.0.0.1:8000/auth/users/ ***registra usuario***
http://127.0.0.1:8000/api/token/ ***obtiene token***
http://127.0.0.1:8000/auth/token/login/ ***crea token***
http://127.0.0.1:8000/api/token/refresh/ ***actualiza token***
http://127.0.0.1:8000/api/restaurant/menu-items/ ***agregar o filtrar elementos del menu***

***WEB LittleLemon***
http://127.0.0.1:8000/
http://127.0.0.1:8000/api/restaurant/book/
http://127.0.0.1:8000/api/restaurant/menu/
http://127.0.0.1:8000/api/restaurant/about/

http://127.0.0.1:8000/cart/menu-items 

# Does the application connect the backend to a MySQL database?

![image](https://github.com/user-attachments/assets/9f1ddf3e-cfd8-4b5f-b902-786fc14c6acf)


# Are the menu and table reservation APIs implemented?

**MENU API**

http://127.0.0.1:8000/api/restaurant/menu/

![image](https://github.com/user-attachments/assets/c8e44b4d-47e3-4eb0-85c4-6fcdb2b8a761)


**TABLE RESERVATION**

http://127.0.0.1:8000/api/booking/

![image](https://github.com/user-attachments/assets/940399bf-9c35-4294-a4a6-f8afc8fe11cf)


# Is the application configured with user registration and authentication?

**USER REGISTRATION**

http://127.0.0.1:8000/auth/users/

![image](https://github.com/user-attachments/assets/a81cda2d-1ddc-43d1-b42c-4cc8ebf2be14)

**USER AUTHENTICATION**

http://127.0.0.1:8000/auth/token/login/

![image](https://github.com/user-attachments/assets/e1d031fb-63b6-4517-a2b2-3b260bba190b)


# Does the application contain unit tests?

Yes, the application contains unit tests for Models and Serializers in the tests.py file.
You can check by running:

`python manage.py test`

![image](https://github.com/user-attachments/assets/7778431e-e44b-4005-9611-f784500fd5d5)
