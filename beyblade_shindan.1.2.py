import streamlit as st
import random

# ------------------------
# 初期化
# ------------------------
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.answers = []
    st.session_state.questions = []

# ------------------------
# 質問データ（修正版）
# ------------------------
base_questions = [
    ("やすみじかん、なにしてる？", [
        "A はしりまわってあそぶ",
        "B みんなのようすを見てうごく",
        "C すわってしずかにあそぶ",
        "D きぶんであそびかえる"
    ]),
    ("ともだちとけんかしたら？", [
        "A すぐいいかえす",
        "B いちどきいてからはなす",
        "C あまり気にしない",
        "D あいてにあわせてかえる"
    ]),
    ("ゲームでだいじなのは？", [
        "A はやくかつこと",
        "B まけないこと",
        "C ながくつづけること",
        "D あいてにあわせること"
    ]),
    ("しゅくだいはどうする？", [
        "A いっきにおわらせる",
        "B ていねいにやる",
        "C すこしずつやる",
        "D きぶんでやりかたをかえる"
    ]),
    ("あたらしいあそびをするときは？", [
        "A すぐやってみる",
        "B ルールを見てからやる",
        "C ゆっくりなれる",
        "D みんなにあわせる"
    ]),
]

extra_questions = [
    ("ヒーローになるなら？", [
        "A こうげきでたたかう",
        "B まもりながらたたかう",
        "C ずっとがんばる",
        "D なんでもできる"
    ]),
    ("すきなどうぶつは？", [
        "A ライオン",
        "B ゾウ",
        "C カメ",
        "D サル"
    ]),
    ("ふしぎなちからをみにつけるなら？", [
        "A いっしゅんでパワーアップ",
        "B なんでもまもるバリアー",
        "C どんなダメージもすぐにかいふく",
        "D あいてにあわせていろんなちからがつかえる"
    ]),
]

# ------------------------
# 質問生成
# ------------------------
def generate_questions():
    q = base_questions.copy()
    q.append(random.choice(extra_questions))
    random.shuffle(q)
    return q

# ------------------------
# 判定（同点対策あり）
# ------------------------
def get_result(answers):
    count = {"A":0, "B":0, "C":0, "D":0}
    for a in answers:
        count[a] += 1

    max_score = max(count.values())
    top_types = [k for k, v in count.items() if v == max_score]

    # 同点ならバランス
    if len(top_types) > 1:
        return "バランス"

    result = top_types[0]

    if result == "A":
        return "アタック"
    elif result == "B":
        return "ディフェンス"
    elif result == "C":
        return "スタミナ"
    else:
        return "バランス"

# ------------------------
# トップ画面
# ------------------------
if st.session_state.step == 0:
    st.title("🌀 ベイブレードしんだん")
    st.write("キミにぴったりのタイプをみつけよう！")

    if st.button("▶ スタート！"):
        st.session_state.questions = generate_questions()
        st.session_state.answers = []
        st.session_state.step = 1

# ------------------------
# 質問画面
# ------------------------
elif st.session_state.step <= len(st.session_state.questions):

    q_index = st.session_state.step - 1
    question, options = st.session_state.questions[q_index]

    st.write(f"Q{st.session_state.step} / {len(st.session_state.questions)}")
    st.subheader(question)

    st.radio("", options, key=f"q_{q_index}")

    if st.button("つぎへ"):
        selected = st.session_state[f"q_{q_index}"]
        st.session_state.answers.append(selected[0])
        st.session_state.step += 1

# ------------------------
# 結果画面
# ------------------------
else:
    result = get_result(st.session_state.answers)

    st.title("🎉 けっか！")

    if result == "アタック":
        st.header("💥 アタックタイプ！")
        st.write("ドカンと決める！はやくうごいて勝つ！")

        st.image("https://m.media-amazon.com/images/I/61MpAh-qOsL._AC_SY450_.jpg", width=200)
        st.write("ドランソード")
        st.link_button("これにする！", "https://www.amazon.co.jp/%E3%82%BF%E3%82%AB%E3%83%A9%E3%83%88%E3%83%9F%E3%83%BC-TAKARA-TOMY-BEYBLADE-BX-01/dp/B0C52R16P1/ref=sr_1_2?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=2H8OTT14REXTQ&dib=eyJ2IjoiMSJ9.pQ365hsYiqIE9suuCA2NUQhCvnfEa9NcHgq-1ibW5UAv5zaDalxLMfzq5i6GQAE5xwsCUocXU7gaGZguFWHrD2KKzjfdiVk76qDotoIFByE2h4Au3SxE4uher1wjkTN--9KS2d6j8tsjGu7UNcGFme8D5KGO2bYlyuKOf67mPkF7rNM3eXsdy6HLMOG7HEJ4Rx-jeKoIGWdRYXbAqe16NwcDfkzKjqG01hqCNanAhu_21C8lcPCAKQmPzTi9jPlUY0B3mrJ-mB7INQUDMT5HE-frkT2xzchig2fGgQsMICQ.rNG60mmHa9BE0SuxHYUHD6Ak1kUMSoEI7TBNGj68J30&dib_tag=se&keywords=%E3%83%89%E3%83%A9%E3%83%B3%E3%82%BD%E3%83%BC%E3%83%89&qid=1776523162&sprefix=%E3%83%89%E3%83%A9%E3%83%B3%E3%82%BD%E3%83%BC%E3%83%89%2Caps%2C188&sr=8-2&th=1")

        st.image("https://m.media-amazon.com/images/I/715NtHVPy-L._AC_SY450_.jpg", width=200)
        st.write("フェニックスウイング")
        st.link_button("これにする！", "https://www.amazon.co.jp/BEYBLADE-%E3%83%99%E3%82%A4%E3%83%96%E3%83%AC%E3%83%BC%E3%83%89X-BX-23-%E3%83%95%E3%82%A7%E3%83%8B%E3%83%83%E3%82%AF%E3%82%B9%E3%82%A6%E3%82%A4%E3%83%B3%E3%82%B0-9-60GF/dp/B0CMZSRJ3Q/ref=sr_1_4?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=3UR4RUMP2N8VZ&dib=eyJ2IjoiMSJ9.D1JsnqMoKaZUFo4MQpvWHtkPmoT32umFN34VNprTlsbX_VaH40xtIXhq1tVMPL3tImm_RobT1x-PMo_1eG_5huqbPYk9QupJhiPPTl6H53jCqPMbXD5NS2YXBL5IRLqkJqe4HHYs3dOypAqVI0WUeL1yEOGt8pHsiYmK_fsxjblhSHLMuUtDnO8Og83eB8VmhQgt10B9MwoPUvqw0fJqCDnjGBMQdqDN-6K0CQhc3R1fhIwd3xFkQHl9sUJ4La_c0FRlKfeguRArRmapNAf-sxx5W5RZmL3u7Mm0ROZBLdw.VueAIM2GS3mBm2tWCoB9nfT4wbwppfAJWGrd8gdmIBM&dib_tag=se&keywords=%E3%83%95%E3%82%A7%E3%83%8B%E3%83%83%E3%82%AF%E3%82%B9%E3%82%A6%E3%82%A3%E3%83%B3%E3%82%B0&qid=1776523122&sprefix=%E3%83%95%E3%82%A7%E3%83%8B%E3%83%83%E3%82%AF%E3%82%B9%E3%82%A6%E3%82%A4%E3%83%B3%E3%82%B0%2Caps%2C183&sr=8-4")

    elif result == "ディフェンス":
        st.header("🛡 ディフェンスタイプ！")
        st.write("まもってチャンス！あいてのこうげきをうける！")

        st.image("https://m.media-amazon.com/images/I/61N7ksTpjhL._AC_SY450_.jpg", width=200)
        st.write("ナイトフォートレス")
        st.link_button("これにする！", "https://www.amazon.co.jp/%E3%82%BF%E3%82%AB%E3%83%A9%E3%83%88%E3%83%9F%E3%83%BC-TAKARA-TOMY-CX-14-%E3%83%8A%E3%82%A4%E3%83%88%E3%83%95%E3%82%A9%E3%83%BC%E3%83%88%E3%83%AC%E3%82%B9GV8-70UN/dp/B0GMDYS21K/ref=sr_1_3?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=3SC4GPK5205K7&dib=eyJ2IjoiMSJ9.GuA75bULS5M4odGGTK2ZY-zyUTIP9mDoz4YsmXVrdIuyqIITepW_z5DGAiAz5zhqoaeuKdr-U6EVGP4i7wdfQ8VKqJfkFZZ0pYqmF4wr91MJBLY6RPo-T5x8-PNuWXkBdQcT1Fh3TpSiJSon_GqXMQ.wz_KvUnttLBqmn_Vl3BHIrReDwU25aUOk8nEWzyE1uU&dib_tag=se&keywords=%E3%83%8A%E3%82%A4%E3%83%88%E3%83%95%E3%82%A9%E3%83%BC%E3%83%88%E3%83%AC%E3%82%B9&qid=1776523093&sprefix=%E3%83%8A%E3%82%A4%E3%83%88%E3%83%95%E3%82%A9%E3%83%BC%E3%83%88%E3%83%AC%E3%82%B9%2Caps%2C199&sr=8-3")

        st.image("https://m.media-amazon.com/images/I/71AMNY-FmqL._AC_SY450_.jpg", width=200)
        st.write("レオンクレスト")
        st.link_button("これにする！", "https://www.amazon.co.jp/BEYBLADE-%E3%83%99%E3%82%A4%E3%83%96%E3%83%AC%E3%83%BC%E3%83%89X-UX-06-%E3%83%AC%E3%82%AA%E3%83%B3%E3%82%AF%E3%83%AC%E3%82%B9%E3%83%88-7-60GN/dp/B0D91K2WMS/ref=sr_1_5?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=36AOAR8P19W00&dib=eyJ2IjoiMSJ9.-U1rPp6c3Akt16_EZNidaxdcfRIpKtz0W9DasB7q52DsJG4DRYIbjLCzf8vyAMw7aDUnitjUwWpnZvr8DnByb0tesSycKZmiQ60Vn-tLnkPPBcRn6X9DVok9y7ZUO0X6hq3IwWLGzpFpbbVZ30SIxL-19yvqKI1_5eotBZ_GT7wvScmSBRnQL0XAcqz7EvPfAvKHOdkEmXT4ziILdBqnC1kCCAXsFY_ZSoHYyKqyGHJUMdKKsqbPxRvC8qz3JaULnkv1_LnRd7fL46uztu5cV7oVE_Mm856Sv1qa-Q6nBXQ.i1tFXSCN88GsGI60PWqdY8uia0UIN91BvZ5yhx0BdnM&dib_tag=se&keywords=%E3%83%AC%E3%82%AA%E3%83%B3%E3%82%AF%E3%83%AC%E3%82%B9%E3%83%88&qid=1776523068&sprefix=%E3%83%AC%E3%82%AA%E3%83%B3%E3%82%AF%E3%83%AC%E3%82%B9%E3%83%88%2Caps%2C198&sr=8-5")

    elif result == "スタミナ":
        st.header("🔄 スタミナタイプ！")
        st.write("さいごまでぐるぐる！ながくがんばる！")

        st.image("https://m.media-amazon.com/images/I/61qO6OBNzBL._AC_SY450_.jpg", width=200)
        st.write("ウィザードアーク")
        st.link_button("これにする！", "https://www.amazon.co.jp/BEYBLADE-%E3%83%99%E3%82%A4%E3%83%96%E3%83%AC%E3%83%BC%E3%83%89X-CX-02-%E3%82%A6%E3%82%A3%E3%82%B6%E3%83%BC%E3%83%89%E3%82%A2%E3%83%BC%E3%82%AF-R4-55LO/dp/B0DWSRHP7J/ref=sr_1_5?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=39TL3NRD0NKV&dib=eyJ2IjoiMSJ9.9uLmfras1txzi3ho2XZ3hDdKLtuqTG436ACC-szk32XmwDc9EM8Uftcd2g_PxzGs4VffT8l3bBKk8A6WMoR_NI3jebV-d0FMMlJ3ZiQJFpoKQ9WEC4Y4GVTfyn9LxGtOT4Q_GTZcS2vPSt0s5G7EIoFA3a3srQJ3iQNbP5wKCBuXIK-77ptX9pdoYQ5laYLHO1bUHOtU33LBEqOmcrYebj9_Rj-UaP8VUDCcwuavXHyva44fnyyvdb8v55VV8OY4PRAHLTR1E6P1zu32ptWgD-ZbTkFHPVR3lSMrlvlaAaY.LyE-C-nO_ySwYd3Y2kxkTy33ZVgBL8quDoEAzinZsqo&dib_tag=se&keywords=%E3%82%A6%E3%82%A3%E3%82%B6%E3%83%BC%E3%83%89%E3%82%A2%E3%83%BC%E3%82%AF&qid=1776523031&sprefix=%E3%82%A6%E3%82%A3%E3%82%B6%E3%83%BC%E3%83%89%E3%82%A2%E3%83%BC%E3%82%AF%2Caps%2C204&sr=8-5&th=1")

        st.image("https://m.media-amazon.com/images/I/61aJExH96+L._AC_SY450_.jpg", width=200)
        st.write("ヘルズサイズ")
        st.link_button("これにする！", "https://www.amazon.co.jp/%E3%82%BF%E3%82%AB%E3%83%A9%E3%83%88%E3%83%9F%E3%83%BC-TAKARA-TOMY-BEYBLADE-BX-02/dp/B0C52C4L3T/ref=sr_1_3?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=3AAU4I7UEVM0G&dib=eyJ2IjoiMSJ9.mR0BEncGuq8mWWz77cnhgFcJFu1qlkAa-CoxcN6P-dZW5MoMjWxAtVuwICNYp76JstOZLc0f0aXkpN5aoIAYlernFq5BT9fKBV2zJS9XGJiBFnwMnY-kMJaSkvPf2JxMyAv3ld0b1kfAid51FrQjHQ32756ehlsQxHfiqr-6FuU16EmLoR-ELV-LqFKfLCVZCD-lyBKBi8FFFG5s-_WkHd3m7peQqNO3oUKHZVMsY-fsZTGuFvRFdh_6ZTEkSg_gUUzUePSuJHgPDXTqd-I7Yhpesg2P75q9ehS-GKJaf2I.I0LQapxYcyeklqkbFYRN3593YhilPicb_vl4ORFjt-I&dib_tag=se&keywords=%E3%83%98%E3%83%AB%E3%82%BA%E3%82%B5%E3%82%A4%E3%82%BA&qid=1776523012&sprefix=%E3%83%98%E3%83%AB%E3%82%BA%E3%82%B5%E3%82%A4%E3%82%BA%2Caps%2C203&sr=8-3")

    else:
        st.header("⚡ バランスタイプ！")
        st.write("なんでもできる！あいてにあわせる！")

        st.image("https://m.media-amazon.com/images/I/61WEAT7WNKL._AC_SY450_.jpg", width=200)
        st.write("エンペラーマイト")
        st.link_button("これにする！", "https://www.amazon.co.jp/%E3%82%BF%E3%82%AB%E3%83%A9%E3%83%88%E3%83%9F%E3%83%BC-TAKARA-TOMY-BEYBLADE-%E3%82%A8%E3%83%B3%E3%83%9A%E3%83%A9%E3%83%BC%E3%83%9E%E3%82%A4%E3%83%88%E3%83%87%E3%83%83%E3%82%AD%E3%82%BB%E3%83%83%E3%83%88/dp/B0FV6Y4MH4/ref=sr_1_5?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=3W2O2H6RQBQR6&dib=eyJ2IjoiMSJ9.2BtPvi60H-upv-zqIBhZ1azwJXIXQbEC3MEQS78GqqvavhQbcCh1HEdLnWSk2Q-tZ7OxvFwKEJZZTtYivEn5qSEKctXLcX78C96WnbWO09_3jtSvTZifCe-sM529tnLK6B4jg0LHMxHMZoxVmq_4tFNGzJdBGCNh1PYxI3AzpdB0AYNRQJcVRMsR3A1SglqHaeT7ht-BgH8GRA1kp8uF4vYpEKCdb-eRuMddehwroK554j8Mzc8-qsIKz6E3HIX7FA5NMPFSw7m9zTMwkhVuyOZmhfu7Ig9Jfymr4YHo-Qc.pdKviIFw9R82lUnceanRjvwFo_wlNz5tI4ftknt4f0s&dib_tag=se&keywords=%E3%82%A8%E3%83%B3%E3%83%9A%E3%83%A9%E3%83%BC&qid=1776522698&sprefix=%E3%82%A8%E3%83%B3%E3%83%9A%E3%83%A9%E3%83%BC%E3%83%9E%E3%82%A4%E3%83%88%2Caps%2C173&sr=8-5&th=1")

        st.image("https://m.media-amazon.com/images/I/712keT+tMML._AC_SY450_.jpg", width=200)
        st.write("スコーピオスピア")
        st.link_button("これにする！", "https://www.amazon.co.jp/%E3%82%BF%E3%82%AB%E3%83%A9%E3%83%88%E3%83%9F%E3%83%BC-TAKARA-TOMY-UX-14-%E3%82%B9%E3%82%B3%E3%83%BC%E3%83%94%E3%82%AA%E3%82%B9%E3%83%94%E3%82%A20-70Z/dp/B0F47G3QJT/ref=sr_1_2?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=2LLZXD04KRYS5&dib=eyJ2IjoiMSJ9.-urKO3cuxtXfNLxxag_e9Ux_GQ29Qh-9zS8Z8NfSggDuGg9F8v7IMqcwB2sm3VuOwzNFACJWHeY0e-g1vldMCT4umcCGPkaEnDUmhPqiFNtQxdDW8QbEu9Pe2qcfBs8eAUH3oBDVTGD9L8uBNtg9Vzb90745uoYlevxHfQ2Rb5k.azkvlMgH437UbXP9nWeHfBsmX6GCff2_1kfQCPGTTLI&dib_tag=se&keywords=%E3%82%B9%E3%82%B3%E3%83%BC%E3%83%94%E3%82%AA%E3%83%B3%E3%83%94%E3%82%A2&qid=1776522994&sprefix=%E3%82%B9%E3%82%B3%E3%83%BC%E3%83%94%E3%82%AA%E3%82%B9%E3%83%94%E3%82%A2%2Caps%2C203&sr=8-2")

    if st.button("🔁 もういちどやる"):
        st.session_state.step = 0