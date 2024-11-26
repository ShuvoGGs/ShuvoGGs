import streamlit as st
st.title('PROJECT-1')
st.header('A POEM of BRICK AND LIGHT')
st.text("A Poem of Brick and Light” is a building that speaks the language of both structure and soul. Its walls, composed of sturdy brick, are not merely foundations but verses in a timeless narrative, each brick a word, each seam a stanza. Light spills through the openings, illuminating the interior like thoughts catching the sun, casting shadows that dance like lines of poetry in motion. This architectural ode merges the tactile warmth of the earth with the ethereal glow of enlightenment, creating a space where every corner whispers of inspiration and every surface hums with the quiet rhythm of a story yet to be fully told")
cover_photo=r'Image\extended_a3_image.jpg'
st.image(cover_photo)
plan=r"Image\Plan.png"
st.image(plan)
st.text('Architect-MD.HASAN MAHMUD')
st.header('Animation')
video= r"Image\v.MP4"
st.video(video, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)