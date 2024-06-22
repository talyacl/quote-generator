import random

def get_random_quote():
    quotes = [
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
        "So many books, so little time. - Frank Zappa",
        "If you tell the truth, you don't have to remember anything. - Mark Twain",
        "A room without books is like a body without a soul. - Marcus Tullius Cicero",
        "You only live once, but if you do it right, once is enough. - Mae West",
        "Be the change that you wish to see in the world. - Mahatma Gandhi",
        "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
        "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. - Ralph Waldo Emerson",
        "I have not failed. I've just found 10,000 ways that won't work. - Thomas A. Edison",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "The best way to predict the future is to invent it. - Alan Kay",
        "The purpose of our lives is to be happy. - Dalai Lama",
        "The power of imagination makes us infinite. - John Muir",
        "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it. - Jordan Belfort",
        "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
        "The best preparation for tomorrow is doing your best today. - H. Jackson Brown, Jr.",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "The journey of a thousand miles begins with one step. - Lao Tzu",
        "The mind is everything. What you think you become. - Buddha",
        "The only way to achieve the impossible is to believe it is possible. - Charles Kingsleigh",
        "The way to get started is to quit talking and begin doing. - Walt Disney",
        "Your time is limited, so don't waste it living someone else's life. - Steve Jobs",
        "If life were predictable it would cease to be life, and be without flavor. - Eleanor Roosevelt",
        "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough. - Oprah Winfrey",
        "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success. - James Cameron",
        "Life is what happens when you're busy making other plans. - John Lennon"
    ]
    return random.choice(quotes)

def main():
    print("Welcome to the Quote Generator!")
    while True:
        user_input = input("Press Enter to get a new quote or type 'exit' to quit: ")
        if user_input.lower() == 'exit':
            print("Thank you for using the Quote Generator. Goodbye!")
            break
        else:
            print("\n" + get_random_quote() + "\n")

if __name__ == "__main__":
    main()
