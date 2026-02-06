import streamlit as st
import streamlit.components.v1 as components

# Constrain the main container to a phone-like width and tighten padding
st.set_page_config(page_title="Live Feed Viewer", layout="centered")
st.markdown(
	"""
	<style>
	.reportview-container .main .block-container{
		max-width:420px;
		padding-left:12px;
		padding-right:12px;
	}
	footer {visibility: hidden;}
	</style>
	""",
	unsafe_allow_html=True,
)

st.title("📹 Live Feed Viewer")

# Default live feed URL (you can change this in the code or via the text input)
DEFAULT_FEED = "http://10.0.0.131:8501/video_feed"

# Move feed settings to the top (better for small screens)
st.header("Feed settings")
feed_url = st.text_input("Live feed URL", value=DEFAULT_FEED)

st.markdown(f"**Streaming from:** {feed_url}")

# Embed the live feed using an iframe sized for phones
components.iframe(feed_url, width=360, height=720, scrolling=False)
