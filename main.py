import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(
    page_title="💖 내가 치이카와 캐릭터라면? 💖",
    page_icon="🐥",
    layout="centered"
)

# 2. 큐티 파스텔 디자인 (CSS)
st.markdown("""
<style>
    .stApp {
        background-color: #FFF9FB;
        font-family: 'Nanum Gothic', sans-serif;
    }
    
    .title-box {
        text-align: center;
        background: white;
        padding: 25px;
        border-radius: 30px;
        box-shadow: 0px 8px 20px rgba(255, 192, 203, 0.4);
        border: 3px dashed #FFB6C1;
        margin-bottom: 30px;
    }
    
    .main-title {
        color: #FF69B4;
        font-size: 2.1rem;
        font-weight: 900;
        margin: 0;
    }
    
    .result-card {
        background: white;
        border-radius: 25px;
        padding: 30px;
        border: 3px solid #FFC0CB;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        text-align: center;
    }

    div.stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #FFB6C1, #FF69B4);
        color: white !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 15px 20px !important;
        font-size: 1.3rem !important;
        font-weight: bold !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. 메인 타이틀
st.markdown("""
<div class="title-box">
    <h1 class="main-title">🎀 내가 치이카와 캐릭터라면? 🎀</h1>
    <p style="color: #8A2BE2; margin-top: 8px; font-weight: bold;">
        질문을 고르고 나의 치이카와 본캐를 찾아보세요! ✨
    </p>
</div>
""", unsafe_allow_html=True)

# 4. 테스트 질문 폼
with st.form("chiikawa_quiz"):
    st.subheader("Q1. 주말에 약속이 갑자기 취소되었을 때 당신은?")
    q1 = st.radio("", [
        "오히려 좋아! 집에서 푹 쉬면서 조용히 힐링 🛋️",
        "바로 긍정 파워! 다른 친구에게 연락해 나간다 📱",
        "우라!! 소리 지르고 하고 싶던 딴짓을 마구 한다 💃",
        "느긋하게 맛있는 안주나 간식을 세팅하고 혼술/혼밥 🍻",
        "전문가답게 자기계발을 하거나 빡세게 운동을 한다 ⚔️",
        "귀여운 나를 칭찬해 줄 사람을 찾아서 어슬렁거린다 🎀",
        "침대에 누워서 침착하게 개소리(?) 영상이나 침투부를 본다 🛏️",
        "인터넷 켜고 폼나게 관전하거나 악을 지른다 💥"
    ], key="q1")

    st.divider()

    st.subheader("Q2. 길 가다가 무서운 문제나 토벌 대상(괴물)을 만난다면?")
    q2 = st.radio("", [
        "으앙! 눈물 글썽이지만 용기를 쥐어짜서 맞선다 🥹",
        "'어떻게든 될 거야!' 하고 밝게 웃으며 해결책을 찾는다 🐱",
        "냅다 괴성을 지르며 몸으로 부딪쳐서 제압한다 🐰",
        "경험자의 여유로 한 발짝 뒤에서 차분하게 대처한다 🌰",
        "강력한 스승님 포스로 단칼에 빠르게 제압한다 🦦",
        "남 뒤로 쏙 숨어서 귀여운 척으로 넘어가려고 한다 🐿️",
        "킹받게 시비 걸다가 킹받는 표정으로 딴소리를 한다 👨‍🦲",
        "피파 하다가 골 먹힌 것처럼 샷건 치고 소리 지른다 ⚽"
    ], key="q2")

    st.divider()

    st.subheader("Q3. 내가 가장 바라는 완벽한 여행 스타일은?")
    q3 = st.radio("", [
        "조용하고 아기자기한 감성 카페 탐방 🍵",
        "친구들과 맛있는 거 나눠먹고 수다 떠는 힐링 여행 🥐",
        "어디로 튈지 모르는 스릴 만점 액티비티 🪂",
        "풍경 좋은 곳에서 묵묵히 즐기는 미식 식도락 🍱",
        "카리스마 넘치는 겉바속촉 디저트 탐방 🍰",
        "내가 세상에서 제일 빛나는 핫플 럭셔리 여행 👑",
        "킹받는 털보 빡빡이 친구와 둘이 떠나는 병맛 여행 👬",
        "인방 텐션 200% 터지는 미친 아드레날린 여행 🔥"
    ], key="q3")

    st.write("")
    submit = st.form_submit_button("✨ 나의 치이카와 본캐 결과 확인하기! ✨")

# 5. 결과 점수 계산
if submit:
    st.balloons()
    
    score = {
        "치이카와": 0, "하치와레": 0, "우사기": 0, "크리만쥬": 0,
        "랏코": 0, "모몽가": 0, "침주": 0, "감스트": 0
    }
    
    # Q1
    if "푹 쉬면서" in q1: score["치이카와"] += 1
    elif "다른 친구" in q1: score["하치와레"] += 1
    elif "우라!!" in q1: score["우사기"] += 1
    elif "혼술" in q1: score["크리만쥬"] += 1
    elif "자기계발" in q1: score["랏코"] += 1
    elif "칭찬해 줄" in q1: score["모몽가"] += 1
    elif "침착하게" in q1: score["침주"] += 3
    elif "관전하거나" in q1: score["감스트"] += 3

    # Q2
    if "눈물" in q2: score["치이카와"] += 1
    elif "어떻게든" in q2: score["하치와레"] += 1
    elif "몸으로 부딪쳐" in q2: score["우사기"] += 1
    elif "차분하게" in q2: score["크리만쥬"] += 1
    elif "단칼에" in q2: score["랏코"] += 1
    elif "귀여운 척" in q2: score["모몽가"] += 1
    elif "킹받게" in q2: score["침주"] += 3
    elif "피파" in q2: score["감스트"] += 3

    # Q3
    if "감성 카페" in q3: score["치이카와"] += 1
    elif "친구들과" in q3: score["하치와레"] += 1
    elif "액티비티" in q3: score["우사기"] += 1
    elif "식도락" in q3: score["크리만쥬"] += 1
    elif "디저트" in q3: score["랏코"] += 1
    elif "핫플" in q3: score["모몽가"] += 1
    elif "병맛" in q3: score["침주"] += 3
    elif "감스트" in q3: score["감스트"] += 3

    best_char = max(score, key=score.get)

    st.write("")
    
    # 6. 캐릭터별 결과 카드 출력
    if best_char == "치이카와":
        st.markdown("""
        <div class="result-card">
            <div style="font-size: 5rem;">🥹</div>
            <h2 style="color:#FF69B4;">겁 많지만 용기 있는 '치이카와'</h2>
            <p style="color:#666;">당신은 마음이 부드럽고 순수한 사랑둥이! 겁이 많아 눈물도 자주 흘리지만, 소중한 친구를 위해서라면 끝까지 용기를 내는 멋진 사람이에요.</p>
            <hr style="border:1px dashed #FFC0CB;">
            <p>✈️ <b>추천 찰떡 여행지:</b> 따뜻한 정이 있는 전주 한옥마을 🍡</p>
        </div>
        """, unsafe_allow_html=True)

    elif best_char == "하치와레":
        st.markdown("""
        <div class="result-card">
            <div style="font-size: 5rem;">🐱</div>
            <h2 style="color:#4169E1;">'어떻게든 될 거야!' 긍정왕 '하치와레'</h2>
            <p style="color:#666;">어떤 어려움이 와도 '어떻게든 될 거야!'를 외치는 초긍정 사교왕! 친구를 진심으로 아끼고 주변에 행복한 바이러스를 전파해요.</p>
            <hr style="border:1px dashed #FFC0CB;">
            <p>✈️ <b>추천 찰떡 여행지:</b> 에너지가 넘치는 발리 해변 🏄‍♂️</p>
        </div>
        """, unsafe_allow_html=True)

    elif best_char == "우사기":
        st.markdown("""
        <div class="result-card">
            <div style="font-size: 5rem;">🐰</div>
            <h2 style="color:#FFD700;">자유로운 영혼의 광기 '우사기'</h2>
            <p style="color:#666;">우라?! 야하-!! 남들 시선은 전혀 신경 쓰지 않는 미친 텐션의 자유로운 영혼! 예측 불가능하지만 알고 보면 능률 최강자예요.</p>
            <hr style="border:1px dashed #FFC0CB;">
            <p>✈️ <b>추천 찰떡 여행지:</b> 24시간 핫한 미국 라스베이거스 🎰</p>
        </div>
        """, unsafe_allow_html=True)

    elif best_char == "크리만쥬":
        st.markdown("""
        <div class="result-card">
            <div style="font-size: 5rem;">🌰</div>
            <h2 style="color:#D2691E;">캬-! 낭만을 아는 미식가 '크리만쥬'</h2>
            <p style="color:#666;">말없이 묵묵하지만 주변을 은근히 챙겨주는 어른스러운 스타일! 시원한 음료와 맛있는 안주 하나면 세상을 다 가진 듯 힐링하는 감성파입니다.</p>
            <hr style="border:1px dashed #FFC0CB;">
            <p>✈️ <b>추천 찰떡 여행지:</b> 운치 있는 일본 교토의 선술집 🍺</p>
        </div>
        """, unsafe_allow_html=True)

    elif best_char == "랏코":
        st.markdown("""
        <div class="result-card">
            <div style="font-size: 5rem;">🦦</div>
            <h2 style="color:#4682B4;">카리스마 속 반전 귀여움 '랏코 스승님'</h2>
            <p style="color:#666;">토벌 순위 1위의 엄청난 실력자! 겉은 쿨하고 카리스마 넘치지만 달콤한 파페를 좋아하는 엄청난 반전 매력의 소유자군요.</p>
            <hr style="border:1px dashed #FFC0CB;">
            <p>✈️ <b>추천 찰떡 여행지:</b> 스위스의 장엄한 대자연 🏔️</p>
        </div>
        """, unsafe_allow_html=True)

    elif best_char == "모몽가":
        st.markdown("""
        <div class="result-card">
            <div style="font-size: 5rem;">🐿️</div>
            <h2 style="color:#87CEEB;">칭찬해라!! 귀염둥이 떼쟁이 '모몽가'</h2>
            <p style="color:#666;">귀여움 하나로 세상을 정복하려는 욕망의 덩어리! 남들에게 오냐오냐 칭찬받는 걸 세상에서 제일 좋아하는 솔직 뻔뻔 사랑둥이예요.</p>
            <hr style="border:1px dashed #FFC0CB;">
            <p>✈️ <b>추천 찰떡 여행지:</b> 인생샷 천국 싱가포르 호캉스 🏙️</p>
        </div>
        """, unsafe_allow_html=True)

    # 🚨 히든 낚시 결과 1: 침착맨과 주호민
    elif best_char == "침주":
        st.markdown("""
        <div class="result-card" style="border: 4px solid #FF4500;">
            <div style="font-size: 5rem;">👨‍🦲🧔‍♂️</div>
            <h1 style="color:#FF4500; font-size: 1.8rem;">🚨 [대반전 낚시 성공!] 🚨</h1>
            <h2 style="color:#333;">당신은 치이카와가 아니라... '침착맨 & 주호민'입니다!</h2>
            <p style="color:#555;">
                치이카와 세상인 줄 알고 들어왔겠지만... 당신 안에 숨어있던 <b>킹받음과 털보+빡빡이 케미</b>가 폭발하고 말았습니다!<br>
                침투부 특유의 킹받는 텐션과 논리로 주변 사람을 킹받게 만드는 천재적인 재능을 가졌군요.
            </p>
            <hr style="border:1px dashed #FF4500;">
            <p>🎒 <b>필수 아이템:</b> 고피자 세트 & 킹받는 짤</p>
            <p>✈️ <b>추천 찰떡 여행지:</b> 침착맨 스트리밍 방구석 1열 🛏️</p>
        </div>
        """, unsafe_allow_html=True)

    # 🚨 히든 낚시 결과 2: 감스트
    elif best_char == "감스트":
        st.markdown("""
        <div class="result-card" style="border: 4px solid #1E90FF;">
            <div style="font-size: 5rem;">⚽💥</div>
            <h1 style="color:#1E90FF; font-size: 1.8rem;">💥 [대반전 낚시 성공!] 💥</h1>
            <h2 style="color:#333;">당신은 치이카와가 아니라... '감스트'입니다!</h2>
            <p style="color:#555;">
                귀여운 척 속였지만 속일 수 없는 <b>책상 샷건과 소리 지르기 텐션</b>!!<br>
                관전하다가 소리 지르고 리액션 뿜뿜하는 당신이야말로 인방계의 진정한 감스트 캐릭터입니다!
            </p>
            <hr style="border:1px dashed #1E90FF;">
            <p>🎒 <b>필수 아이템:</b> 튼튼한 책상 (샷건용) & 피파 카드팩</p>
            <p>✈️ <b>추천 찰떡 여행지:</b> 영국 프리미어리그 축구 직관 현장 ⚽</p>
        </div>
        """, unsafe_allow_html=True)
