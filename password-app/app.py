import streamlit as st
import random

st.title("مولد كلمات السر 🔐")
st.header("أهلا! هنا بنسوي كلمات سر قوية 💪")

# ========== 🔐 الجزء الأول: المولد ==========

length = st.slider("طول كلمة السر", 4, 32, 12)
st.write(f"اخترت طول: {length}")

use_letters = st.checkbox("حروف 🔤", value=True)
use_numbers = st.checkbox("أرقام 🔢", value=True)
use_symbols = st.checkbox("رموز 🔣", value=False)

letters = ""

if use_letters:
    letters += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
if use_numbers:
    letters += "0123456789"
if use_symbols:
    letters += "!@#$%^&*"

if st.button("سوّ كلمة سر 🔐"):
    if letters == "":
        st.error("لازم تختار شي واحد على الأقل! ☑️")
    else:
        while True:
            password = ""
            for i in range(length):
                password += random.choice(letters)

            has_letter = False
            has_symbol = False
            has_number = False

            for ch in password:
                if ch.isalpha():
                    has_letter = True
                if ch in "!@#$%^&*":
                    has_symbol = True
                if ch in "0123456789":
                    has_number = True

            if use_letters and not has_letter:
                continue
            if use_symbols and not has_symbol:
                continue
            if use_numbers and not has_number:
                continue
            break

        st.code(password)

# ========== 🕵️ الجزء الثاني: الفاحص ==========

st.divider()
st.header("🕵️ فاحص كلمة السر")
st.caption("⚠️ للتجربة بس: لا تكتب كلمة سرك الحقيقية")

pw = st.text_input("اكتب كلمة السر", type="password")

st.write("اختياري: عشان نتأكد إن كلمة السر ما فيها معلوماتك 👤")
name = st.text_input("اسمك (اختياري)")
year = st.text_input("سنة ميلادك (اختياري)")

if st.button("افحص 🕵️"):
    if pw == "":
        st.error("اكتب كلمة سر أول! ✍️")
    else:
        good = []
        bad = []

        # 📏 1. الطول
        if len(pw) >= 12:
            good.append(f"الطول ممتاز ({len(pw)} خانة)")
        elif len(pw) >= 8:
            bad.append(f"الطول مقبول ({len(pw)} خانة)، الأفضل 12 أو أكثر")
        else:
            bad.append(f"قصيرة جدًا ({len(pw)} خانة)")

        # 🎲 2. التنوع
        has_lower = False
        has_upper = False
        has_number = False
        has_symbol = False

        for ch in pw:
            if ch.islower():
                has_lower = True
            elif ch.isupper():
                has_upper = True
            elif ch.isdigit():
                has_number = True
            else:
                has_symbol = True

        kinds = 0
        if has_lower:
            kinds += 1
        if has_upper:
            kinds += 1
        if has_number:
            kinds += 1
        if has_symbol:
            kinds += 1

        if kinds >= 3:
            good.append(f"متنوعة ({kinds} أنواع من 4)")
        else:
            bad.append(f"مو متنوعة ({kinds} أنواع بس)، ضيف حروف كبيرة وصغيرة وأرقام ورموز")

        # 🔁 3. التكرار
        repeated = False
        for i in range(len(pw) - 2):
            if pw[i] == pw[i + 1] == pw[i + 2]:
                repeated = True
        if len(set(pw)) <= 2:
            repeated = True

        if repeated:
            bad.append("فيها تكرار (مثل 111 أو 121212)")
        else:
            good.append("ما فيها تكرار")

        # 👤 4. المعلومات الشخصية
        personal = False
        if name.strip() != "" and name.strip().lower() in pw.lower():
            personal = True
        if year.strip() != "" and year.strip() in pw:
            personal = True

        if personal:
            bad.append("فيها معلوماتك الشخصية (اسمك أو سنة ميلادك)")
        elif name.strip() != "" or year.strip() != "":
            good.append("ما فيها المعلومات الشخصية اللي كتبتها")

        # 📋 النتائج
        for msg in good:
            st.success("✅ " + msg)
        for msg in bad:
            st.error("❌ " + msg)


        # 🏆 الحكم النهائي
        if len(bad) == 0:
            st.success("🏆 النتيجة: قوية جدًا!")
            st.balloons()
        elif len(bad) <= 2:
            st.warning("😐 النتيجة: متوسطة")
        else:
            st.error("😰 النتيجة: ضعيفة")
        st.info("🔄 تذكير: لا تستخدم نفس كلمة السر بأكثر من حساب. هذا ما نقدر نفحصه، بس مهم جدًا!")