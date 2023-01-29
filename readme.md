# Crowdfunding Project: Fans Only

#### Introducing a revolutionary new crowdfunding platform that lets fans bring back their favorite cancelled TV shows and movies! With this platform, you can donate money to help revive a cancelled series or support the creation of a sequel to your favourite film. Whether you're a die-hard fan or just want to see more of your favourite characters, this platform gives you the power to make it happen. 


### Features
#### User Accounts
- Username
- Email Address
- Password
#### Projects
- Create a new project
    - Owner (a user)
    - Description
    - Image
    - Target amount to fundraise
    - Open/close i.e. accepting new supporters and donations
    - When the project was created
- Ability to pledge to a project
    - An amount
    - The project the pledge is for
    - The supporter
    - Whether the pledge is anonymous or not
    - A comment to go with the pledge




### Part A Submission
- A link to the GitHub repository containing the code for [project.](https://github.com/SheCodesAus/she-codes-crowdfunding-api-project-adriannachong)
- A link to the [deployed project.](https://dark-darkness-9221.fly.dev/projects/)
- A screenshot of Insomnia, demonstrating a successful [GET method](https://github.com/SheCodesAus/she-codes-crowdfunding-api-project-adriannachong/blob/main/screenshot%20-%20get%20method.png) for any endpoint.
- A screenshot of Insomnia, demonstrating a successful [POST method](https://github.com/SheCodesAus/she-codes-crowdfunding-api-project-adriannachong/blob/main/screenshot%20-%20post%20method.png) for any endpoint.
- A screenshot of Insomnia, demonstrating a [token being returned.](https://github.com/SheCodesAus/she-codes-crowdfunding-api-project-adriannachong/blob/main/screenshot%20-%20token%20returned.png)
- Step by step instructions for how to register a new user and create a new project. 
#### 1. Create User
```
curl --request POST \
  --url http://localhost:8000/users/ \
  --header 'Authorization: Token 8e20271c59fdf1e68b72ee6e38d60aba1edc47f6' \
  --header 'Content-Type: application/json' \
  --data '{
    "username": "username123",
    "email": "fakeemail@email.com",
		"password": "password"
}'

create authentication_token

curl --request POST \
  --url http://localhost:8000/api-token-auth/ \
  --header 'Content-Type: application/json' \
  --data '{
"username": "adminname",
"password": "adminpassword"
}'
```
#### 2. Create New Project 
```
curl --request POST \
  --url http://localhost:8000/projects/ \
  --header 'Authorization: Token 8e20271c59fdf1e68b72ee6e38d60aba1edc47f6' \
  --header 'Content-Type: application/json' \
  --data '{
	"title": "Donate a dog",
	"description": "Please help, we need a dog for she codes plus, our class lacks barks.",
	"goal": 1,
	"image": "https://upload.wikimedia.org/wikipedia/commons/c/c1/Dollar_bill_and_small_change.jpg",
	"is_open": true,
	"date_created": "2023-01-28T05:25:59.759Z"
}'
```
- A refined [API specification and Database Schema.](https://docs.google.com/document/d/1xWHVMj9vnV-NbYiie3esstoxiwoudotASchv9ftUuDg/edit?usp=sharing)


