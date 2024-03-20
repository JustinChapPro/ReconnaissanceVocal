## Détection de Mots-Clés en Streaming Audio
Ce projet utilise l'API Google Cloud Speech-to-Text pour détecter des mots-clés spécifiques en temps réel dans un flux audio capturé via le microphone.

## Prérequis
- Python 3.x
- Un compte Google Cloud avec le service Speech-to-Text activé.
- Un fichier de credentials JSON pour votre compte Google Cloud.

## Dépendances
Ce projet nécessite les paquets suivants :

- pyaudio pour la capture audio.
- google-cloud-speech pour l'intégration avec l'API Google Cloud Speech-to-Text.
- google-auth pour l'authentification auprès de Google Cloud.
Vous pouvez les installer en utilisant pip :
- pip install pyaudio google-cloud-speech google-auth
## Configuration
Authentification Google Cloud : Avant d'exécuter le script, assurez-vous de disposer d'un fichier de credentials JSON pour l'API Google Cloud Speech-to-Text.
Définissez la variable d'environnement GOOGLE_APPLICATION_CREDENTIALS en pointant vers votre fichier de credentials JSON 
- export GOOGLE_APPLICATION_CREDENTIALS="chemin/vers/votre/fichier-de-credentials.json"
Sur Windows, utilisez :
- set GOOGLE_APPLICATION_CREDENTIALS=chemin\vers\votre\fichier-de-credentials.json
## Modification du code :
- Remplacez "Mettre fichier .json ici!" par le chemin de votre fichier de credentials JSON dans le script. (Cette étape est optionnelle si vous avez déjà configuré la variable d'environnement GOOGLE_APPLICATION_CREDENTIALS.)

## Utilisation
Pour exécuter le script, ouvrez un terminal ou une invite de commande et naviguez jusqu'au dossier contenant le script. Ensuite, exécutez :
- python nom_du_script.py
Remplacez nom_du_script.py par le nom réel de votre fichier script.

## Fonctionnement
Le script écoute en continu le microphone par défaut de votre système et analyse l'audio capturé en temps réel. Lorsqu'il détecte le mot-clé spécifié (par défaut, "Hello"), il affiche un message dans la console. Le compteur augmente à chaque détection du mot-clé.

## Auteur
- Nom : Justin Chaput
- Email: justinchaps@hotmail.com

## Licence


