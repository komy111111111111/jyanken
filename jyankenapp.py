import random
import streamlit as st

st.title("じゃんけんゲーム")

# ボタンを作成
btn_gu = st.button("グー")
btn_choki = st.button("チョキ")
btn_pa = st.button("パー")

# コンピュータの手をランダムに選択
computer_hand = random.choice(["グー", "チョキ", "パー"])

# ボタンがクリックされた場合の処理
if btn_gu:
    if computer_hand == "グー":
        result = "あいこです。"
    elif computer_hand == "チョキ":
        result = "あなたの勝ちです！"
    else:
        result = "あなたの負けです。"
elif btn_choki:
    if computer_hand == "グー":
        result = "あなたの負けです。"
    elif computer_hand == "チョキ":
        result = "あいこです。"
    else:
        result = "あなたの勝ちです！"
elif btn_pa:
    if computer_hand == "グー":
        result = "あなたの勝ちです！"
    elif computer_hand == "チョキ":
        result = "あなたの負けです。"
    else:
        result = "あいこです。"

# 結果を表示
st.write("あなたの手：" + btn_gu or btn_choki or btn_pa)
st.write("コンピュータの手：" + computer_hand)
st.write("結果：" + result)