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
# Title of the page
st.title("YouTube and Quizizz Embed Page")

# YouTube Embed
st.header("Embed a YouTube Video")
video_id = st.text_input("Enter the YouTube video ID (e.g., dQw4w9WgXcQ):")
if video_id:
    video_url = f"https://www.youtube.com/embed/{video_id}"
    st.markdown(f'<iframe width="560" height="315" src="{video_url}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

# Quizizz Embed
st.header("Embed a Quiz from Quizizz")
quiz_id = st.text_input("Enter the Quizizz quiz ID:")
if quiz_id:
    quiz_url = f"https://quizizz.com/join/quiz/{quiz_id}/start"
    st.markdown(f'<iframe src="{quiz_url}" width="100%" height="600px" frameborder="0"></iframe>', unsafe_allow_html=True)

st.sidebar.text("Made with Streamlit")
Here’s how this code works:

The st.text_input function is used to get the YouTube video ID and Quizizz quiz ID from the user.
Once these IDs are provided, the respective URLs are constructed.
The st.markdown function with the unsafe_allow_html=True parameter is used to embed the constructed URLs as iframes.
Please note: The use of unsafe_allow_html=True can be a security risk if you allow untrusted content to be embedded or displayed. Make sure you trust the content you're embedding.








if __name__ == "__main__":
    run()
