import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="💖 나의 성향으로 알아보는 캐릭터 테스트 💖",
    page_icon="🔮",
    layout="centered"
)

# 커스텀 큐티 CSS
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
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# 타이틀
st.markdown("""
<div class="title-box">
    <h1 class="main-title">🎀 나의 라이프스타일 캐릭터 테스트 🎀</h1>
    <p style="color: #8A2BE2; margin-top: 8px; font-weight: bold;">
        8개의 세밀한 질문으로 나만의 숨겨진 본캐 캐릭터를 찾아보세요! ✨
    </p>
</div>
""", unsafe_allow_html=True)

# 질문 폼
with st.form("personality_quiz"):
    
    # Q1
    st.subheader("Q1. 주말에 갑자기 예정되어 있던 약속이 취소되었을 때 당신은?")
    q1 = st.radio("", [
        "아쉬우니까 지금이라도 나올 수 있는 다른 친구들을 물색해 본다.",
        "오히려 좋아! 혼자 조용히 집에서 쉬거나 영화를 본다.",
        "갑자기 생긴 자유시간! 평소 미뤄뒀던 액티비티나 즉흥적인 일을 벌인다.",
        "소파나 침대에 누워 모바일 게임을 하거나 인강/영상 스트리밍을 정주행한다."
    ], key="q1")
    st.divider()

    # Q2
    st.subheader("Q2. 낯선 사람들과 함께하는 모임이나 파티에 갔을 때 당신의 모습은?")
    q2 = st.radio("", [
        "처음엔 어색해서 구석에 있지만, 누군가 먼저 말을 걸어주면 잘 호응한다.",
        "주도적으로 분위기를 띄우며 사람들에게 질문을 던지고 친해진다.",
        "대화의 맥락과 상관없이 갑자기 웃기거나 엉뚱한 한 마디로 존재감을 나타낸다.",
        "약간 킹받게(?) 유머러스한 장난을 치거나 주변 반응을 관찰하며 즐긴다."
    ], key="q2")
    st.divider()

    # Q3
    st.subheader("Q3. 예상치 못한 큰 문제나 지연 상황(비행기 지연, 일정 차질)이 발생했다면?")
    q3 = st.radio("", [
        "'어떻게든 해결책이 있겠지!' 긍정적으로 생각하며 빠르게 다음 대안을 찾는다.",
        "순간 당황해서 가슴이 철렁하지만, 마음을 가다듬고 주변에 도움을 요청한다.",
        "해결책을 고민하기보단 우선 감정이나 답답함을 소리로 표현하거나 스트레스를 풀 방법을 찾는다.",
        "전문적이고 능숙하게 매뉴얼을 확인하거나 상황을 깔끔하게 정리한다."
    ], key="q3")
    st.divider()

    # Q4
    st.subheader("Q4. 힘든 하루를 마치고 집에 돌아왔을 때 가장 필요한 나만의 힐링 방식은?")
    q4 = st.radio("", [
        "시원한 음료나 맛있는 야식을 세팅하고 혼자 넷플릭스 보며 혼술/혼밥하기",
        "달콤한 디저트나 카페 음료를 마시며 나만의 리프레시 시간 갖기",
        "친구에게 전화해서 오늘 있었던 일 폭풍 수다 떨기",
        "소리를 지르거나 게임에 몰입하면서 아드레날린 뿜뿜 시키기"
    ], key="q4")
    st.divider()

    # Q5
    st.subheader("Q5. 친구가 나에게 '너 진짜 독특하다'라는 말을 했을 때 나의 반응은?")
    q5 = st.radio("", [
        "독특한가...? 내가 이상한가 싶어서 살짝 신경 쓰이고 걱정된다.",
        "칭찬으로 받아들이고 내 매력을 알아본 것 같아 내심 흐뭇해한다.",
        "칭찬이지? 고마워! 하고 당당하게 넘긴다.",
        "어쩌라고? 내 맘인데~ 하며 별 신경 안 쓴다."
    ], key="q5")
    st.divider()

    # Q6
    st.subheader("Q6. 쇼핑하러 갔을 때 당신의 소비 패턴에 가장 가까운 것은?")
    q6 = st.radio("", [
        "아기자기하고 귀여운 소품을 보면 나도 모르게 장바구니에 담는다.",
        "실용적이고 퀄리티 높은 제품 위주로 꼼꼼하게 비교해서 구매한다.",
        "눈에 띄는 핫아이템이나 남들에게 보여주기 좋은 화려한 것을 선택한다.",
        "사고 싶은 게 생기면 묻지도 따지지도 않고 바로 충동구매한다."
    ], key="q6")
    st.divider()

    # Q7
    st.subheader("Q7. 여럿이서 게임을 할 때 당신이 주로 맡는 역할은?")
    q7 = st.radio("", [
        "팀원들을 챙기고 긍정적인 파이팅을 불어넣는 분위기 메이커",
        "조용히 실력을 발휘해서 버스 기사 역할을 해주는 에이스",
        "게임 내용보다는 채팅이나 음성으로 훈수 두고 킹받게 만드는 트롤/개그 캐릭터",
        "지면 책상 치거나 소리 지르며 제일 몰입해서 승부욕을 불태우는 열정파"
    ], key="q7")
    st.divider()

    # Q8
    st.subheader("Q8. 당신이 생각하는 이상적인 휴가 장소는?")
    q8 = st.radio("", [
        "조용하고 감성 가득한 시골 마을이나 한옥 게스트하우스",
        "볼거리, 먹거리, 럭셔리한 핫플이 즐비한 휴양지",
        "언제 무슨 일이 터질지 모르는 액티비티 & 스릴 넘치는 해외 도시",
        "스포츠 경기 관람이나 스트리밍 방송과 함께하는 텐션 높고 아드레날린 터지는 곳"
    ], key="q8")

    st.write("")
    submit = st.form_submit_button("✨ 나의 본캐 캐릭터 결과 확인하기 ✨")

# 점수 계산 알고리즘
if submit:
    st.balloons()
    
    score = {
        "치이카와": 0, "하치와레": 0, "우사기": 0, "크리만쥬": 0,
        "랏코": 0, "모몽가": 0, "침주": 0, "감스트": 0
    }
    
    # Q1 가산점
    if "다른 친구" in q1: score["하치와레"] += 2
    elif "조용히 집" in q1: score["치이카와"] += 2; score["크리만쥬"] += 1
    elif "액티비티" in q1: score["우사기"] += 2
    elif "정주행" in q1: score["침주"] += 3; score["감스트"] += 1

    # Q2 가산점
    if "말을 걸어주면" in q2: score["치이카와"] += 2
    elif "주도적으로" in q2: score["하치와레"] += 2
    elif "엉뚱한 한 마디" in q2: score["우사기"] += 2
    elif "킹받게" in q2: score["침주"] += 3

    # Q3 가산점
    if "긍정적으로" in q3: score["하치와레"] += 2
    elif "당황해서" in q3: score["치이카와"] += 2
    elif "감정이나 답답함" in q3: score["우사기"] += 1; score["감스트"] += 3
    elif "전문적이고" in q3: score["랏코"] += 3

    # Q4 가산점
    if "혼술/혼밥" in q4: score["크리만쥬"] += 3
    elif "디저트" in q4: score["랏코"] += 2
    elif "폭풍 수다" in q4: score["하치와레"] += 2
    elif "소리를 지르거나" in q4: score["감스트"] += 3

    # Q5 가산점
    if "신경 쓰이고" in q5: score["치이카와"] += 2
    elif "내심 흐뭇" in q5: score["모몽가"] += 3
    elif "당당하게" in q5: score["우사기"] += 2
    elif "어쩌라고" in q5: score["침주"] += 2

    # Q6 가산점
    if "아기자기" in q6: score["치이카와"] += 2
    elif "실용적" in q6: score["랏코"] += 2
    elif "핫아이템" in q6: score["모몽가"] += 3
    elif "충동구매" in q6: score["우사기"] += 2; score["감스트"] += 1

    # Q7 가산점
    if "분위기 메이커" in q7: score["하치와레"] += 2
    elif "에이스" in q7: score["랏코"] += 2
    elif "킹받게" in q7: score["침주"] += 3
    elif "열정파" in q7: score["감스트"] += 3

    # Q8 가산점
    if "시골 마을" in q8: score["치이카와"] += 2; score["크리만쥬"] += 1
    elif "핫플" in q8: score["모몽가"] += 2
    elif "스릴 넘치는" in q8: score["우사기"] += 2
    elif "아드레날린" in q8: score["감스트"] += 3; score["침주"] += 1

    # 최고 점수 계산
    best_char = max(score, key=score.get)

    st.write("")
    
    # 결과 화면
    if best_char == "치이카와":
        st.markdown("""
        <div class="result-card">
            <div style="font-size: 4.5rem;">🥹</div>
            <h2 style="color:#FF69B4;">마음 따뜻한 용기파 '치이카와'</h2>
            <p style="color:#666;">당신은 순수하고 다정한 감성의 소유자! 걱정이 많아 쉽게 당황하기도 하지만, 소중한 사람을 위해서라면 끝까지 용기를 내는 멋진 면모를 가지고 있어요.</p>
            <hr style="border:1px dashed #FFC0CB;">
            <p>✈️ <b>추천 힐링 장소:</b> 따뜻한 정이 남아있는 잔잔한 감성 시골 마을 🍡</p>
        </div>
        """, unsafe_allow_html=True)

    elif best_char == "하치와레":
        st.markdown("""
        <div class="result-card">
            <div style="font-size: 4.5rem;">🐱</div>
            <h2 style="color:#4169E1;">초긍정 서포터 '하치와레'</h2>
            <p style="color:#666;">어떤 나쁜 상황 속에서도 '어떻게든 될 거야!'를 외치는 긍정왕! 친구들을 진심으로 아끼며 주변에 맑은 에너지를 퍼뜨리는 타입입니다.</p>
            <hr style="border:1px dashed #FFC0CB;">
            <p>✈️ <b>추천 힐링 장소:</b> 사람들의 웃음소리가 넘치는 휴양지 해변 🏄자</p>
        </div>
        """, unsafe_allow_html=True)

    elif best_char == "우사기":
        st.markdown("""
        <div class="result-card">
            <div style="font-size: 4.5rem;">🐰</div>
            <h2 style="color:#FFD700;">자유로운 영혼의 능력자 '우사기'</h2>
            <p style="color:#666;">남의 시선 따위는 신경 쓰지 않는 미친 텐션과 마이웨이! 막무가내처럼 보여도 행동력이 뛰어나고 본업은 기막히게 잘 해내는 반전 실력자입니다.</p>
            <hr style="border:1px dashed #FFC0CB;">
            <p>✈️ <b>추천 힐링 장소:</b> 24시간 멈추지 않는 액티비티 천국 🎰</p>
        </div>
        """, unsafe_allow_html=True)

    elif best_char == "크리만쥬":
        st.markdown("""
        <div class="result-card">
            <div style="font-size: 4.5rem;">🌰</div>
            <h2 style="color:#D2691E;">낭만을 아는 미식가 '크리만쥬'</h2>
            <p style="color:#666;">겉은 덤덤해 보여도 속정이 깊은 낭만파! 지친 하루 끝에 좋아하는 음식과 시원한 음료 한 잔으로 세상을 다 가진 듯 힐링할 줄 아는 멋쟁이입니다.</p>
            <hr style="border:1px dashed #FFC0CB;">
            <p>✈️ <b>추천 힐링 장소:</b> 운치 있는 골목 안쪽 소박한 맛집/선술집 🍺</p>
        </div>
        """, unsafe_allow_html=True)

    elif best_char == "랏코":
        st.markdown("""
        <div class="result-card">
            <div style="font-size: 4.5rem;">🦦</div>
            <h2 style="color:#4682B4;">겉바속촉 카리스마 리더 '랏코'</h2>
            <p style="color:#666;">자기 관리가 철저하고 일 처리가 깔끔한 전문가 타입! 카리스마 넘치고 쿨해 보이지만, 귀여운 디저트 하나에 사르르 녹는 반전 매력이 있습니다.</p>
            <hr style="border:1px dashed #FFC0CB;">
            <p>✈️ <b>추천 힐링 장소:</b> 고급스러운 디저트 카페 & 장엄한 자연 🏔️</p>
        </div>
        """, unsafe_allow_html=True)

    elif best_char == "모몽가":
        st.markdown("""
        <div class="result-card">
            <div style="font-size: 4.5rem;">🐿️</div>
            <h2 style="color:#87CEEB;">관심을 즐기는 당당한 사랑둥이 '모몽가'</h2>
            <p style="color:#666;">자신이 매력적이라는 사실을 너무 잘 알고 있는 주체적인 타입! 칭찬받는 것을 좋아하고 뻔뻔할 정도로 당당하지만 미워할 수 없는 존재감을 자랑합니다.</p>
            <hr style="border:1px dashed #FFC0CB;">
            <p>✈️ <b>추천 힐링 장소:</b> 인생샷과 플렉스를 원 없이 즐기는 럭셔리 핫플 🏙️</p>
        </div>
        """, unsafe_allow_html=True)

    # 🚨 히든 낚시 결과 1: 침착맨과 주호민
    elif best_char == "침주":
        st.markdown("""
        <div class="result-card" style="border: 4px solid #FF4500;">
            <div style="font-size: 5rem;">👨‍🦲🧔‍♂️</div>
            <h1 style="color:#FF4500; font-size: 1.8rem;">🚨 [대반전 히든 캐릭터 당첨!] 🚨</h1>
            <h2 style="color:#333;">당신은 치이카와가 아니라... '침착맨 & 주호민'입니다!</h2>
            <p style="color:#555;">
                치이카와 성향 테스트인 줄 알고 들어왔지만... 당신 선택지에 숨어있던 <b>킹받음과 병맛 케미</b>가 폭발하고 말았습니다!<br>
                말도 안 되는 킹받는 논리와 엉뚱함으로 사람들을 사로잡는 천재적인 스트리머 기질을 가지고 계시네요!
            </p>
            <hr style="border:1px dashed #FF4500;">
            <p>🎒 <b>필수 아이템:</b> 고피자 세트 & 킹받는 짤 표정</p>
            <p>✈️ <b>추천 찰떡 여행지:</b> 침착맨 침투부 라이브 방구석 1열 🛏️</p>
        </div>
        """, unsafe_allow_html=True)

    # 🚨 히든 낚시 결과 2: 감스트
    elif best_char == "감스트":
        st.markdown("""
        <div class="result-card" style="border: 4px solid #1E90FF;">
            <div style="font-size: 5rem;">⚽💥</div>
            <h1 style="color:#1E90FF; font-size: 1.8rem;">💥 [대반전 히든 캐릭터 당첨!] 💥</h1>
            <h2 style="color:#333;">당신은 치이카와가 아니라... '감스트'입니다!</h2>
            <p style="color:#555;">
                조용한 아기자기 테스트인 척 질문을 풀었지만 숨길 수 없는 <b>책상 샷건과 소리 지르기 텐션</b>!!<br>
                게임에 누구보다 진심이고 감정표현이 솔직해 주변 사람들에게 시원시원하고 아드레날린 폭발하는 재미를 선사하는 사람입니다!
            </p>
            <hr style="border:1px dashed #1E90FF;">
            <p>🎒 <b>필수 아이템:</b> 튼튼한 책상 (샷건용) & 피파 카드팩</p>
            <p>✈️ <b>추천 찰떡 여행지:</b> 프리미어리그 축구 경기장 맨 앞자리 ⚽</p>
        </div>
        """, unsafe_allow_html=True)
