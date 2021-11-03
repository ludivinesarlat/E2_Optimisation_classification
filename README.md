# E2_Optimisation_classification

Ce projet s'inscrit dans le cadre de la validation de mon titre pro Développeuse IA. 

A partir de scraping de titres de journaux, un modèle de type NLP a été entrainé et mis à 
disposition via une application Flask, application qui prédit, à partir d'un titre proposé, 
le journal qui aurait pu publié cet article.
Le projet est présenté dans le pdf E2_final.

Plusieurs Notebooks récupèrent les articles sur le net et les enregistrent en csv.
Un notebook concatère les csv obtenus. Un autre notebook insère les données en base.
Un notebook modelisation.ipynb teste et entraine plusieurs modèles.

Le répertoire Flask_journal contient les fichiers utilisés pour l'application.
