import streamlit as st
from streamlit_ketcher import st_ketcher  # Import the Streamlit Ketcher component
from streamlit.components.v1 import html
import os
from io import StringIO
from ase.io import read, write
from pyperclip import copy
import base64
from stmol import showmol
import py3Dmol
import pormake as pm
import tempfile
import sys
import os
import mofography.mofography as mgr
from ase.io import read
from ase.data import vdw_radii
import numpy as np
from ase.units import _amu

sys.path.append(os.path.abspath('mofography'))

# -------------------- Utility Functions -------------------- #

def convert_cif_to_xyz(cif_file):
    """
    Convert CIF content to XYZ format using ASE.

    Args:
        cif_file (str): Path to the CIF file.

    Returns:
        str: XYZ formatted string.
    """
    try:
        structure = read(cif_file)
        xyz_io = StringIO()
        write(xyz_io, format='xyz', images=structure)
        return xyz_io.getvalue()
    except Exception as e:
        st.error(f"Error converting CIF to XYZ: {e}")
        return None


def copy_to_clipboard(text):
    """
    Copy text to the clipboard and notify the user.

    Args:
        text (str): Text to copy.
    """
    try:
        copy(text)
        st.success("Copied to clipboard!")
    except Exception as e:
        st.error(f"Failed to copy to clipboard: {e}")


def generate_download_link(cif_content, filename):
    """
    Generate a download link for the CIF file.

    Args:
        cif_content (str): Content of the CIF file.
        filename (str): Desired filename for download.

    Returns:
        str: HTML anchor tag for downloading.
    """
    try:
        b64 = base64.b64encode(cif_content.encode()).decode()
        href = f'<a href="data:file/cif;base64,{b64}" download="{filename}">Download CIF File</a>'
        return href
    except Exception as e:
        st.error(f"Failed to generate download link: {e}")
        return ""


def load_cif_file(file_path):
    """
    Load CIF file content from a given path.

    Args:
        file_path (str): Path to the CIF file.

    Returns:
        str: Content of the CIF file.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        st.error(f"Failed to load CIF file: {e}")
        return ""


def display_mof_info(mof_name):
    """
    Display information about a selected MOF in the sidebar.

    Args:
        mof_name (str): Name of the MOF.
    """
    st.sidebar.title("MOF Information")
    info = {
        "ZIF-8": {
            "description": """
            **ZIF-8 (Zeolitic Imidazolate Framework-8)** is a metal-organic framework composed of zinc ions coordinated with 2-methylimidazolate linkers. It has a sodalite-type topology and is renowned for its exceptional thermal and chemical stability. Discovered in 2006, ZIF-8's porous structure features large cavities connected by small apertures, making it suitable for selective gas adsorption and separation.

            **History & Development**: ZIF-8 is part of the larger family of zeolitic imidazolate frameworks (ZIFs), which combine the properties of zeolites and metal-organic frameworks. Its discovery expanded the possibilities for gas storage and separation technologies.

            **Uses**: ZIF-8 is widely studied for applications in gas storage (especially hydrogen and carbon dioxide), gas separation, catalysis, drug delivery, and as a component in membranes for selective separation processes.

            **Importance**: Its stability and tunable porosity make ZIF-8 a valuable material in addressing energy and environmental challenges, such as carbon capture and storage, and developing advanced filtration systems.
            """,
            "uses": "Gas separation, Catalysis, Drug delivery, Carbon capture",
            "importance": """
            ZIF-8's unique combination of stability and porosity has made it a material of significant interest across various fields. Its ability to selectively adsorb gases positions it as a key player in reducing greenhouse gas emissions and advancing clean energy technologies.
            """
        },
        "HKUST-1": {
            "description": """
            **HKUST-1 (Hong Kong University of Science and Technology-1)**, also known as **MOF-199**, is a copper-based metal-organic framework composed of copper ions and benzene-1,3,5-tricarboxylate linkers. It was one of the earliest and most studied MOFs due to its high surface area and open metal sites.

            **History & Development**: Synthesized in 1999, HKUST-1 demonstrated the potential of MOFs in gas storage applications. Its structure consists of paddlewheel copper dimers connected by organic linkers, forming large pores.

            **Uses**: HKUST-1 is used in gas storage (notably methane and hydrogen), gas separation, catalysis, and sensing. Its open metal sites make it suitable for catalytic reactions and adsorption processes.

            **Importance**: As a pioneering MOF, HKUST-1 showcased the versatility and promise of MOFs in addressing energy storage and environmental challenges. It remains a benchmark material in MOF research.
            """,
            "uses": "Gas storage, Catalysis, Gas separation",
            "importance": """
            The development of HKUST-1 marked a significant milestone in MOF chemistry, demonstrating how metal-organic frameworks can achieve high surface areas and porosities, essential for effective gas storage and separation technologies.
            """
        },
        "IRMOF-1": {
            "description": """
            **IRMOF-1 (Isoreticular Metal-Organic Framework-1)**, also known as **MOF-5**, is a zinc-based MOF constructed from zinc oxide clusters connected by terephthalate linkers (benzene-1,4-dicarboxylate). It was synthesized in 1999 and is recognized for its high surface area and porosity.

            **History & Development**: IRMOF-1 is the first in a series of isoreticular MOFs, which share the same topology but can have varied linkers to modify properties. Its creation demonstrated the potential for tailoring MOF structures for specific applications.

            **Uses**: IRMOF-1 is utilized in gas storage (hydrogen, methane), gas separation, catalysis, and sensing. Its large pore sizes make it effective for storing significant amounts of gases.

            **Importance**: The development of IRMOF-1 highlighted the modularity of MOFs, allowing for the design of materials with customized properties by simply changing the organic linker.
            """,
            "uses": "Gas storage, Catalysis, Gas separation",
            "importance": """
            IRMOF-1's design principle paved the way for the synthesis of numerous MOFs with tailored functionalities, significantly impacting materials science and engineering for energy and environmental applications.
            """
        },
        "MIL-101": {
            "description": """
            **MIL-101 (Materials of Institute Lavoisier-101)** is a chromium-based MOF with terephthalate linkers. It boasts an exceptionally high surface area and large pore volume, featuring mesoporous cages accessible through microporous windows.

            **History & Development**: Developed in 2005 by researchers at the Institut Lavoisier, MIL-101 is notable for its giant pores and high thermal stability, expanding the potential applications of MOFs to include larger guest molecules.

            **Uses**: MIL-101 is used in gas storage (hydrogen, methane, carbon dioxide), catalysis, drug delivery, and adsorption of large organic molecules due to its spacious pores.

            **Importance**: MIL-101's ability to accommodate large molecules and its robust stability make it a versatile material for applications in catalysis and environmental remediation.
            """,
            "uses": "Gas storage, Catalysis, Drug delivery, Adsorption",
            "importance": """
            The unique properties of MIL-101 demonstrate how MOFs can bridge the gap between microporous and mesoporous materials, offering new opportunities in fields requiring the processing of larger molecules.
            """
        },
        "UIO-66": {
            "description": """
            **UIO-66 (University of Oslo-66)** is a zirconium-based MOF consisting of Zr6O4(OH)4 clusters connected by terephthalate linkers. It is distinguished by its exceptional thermal and chemical stability, even in water and acidic conditions.

            **History & Development**: Discovered in 2008 by researchers at the University of Oslo, UIO-66 introduced a new class of robust MOFs that could withstand harsher environments, broadening the practical applications of MOFs.

            **Uses**: UIO-66 is employed in gas storage, catalysis, drug delivery, and environmental remediation. Its stability allows it to be used in aqueous systems and under acidic conditions.

            **Importance**: The robustness of UIO-66 makes it valuable for real-world applications where stability is crucial, such as in catalysis and separation processes under challenging conditions.
            """,
            "uses": "Gas storage, Catalysis, Drug delivery, Environmental remediation",
            "importance": """
            UIO-66's stability has set a benchmark for the development of durable MOFs, enabling their use in industrial processes and expanding the scope of MOF applications in various fields.
            """
        }
    }
    if mof_name in info:
        st.sidebar.subheader(mof_name)
        mof_info = info[mof_name]
        st.sidebar.markdown(mof_info['description'])
        st.sidebar.write(f"- **Uses**: {mof_info['uses']}")
        st.sidebar.markdown(f"**Importance**: {mof_info['importance']}")
    else:
        st.sidebar.write("No information available for this MOF.")

# -------------------- MOF Analysis Functions -------------------- #

def compute_surface_area(cif_path):
    """Compute the surface area (m²/g) of a MOF from a CIF file."""
    mat_atoms = read(cif_path)

    # Ensure CIF file was loaded correctly
    if mat_atoms is None or len(mat_atoms) == 0:
        raise ValueError("Error: CIF file is empty or could not be read.")

    # Compute the distance grid
    dgrid = mgr.dgrid_from_atoms_cpu(mat_atoms, spacing=0.5)

    # Convert Dask array to NumPy (ensure it's a valid 3D grid)
    #dgrid = dgrid.compute()  # Converts from Dask to NumPy  [ONLY NEEDED WHEN USING dgrid_from_atoms]

    if not isinstance(dgrid, np.ndarray) or len(dgrid.shape) != 3:
        raise ValueError(f"Expected a 3D NumPy array for dgrid, but got shape {dgrid.shape}")

    # Removed He, and chose a nitrogen probe (N₂, 1.86 Angstrom) instead.
    probe_radius = 1.86

    # Compute isosurface mesh
    isosurface_mesh = mgr.get_isosurface_mesh(dgrid, probe_radius, mat_atoms)

    # Compute mass in grams
    mass_g = mat_atoms.get_masses().sum() * _amu * 1000  

    # Compute surface area in m²/g
    sa_m2g = isosurface_mesh.area_faces.sum() * 1e-20 / mass_g  

    return sa_m2g


def run_pormake(node_smiles, linker_smiles, topology):
    """
    Generates a MOF using PoRMake with the given node, linker, and topology.
    
    Args:
        node_smiles (str): SMILES string of the selected node.
        linker_smiles (str): SMILES string of the selected linker.
        topology (str): Name of the topology selected.
    
    Returns:
        str: CIF content of the generated MOF.
    """
    try:
        database = pm.Database()
        topo = database.get_topology(topology)
        node = pm.BuildingBlock.from_smiles(node_smiles)
        linker = pm.BuildingBlock.from_smiles(linker_smiles)
        mof = pm.MOF(topo, [node, linker])
        cif_content = mof.to_cif()
        return cif_content
    except Exception as e:
        return f"Error generating MOF: {str(e)}"

# -------------------- Visualization Function -------------------- #

def show_stmol(content, file_format='cif', supercell=(1, 1, 1)):
    """
    Visualize the molecule using py3Dmol with optional supercell replication.

    Args:
        content (str): CIF or XYZ content of the molecule.
        file_format (str): Format of the content ('cif' or 'xyz').
        supercell (tuple): Number of repetitions in (a, b, c) directions.
    """
    from ase.io import read, write
    from io import StringIO

    try:
        bg_color = st.color_picker("Choose background color", "#161A1D")
        mol = py3Dmol.view(width=700, height=500)

        if supercell != (1, 1, 1):
            # Read the CIF content using ASE
            cif_io = StringIO(content)
            structure = read(cif_io, format='cif')
            # Create the supercell
            structure *= supercell
            # Convert the supercell structure to XYZ format
            xyz_io = StringIO()
            write(xyz_io, structure, format='xyz')
            xyz_content = xyz_io.getvalue()
            # Visualize the supercell
            mol.addModel(xyz_content, 'xyz')
        else:
            # Visualize the original unit cell
            mol.addModel(content, file_format)
            if file_format == 'cif':
                mol.addUnitCell()

        mol.setStyle({'stick': {}})
        mol.setBackgroundColor(bg_color)
        mol.zoomTo()
        showmol(mol, height=500, width=700)

    except Exception as e:
        st.error(f"An error occurred while visualizing the molecule: {e}")
