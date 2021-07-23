# Mock API
This is a simple project to mock some responses for specific endpoints and you can run it locally to simulate an API.

It uses the django admin to enter new endpoints and the mock response, and based on the endpoint and the http method its going to provide your json response.

You can see more about the django admin [here](https://docs.djangoproject.com/en/3.0/ref/django-admin/)


# How to run it?

Its under docker and docker compose so just `run docker-compose build and docker-compose up`. 

It should be ready to use online in your `http://localhost:8000/admin`


# How to create a user to the admin interface?

You have to create a superuser for the django admin interface.

Its quite easy. You only have to run the `python manage.py createsuperuser` command.

Let me show how to do it under the docker container: `docker exec -it mock-api_web_1 python manage.py createsuperuser`.

Then you only have to fill the inputs there.

![creating a django admin superuser](/docs/images/creating_admin_superuser.png)

You can see more about the django admin [here](https://docs.djangoproject.com/en/3.0/ref/django-admin/).


# How it works?

Basically you can create new endpoints via the `localhost:8000/admin` and access those endpoints on the address: `localhost:8000/anything/you/have/created`

To create a new endpoint you have to click in the “Add path” button under the Paths section.

![admin paths section](/docs/images/admin_paths.png)

Then you just put the endpoint settings here. The endpoint can have the {string} and the {integer} variables on it.

Select the http method you want to request for that endpoint and then the JSON body to return and the http status code.

![creating a new path](/docs/images/creating_a_path.png)

![requesting that path via postman](/docs/images/requesting_an_endpoint_via_postman.png)

In case of PUT/PATCH/POST methods you also can specify a definition of the request body following the OpenAPI spec in json format. [OPENAPI SPECIFICATION](https://swagger.io/specification/)

![editing a path](/docs/images/editing_a_path.png)

# Possible next features
- import swagger/openapi files in order to create the endpoint
