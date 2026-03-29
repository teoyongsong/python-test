"""
Python practice quizzes — Streamlit wrapper around the existing HTML/JS app.

Local:   streamlit run app.py
Cloud:   https://share.streamlit.io — point the app at this repo, main file `app.py`.
"""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

BASE = Path(__file__).resolve().parent


@st.cache_data
def build_quiz_html() -> str:
    index_path = BASE / "index.html"
    data_path = BASE / "quiz-data.js"
    if not index_path.is_file() or not data_path.is_file():
        raise FileNotFoundError(
            f"Missing {index_path.name} or {data_path.name} next to app.py."
        )
    index_html = index_path.read_text(encoding="utf-8")
    quiz_js = data_path.read_text(encoding="utf-8")
    inlined = index_html.replace(
        '<script src="quiz-data.js"></script>',
        f"<script>\n{quiz_js}\n</script>",
    )
    return inlined.replace(
        'Load <span class="code" style="font-size: inherit">quiz-data.js</span> from the same folder · No login required',
        "Quiz data is bundled with this page · Works in Streamlit",
    )


def main() -> None:
    st.set_page_config(
        page_title="Python practice quizzes",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    st.title("Python & ML practice quizzes")
    st.caption(
        "Seven topics · 10 random questions per attempt from a bank of 30 · Use the embedded app below."
    )

    try:
        html = build_quiz_html()
    except FileNotFoundError as e:
        st.error(str(e))
        return

    # Tall iframe so most sessions fit without a tiny inner scroll area.
    components.html(html, height=2000, scrolling=True)


if __name__ == "__main__":
    main()
