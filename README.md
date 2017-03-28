# Big-Data-MapReduce-Design-Patterns
Le but de ce Tp est de mettre en oeuvre les Patrons de Conception MapReduce
Nous utilisons le langage Python pour développer les Mappers et les Reducers.
# Patrons de Filtrage : Filtrage Simple
On se propose de réaliser un programme MapReduce mettant en oeuvre le patron de Filtrage.
Comme exemple pour ce patron de conception nous allons compter le nombre de posts avec une seule phrase ou moins pour ceci on developpe :
- Un Mapper permettant d’extraire uniquement les posts d’une phrase ou moins 
- Un Reducer permettant de calculer le nombre de posts d'une phrase ou moins
==> On trouve 32562  posts ayant une phrase ou moins 

# Patrons de Récapitulation
On se propose de réaliser des programme MapReduce mettant en oeuvre les patrons de Récapitulation.
On distingue deux types pour ce patron de conception
Index ,Récapitulation
## Index
On vise à créer dans cette partie un index pour nos données, c’est à dire un fichier permettant d’afficher pour chaque mot, dans quels posts du forum est-ce qu’il a été mentionné, et combien de fois.
On utilise pour ceci :
- Un Mapper permettant d’extraire les différents mots d’un post le resultat sera sous la forme (word,node_id)
- Un Reducer permettant de donner, pour chacun des mots, le nombre d’occurrences, ainsi que la liste des node_id dans lesquels il apparaît
## Moyenne
On s’intéresse dans cette partie à calculer la moyenne des ventes chaque jour de la semaine .On utilise pour ceci :
- Un Mapper permettant d’extraire le cout de vente pour chaque jour de la semaine le resultat sera sous la forme (day,cost)
- Un Reducer permettant de calculer la moyenne des ventes pour chaque jour de la semaine
==>la valeur moyenne des ventes le Dimanche est  249.946443251
## Combiner
On Crée un programme MapReduce permettant de calculer la somme des ventes par jour de la semaine en utilisant :
- Un Mapper permettant d’extraire le cout de vente pour chaque jour de la semaine le resultat sera sous la forme (day,cost)
- Un Reducer permettant de calculer la somme des ventes pour chaque jour de la semaine
On teste ce job d’abord sans combiner, puis avec combiner et on visualise à chaque fois la somme des ventes le dimanche et la valeur du Reduce Input Records on trouve :
Sans Combiner
Reduce input records 	0 	4138476 	4138476   (Map, Reduce ,Total)
6 	150296795.47
Avec combiner
Reduce input records 	0 	14 	14 (Map,Reduce,Total)
6  	150296795.47
==>On conclue que l'utilisation du combiner permet de diminuer le travail du Reducer ainsi que le traffic réseau 

# Patrons Structurels 
On se propose de réaliser une application mettant en oeuvre le patron de conception structurel.
Pour cela, nous allons réaliser la jointure de deux ensembles de données: les fichiers délimités forum_nodes dont les champs sont de la forme suivante :<br/>
 node_id	 title	tagnames	author_id	 body	node_type	parent_id	abs_parent_id	added_at	score	state_string	last_edited_id	last_activity_by_id last_activity_at	active_revision_id	extra, extra_ref_id	extra_count
 et forum_users dont les champs sont de la forme suivante :<br/>
user_ptr_id	reputation	gold	silver	bronze<br/>
Ils ont une clef en commun :author_id dans le fichier forum_nodes et user_ptr_id dans forum_users
On crée un job MapReduce permettant de donner, pour chaque post, les données suivantes:
"id" "title" "tagnames" "author_id" "node_type" "parent_id" "abs_parent_id" "added_at" "score" "reputation" "gold" "silver" "bronze"<br/>
On utilise : 
- Un Mapper permettant de parcourir les fichiers forum_users et forum_nodes et d'extraire de chacune des entrées les données nécessaires en utilisant comme clef author_id
- Un Reducer permettant de faire l’opération de jointure entre les deux fichiers

==> la réputation de l’auteur du post dont l’identifiant est 100002517 est 6149


