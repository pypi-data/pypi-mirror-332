import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem


def generate_conformers(
    mol: Chem.Mol,
    n_conf: int = 1,
    delta: float = 10,
    n_threads: int = 0,
    remove_high_e_confs: bool = True,
    only_converged_confs: bool = True,
    align: bool = True,
) -> tuple[Chem.Mol, pd.DataFrame, pd.Series]:
    """
    Generate conformers for an RDKit molecule

    :param mol: the input molecule
    :param n_conf: the number of conformers to generate
    :param delta: only accept conformers if they are within delta_e of the lowest energy conformer
    :param n_threads: number of threads to run with. 0 defaults to all available threads
    :param remove_high_e_confs: if True, remove high energy conformers
    :param only_converged_confs: if True, remove conformers that don't converge
    :param align: if True, align the conformers by minimizing the RMSD

    :return mol: Chem.Mol; updated molecule with conformers
    :return energies: pd.DataFrame; conformer indexes, energies, and convergence
    :return mask: pd.Series; a mask of booleans for each
    """

    mol = Chem.AddHs(mol)
    ids = AllChem.EmbedMultipleConfs(
        mol,
        numConfs=n_conf,
        useBasicKnowledge=True,  # - useBasicKnowledge : impose basic knowledge such as flat rings
        enforceChirality=True,
        numThreads=n_threads,
        randomSeed=42,
    )

    results = AllChem.UFFOptimizeMoleculeConfs(mol, numThreads=n_threads)
    energies = []
    for _id, result in zip(ids, results):
        not_converged, energy = result
        energies.append({"id": _id, "not_converged": not_converged, "energy": energy})
    energies = pd.DataFrame(energies)

    # starting with everyone as True (moving forward)
    mask = energies["id"].apply(lambda x: True)

    if remove_high_e_confs:
        # unsure about the units of energy
        mask = mask & (energies["energy"] <= energies["energy"].min() + delta)

    if only_converged_confs:
        #  if not_converged == 0, then the geometry didn't converge.
        mask = mask & (energies["not_converged"] != 0)

    # remove conformers that didn't make the cut
    for _id in energies[~mask]["id"]:
        mol.RemoveConformer(_id)

    if align:
        AllChem.AlignMolConformers(mol)

    return mol, energies, mask
