import time
import heapq

class Post:
    def __init__(self, post_id, content, timestamp, likes, comments, user_interactions):
        self.post_id = post_id
        self.content = content
        self.timestamp = timestamp
        self.likes = likes
        self.comments = comments
        self.user_interactions = user_interactions

    def rank_score(self):
        """Calculate ranking score."""
        return (self.likes * 2) + (self.comments * 3) + (self.user_interactions * 4) + (self.timestamp * 0.1)

class Feed:
    def __init__(self):
        self.posts = []  # Store posts in a list

    def add_post(self, post):
        self.posts.append(post)  # Simply append to list
        print(f"Added post: {post.content} -> Score: {post.rank_score()}")  # Debug print

    def get_top_posts(self, k):
        """Return top k posts sorted by rank (higher score first)."""
        sorted_posts = sorted(self.posts, key=lambda post: post.rank_score(), reverse=True)  
        return sorted_posts[:k]

# Testing
if __name__ == "__main__":
    feed = Feed()
    feed.add_post(Post(1, "Hello, world!", time.time(), 10, 2, 5))
    feed.add_post(Post(2, "Learning Flask!", time.time(), 15, 5, 8))
    feed.add_post(Post(3, "DSA in action!", time.time(), 8, 4, 6))

    print("\n=== Top Posts ===")
    top_posts = feed.get_top_posts(2)

    for post in top_posts:
        print(post.content, "-> Score:", post.rank_score())
