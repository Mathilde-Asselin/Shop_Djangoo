# :rocket: Eshop Django 

[![forthebadge](https://forthebadge.com/images/badges/built-by-developers.svg)](https://forthebadge.com)[![forthebadge](http://forthebadge.com/images/badges/powered-by-electricity.svg)](http://forthebadge.com)

Voici notre projet Django du 04.03.2022 - Mathilde Asselin & Hugo Boudalier

## :boom: Démarrage

```bash
git clone git@github.com:Mathilde-Asselin/Shop_Djangoo.git
```
```bash
pip install channels
```
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
```bash
python manage.py runserver
```
Et let's go !

## 🏗 Project architecture
```shell
.
├── README.md
├── chat #Système de messagerie  
├── Django_App #Crud exo 01 
├── Django_Math #Base
├── Shop_App #Eshop exo 02
```

## 🔔 Différentes routes

Exercice n°02 - Eshop Django
- Eshop : /Shop_App => Permet d'accéder à l'exo n°02
- Eshop update & details : /Shop_App/id/update => Index de l'eshop

Exercice n°02 - Service messagerie
- Chat : /chat => Permet d'accéder à la page messagerie  

Exercice n°01 - CRUD 
- Crud create : /Django_App => Permet d'accéder à l'exo01 et à la création des questions
- Crud list : /Django_App/listview => Liste des questions
- Crud detail : /Django_App/listview/id => Detail des questions
- Crud update : /Django_App/listview/id/update => Modification des questions
- Crud delete : /Django_App/listview/1/delete => Supression des questions 
 
 ID pour exo 01 : 1,2 et le suivant est le 11

## 💻 Auteur

* Mathilde Asselin
* Hugo Boudalier