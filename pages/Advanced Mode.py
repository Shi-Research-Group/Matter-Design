import streamlit as st
from streamlit_ketcher import st_ketcher
from streamlit.components.v1 import html
from ase.io import read, write
from pyperclip import copy
from stmol import showmol
import pormake as pm
import utils

# Advanced Mode: Design Your Own MOF
def advanced_page():
    st.header("Advanced Mode: Design Your Own MOF")

    # Step 1: Select a Node
    st.subheader("Step 1: Select a Node")
    node_options = {
        "Zn(II) Node": "[Zn+2]",  
        "Cu(II) Paddlewheel": "[Cu+2]",  
        # Add more nodes with their SMILES representations
    }
    node = st.selectbox("Choose Node", list(node_options.keys()))
    node_smiles = node_options[node]

    # Step 2: Select a Topology (Based on Node)
    st.subheader("Step 2: Select a Topology")
    topology_options = {
        "Zn(II) Node": ["pcu", "fcu", "bcu"],
        "Cu(II) Paddlewheel": ["sql", "tbo", "pts"],
        # Define topologies for different nodes
    }
    available_topologies = topology_options.get(node, [])
    topology = st.selectbox("Choose Topology", available_topologies)

    # Step 3: Select or Create a Linker
    st.subheader("Step 3: Select or Create a Linker")
    linker_choice = st.radio("Linker Options", ["Select from Preset Linkers", "Draw Your Own Linker"])

    if linker_choice == "Select from Preset Linkers":
        linker_options = {
            "Terephthalic Acid": "OC(=O)c1ccccc1C(=O)O",
            "BPDC": "OC(=O)c1ccc(cc1)C(=O)O",
        }
        linker = st.selectbox("Choose Linker", list(linker_options.keys()))
        linker_smiles = linker_options[linker]
    else:
        st.subheader("Draw Linker with Chemical Molecule Component")
        linker_smiles = st_ketcher()
        if linker_smiles:
            st.write("SMILES String:")
            st.text(linker_smiles)
        else:
            st.warning("Please draw a molecule to generate a SMILES string.")

    # Step 4: Generate MOF
    if st.button("Generate MOF"):
        if linker_smiles and node_smiles and topology:
            with st.spinner('Generating CIF...'):
                cif_content = utils.run_pormake(node_smiles, linker_smiles, topology)

            if cif_content:
                st.success("CIF Generated Successfully!")
                st.code(cif_content, language='cif')
                st.markdown(utils.generate_download_link(cif_content, "generated_mof.cif"), unsafe_allow_html=True)

                # Supercell dimensions
                st.subheader("Specify Supercell Dimensions")
                col1, col2, col3 = st.columns(3)
                with col1:
                    a = st.number_input('a', min_value=1, max_value=5, value=1, step=1, key='a_make')
                with col2:
                    b = st.number_input('b', min_value=1, max_value=5, value=1, step=1, key='b_make')
                with col3:
                    c = st.number_input('c', min_value=1, max_value=5, value=1, step=1, key='c_make')
                supercell = (a, b, c)

                # Visualize the generated MOF
                st.subheader("3D Visualization")
                utils.show_stmol(cif_content, file_format='cif', supercell=supercell)

                # Analyze with ZEO++
                st.subheader("MOF Analysis")
                with st.spinner('Analyzing with ZEO++...'):
                    zeopp_result = utils.run_zeopp(cif_content)

                if zeopp_result:
                    st.write(zeopp_result)
        else:
            st.error("Please select a node, topology, and provide a valid linker SMILES string.")

advanced_page()