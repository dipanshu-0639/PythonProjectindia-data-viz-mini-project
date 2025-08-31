import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
df=pd.read_csv('india1.csv')

list_of_state=list(df['State'].unique())
list_of_state.insert(0,'Overall India')

st.sidebar.title('India Data visualization')

selected_state=st.sidebar.selectbox('Select a State',list_of_state)
primary=st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[5:]))
secondary=st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[5:]))

plot=st.sidebar.button('Plot Graph')

if plot:
    # Stylish section header
    st.markdown("""
        <div style="background-color:#1FBFA3;padding:10px;border-radius:10px;">
            <h2 style="color:#1565C0;"> India Data Visualization Dashboard  </h2>
        </div>
        """, unsafe_allow_html=True)

    # Beautiful legend with icons and colors
    st.markdown("""
        <hr>
        <span style="font-size:20px;color:#43A047;"> <b>Size</b></span> <span style="font-size:16px;">represents <b>Primary Parameter</b></span>  
        <br>
        <span style="font-size:20px;color:#1E88E5;"> <b>Color</b></span> <span style="font-size:16px;">represents <b>Secondary Parameter</b></span>
        <hr>
        """, unsafe_allow_html=True)

    # Add info or success banners
    st.success("Please select the desired parameters and click *Plot Graph* to visualize the data! ")

    # Use columns for neat layout
    col1, col2 = st.columns(2)
    col1.markdown(f"<span style='color:#E53935;font-size:18px;'> <b>Primary:</b> <code>{primary}</code></span>", unsafe_allow_html=True)
    col2.markdown(f"<span style='color:#3949AB;font-size:18px;'> <b>Secondary:</b> <code>{secondary}</code></span>", unsafe_allow_html=True)
    if selected_state=='Overall India':

        fig = px.scatter_map(df, lat="Latitude", lon="Longitude", size=primary,color=secondary,color_continuous_scale='Viridis',size_max=35,zoom=3,width=1200,height=700,hover_name='District',map_style="carto-positron")
        st.plotly_chart(fig,use_container_width=True)

    else:
        state_df=df[df['State']==selected_state]
        fig = px.scatter_map(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, color_continuous_scale='Viridis',size_max=35, zoom=3,hover_name='District',
                             width=1200, height=700, map_style="carto-positron")
        st.plotly_chart(fig, use_container_width=True)
