# neural-jepa

[draft]

Exploration pour comparer les représentations apprises par I-JEPA avec l'activité du cortex visuel. 

L'idée de base: voir si le fait de prédire dans l'espace latent (plutôt que de reconstruire des pixels bruts) donne des représentations qui ressemblent un peu plus à ce qu'on observe dans la hiérarchie visuelle.

## Notes 
- Le cerveau ne passe pas son temps à recalculer chaque pixel: il fait plutôt du codage prédictif en essayant d'anticiper ce qui vient ensuite à un niveau plus abstrait.
- Les modèles comme MAE forcent la reconstruction au pixel près, ce qui paraît assez peu réaliste biologiquement. À l'inverse, l'approche de JEPA prédit directement dans l'espace des embeddings. Je suis curieuse de voir si les couches intermédiaires s'alignent mieux avec les aires visuelles (de V1 vers le cortex inférotemporal) qu'un modèle génératif classique.

**Protocole envisagé:**
1. Extraire les activations des couches sur des images naturelles.
2. Tester un modèle d'encodage linéaire simple (ridge regression) pour prédire des réponses neuronales réelles — à voir encore entre les données fMRI de NSD ou les enregistrements Neuropixels de l'Allen Institute.
3. Regarder aussi via une analyse de similarité représentationnelle pour comparer directement la géométrie des espaces sans avoir à fitter trop de paramètres.

## Quick check

Validation rapide:

```bash
python scratchpad.py