# Kong Arthur Guest Management Service

Denne applikation er en Flask-baseret REST API, der håndterer CRUD-operationer for en gæstedatabase. Dataene gemmes i en SQLite-database (`guests.db`), som er forbundet til Docker-volumenet for at sikre persistent data.

## Funktionalitet

API'et tilbyder følgende funktioner:

- **Få alle gæster** - Henter en liste over alle gæster.
- **Søg efter gæst efter efternavn** - Henter en gæst baseret på efternavn.
- **Tilføj ny gæst** - Tilføjer en ny gæst til databasen.
- **Opdater gæsteinformation** - Opdaterer en eksisterende gæsts oplysninger.
- **Hent gæst efter ID** - Henter en gæsts detaljer ved hjælp af deres unikke ID.
- **Slet gæst efter ID** - Sletter en gæst baseret på deres ID.

## Endpoints

### GET /guests
Returnerer en liste over alle gæster.

```http
GET /guests
