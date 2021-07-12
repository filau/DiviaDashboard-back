# Divia dashboard (back-end)

Vous souhaitez consulter les horaires de votre bus ou tramway Divia depuis votre smartphone de manière directe, simplement en lançant une application&nbsp;? Alors, utilisez *Divia dashboard*&nbsp;! Ceci est le *back-end* de l’application.

## Configuration du serveur
* Installer Python 3, et les modules `flask`, `waitress` et `divia-api` ([développé par moi-même&nbsp;!](https://github.com/filau/python_divia_api)).
* Lancer `main.py`&nbsp;:
```
$  [python | python3] main.py
```
* Et le tour est joué&nbsp;!

## Format d’une requête

> **Méthode&nbsp;:** `GET`

> **Chemin&nbsp;:** `/divia`

> **Arguments HTTP&nbsp;:**
> * `line_id`&nbsp;: identifiant unique de la ligne&nbsp;;
> * `stop_code`&nbsp;: identifiant unique de l’arrêt.
