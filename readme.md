# Crowdfunding Project: Fans Only

#### Introducing a revolutionary new crowdfunding platform that lets fans bring back their favorite cancelled TV shows and movies! With this platform, you can donate money to help revive a cancelled series or support the creation of a sequel to your favourite film. Whether you're a die-hard fan or just want to see more of your favourite characters, this platform gives you the power to make it happen. 

### Features
#### User Accounts
- [x] Username
- [x] Email Address
- [x] Password
#### Projects
- Create a new project
    - [x] Owner (a user)
    - [x] Description
    - Image
    - [x] Target amount to fundraise
    - Open/close i.e. accepting new supporters and donations
    - [x] When the project was created
- Ability to pledge to a project
    - [x] An amount
    - [x] The project the pledge is for
    - [x] The supporter
    - [x] Whether the pledge is anonymous or not
    - [x] A comment to go with the pledge



### Part A Submission
- A link to the GitHub repository containing the code for your [project.] (https://github.com/SheCodesAus/she-codes-crowdfunding-api-project-adriannachong)
- A link to the [deployed project.](https://dark-darkness-9221.fly.dev/projects/)
- A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
- A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
- A screenshot of Insomnia, demonstrating a token being returned.
- Step by step instructions for how to register a new user and create a new project. 
- Your refined [API specification and Database Schema.](https://docs.google.com/document/d/1xWHVMj9vnV-NbYiie3esstoxiwoudotASchv9ftUuDg/edit?usp=sharing)

```
#### 1. Create User
curl --request POST \
  --url http://localhost:8000/users/ \
  --header 'Authorization: Token 8e20271c59fdf1e68b72ee6e38d60aba1edc47f6' \
  --header 'Content-Type: application/json' \
  --data '{
    "username": "sierraa",
    "email": "sierra@email.com",
		"password": "password"
}'

create authentication_token

curl --request POST \
  --url http://localhost:8000/api-token-auth/ \
  --header 'Content-Type: application/json' \
  --data '{
"username": "admin",
"password": "adminpassword"
}'
```
```
#### 2. Create New Project 

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