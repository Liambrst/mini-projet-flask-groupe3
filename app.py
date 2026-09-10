from flask import Flask, render_template, request, abort
import json
import os

app = Flask(__name__)

def charger_donnees():
    chemin_fichier = os.path.join(app.root_path, 'data', 'data.json')
    try:
        with open(chemin_fichier, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@app.route('/')
def index():
    equipements = charger_donnees()
    
    recherche = request.args.get('recherche', '').lower()
    filtre_type = request.args.get('type', '')
    filtre_statut = request.args.get('statut', '')

    if recherche or filtre_type or filtre_statut:
        resultats = []
        for eq in equipements:
            match_recherche = (recherche in eq['hostname'].lower() or recherche in eq['ipv4']) if recherche else True
            match_type = (eq['natureEquipement'] == filtre_type) if filtre_type else True
            match_statut = (eq['etatLiaison'] == filtre_statut) if filtre_statut else True
            
            if match_recherche and match_type and match_statut:
                resultats.append(eq)
        equipements = resultats

    return render_template('index.html', equipements=equipements)

@app.route('/detail/<int:id>')
def detail(id):
    equipements = charger_donnees()
    equipement_trouve = next((eq for eq in equipements if eq['id'] == id), None)
    
    if equipement_trouve is None:
        abort(404)
        
    return render_template('detail.html', equipement=equipement_trouve)

if __name__ == '__main__':
    app.run(debug=True)