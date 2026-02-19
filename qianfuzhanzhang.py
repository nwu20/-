import streamlit as st
import random

# 1. 设置网页标题和图标
st.set_page_config(page_title="保密局答案之书", page_icon="📻")

# 2. 站长金句库
quotes = [
    {"text": "凝聚意志，保卫领袖，这八个字我研究了十五年，结果就是两个字：搞钱！", "role": "吴敬中", "advice": "建议：看透事物本质。别被虚假的口号忽悠。"},
    {"text": "嘴上都是主义，那心里全是生意。", "role": "吴敬中", "advice": "建议：别听别人唱高调。多看看他背后的利益驱动。"},
    {"text": "你断人家的财路，人家会断你的生路。", "role": "吴敬中", "advice": "建议：职场大忌。千万别乱动别人的蛋糕。"},
    {"text": "有人缘，就是有能力呀！", "role": "吴敬中", "advice": "建议：别光顾着埋头干活。搞好人际关系也是硬实力。"},
    {"text": "什么叫不合适？合适都是讲条件的。", "role": "吴敬中", "advice": "建议：别急着拒绝。筹码给够了什么都好谈。"},
    {"text": "本来想露脸，结果把屁股露出来了。", "role": "吴敬中", "advice": "建议：别急于表现自己。准备不足容易弄巧成拙。"},
    {"text": "信任是一种滑稽的好感，我求之，但不得之。", "role": "吴敬中", "advice": "建议：不要轻易相信任何人。凡事留个心眼。"},
    {"text": "你以为别人不知道，其实别人只是不说罢了。", "role": "吴敬中", "advice": "建议：别自作聪明。很多事大家只是看破不说破。"},
    {"text": "我不管什么大局，我只管我的余生。", "role": "吴敬中", "advice": "建议：少操心那些宏大叙事。先保全自己最重要。"},
    {"text": "这种事儿，不查都是天灾，一查全是人祸。", "role": "吴敬中", "advice": "建议：事情水很深。建议你不要随便去蹚浑水。"},
    {"text": "时间像一头野驴呀，跑起来就不停。", "role": "吴敬中", "advice": "建议：抓紧时间。别再拖延了。"},
    {"text": "峨眉峰，还他妈独照，颇具浪漫主义气质啊。", "role": "吴敬中", "advice": "建议：别整那些虚头巴脑的。务实一点。"},
    {"text": "活着，就有希望。", "role": "吴敬中", "advice": "建议：熬住。留得青山在不怕没柴烧。"},
    {"text": "事情既然已经到了这一步，后悔也没有用。", "role": "吴敬中", "advice": "建议：接受现实。向前看。"},
    {"text": "不是我们无能，是共军太狡猾。", "role": "吴敬中", "advice": "建议：适当原谅自己。有时候确实是大环境不行。"}
]

# 3. 初始化状态
if 'drawn' not in st.session_state:
    st.session_state.drawn = False
if 'result' not in st.session_state:
    st.session_state.result = None

# 4. 界面设计
st.title("📻 保密局答案之书")
st.subheader("心中默念困惑。听听天津站吴站长怎么说。")
st.markdown("---")

# 5. 交互逻辑
if not st.session_state.drawn:
    if st.button("☎️ 拨通专线，请站长指示", use_container_width=True):
        st.session_state.result = random.choice(quotes)
        st.session_state.drawn = True
        st.rerun()
else:
    res = st.session_state.result
    st.info(f"「 {res['text']} 」")
    st.caption(f"—— 天津站站长 {res['role']}")
    st.success(f"**【机密批示】** {res['advice']}")
    
    st.markdown("---")
    
    if st.button("挂断电话，重新请示", use_container_width=True):
        st.session_state.drawn = False
        st.rerun()

# 6. 页脚
st.markdown("<br><br><p style='text-align: center; color: gray; font-size: 14px;'>绝密档案。阅后即焚。</p>", unsafe_allow_html=True)