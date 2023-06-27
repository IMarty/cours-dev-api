# Users / Customers

## Création de la table (15min)

Pas dans PGAdmin mais dans "models_orm.py"
tablename => customer
id ... même que "Products" + primary_key=True
email => "String"+ unique=True
password => "String"
created_at ... même que "Products"

## Ajout d'utilisateur (20min) -> 16h15
1. Router /customers
2. Requête POST /customers
3. Ajouter un DTO pour le body sur POST
(Pour l'instant le pass est stocké en claire / non hashé) -> à changer avec Igor.
4. Gérer l'erreur en cas de doublon (Ajout d'un autre customer avec la même adresse mail)

## Ensemble : DTO de response
## Ensemble : Encryption 


## Get User Details (30min)
GET /customers Liste de tous les customers
GET /customers/{customer_id} Détail d'un customer.

