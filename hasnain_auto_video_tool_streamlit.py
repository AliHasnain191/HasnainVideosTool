import streamlit as st
from moviepy.editor import VideoFileClip, concatenate_videoclips

st.set_page_config(page_title="Hasnain Auto Video Tool", layout="centered")
st.title("🎬 Hasnain Auto Video Generator")
st.markdown("**Upload multiple video clips, merge them, and download the final video.**")

uploaded_files = st.file_uploader("📁 Upload multiple video clips", type=["mp4", "mov", "avi"], accept_multiple_files=True)

if uploaded_files:
    clips = []
    for file in uploaded_files:
        with open(file.name, "wb") as f:
            f.write(file.getbuffer())
        clips.append(VideoFileClip(file.name))

    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile("output.mp4")

    with open("output.mp4", "rb") as f:
        st.download_button("⬇️ Download Final Video", f, file_name="merged_video.mp4", mime="video/mp4")