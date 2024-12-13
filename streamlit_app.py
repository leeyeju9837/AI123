#기본적인 Streamlit 페이지 예제

# streamlit_app.py
import streamlit as st
import pandas as pd

# 1. 제목
st.title("이예주의 스트림릿 서비스")

# 2. 부제목
st.subheader("루시의 서비스")

# 3. 판다스 데이터프레임 기반 표 출력
df = pd.DataFrame({
    "이름": ["신예찬", "최상엽", "조원상","신광일기본적인 Streamlit 페이지 예제

# streamlit_app.py
import streamlit as st
import pandas as pd

# 1. 제목
st.title("이예주의 스트림릿 서비스")

# 2. 부제목
st.subheader("루시의 서비스")

# 3. 판다스 데이터프레임 기반 표 출력
df = pd.DataFrame({
    "이름": ["신예찬", "최상엽", "조원상","신광일"],
    "나이": [32, 30, 28, 27],
    "국적": ["Korea", "Korea", "Korea", "Korea"]
})
st.write("데이터프레임 예제")
st.dataframe(df)

# 4. HTML 활용 예제
st.write("HTML 예제")
st.markdown(
    """
    <div style="color: blue; font-size: 20px;">
        HTML을 활용한 예시 텍스트입니다.
    </div>
    """,
    unsafe_allow_html=True
)

# 5. HTML과 CSS 활용 예제
st.write("HTML과 CSS 예제")
st.markdown(
    """
    <style>
    .styled-box {
        padding: 10px;
        margin: 5px;
        background-color: lightgreen;
        border-radius: 5px;
        color: darkgreen;
    }
    </style>
    <div class="styled-box">
        HTML과 CSS를 함께 사용하여 스타일링한 박스입니다.
    </div>
    """,
    unsafe_allow_html=True
)

# 6. 이미지 표시
st.write("루시밴드 멤버들")
st.image("https://i.namu.wiki/i/5vsFbyVySITxUZ29vVbtKQtVnoi_r0ops0cpTOvOANQyJTw9rTV5993iEbmOxKz5h7334XztsENl2I0NekMKGouILphoabHQVLOxNxgwztrEyhqTFQs-s2XXc0UEsRx0jN2nQLLZrBAxiaU0peQtQQ.webp", caption="Streamlit 로고")

# 7. 유튜브 링크 (썸네일 표시)
st.write("유튜브 동영상 예제")
st.video("https://www.youtube.com/watch?v=B2iAodr0fOo")

