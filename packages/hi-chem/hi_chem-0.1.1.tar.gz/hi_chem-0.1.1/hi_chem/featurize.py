from rdkit import Chem
from rdkit.Chem import rdFingerprintGenerator
from rdkit.Chem import MACCSkeys
import numpy as np
from typing import Union, Callable, Optional

import traceback
from typing import Dict, Any, Optional, Union
from rdkit.Chem import Descriptors


def get_descriptors(mol, missing_val: Optional[Any] = None) -> Dict[str, Any]:
    """
    Calculate the full list of descriptors for a molecule.

    Parameters:
    -----------
    mol : rdkit.Chem.rdchem.Mol
        The molecule for which to calculate descriptors
    missing_val : Any, optional
        Value to use when a descriptor calculation fails

    Returns:
    --------
    Dict[str, Any]
        Dictionary mapping descriptor names to their calculated values
    """
    descriptors = {}

    for name, func in Descriptors._descList:
        try:
            descriptors[name] = func(mol)
        except Exception:
            traceback.print_exc()
            descriptors[name] = missing_val

    return descriptors


def get_fp_generator(fpkey: str = "ecfp4", n_bits: Optional[int] = 1024) -> Callable:
    """
    Get a function that generates molecular fingerprints of the specified type.

    Args:
        fpkey: The type of fingerprint to generate
        n_bits: The size of the fingerprint in bits

    Returns:
        A function that takes a molecule and returns a numpy array of the fingerprint
    """
    fpkey = fpkey.lower()

    # Define fingerprint generators with the specified number of bits
    fp_generators = {
        "ecfp4": rdFingerprintGenerator.GetMorganGenerator(radius=2, fpSize=n_bits),
        "ecfp6": rdFingerprintGenerator.GetMorganGenerator(radius=3, fpSize=n_bits),
        "rdkit": rdFingerprintGenerator.GetRDKitFPGenerator(fpSize=n_bits),
        "atompairs": rdFingerprintGenerator.GetAtomPairGenerator(fpSize=n_bits),
        "torsion": rdFingerprintGenerator.GetTopologicalTorsionGenerator(fpSize=n_bits),
    }

    if fpkey in fp_generators:
        generator = fp_generators[fpkey]
        return lambda mol: generator.GetFingerprintAsNumPy(mol)

    # n_bits doesn't matter for MACCS or DESCRIPTORS as they are a fixed set of calculations
    elif fpkey == "maccs":
        return lambda mol: np.frombuffer(
            MACCSkeys.GenMACCSKeys(mol).ToBitString().encode(), "u1"
        )
    elif fpkey == "descriptors":
        return lambda mol: np.array([value for value in get_descriptors(mol).values()])
    else:
        raise ValueError(f"Invalid generator: {fpkey}")


# Cache for fingerprint generators to avoid recreating them
GENERATORS = {}


def mol_to_numpy_fingerprint(
    mol: Chem.Mol, fpkey: str = "ecfp6", n_bits: int = 1024, errors_ok: bool = True
) -> Optional[np.ndarray]:
    """
    Converts a given molecule to a numpy-based fingerprint representation
    using a specified fingerprint type and bit length. This function utilizes
    a global cache of fingerprint generators to enhance performance by
    reusing previously created generators.

    Args:
        mol (Chem.Mol): The molecule to be converted to a fingerprint.
        fpkey (str): The type of fingerprint to be generated. Default is
            "ecfp6".
        n_bits (int): The number of bits for the generated fingerprint.
            Default is 1024.
        errors_ok (bool): Whether to suppress errors and return None if an
            error occurs during fingerprint generation. Default is True.

    Returns:
        Optional[np.ndarray]: A numpy array representing the fingerprint
            of the molecule if successful, or None if errors_ok is True
            and an error occurs.

    Raises:
        Exception: If an error occurs during fingerprint generation and
            errors_ok is False.
    """
    global GENERATORS
    fpkey = fpkey.lower()
    name = f"{fpkey}_{n_bits}"

    if name in GENERATORS:
        generator = GENERATORS[name]
    else:
        generator = get_fp_generator(fpkey=fpkey, n_bits=n_bits)
        GENERATORS[name] = generator

    try:
        fp = generator(mol)
        return fp
    except Exception as e:
        if errors_ok:
            return None
        raise e
