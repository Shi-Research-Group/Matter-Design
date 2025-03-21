import mofography as mgr
from pathlib import Path
from ase.io import read
from ase.data import vdw_radii
from ase.units import _amu
import numpy as np


path_to_cif = Path("./fidriv_clean.cif")
mat_atoms = read(path_to_cif)
# compute the distance grid, use a finer grid for more resoluation
# or interpolate using mgr.zoom_grid(dgrid, 2)
dgrid = mgr.dgrid_from_atoms(mat_atoms, spacing=0.5)
# let's set a probe radius and compute the isosurface, in this case let's use helium
probe_radius = vdw_radii[2]  #   helium atomic number is 2
isosurface_mesh = mgr.get_isosurface_mesh(dgrid, probe_radius, mat_atoms)
mass_g = mat_atoms.get_masses().sum() * _amu * 1000  # this is in grams
sa_m2g = isosurface_mesh.area_faces.sum() * 1e-20 / mass_g

# compute the void volume in different units, same probe
# also same as probe-occupiable volume
void_fraction = np.sum(dgrid > 0) / dgrid.size
voxel_volume = mat_atoms.get_volume() / dgrid.size  # this is in A^3
void_volume = np.sum(dgrid > probe_radius) * voxel_volume  # this is in A^3
void_volume_cc_cc = void_volume / mat_atoms.get_volume()  # this is in A^3/A^3
mass_g = mat_atoms.get_masses().sum() * _amu * 1000  #  this is in g
void_volume_cc_g = void_volume * 1e-24 / mass_g  # this is in cm^3/g