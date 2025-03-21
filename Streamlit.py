import streamlit as st
from streamlit_ketcher import st_ketcher  # Import the Streamlit Ketcher component
from streamlit.components.v1 import html
import os
import subprocess
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
import utils
sys.path.append(os.path.abspath('mofography'))

# -------------------- Main Application -------------------- #

def main():
    st.title("MOF Design and Analysis App")


    st.header("Choose A Metal Organic Framework From Below:")
    mof_dir = 'mof_files'
    if not os.path.exists(mof_dir):
        st.error(f"The directory '{mof_dir}' does not exist. Please ensure it contains CIF files.")
        return

    mof_files = [f for f in os.listdir(mof_dir) if f.endswith('.cif')]
    if not mof_files:
        st.error(f"No CIF files found in the '{mof_dir}' directory.")
        return

    mof_names = [os.path.splitext(f)[0] for f in mof_files]  # Remove .cif extension for display
    mof_name = st.selectbox("Choose MOF", mof_names)

    if mof_name:
        cif_file_path = os.path.join(mof_dir, mof_name + ".cif")
        cif_content = utils.load_cif_file(cif_file_path)
        if not cif_content:
            st.error("Failed to load CIF content.")
            return
        utils.display_mof_info(mof_name)

        st.subheader("3D Visualization")
        # Add input fields for supercell dimensions
        st.write("Specify supercell dimensions (number of unit cells in each direction):")
        col1, col2, col3 = st.columns(3)
        with col1:
            a = st.number_input('a', min_value=1, max_value=5, value=1, step=1, key='a_view')
        with col2:
            b = st.number_input('b', min_value=1, max_value=5, value=1, step=1, key='b_view')
        with col3:
            c = st.number_input('c', min_value=1, max_value=5, value=1, step=1, key='c_view')
        supercell = (a, b, c)

        # Visualize the generated MOF
        st.subheader("3D Visualization")
        utils.show_stmol(cif_content, file_format='cif', supercell=supercell)

        # Compute and display surface area
        st.subheader("Surface Area Analysis")
        with st.spinner("Computing surface area..."):
            surface_area = utils.compute_surface_area(cif_file_path)
        if surface_area:
            st.success(f"Surface Area: {surface_area:.2f} m²/g")
        else:
            st.error("Failed to compute surface area.")


if __name__ == "__main__":
    main()
