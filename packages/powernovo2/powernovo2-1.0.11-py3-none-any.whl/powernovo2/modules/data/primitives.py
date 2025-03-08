"""Fundamental dataclasses for modules."""
from __future__ import annotations

import re
from collections.abc import Sequence
from dataclasses import dataclass

import numpy as np
import torch
from numpy.typing import ArrayLike
from pyteomics import proforma
from pyteomics.proforma import GenericModification, MassModification
from spectrum_utils.spectrum import MsmsSpectrum

"""Constants."""
HYDROGEN = 1.007825035
OXYGEN = 15.99491463
H2O = 2 * HYDROGEN + OXYGEN
PROTON = 1.00727646688
C13 = 1.003355
MASS_SCALE = 10000
PRECURSOR_DIM = 3
MAX_MASS = 4000


MASSIVE_KB_MOD = {
    "+42.011": "[Acetyl]-",
    "+43.006": "[Carbamyl]-",
    "-17.027": "[Ammonia-loss]-",
    "+43.006-17.027": "[+25.980265]-",  # Not in Unimod
    "M+15.995": "M[Oxidation]",
    "N+0.984": "N[Deamidated]",
    "Q+0.984": "Q[Deamidated]",
    "C+57.021": "C[Carbamidomethyl]",
    "S+79.966": "S[Phospho]",
    "T+79.966": "T[Phospho]",
    "Y+79.966": "Y[Phospho]",
}
MASSIVE_KB_MOD_MAP = {
    "[Acetyl]-": '(+42.01)',
    "[Carbamyl]-": '(43.01)',
    "[Ammonia-loss]-": '',
    "[+25.980265]-": '',
    "M[Oxidation]": 'M(+15.99)',
    "N[Deamidated]": 'N(+.98)',
    "Q[Deamidated]": 'Q(+.98)',
    "C[Carbamidomethyl]": 'C(+57.02)',
    "S[Phospho]": 'S(+79.97)',
    "T[Phospho]": 'T(+79.97)',
    "Y[Phospho]": 'Y(+79.97)'
}


@dataclass
class Peptide:
    """A peptide sequence with or without modification and/or charge.

    Parameters
    ----------
    sequence : str
        The bare amino acid sequence.
    modifications : iterable of str, float, or None, optional
        The modification at each amino acid. This should be the length of
        ``sequence`` + 2, where index 0 and -1 are used for N- and C-terminal
        modification respectively. Use ``None`` in the iterable to specify
        unmodified positions. When ``modifications`` is ``None``, it is assumed
        that no modifications are present.
    charge : int, optional
        The charge of the peptide.
    """

    sequence: str
    modifications: Sequence[str | float | None] | None = None
    charge: int | None = None

    def __post_init__(self) -> None:
        """Validate the provided parameters."""
        if self.modifications is not None:
            if len(self.modifications) != len(self.sequence) + 2:
                raise ValueError(
                    "'modifications' must be two elements longer than "
                    "'sequences' to account for terminal modifications."
                )

        if self.modifications is None:
            self.modifications = [None] * (len(self.sequence) + 2)

        # Parse modifications into Pyteomics' format
        parsed = [None] * (len(self.sequence) + 2)
        for idx, mod in enumerate(self.modifications):
            if mod is None:
                continue

            try:
                mod = [MassModification(mod)]
            except ValueError:
                try:
                    mod = [GenericModification(mod)]
                except (AttributeError, TypeError):
                    pass
            except TypeError:
                pass

            parsed[idx] = mod

        self.modifications = parsed
        n_mod = self.modifications[0]
        c_mod = self.modifications[-1]

        self.proforma = proforma.to_proforma(
            sequence=list(zip(self.sequence, self.modifications[1:-1])),
            n_term=[n_mod] if n_mod is not None else n_mod,
            c_term=[c_mod] if c_mod is not None else c_mod,
            charge_state=self.charge,
        )

    def split(self) -> list[str]:
        """Split the modified peptide for tokenization."""
        if self.modifications is None:
            return list(self.sequence)

        out = []
        for idx, (aa, mods) in enumerate(
                zip(f"-{self.sequence}-", self.modifications)
        ):
            if mods is None:
                if idx and (idx < len(self.modifications) - 1):
                    out.append(aa)

                continue

            if len(mods) == 1:
                try:
                    modstr = f"[{mods[0].name}]"
                except (AttributeError, ValueError):
                    modstr = f"[{mods[0].mass:+0.6f}]"
            else:
                modstr = f"[{sum([m.mass for m in mods]):+0.6f}]"

            if not idx:
                out.append(f"{modstr}-")
            else:
                out.append(f"{aa}{modstr}")

        return out

    @classmethod
    def from_proforma(
            cls,
            sequence: str,
    ) -> Peptide:
        """Create a Peptide from a ProForma 2.0 string.

        Parameters
        ----------
        sequence : str
            A ProForma 2.0-compliant string.

        Returns
        -------
        Peptide
            The parsed ProForma peptide.
        """

        pep, meta = proforma.parse(sequence)

        try:
            charge = meta["charge_state"].charge
        except AttributeError:
            charge = None

        static_mods = {}
        for mod_rule in meta["fixed_modifications"]:
            for res in mod_rule.targets:
                static_mods[res] = mod_rule.modification_tag

        seq = [None] * len(pep)
        mods = [None] * (len(pep) + 2)
        mods[0] = meta["n_term"]
        mods[-1] = meta["c_term"]
        for idx, (res, var_mods) in enumerate(pep):
            seq[idx] = res
            if res in static_mods:
                if var_mods is None:
                    var_mods = []

                var_mods.insert(0, static_mods[res])

            mods[idx + 1] = var_mods

        return cls("".join(seq), mods, charge)

    @classmethod
    def from_massivekb(
            cls,
            sequence: str,
            charge: int | None = None,
    ) -> Peptide:
        """Create a Peptide from MassIVE-KB annotations.

        MassIVE-KB includes N-term carbamylation, NH3-loss, acetylation,
        as well as M oxidation, and deamidation of N and Q, in a
        manner that does not comply with the ProForma standard.

        Parameters
        ----------
        sequence : str
            The peptide sequence from MassIVE-KB
        charge : int, optional
            The charge state of the peptide.

        Returns
        -------
        Peptide
            The parsed MassIVE peptide after conversion to a ProForma
            format.
        """
        sequence = cls.massivekb_to_proforma(sequence, charge)
        return cls.from_proforma(sequence)

    @classmethod
    def massivekb_to_proforma(
            cls, sequence: str, charge: int | None = None
    ) -> str:
        """Convert a MassIVE-KB peptide sequence to ProForma.

        MassIVE-KB includes N-term carbamylation, NH3-loss, acetylation,
        as well as M oxidation, and deamidation of N and Q, in a
        manner that does not comply with ProForma.

        Parameters
        ----------
        sequence : str
            The peptide sequence from MassIVE-KB
        charge : int, optional
            The charge state of the peptide.

        Returns
        -------
        str
            The parsed MassIVE peptide after conversion to a ProForma
            format.
        """
        sequence = "".join(
            [
                MASSIVE_KB_MOD.get(aa, aa)
                for aa in re.split(r"(?<=.)(?=[A-Z])", sequence)
            ]
        )
        if charge is not None:
            sequence += f"/{charge}"

        return sequence







class MassSpectrum(MsmsSpectrum):
    """A mass spectrum.

    Parameters
    ----------
    filename: str
        The file from which the spectrum originated.
    scan_id: str
        The Hupo PSI standard scan identifier.
    mz: array of shape (n_peaks,)
        The m/z values.
    intensity: array of shape (n_peaks, )
        The intensity values.
    retention_time: float, optional
        The measured retention time.
    ion_mobility: float, optional
        The measured ion mobility.
    precursor_mz: float, optional
        The precursor ion m/z, if applicable.
    precursor_charge: int, optional
        The precursor charge, if applicable.
    label: str, optional
        A label for the mass spectrum. This is typically an
        annotation, such as the generating peptide sequence,
        but is distinct from spectrum_utils' annotation.
    """

    def __init__(
            self,
            filename: str,
            scan_id: str,
            mz: ArrayLike,
            intensity: ArrayLike,
            retention_time: float | None = None,
            ion_mobility: float | None = None,
            precursor_mz: float | None = None,
            precursor_charge: int | None = None,
            label: str | None = None,
    ) -> None:
        """Initialize a MassSpectrum."""
        self.filename = filename
        self.scan_id = scan_id
        self.label = label

        # Not currently supported by spectrum_utils:
        self.ion_mobility = ion_mobility

        # spectrum_utils requires a precursor. Will remove after
        # I make a PR:
        if precursor_mz is None:
            precursor_mz = np.nan

        if precursor_charge is None:
            precursor_charge = np.nan

        super().__init__(
            identifier=str(scan_id),
            precursor_mz=precursor_mz,
            precursor_charge=precursor_charge,
            mz=mz,
            intensity=intensity,
            retention_time=retention_time,
        )

    @property
    def usi(self) -> str:
        """The Universal Spectrum Identifier."""
        index_type, scan = self.scan_id.split("=")
        fname = re.sub(
            ".(gz|tar|tar.gz|zip|bz2|tar.bz2)$",
            "",
            self.filename,
            flags=re.IGNORECASE,
        )
        fname = re.sub(
            ".(raw|mzml|mzxml|mgf|d|wiff)$",
            "",
            fname,
            flags=re.IGNORECASE,
        )
        return ":".join([fname, index_type, scan])

    @property
    def precursor_mass(self) -> float:
        """The monoisotopic mass."""
        return (self.precursor_mz - PROTON) * self.precursor_charge

    def to_tensor(self) -> torch.tensor:
        """Combine the m/z and intensity arrays into a single tensor.

        Returns
        -------
        torch.tensor of shape (n_peaks, 2)
            The mass spectrum information.
        """
        return torch.tensor(np.vstack([self.mz, self.intensity]).T)
