import streamlit as st
import random
import time

# 1. 페이지 설정 (제목, 이모지, 레이아웃)
st.set_page_config(
    page_title="💖 뽀짝MBTI의 비밀 여행 가방 🧳",
    page_icon="🔮",
    layout="centered"
)

# 2. 커스텀 CSS (귀엽고 깜찍한 파스텔 감성 + 카드 애니메이션)
st.markdown("""
<style>
    /* 전체 배경 그라데이션 및 폰트 */
    .stApp {
        background: linear-gradient(135deg, #FFF0F5 0%, #E6E6FA 100%);
        font-family: 'Comic Sans MS', 'Chalkboard SE', 'Nanum Gothic', sans-serif;
    }
    
    /* 제목 타이틀 스타일링 */
    .title-box {
        text-align: center;
        background: white;
        padding: 20px;
        border-radius: 30px;
        box-shadow: 0px 8px 20px rgba(255, 182, 193, 0.4);
        border: 3px dashed #FFB6C1;
        margin-bottom: 25px;
    }
    
    .title-text {
        color: #FF1493;
        font-size: 2.2rem;
        font-weight: 900;
        margin: 0;
    }
    
    .sub-text {
        color: #8A2BE2;
        font-size: 1rem;
        margin-top: 5px;
    }

    /* 선택 상자 및 라벨 */
    .stSelectbox label {
        color: #FF69B4 !important;
        font-size: 1.2rem !important;
        font-weight: bold;
    }

    /* 핑크 둥글둥글 버튼 */
    div.stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #FFB6C1, #FF69B4);
        color: white !important;
        border-radius: 25px !important;
        border: none !important;
        padding: 15px 30px !important;
        font-size: 1.3rem !important;
        font-weight: bold !important;
        box-shadow: 0px 5px 15px rgba(255, 105, 180, 0.4);
        transition: all 0.3s ease;
    }
    
    div.stButton > button:hover {
        transform: scale(1.03);
        box-shadow: 0px 8px 25px rgba(255, 105, 180, 0.6);
    }

    /* 추천 결과 카드 */
    .result-card {
        background: white;
        border-radius: 25px;
        padding: 25px;
        margin-top: 20px;
        border: 4px solid #FFC0CB;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        text-align: center;
    }

    .place-title {
        color: #FF1493;
        font-size: 1.8rem;
        font-weight: bold;
        margin-bottom: 10px;
    }

    .desc-text {
        color: #4A4A4A;
        font-size: 1.1rem;
        line-height: 1.6;
        background: #FFF5F7;
        padding: 15px;
        border-radius: 15px;
        margin: 15px 0;
    }

    /* 정보 태그 바 */
    .tag-container {
        display: flex;
        justify-content: space-around;
        margin-top: 15px;
    }

    .tag {
        background: #E6E6FA;
        color: #4B0082;
        padding: 8px 15px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# 3. 데이터베이스 (MBTI + 여행지 + 메이트 + 럭키아이템 + 추천 BGM)
mbti_db = {
    "ISTJ": {"place": "경주 황리단길 & 정갈한 유적지", "emoji": "🏯", "desc": "계획표대로 딱딱 맞춰 걷는 완벽하고 안락한 시간! 밤엔 동궁과 월지 야경으로 고요하게 감성 충전 🌙", "mate": "ESFP", "item": "⏱️ 탁상용 시계", "bgm": "🎧 피아노 소나타 모음집"},
    "ISFJ": {"place": "전주 한옥마을 다도 체험", "emoji": "🍵", "desc": "따스한 툇마루에 앉아 따뜻한 차 한 잔! 소중한 사람들과 도란도란 정다운 추억 쌓기 🍡", "mate": "ESTP", "item": "🍵 따뜻한 보온병", "bgm": "🎧 잔잔한 어쿠스틱 기타"},
    "INFJ": {"place": "스위스 인터라켄 동화 마을", "emoji": "🏔️", "desc": "눈앞에 펼쳐진 동화 같은 자연! 복잡한 생각은 지우고 웅장한 대자연 속에서 사색에 잠겨보세요 🌲", "mate": "ENFP", "item": "📓 일기장과 펜", "bgm": "🎧 지브리 오케스트라"},
    "INTJ": {"place": "영국 런던의 대형 박물관 투어", "emoji": "🏛️", "desc": "지적 호기심을 200% 충전하는 지식 탐험! 거대한 역사의 숨결을 차분하게 느낄 수 있는 오붓한 도시 🇬🇧", "mate": "ENTP", "item": "🎧 노이즈 캔슬링 헤드폰", "bgm": "🎧 클래식 체로 소나타"},
    "ISTP": {"place": "뉴질랜드 퀸스타운 번지점프", "emoji": "🪂", "desc": "백마디 말보다 직접 몸으로 느끼는 스릴! 답답함 싹 날려버리는 아드레날린 뿜뿜 액티비티 🇳🇿", "mate": "ESFJ", "item": "멀티툴(맥가이버 칼)", "bgm": "🎧 시원한 비트의 록 음악"},
    "ISFP": {"place": "제주도 돌담길 & 감성 오션뷰 카페", "emoji": "🍊", "desc": "알람 없이 누워서 시작하는 하루! 걷다가 끌리는 카페에 들어가 파도 소리 들으며 유유자적 힐링 🌊", "mate": "ENFJ", "item": "📸 필름 카메라", "bgm": "🎧 인디 뮤지션의 몽환적인 노래"},
    "INFP": {"place": "아이슬란드 오로라 몽환 돔 캠핑", "emoji": "🌌", "desc": "밤하늘에 쏟아지는 오로라 아래에서 낭만 1000% 충전! 상상 속 꿈꾸던 동화가 현실이 되는 곳 ❄️", "mate": "ENTJ", "item": "🧥 수분 촉촉 미스트", "bgm": "🎧 Lo-Fi 칠합 비트"},
    "INTP": {"place": "일본 교토의 비밀 사찰 & 헌책방", "emoji": "🏮", "desc": "사람 없는 조용한 골목길 탐방! 홀로 호기심 탐구하며 신비로운 분위기를 만끽하기 ⛩️", "mate": "ESTJ", "item": "📖 두꺼운 소설책", "bgm": "🎧 빗소리와 재즈 피아노"},
    "ESTP": {"place": "미국 라스베이거스 스트립 축제", "emoji": "🎰", "desc": "화려한 조명! 쉴 새 없이 터지는 이벤트! 온몸으로 에너지 느낄 준비 되셨나요? 🔥", "mate": "ISFJ", "item": "🕶️ 힙한 선글라스", "bgm": "🎧 신나는 EDM / 팝송"},
    "ESFP": {"place": "스페인 바르셀로나 플라멩코 페스티벌", "emoji": "💃", "desc": "보는 사람도 춤추게 만드는 흥의 도시! 맛있는 타파스 먹으며 새로운 친구들과 짠~! 🥂", "mate": "ISTJ", "item": "🎉 블링블링 액세서리", "bgm": "🎧 라틴 팝 & 댄스곡"},
    "ENFP": {"place": "발리 꾸따 해변 서핑 & 비치 파티", "emoji": "🏄‍♀️", "desc": "통통 튀는 텐션으로 파도 타기! 지나가는 모든 사람과 친구가 되는 기적을 경험해보세요 🌴", "mate": "INFJ", "item": "🎨 알록달록 비치타월", "bgm": "🎧 신나는 서프 록"},
    "ENTP": {"place": "몽골 고비 사막 은하수 질주", "emoji": "🐪", "desc": "평범한 건 거부한다! 사막 위를 달리고 밤엔 은하수 텐트에서 차원이 다른 엉뚱발랄 경험하기 ✨", "mate": "INTJ", "item": "🧭 방위 컴퍼스", "bgm": "🎧 인디 록 & 시티팝"},
    "ESTJ": {"place": "싱가포르 마리나베이 도심 호캉스", "emoji": "🏙️", "desc": "완벽하고 치밀한 동선, 5성급 호텔에서의 럭셔리함! 스마트하고 효율적인 완벽 투어 🇸🇬", "mate": "INTP", "item": "💳 혜택 좋은 트래블 카드", "bgm": "🎧 세련된 라운지 음악"},
    "ESFJ": {"place": "베트남 다낭 프리미엄 리조트 먹방", "emoji": "🥭", "desc": "너 한 입 나 한 입! 다정하게 맛있는 음식 나누며 다 같이 우정 뿜뿜 추억 남기기 💗", "mate": "ISTP", "item": "🎁 모두 나눠줄 간식 주머니", "bgm": "🎧 훈훈한 K-POP 발라드"},
    "ENFJ": {"place": "이탈리아 피렌체 로맨틱 골목길", "emoji": "🎨", "desc": "거리마다 따스함과 감성이 가득! 사랑하는 사람들에게 감동 선물해주고 인생샷 완성 🇮🇹", "mate": "ISFP", "item": "💌 예쁜 손편지지", "bgm": "🎧 감성 가득한 영화 OST"},
    "ENTJ": {"place": "미국 뉴욕 맨해튼 헬기 투어", "emoji": "🗽", "desc": "빌딩 숲 한가운데서 도심을 내려다보는 열정! 야망과 도전을 가득 채우고 돌아올 거대한 여행 🌆", "mate": "INFP", "item": "💼 간지나는 명함집/수첩", "bgm": "🎧 웅장한 영화 트레일러 음악"}
}

# 4. 상단 헤더 뷰
st.markdown("""
<div class="title-box">
    <h1 class="title-text">✨ 💖 MBTI 비밀 여행 가방 💖 ✨</h1>
    <p class="sub-text">🔮 나만의 성격 유형을 넣으면, 찰떡궁합 여행지를 뿅하고 꺼내드려요! ( 🌟‿🌟 )</p>
</div>
""", unsafe_allow_html=True)

# 5. 사용자 입력 섹션 (3컬럼 구조)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    selected_mbti = st.selectbox(
        "🎀 당신의 MBTI를 뽑아주세요!",
        list(mbti_db.keys()),
        index=6  # 기본값 INFP
    )
    
    st.write("") # 간격 조정
    start_button = st.button("✈️ 나만을 위한 여행 가방 싸기! ✨")

# 6. 결과 출력 영역
if start_button:
    # 깜찍한 로딩 효과
    with st.spinner("🎀 몽실몽실 여행 가방 싸는 중... 잠시만 기다려주세요! 🎀"):
        time.sleep(0.7)
    
    # 팡팡 터지는 애니메이션 
    st.balloons()
    st.snow()
    
    data = mbti_db[selected_mbti]
    
    # 예쁜 커스텀 디자인 카드 출력
    st.markdown(f"""
    <div class="result-card">
        <div style="font-size: 4rem;">{data['emoji']}</div>
        <div class="place-title">[{selected_mbti}] {data['place']}</div>
        <div class="desc-text">{data['desc']}</div>
        
        <div class="tag-container">
            <div class="tag">💘 찰떡 메이트: {data['mate']}</div>
            <div class="tag">🎒 행운 아이템: {data['item']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    
    # 추가 깜찍 요소: 음악 추천 & 럭키 쿠키
    c1, c2 = st.columns(2)
    with c1:
        st.info(f"🎵 **추천 여행 BGM**\n\n{data['bgm']}")
    with c2:
        cookie_msg = [
            "맛있는 디저트 먹을 운명이 보여요! 🍰",
            "인생샷 100장 건질 수 있어요! 📸",
            "생각지도 못한 귀여운 인연을 만날 거예요! 🐾",
            "여행지에서 득템할 운명이에요! 🎁"
        ]
        st.success(f"🥠 **오늘의 여행 포춘쿠키**\n\n{random.choice(cookie_msg)}")
