# Application Meteo avec Django
Cette application web développée avec Django permet de consulter la météo actuelle d'une ville en utilisant l'API OpenWeatherMap.

## Fonctionnalités
    Affichage de la température, des conditions météorologiques et de l'humidité pour une ville donnée.
    Utilisation de Bootstrap pour une mise en page responsive et une interface utilisateur agréable.
    Gestion des requêtes API à l'aide de Python et de la bibliothèque requests.

## Prérequis
Avant de commencer, assurez-vous d'avoir installé les outils suivants :
    Python 3.x
    Django
    Clé API OpenWeatherMap (gratuite ou payante)

## Installation
    Clonez ce repository :

```bash
git clone https://github.com/votre_utilisateur/votre_repo.git
```

## Installez les dépendances Python :
```bash
pip install -r requirements.txt
```

## Configurez votre clé API OpenWeatherMap :
    Obtenez une clé API gratuite sur OpenWeatherMap.
    Ajoutez votre clé API dans le fichier settings.py de Django :
```python
# settings.py
OPENWEATHERMAP_API_KEY = 'votre_clé_api'
```

#Utilisation
    Lancez le serveur Django :
```bash
python manage.py runserver
```
## Accédez à l'application dans votre navigateur :

```arduino
http://127.0.0.1:8000/
```

Entrez le nom d'une ville dans le formulaire et soumettez-le pour voir les informations météo.

## Notes
    Cette application est destinée à des fins d'apprentissage et peut être étendue avec d'autres fonctionnalités telles que la prévision météorologique sur plusieurs jours, l'ajout de cartes interactives, etc.
    Assurez-vous de respecter les conditions d'utilisation de l'API OpenWeatherMap lors de l'utilisation de votre clé API.
