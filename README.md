![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/css-%23663399.svg?style=for-the-badge&logo=css&logoColor=white)
![Python](https://img.shields.io/badge/python-%233670A0.svg?style=for-the-badge&logo=python&logoColor=ffdd54)

## Lancer le projet
```bash```
pip install flask
python app.py

# Cahier de recette — Application Flask (Inventaire réseau)

---

### Fiche de test 01 : Affichage global de l'inventaire

* **Identifiant :** `FT-01`
* **Objectif :** Vérifier que la page d'accueil liste correctement l'ensemble des équipements du fichier JSON.
* **Prérequis :** Serveur Flask actif (`http://127.0.0.1:5000/`), fichier `data/data.json` non vide.
* **Procédure :**
  1. Ouvrir le navigateur à l'adresse `http://127.0.0.1:5000/`.
  2. Vérifier la présence du bandeau d'en-tête avec le logo (`static/images/logo.png`).
  3. Parcourir la liste des cartes d'équipements affichées.
* **Résultat attendu :** 
  * Toutes les fiches du JSON sont visibles avec leur `hostname`, `natureEquipement`, `zoneTechnique`, `fabricant`, `etatLiaison` et `ipv4`.
  * La page ne lève aucune erreur Jinja (`UndefinedError`) ni page blanche.
* **Statut :** [ ] Conforme  [ ] Non conforme

---

### Fiche de test 02 : Moteur de recherche et filtres

* **Identifiant :** `FT-02`
* **Objectif :** Valider le bon fonctionnement du formulaire de filtrage sur la page principale.
* **Prérequis :** Page d'accueil chargée.
* **Procédure :**
  1. Saisir une adresse IP existante (ex. `192.168.`) ou un nom d'hôte partiel dans le champ texte, puis cliquer sur « Rechercher ».
  2. Saisir une chaîne de caractères inexistante (ex. `introuvable_xyz`) et valider.
  3. Cliquer sur le lien « Réinitialiser ».
* **Résultat attendu :**
  * Étape 1 : Seuls les équipements dont l'IP ou le nom contient la chaîne s'affichent.
  * Étape 2 : Le message « Aucun équipement trouvé. » s'affiche à l'écran.
  * Étape 3 : L'URL redevient `/` et l'ensemble de la liste réapparaît.
* **Statut :** [ ] Conforme  [ ] Non conforme

---

### Fiche de test 03 : Accès à la page de détail d'un équipement

* **Identifiant :** `FT-03`
* **Objectif :** S'assurer que le routage dynamique `/detail/<id>` extrait et affiche la bonne ressource unitaire.
* **Prérequis :** Au moins un équipement visible sur la page d'accueil.
* **Procédure :**
  1. Cliquer sur le lien « Voir le détail » de la première carte.
  2. Vérifier l'URL dans la barre d'adresse (ex. `http://127.0.0.1:5000/detail/1`).
  3. Vérifier les informations affichées sur la page.
  4. Cliquer sur « ← Retour à l'inventaire ».
* **Résultat attendu :**
  * La route `/detail/<id>` renvoie le template `detail.html` avec les données exactes de l'équipement sélectionné.
  * Le bouton de retour renvoie bien sur la racine `/`.
* **Statut :** [ ] Conforme  [ ] Non conforme

---

### Fiche de test 04 : Gestion des erreurs 404 (ID inconnu)

* **Identifiant :** `FT-04`
* **Objectif :** Confirmer que l'application gère proprement les identifiants inexistants sans planter le serveur.
* **Prérequis :** Connaître un identifiant non présent dans `data.json` (ex. `9999`).
* **Procédure :**
  1. Taper directement dans le navigateur : `http://127.0.0.1:5000/detail/9999`.
* **Résultat attendu :**
  * Le navigateur affiche une page d'erreur HTTP 404 standard (« Not Found ») levée par `abort(404)`.
  * Le serveur Flask en console ne lève pas d'exception non gérée (pas de crash serveur).
* **Statut :** [ ] Conforme  [ ] Non conforme

---

### Fiche de test 05 : Outil de diagnostic réseau (Lien Ping externe)

* **Identifiant :** `FT-05`
* **Objectif :** Tester la conformité du bouton d'action vers le service externe de ping.
* **Prérequis :** Se trouver sur une carte d'accueil ou sur une fiche de détail.
* **Procédure :**
  1. Cliquer sur le bouton « Ping » associé à une adresse IPv4.
* **Résultat attendu :**
  * Un nouvel onglet s'ouvre (`target="_blank"`).
  * L'adresse ciblée correspond exactement au schéma `https://ping.pe/<ipv4>`.
* **Statut :** [ ] Conforme  [ ] Non conforme
