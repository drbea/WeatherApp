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
git clone https://github.com/drbea/WeatherApp.git
```

## Installez les dépendances Python :
```bash
pip install -r requirements.txt
```

## Créer un fichier nommé:   .env
y mettre votre clé api d'open weather map obtenu et le chargé a travers le module dotenv dans les paramètres de votre projet 


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


# mkdir -p ecom/env ecom/src/models ecom/src/views ecom/src/urls ecom/images/users ecom/images/banners ecom/images/logos ecom/css ecom/templates
## Cette commande est déjà assez optimisée pour créer la structure de répertoires en une seule fois. Toutefois,
## pour rendre le tout plus lisible ou éviter de répéter des chemins communs, vous pourriez regrouper les chemins similaires
## à l'aide d'accolades {}. Cela réduit la redondance dans la commande, comme suit :
```bash
mkdir -p ecom/{env,src/{models,views,urls},images/{users,banners,logos},css,templates}
```
Explication :
```bash
ecom/{env,src/{models,views,urls},images/{users,banners,logos},css,templates} :
```
Le ecom est commun à tous les répertoires.
Ensuite, les accolades {} permettent de lister les différents répertoires à créer.
Vous pouvez imbriquer les accolades pour créer plusieurs sous-répertoires en une seule commande.
Résultat final
Cette commande alternative produira exactement la même structure de répertoires que celle de départ, tout en étant plus compacte et lisible :

```bash
Copy code
ecom/
├── env/
├── src/
│   ├── models/
│   ├── views/
│   └── urls/
├── images/
│   ├── users/
│   ├── banners/
│   └── logos/
├── css/
└── templates/
```
Cette version améliore la clarté et la maintenance du code, surtout dans des commandes longues ou complexes.
