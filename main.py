import streamlit as st
import random

# 페이지 설정 (제목, 이모지, 레이아웃)
st.set_page_config(
    page_title="💖 뽀짝MBTI 여행지 추천 💖",
    page_icon="✈️",
    layout="centered"
)

# MBTI별 큐티뽀짝 여행지 데이터
mbti_db = {
    "ISTJ": {"place": "📌 경주 역사 탐방", "desc": "차분하고 정돈된 분위기에서 야경과 유적지를 천천히 걷는 완벽한 계획 여행! 🌸", "emoji": "🏯"},
    "ISFJ": {"place": "📌 전주 한옥마을", "desc": "따뜻하고 아늑한 한옥에서 맛있는 음식 먹으며 조용하게 힐링하기 🍡", "emoji": "🍵"},
    "INFJ": {"place": "📌 스위스 인터라켄", "desc": "조용히 자연을 바라보며 사색에 잠길 수 있는 꿈같은 동화 속 마을 🏔️", "emoji": "🌲"},
    "INTJ": {"place": "📌 영국 런던", "desc": "박물관과 미술관, 역사가 깊은 거리에서 지적 호기심을 만끽하기 🏛️", "emoji": "🇬🇧"},
    "ISTP": {"place": "📌 뉴질랜드 퀸스타운", "desc": "자유롭게 스릴 만점 액티비티를 즐기며 스트레스 날려버리기! 🪂", "emoji": "🇳🇿"},
    "ISFP": {"place": "📌 제주도 돌담길", "desc": "발길 닿는 대로 유유자적 걷다가 만나는 예쁜 카페와 바다 전망 🌊", "emoji": "🍊"},
    "INFP": {"place": "📌 아이슬란드 레이캬비크", "desc": "밤하늘 몽환적인 오로라를 바라보며 감성 1000% 채우기 🌌", "emoji": "❄️"},
    "INTP": {"place": "📌 일본 쿄토", "desc": "고즈넉한 골목과 인적 드문 사찰을 홀로 탐방하는 조용한 로드 ⛩️", "emoji": "🏮"},
    "ESTP": {"place": "📌 미국 라스베이거스", "desc": "화려한 조명, 신나는 쇼! 에너지가 넘치는 짜릿한 도시 탐험 🎰", "emoji": "🇺🇸"},
    "ESFP": {"place": "📌 스페인 바르셀로나", "desc": "열정적인 음악과 춤, 언제나 축제 같은 분위기의 정열도시 💃", "emoji": "🇪🇸"},
    "ENFP": {"place": "📌 발리 꾸따 해변", "desc": "통통 튀는 에너지로 자유롭게 서핑하고 사람들과 어울리기! 🏄‍♀️", "emoji": "🌴"},
    "ENTP": {"place": "📌 몽골 울란바토르", "desc": "넓은 초원 위 사막을 질주하고 별을 보는 엉뚱하고 매력적인 여행 🐪", "emoji": "🇲🇳"},
    "ESTJ": {"place": "📌 싱가포르", "desc": "깔끔함의 정석! 체계적이고 효율적인 맞춤형 최고급 도심 여행 🏙️", "emoji": "🇸🇬"},
    "ESFJ": {"place": "📌 베트남 다낭", "desc": "사랑하는 사람들과 함께 다정하게 리조트 힐링과 먹방 즐기기 🥭", "emoji": "🇻🇳"},
    "ENFJ": {"place": "📌 이탈리아 피렌체", "desc": "낭만적이고 로맨틱한 거리에서 사람들과 훈훈한 추억 쌓기 🎨", "emoji": "🇮🇹"},
    "ENTJ": {"place": "📌 미국 뉴욕", "desc": "열정 넘치는 사람들과 빌딩 숲 사이에서 리더십을 충전하는 여행 🗽", "emoji": "🌆"}
}

# 핑크핑크한 예쁜 스타일 적용 (CSS)
st.markdown("""
    <style>
    .main {
        background-color: #FFF0F5;
    }
    .stSelectbox label {
        color: #FF69B4 !important;
        font-size: 1.2rem !important;
        font-weight: bold;
    }
    .stButton>button {
        background-color: #FFB6C1;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
        font-size: 1.1rem;
    }
    .stButton>button:hover {
        background-color: #FF69B4;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# 메인 화면 귀여운 타이틀
st.title("💖 뽀짝뽀짝 MBTI 여행지 추천 ✈️")
st.write("당신의 **MBTI**를 알려주시면 취향저격 맞춤형 여행지를 찾아드릴게요! ( 🌟‿🌟 )")

st.divider()

# 사용자 입력 (MBTI 선택박스)
mbti_list = list(mbti_db.keys())
user_mbti = st.selectbox("👇 당신의 MBTI를 선택해 주세요!", mbti_list)

# 버튼 클릭 이벤트
if st.button("✨ 나만의 맞춤 여행지 알려줘! ✨"):
    # 풍선 팡팡 이펙트
    st.balloons()
    
    data = mbti_db[user_mbti]
    
    st.markdown(f"### 🎀 {user_mbti}만을 위한 찰떡 여행지 🎀")
    
    # 카드 형태로 결과 보여주기
    with st.container():
        st.info(f"{data['emoji']} **추천 destination:** **{data['place']}**\n\n{data['desc']}")
    
    # 귀여운 마무리 응원 문구
    wishes = [
        "행복하고 안전한 여행이 되길 바랄게요! 💕",
        "인생샷 1000장 찍고 올 준비 하세요! 📸",
        "생각만 해도 두근두근 떨리는 여행이 될 거예요! 💓"
    ]
    st.success(f"🎉 {random.choice(wishes)}")
