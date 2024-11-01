# Kong Arthur Guest Management Service

This application is a Flask-based REST API that handles CRUD operations for a guest database. The data is stored in an SQLite database (`guests.db`), which is connected to a Docker volume to ensure persistent data.

## Functionality

The API offers the following features:

- **Get all guests** - Retrieves a list of all guests.
- **Search for a guest by last name** - Retrieves a guest based on their last name.
- **Add a new guest** - Adds a new guest to the database.
- **Update guest information** - Updates an existing guest's information.
- **Get a guest by ID** - Retrieves a guest's details using their unique ID.
- **Delete a guest by ID** - Deletes a guest based on their ID.

## Endpoints

### GET /guests
Returns a list of all guests.

```bash
GET /guests
```
Respons code:
- 200, Ok
- 404, Not found


### GET /guests/search?last_name={last_name}
Searches for a guest based on their last name.

```bash
GET /guests/search?last_name={last_name}
```
Respons code:
- 200, Ok
- 404, Not found




### POST /guests
Adds a new guest to the database.

```bash
POST /guests
```
Inside the body, the text should be in JSON-format
```bash
{
"first_name": "Lucas",
"last_name": "Jacobsen,
"country": "Denmark"  
}
```
Respons code:
- 201, Created
- 400, Bad request



### PUT /guests/{id}
Updates an existing guest's information.

```bash
PUT /guests/{id}
```
Respons code:
- 200, Ok
- 404, Not found



### GET /guests/{id}
Retrieves a guest's details based on their ID.

```bash
GET /guests/{id}
```
Respons code:
- 200, Ok
- 404, Not found




### DELETE /guests/{id}
Deletes a guest based on their ID.

```bash
DELETE /guests/{id}
```
Respons code:
- 200, Ok
- 404, Not found




## Installation


### Build and run the application

1. Build the Docker image:

   ```bash
   docker build -t kong_arthur_guest .
   ```


2. Run the Docker container with a volume binding:

   ```bash
   docker run -it -p 5000:5000 -v miniprojekt:/app/data kong_arthur_guest
   ```



