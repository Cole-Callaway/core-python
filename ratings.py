"""Restaurant rating lister."""


# put your code here
def process_scores():
    scores_text = open('scores.txt')

    scores = {}

    for line in scores_text:
        line = line.rstrip()
        restaurant, score = line.split(':')
        scores[restaurant] = int(score)
    return scores

def add_restaurant(scores):

    print('Please add a rating to your favorite restaurant')
    restaurant = input("restaurant name: ")
    rating = int(input("rating: "))

    scores[restaurant] = rating

def print_sorted_scores(scores):

    for restaurant, rating  in sorted(scores.items()):
        print(f"{restaurant} is rated at {rating}")

scores = process_scores()

add_restaurant(scores)

print_sorted_scores(scores)