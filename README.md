# Password Checker

Un programme Python permettant d'évaluer la robustesse d'un mot de passe grâce à la bibliothèque **zxcvbn**.

## Fonctionnalités

- Analyse de la force d'un mot de passe.
- Attribution d'un score de 0 à 4.
- Estimation du temps nécessaire pour casser le mot de passe.
- Suggestions d'amélioration.
- Avertissements sur les mots de passe faibles.

## Installation

### Cloner le dépôt

```bash
git clone https://github.com/votre-utilisateur/password-checker.git
cd password-checker
```

### Installer les dépendances

```bash
pip install zxcvbn
```

ou

```bash
python -m pip install zxcvbn
```

## Utilisation

Lancer le script :

```bash
python Password.py
```

Entrer ensuite le mot de passe à analyser.

### Exemple

```text
Entrez votre mot de passe : Azerty123

=== Analyse du mot de passe ===
Score : 1 / 4
Faible

Temps estimé pour le casser :
quelques heures

Suggestions :
- Ajoutez un ou deux mots supplémentaires.
- Évitez les mots courants et les séquences prévisibles.
```

## Barème des scores

| Score | Niveau |
|---------|---------|
| 0 | Très faible |
| 1 | Faible |
| 2 | Moyen |
| 3 | Fort |
| 4 | Très fort |

## Technologies utilisées

- Python 3
- zxcvbn

