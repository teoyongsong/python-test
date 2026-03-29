# Python & ML practice quizzes

A browser-based quiz app with **seven** topics for learners: Python basics, NumPy/Pandas, data cleaning and EDA, introductory machine learning (including linear regression and scaling), classification models (k-NN, logistic regression, decision trees), and model evaluation with hyperparameter tuning.

Each topic has a **bank of 30** multiple-choice questions. Every attempt draws **10** questions at random and shuffles their order. After you finish, you can review explanations, **print** results (or save as PDF from the print dialog), or **download** a plain-text summary.

## Project layout

| File | Purpose |
|------|---------|
| `index.html` | Quiz UI, styles, and client-side logic |
| `quiz-data.js` | Question banks (`window.QUIZ_BANKS`) |
| `app.py` | [Streamlit](https://streamlit.io) wrapper that inlines the JS so the app runs in an iframe |
| `requirements.txt` | Python dependency for Streamlit |
| `.gitignore` | Ignores virtualenvs, caches, and Streamlit secrets |

## Run in the browser (static)

Keep `index.html` and `quiz-data.js` in the **same folder**, then either:

- Open `index.html` directly in your browser, or  
- From that folder, run a small HTTP server (some browsers are stricter about loading local scripts):

  ```bash
  python3 -m http.server 8080
  ```

  Then visit `http://localhost:8080/`.

## Run with Streamlit

```bash
pip install -r requirements.txt
streamlit run app.py
```

Streamlit loads `index.html`, inlines `quiz-data.js` into the page (so paths work inside the embedded view), and displays the quiz in a tall HTML component.

## Deploy on Streamlit Community Cloud

1. Push this directory to a GitHub repository (include `app.py`, `index.html`, `quiz-data.js`, and `requirements.txt`).
2. Sign in at [share.streamlit.io](https://share.streamlit.io) with GitHub.
3. Create a new app: select the repo, branch, and set the main file to **`app.py`**.
4. If the app files live in a subfolder, set that folder as the app **subdirectory**.

Cloud will install dependencies from `requirements.txt` and run `streamlit run app.py`.

## License

Use and adapt for teaching and self-study as you like; attribute if you redistribute substantially.
