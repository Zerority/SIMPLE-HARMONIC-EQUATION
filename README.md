# Visualiseur du Mouvement Harmonique Simple

Une application développée en **Python** permettant de calculer et de visualiser le déplacement d'un **Mouvement Harmonique Simple (MHS)**.

---

## Fonctionnalités

- Interface graphique développée avec **Tkinter**
- Calcul du déplacement d'un mouvement harmonique simple
- Saisie personnalisée des paramètres :
  - Amplitude
  - Fréquence
  - Phase initiale
  - Temps
- Conversion automatique des degrés en radians
- Génération automatique de la courbe du mouvement avec **Matplotlib**
- Mise en évidence du point correspondant à l'instant sélectionné
- Vérification des erreurs de saisie avec des messages explicites

---

## Équation utilisée

Le déplacement est calculé à l'aide de l'équation classique du mouvement harmonique simple :

\[
x(t)=A\cos(\omega t+\varphi)
\]

avec :

- **A** : amplitude
- **ω = 2πf** : pulsation
- **φ** : phase initiale
- **t** : temps

---

## Technologies utilisées

- Python
- Tkinter
- NumPy
- Matplotlib

---

## Installation

Clonez le dépôt :

Installez les bibliothèques nécessaires :

```bash
pip install numpy matplotlib
```

---

## Aperçu

L'application permet de :

- saisir les paramètres du mouvement harmonique ;
- calculer le déplacement à un instant donné ;
- afficher automatiquement la courbe correspondante ;
- visualiser le point associé à l'instant choisi.

---
