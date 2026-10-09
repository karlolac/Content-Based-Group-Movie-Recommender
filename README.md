🎬 CineGroup – Content-Based Movie Recommendation System for Groups
A full-stack Django web application that combines Content-Based Filtering with dynamic group profile aggregation to generate personalized movie recommendations for user groups.

🚀 Key Features
Personal User Profiles: Users can curate their personal movie history by adding films they have watched or enjoyed.

Streamlined UI & Fast Search: Instant movie selection via Autocomplete search, with single-click removal directly from the home dashboard.

Group Recommendations (Core Feature): Select multiple user profiles simultaneously using checkboxes. The recommendation engine aggregates their individual preferences in real time to calculate top movie recommendations for the entire group.

Rich Visuals (TMDB Integration): Dynamic fetching of real-time movie posters and metadata via The Movie Database (TMDB) API.

🛠️ Tech Stack & Architecture
Backend: Python 3, Django Web Framework

Data Science & ML: Pandas, Scikit-learn (TF-IDF Vectorizer, Cosine Similarity)

Frontend: HTML5, Bootstrap 5 (Responsive UI), Bootstrap Icons

External APIs: The Movie Database (TMDB) API

💻 Local Installation & Setup
Clone the repository:

Bash
git clone https://github.com/karlolac/Content-Based-Movie-Recommendation.git
cd Content-Based-Movie-Recommendation
Install dependencies:

Bash
pip install -r requirements.txt
Run the development server:

Bash
python manage.py runserver
Access the application:

Open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
