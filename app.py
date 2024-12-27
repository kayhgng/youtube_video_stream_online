import streamlit as st
import re
import time

# Language Selection
language = st.sidebar.selectbox("Select Language", ["English", "فارسی"])

# Define text content for both languages
if language == "English":
    title = "Stream and Watch Youtube videos Online"
    info = "Developed by Alikay_h --> github.com/kayhgng"
    subheader = "Watch Youtube videos without annoying Comments and Ads, Just Be relax"
    url_input_label = "Video URL"
    url_input_placeholder = "Enter Youtube video URL"
    button_label = "Lets Go!"
    spinner_label = "Loading"
    error_message = "Your video address is invalid dude!"
    additional_info = """
        <div style="text-align: left;">
            You are looking to watch youtube online without any comments and annoying other contents, We developed This Application for you!
        </div>
    """
else:
    title = "دیدن ویدیو یوتیوب آنلاین"
    subheader = "ویدیو یوتیوبو ببین بدون تبلیغ و کامنت فقط تمرکز کن"
    info = "توسعه دهنده: Alikay_h --> github.com/kayhgng"
    url_input_label = "آدرس ویدیو"
    url_input_placeholder = "یه آدرس ویدیو وارد کن"
    button_label = "بزن بریم!"
    spinner_label = "در حال بارگذاری ویدیو..."
    error_message = "آدرست اشتباهه عزیز"
    additional_info = """
        <div style="text-align: right;">
            آیا به دنبال راهی برای افزایش تجربه تماشای یوتیوب هستید؟
            <br>
            بیش از این نگاه نکنید! این اپلیکیشن رابط کاربری تمیز و مینیمالی را برای تجربه ای بدون حواس پرتی ارائه می دهد.
            <br>
            <br>
            فرقی نمی کند معلم، استاد، دانش آموز یا سازمان دهنده باشید، می توانید از اپلیکیشن ما برای حذف تبلیغات، نظرات و ویدیوهای ناخواسته و نامناسب که ممکن است در نوار کناری ظاهر شوند، استفاده کنید.
            <br>
            شما می توانید اطمینان حاصل کنید که دانش آموزان شما تنها محتوایی را که می خواهید ببینند، در حالی که تجربه خود را عاری از حواس پرتی نگه دارید.
        </div>
    """

# Title and Description
st.title(title)
st.subheader(subheader)
st.info(info)

# Function to extract video ID from URL
def extract_video_id(url):
    regex = re.compile(r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})', re.IGNORECASE)
    match = regex.search(url)
    return match.group(1) if match else None

# Function to display the video
def display_video(video_id):
    st.markdown(
        f'<div class="video-container" style="position: relative; width: 100%; max-width: 1024px; margin: 2rem auto; padding-bottom: 56.25%; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); background-color: #fff;">'
        f'<iframe src="https://www.youtube-nocookie.com/embed/{video_id}" frameborder="0" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border-radius: 10px;"></iframe>'
        f'</div>',
        unsafe_allow_html=True
    )
    st.write("---")

# Form for entering YouTube URL
video_url = st.text_input(url_input_label, placeholder=url_input_placeholder)

# Button to play the video
if st.button(button_label):
    with st.spinner(spinner_label):
        time.sleep(5)  # Wait for 5 seconds
    st.success("Have Fun! - Alikay_h")
    video_id = extract_video_id(video_url)
    if video_id:
        display_video(video_id)
    else:
        st.error(error_message)

# Additional Information
st.markdown(additional_info, unsafe_allow_html=True)

# Footer
st.write("---")
st.write("YouTube is the source of content")
st.write("[Made with 🖤 in KayHGNG](https://github.com/kayhgng) | This website **does not store** any data such as cookies to enable essential site functionality.")
st.markdown("---", unsafe_allow_html=True)
