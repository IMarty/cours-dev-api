# Users / Customers

## Création de la table (15min)

Pas dans PGAdmin mais dans "models_orm.py"
tablename => customer
id ... même que "Products" + primary_key=True
email => "String"+ unique=True
password => "String"
created_at ... même que "Products"

## Ajout d'utilisateur (30min)
Router /customers
Requête POST /customers
Ajouter un DTO pour le body sur POST
(Pour l'instant le pass est stocké en claire / non hashé) -> à changer avec Igor.
Gérer l'erreur en cas de doublon (Ajout d'un autre customer avec la même adresse mail)

## Ensemble : Encryption 


## Get User Details (30min)
GET /customers Liste de tous les customers
GET /customers/{customer_id} Détail d'un customer.
C'est normal si ca retourne aussi le mot de passe -> à changer avec Igor 

## Ensemble : DTO de response
