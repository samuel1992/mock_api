# Mock Api

This is a simple project to mock some responses for specific endpoints.
It uses the django admin to enter new endpoints and the mock response, and based on the endpoint and the http method it going to provide your json response.

Its really simple just as a proof of concept so feel free to implement fancier features here =)

# How to run it?
Its under docker and docker compose so just run `docker-compose build` and `docker-compose up`.

# Next features?!
- Implement a pattern match with the body on PUT, POST and PATCH requests
- Return custom response based on a parameter in the request header. That could be useful when you want to simulate an error or something like this.
