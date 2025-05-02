# Installation

```
virtualenv venv
source venv/bin/activate

pip install -r requirement.txt

cd nalo_ice_cream

python manage.py migrate

python manage.py runserver
```

Une fois le serveur lancé, l'automate est accessible à cette URL : http://127.0.0.1:8000/ice_cream/
Le panneau d'administration est à cet URL : http://127.0.0.1:8000/ice_cream/admin

# Nalo lance le 1er glacier automate au monde !!

Tu es un nouveau développeur dans l'équipe Nalo, et ta première tâche consiste à développer le nouvel automate de Nalo. 

On te laisse le goût du design. Nous te recommandons de consacrer entre 2 et 4 heures à cet exercice. 

(Fais-en plus si tu veux 😇, fais-en moins si tu penses avoir montré tout ce qu'il faut 😎).


## Spécifications
Il y a 5 parfums de crème glacée disponibles :
- Chocolat Orange
- Cerise
- Pistache
- Vanille
- Framboise
  
Un pot de glace contient 40 boules.
Chaque boule coûte 2 euros.
Un utilisateur a le choix du nombre de boule et des parfums.


## Requis
- Une page doit permettre la saisie de la commande gérée en API, le prix sera retourné ainsi qu’un code aléatoire unique. Il faut gérer les problèmes de stocks !
- Une page doit permettre de récupérer la commande en entrant le numéro de commande, une représentation graphique de la glace (boule(s)) sera affiché à l'écran
- Une page administrateur permet de voir les recettes, le taux de remplissage des pots de glace
- Un bouton permet de remplir un pot vide, si un pot est vide un e-mail est envoyé à l’adresse de l’administrateur (un print suffit pour ce test)


## Instructions

- [ ] `fork` ce repository
- [ ] Initialise le projet Django
- [ ] Implémente les fonctionnalités requises
- [ ] Teste toutes tes fonctionnalités
- [ ] Publie-le sur GitHub en tant que `pull-request`
- [ ] Envoie-nous le lien et dis-nous approximativement combien de temps tu as passé sur ce travail.

