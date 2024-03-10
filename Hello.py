# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger




st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
      Streamlit is an open-source app framework built specifically for
      Machine Learning and Data Science projects.
      **👈 Select a demo from the sidebar** to see some examples
      of what Streamlit can do!
      ### Want to learn more?
      - Check out [streamlit.io](https://streamlit.io)
      - Jump into our [documentation](https://docs.streamlit.io)
      - Ask a question in our [community
        forums](https://discuss.streamlit.io)
      ### See more complex demos
      - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
      - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
  """
  )

#etape3
data_uploader = st.file_uploader("upload file", type={"csv", "txt", "las"})
if data_uploader is not None:
    data_uploader.seek(8)
    #for loading las files
    string= data_uploader.read().decode() 
    
    log= ls.read(string)
    temp_df1 = log.df()
    temp_df1 = temp_df1.reset_index()
    temp_df1.columns
    temp_df1.rename(columns={'DEPT':'DEPTH', 'SGRC' :' GR', 'TNPL': 'NPHI', 'PEF': 'PE', 'HSI':'CALI'
                            ,'SBD2':'RHOB','PRES2M16IN': 'RS', 'PRES500K48IN':'RT', 'SROP': 'ROP','SFXE': 'FEXP'}, inplace=True)
    temp_df1= temp_df1.dropna()


#etape 4
temp_df1=temp_df1[[ 'DEPTH', 'ROP', 'GR', 'NPHI', 'PE', 'CALI', 'RHOB', 'RS', 'RT', 'ROP', 'FEXP', 'RPM' ]] 
std_cali=temp_df1['CALI'].std()
std_gr=temp_df1['GR'].std()
std_p=temp_df1['NPHI'].mean() #Inbuilt function in Pandas Series
std_d=temp_df1['RHOB'].mean()
mean_r=temp_df1['RT'].mean()
data_df=temp_df1.copy()
    
#etape 5

#all libararies are not imported so import spatial
import scipy 
from scipy import spatial
dis_r=spatial.distance.cdist(
    d_list[i]['RS'].values.reshape(-1, len(d_list[i]['RS'].values)) ,
    d_list[i]['RT'].values.reshape(-1, len (d_list[i]['RT'].values))
)

#etape 6
def log_plot(well, df, depth_mdt, depth_mdt_actual, column_depth, column_GR, column_resistivity, column_NPHI, column_RHOB):
    import matplotlib.pyplot as plt
    from matplotlib.ticker import AutoMinorLocator
    fig, ax = plt.subplots(1,3, figsize=(28,22), dpi=55)
    fig.suptitle(well[0]+ 'Well Logs with Higlighted Pressure Recording Points', size=title_size, y=title_height)
    
    ax[0].minorticks_on()
    ax[8].grid(which='major', linestyle='-', linewidth='1', color='brown')
    ax[0].grid(which='minor', linestyle=':', linewidth='1.5', color='black')
    
    ax[1].minorticks_on()
    ax[1].grid(which='major', linestyle='-', linewidth='1', color='brown')
    ax[1].grid(which='minor', linestyle=':', linewidth='1.5', color='black')



fig1 = well_log_plot(well_name, temp_df1, depth_df_mdt,
                  depth_mdt_actual_7a8, 'DEPTH', 'GR', 'RT', 'NPHI', 'RHOB',
                  )
st.text('Well Data with Highlighted MDT Points')
#st.set_option(depreciation.showpyplotGlobalUse, False)
st.pyplot(fig1, width=35)
#pass through pyplot to maintain the quality of plot


