"""
Streamlit web application that demonstrates a simple interface for askhelmut.

This module creates a web interface using Streamlit to demonstrate the usage of the service provided by
askhelmut.
"""

import streamlit as st

from askhelmut import (
    Service,
    __version__,
)

sidebar = st.sidebar
sidebar.write(
    f" [askhelmut v{__version__}](https://askhelmut.readthedocs.io/en/latest/)",
)
sidebar.write("Built with love in Berlin 🐻")

st.title("🤖 askhelmut ")

# Initialize the service
service = Service()

# Get the message
message = service.get_hello_world()

# Print the message
st.write(f"{message}")
