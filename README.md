# social-media-feed-ranking

A web application that ranks social media posts based on user interactions such as likes, comments, and general engagement. The app uses a custom scoring algorithm to calculate the importance of each post and sorts them accordingly.

## Features
- Users can submit posts with likes, comments, and interactions.
- Posts are ranked based on a scoring algorithm that takes into account the number of likes, comments, and interactions.
- Posts are displayed in descending order of score.
- Each post shows the calculated score, likes, comments, interactions, and the time of posting.

## Technologies Used
- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS
- **Sorting Algorithm**: Python's built-in sorting (Timsort)
- **Time Handling**: Python's `datetime` library

## How to Run the Project
1. Clone this repository:
   git clone https://github.com/bhavani1309/social-media-feed-ranking.git



## Navigate to the project directory:
   cd social-media-feed-ranking

## Install the required dependencies:
   pip install -r requirements.txt
   
## Run the Flask application:
   python app.py

## How the Scoring Works
   The score for each post is calculated using the following formula:
   score = (likes * 2) + (comments * 3) + (interactions * 4)
   
   This score is then used to rank the posts, with the highest-scoring posts appearing first.
   
## Future Improvements
   Add user authentication to track individual users' posts.
   Implement a more advanced scoring algorithm (e.g., incorporating post time, user reputation).
   Add a database to persist posts.

## Authors
   Bhavani Thantanapalli


