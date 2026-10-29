
# Vision-Crafters
## AI-Powered Intelligent Candidate Ranking System

Vision-Crafters is a Python-based candidate ranking system designed to help recruiters shortlist candidates based on job-related skills and requirements.

The application allows recruiters to enter a job description, evaluates sample candidate profiles using keyword-based scoring, and displays ranked candidates through a simple interactive dashboard.

## 🚀 Features

- **Job Description Input:** Enter job requirements through a text area.
- **Candidate Data Processing:** Load candidate information from a CSV file using Pandas.
- **Keyword-Based Matching:** Check job descriptions for keywords such as Python and Java.
- **Candidate Scoring:** Assign scores based on matching programming skills.
- **Candidate Ranking:** Sort candidates by their calculated scores.
- **Interactive Dashboard:** Display candidate details and ranking results using Streamlit.
- **Top Candidate Identification:** Highlight the highest-ranked candidate.
- **Candidate Statistics:** Display the total number of candidates and the highest score.
- **Data Visualization:** Show candidate scores using a bar chart.
- **CSV Export:** Save ranked candidate data to a CSV file.

## ⚙️ How It Works

1. The recruiter enters a job description.
2. The application loads candidate profiles from `candidates.csv`.
3. The system checks for supported keywords, including Python and Java.
4. Candidates receive scores based on the matching keyword.
5. Candidate records are sorted by score in descending order.
6. The dashboard displays the rankings, top candidate, statistics, and score chart.

## 🧮 Scoring Logic

The current Streamlit application uses simple keyword-based scoring:

- **100 points:** Candidates whose skills contain the detected Python or Java keyword.
- **70 points:** Other candidates when Python or Java is detected in the job description.
- **80 points:** All candidates when neither supported keyword is detected.

This is a basic rule-based scoring approach and can be extended with more advanced matching techniques.

## 🛠️ Technologies Used

- **Python** – Application logic and candidate scoring.
- **Pandas** – Candidate data processing and CSV operations.
- **Streamlit** – Interactive web dashboard.
- **CSV** – Candidate data storage and ranked results.
- **Git and GitHub** – Version control and project hosting.

## 📁 Project Structure

```text
Vision-Crafters/
├── app/
│   ├── data/
│   │   ├── candidates.csv
│   │   └── ranked_candidates.csv
│   ├── page.py
│   ├── rank_candidates.py
│   └── ui/
│       └── home.py
├── real_ranker.py
├── submission.csv
├── validate_submission.py
└── README.md
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd Vision-Crafters
```

### 2. Install the required libraries

```bash
pip install pandas streamlit
```

### 3. Launch the Streamlit dashboard

From the project root directory, run:

```bash
streamlit run app/ui/home.py
```

### 4. Use the application

Open the local URL displayed in the terminal, enter a job description, and click **Show Ranked Candidates** to view the results.

## 🎯 Project Objectives

- Simplify initial candidate screening.
- Organize candidate profiles according to job requirements.
- Reduce manual effort in comparing candidate skills.
- Present ranking results through an interactive dashboard.
- Explore practical applications of automation in recruitment.

## 🔮 Future Improvements

- Implement actual resume parsing from PDF and DOCX files.
- Use semantic similarity or embedding-based matching.
- Evaluate multiple skills, experience, and education criteria.
- Generate explanations for individual candidate scores.
- Add downloadable CSV and Excel reports.
- Evaluate ranking accuracy using a larger, diverse dataset.
- Improve ranking fairness and candidate evaluation transparency.

## ⚠️ Limitations

The current dashboard uses sample candidate data and basic keyword-based rules. It does not yet implement full resume uploading, semantic analysis, or a trained machine learning model in the Streamlit workflow. Rankings should be treated as preliminary screening results rather than final hiring decisions.

## 👩‍💻 Project Information

- **Project Name:** Vision-Crafters
- **Project Type:** Candidate Ranking and Recruitment Support
- **Primary Language:** Python
- **Main Framework:** Streamlit
