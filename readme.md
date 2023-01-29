## create user 

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

## create new project 

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
