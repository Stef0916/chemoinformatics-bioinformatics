# Cheminformatics WorkFlow

The objective of this repository is to put together the most important step and applications of cheminformatics focused mainly in drug discovery.

This is inspired on the Cheminformatic specialization from [**Neovarsity**](https://neovarsity.org/)

Here is the list of the notebooks and the information explored:
1. [RDKit generals](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/cheminformatics-workflow/notebooks/1-RDKit-general.ipynb):
    - SMILES representions
    - SMARTS representations
    - Files types
    - Files conversions
2. [Library Filtering](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/cheminformatics-workflow/notebooks/2-Library_filtering.ipynb):
    - Load DataSet from PubChem
    - Remove Nan
    - Remove Duplicates
    - Molecues Visualization
    - Remove Inconclusive Results
    - Remove Active Agonist = Toxic
    - Remove Weak Compounds
3. [ChEMBl webresource](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/cheminformatics-workflow/notebooks/3-chembl_webresource.ipynb):
    - Search for Target Protein
    - Select Homo Sapiens Cyclooxygenase-2
    - Retrieve Bioactivity Data by IC50
    - Remove empty entries
    - Remove duplicates
    - Manage Std Values Units
    - Label: Active, Inactive, Intermediate
    - Convert IC50 to pIC50
4. [Data curation](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/cheminformatics-workflow/notebooks/4-Data_curation.ipynb):
    - Smiles Standarization
    - Fragment Parents
    - Neutralization
    - Normalization
    - Canonical Tautomer
    - Stereo Parents
    - Hydrogen Cleanup
    - Conformer Generation
5. [Molecular descriptors](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/cheminformatics-workflow/notebooks/5-Molecular-descriptors.ipynb):
    - MW, LogP, RB Descriptors
    - Aromatic Rings, Valence Electrons and BalabanJ descriptors
    - General RDKit Molecular Descriptors
6. [Chemical substructre](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/cheminformatics-workflow/notebooks/6-Chemical_substracture.ipynb):
    - Substructure Search with SMARTS pattern
    - Has Substructure
    - Get Substructure
    - More than 1 Chemical Substructure Search
    - Substructure 1 & Substructure 2
    - Substructure 1 OR Substructure 2
7. [Most common substructre](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/cheminformatics-workflow/notebooks/7-Most_common_substracture.ipynb):
    - MCS between 2 molecules
    - MCS between 1 molecule and a Dataset
    - Bermis-Murcko Scaffolds
8. [Chemical similarity](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/cheminformatics-workflow/notebooks/8-Chemical_smilarity.ipynb):
    - Similarity Matrix Pairwise
    - Euclidean and Tanimoto to find th most similar compounds
9. [Fingerprints](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/cheminformatics-workflow/notebooks/9-Fingerprints.ipynb):
    - Morgan Fingerprints
    - Avalon Fingerprints
    - Molecular ACCess System keys (MACCS)
    - Atom-Pair Fingerprints
    - Topological-Torsion Fingerprints
    - RDKit Fingerprints
10. [Fingerprints applications project](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/cheminformatics-workflow/notebooks/10-Fingerprints-applications.ipynb): This project is intented to apply fingerprints in order to compute molecular similarities and clustering within a dataset taken from the literature.
11. [Hydrogen bond donor descriptor project](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/cheminformatics-workflow/notebooks/11-Hydrogen_bond_donor-descriptor.ipynb): The project focused in the creation of a Python code to calculate a molecular descriptor that represents the capacity of the molecule to be a halogen bond donor. Use the code to calculate the halogen bond description for the given dataset. And finally, filter out compounds that do not have the halogen bond.
12. [Activity Cliff](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/cheminformatics-workflow/notebooks/12-Activity_cliff.ipynb): This project aims to study the the Structure-Activity Landscape Index (SALI) which is used to understand the relationship between the structural similarity of compounds and their biological activities, helping to identify activity cliffs.
13. [Clustering](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/cheminformatics-workflow/notebooks/13-Clustering.ipynb): Here, I review two clustering algorithm:
    - K-means
    - Taylor - Butina
14. [Chemical Reaction](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/cheminformatics-workflow/notebooks/14-Chemical_reaction.ipynb): I reviewed the basic of chemical reaction using SMARTS.

## Directory Structure

Inside this folder, you'll discover:

- Notebooks
- Required CSV, sdf and excel
- Images/plots