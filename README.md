# E2_Optimisation_classification

Ce projet s'inscrit dans le cadre de la validation de mon titre pro Développeuse IA. 
Il a été proposé par le formateur.

A partir de scraping d'articles de journaux, un modèle de type NLP a été entrainé et mis à 
disposition via une application Flask, qui, à partir d'un titre proposé, pour prédire 
le journal qui aurait pu publié cet article.
Le projet est présenté dans le pdf E2_final.

Plusieurs Notebooks récupère les articles sur le net et les enregistre en csv.
Un notebook concatère les csv obtenus. Un autre notebook insère les données en base.
Un notebook modelisation.ipynb teste et entraine plusieurs modèles.

Le répertoire Flask_journal contient les fichiers utilisés par l'application.