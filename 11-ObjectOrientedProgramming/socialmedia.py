class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")
    
    def display_timeline(self):
        print(f"--- Oś czasu użytkownika: {self.username} ---")
        if not self.posts:
            print("Brak postów do wyświetlenia.")
        else:
            print(f'Posty: {self.posts}')

        counter = 1
        for post in self.posts:
            # 3. Użycie licznika w wydruku
            print(f"{counter}. {post}")
            # 4. Zwiększenie licznika
            counter += 1
            
    



def main():
    # your program
    media1 = SocialMediaProfile("johndoe")
    media1.add_post("Hello, world!")
    media1.add_post("Had a great day at the park!")
    media1.add_post("What's up, Natalie? How are you?")
    media1.display_timeline()

if __name__ == "__main__":
    main()