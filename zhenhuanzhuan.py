import streamlit as st
import random

# 1. 设置网页标题和图标
st.set_page_config(page_title="甄嬛传答案之书", page_icon="👑")

# 2. 准备金句库
quotes = [
    {"text": "这几年的情爱与时光，终究是错付了！", "role": "甄嬛", "advice": "建议：及时止损，莫再纠缠。"},
    {"text": "粉色娇嫩，你如今几岁了？", "role": "四大爷", "advice": "建议：认清现实，别再装傻。"},
    {"text": "在这宫里，有利用价值的人才能活下去。", "role": "浣碧", "advice": "建议：提升自己的核心竞争力。"},
    {"text": "凡事都要看淡些，心放宽了，日子才好过。", "role": "甄嬛", "advice": "建议：顺其自然，佛系面对。"},
    {"text": "容不容得下是娘娘的气度，能不能让娘娘容下是嫔妾的本事。", "role": "甄嬛", "advice": "建议：别管环境，看你自己能力。"}
]

# 3. 初始化网页记忆（判断是否已经抽过签）
if 'drawn' not in st.session_state:
    st.session_state.drawn = False
if 'result' not in st.session_state:
    st.session_state.result = None

# 4. 界面顶部设计
st.title("🧧 甄嬛传·答案之书")
st.subheader("心中默念你的困惑，自有娘娘为你指点迷津。")
st.markdown("---")

# 5. 核心交互逻辑
if not st.session_state.drawn:
    # 状态一：还没抽签时，显示开示按钮
    if st.button("✨ 请小主开示 ✨", use_container_width=True):
        st.session_state.result = random.choice(quotes)
        st.session_state.drawn = True
        st.rerun() # 刷新页面，让网页记住最新状态
else:
    # 状态二：已经抽签了，显示结果和重新抽签按钮
    res = st.session_state.result
    st.info(f"「 {res['text']} 」")
    st.caption(f"—— {res['role']}")
    st.success(f"**【指点】** {res['advice']}")
    
    st.markdown("---")
    
    if st.button("🔄 退下吧，本宫要重新抽签", use_container_width=True):
        st.session_state.drawn = False # 清除记忆
        st.rerun() # 刷新页面，回到初始状态

# 6. 页脚
st.markdown("<br><br><p style='text-align: center; color: gray; font-size: 14px;'>大梦一场，终须醒。仅供娱乐，切莫较真。</p>", unsafe_allow_html=True)