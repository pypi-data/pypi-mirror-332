from typing import Union
from rdkit import Chem


def mol_from_smiles(smiles: str, errors_ok: bool = True) -> Union[Chem.Mol, None]:
    """
    Translate SMILES into RDKit Mol object

    :param smiles: SMILES string
    :param errors_ok: whether to raise errors or not (ie return None)
    """
    try:
        mol = Chem.MolFromSmiles(smiles)
        return mol
    except BaseException as e:
        if errors_ok:
            return None
        raise e


def mol_to_smiles(mol: Chem.Mol, errors_ok: bool = True) -> Union[Chem.Mol, None]:
    """
    Translate RDKit Mol object into SMILES string

    :param mol: RDKit Mol object
    :param errors_ok: whether to raise errors or not (ie return None)
    """
    try:
        smiles = Chem.MolToSmiles(mol)
        return smiles
    except BaseException as e:
        if errors_ok:
            return None
        raise e


def mol_from_smarts(smarts: str, errors_ok: bool = True) -> Union[Chem.Mol, None]:
    """
    Translate SMARTS into RDKit Mol object

    :param smarts: SMARTS query
    :param errors_ok: whether to raise errors or not (ie return None)
    """
    try:
        mol = Chem.MolFromSmarts(smarts)
        return mol
    except BaseException as e:
        if errors_ok:
            return None
        raise e


def mol_to_smarts(mol: Chem.Mol, errors_ok: bool = True) -> Union[Chem.Mol, None]:
    """
    Translate RDKit Mol object into SMARTS query

    :param mol: RDKit Mol object
    :param errors_ok: whether to raise errors or not (ie return None)
    """
    try:
        smiles = Chem.MolToSmarts(mol)
        return smiles
    except BaseException as e:
        if errors_ok:
            return None
        raise e
