__author__ = 'uhs374h'

from obspy.core import read

st = read("19135123.mseed")
st.plot()