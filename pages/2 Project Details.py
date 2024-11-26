import streamlit as st
st.title('PROJECT-1')


plan=r"Image\Plan.png"
st.image(plan)
st.text('Architect-MD.HASAN MAHMUD')
st.header('Animation')
video= r"Image\v.MP4"
st.video(video, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)