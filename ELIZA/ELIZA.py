import random
import re

reflections = {
    "me": "you",
    "i": "you",
    "am": "are",
    "was": "were",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you": "me",
    "are": "am",
    "you're": "I am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine"
}

psychobabble = [
    (
        r'.* ?(I feel) (.*)',
        [
            "Why do {} {}?", # the groups in the regex above will be reflected, then inserted in place of {} here;
                             # if there are no {}, just the string will be returned
            "Why do you think {} {}?",
            "Where do yo think those feelings are coming from?"
        ]
    ),
    (
        r'.* ?(I remember) (.*)',
        [
            # "Why do {} {}?",
            "What drew you to these memories?",
            "Tell me more about these memories.",
            "What else do you remember?",
            "That is interesting. Please continue.",
            "What feelings do you have about this?"
        ]
    ),
    (
        r'.* ?I dream about (.*)',
        [
            "Is {} a big dream for you?",
            "What will you do after ?",
            "What feelings do you have about {}?"
        ]
    ),
    (
        r'.* ?(I \blike|I \blove|I \bneed|I \bwant) (.*)',
        [
            "Why do {} {}?",
        ]
    ),
    (
        r'.* ?([Mm]y \b[Ff]ather|[Mm]y \bmother|[Mm]y \bbrother|[Mm]y \bsister|[Mm]y \bfamily).*',
        [
            "{}?",
            "Please tell me more about {}.",
        ]
    ),    
    (
        r'.* ?(\bLOL|ha).*',
        [
            "Why are you laughing?",
            "Did I make you laugh?"
        ]
    ),
    (
        r'.{10,1000}',
        [
            "Please tell me more about it.",
            "Tell me more about it.",
            "That's interesting, please go on.",
            "What do you think about it?",
            "What do you feel about it?"
        ]
    ),   
    (
        r'.*',
        [
            "Please tell me more about it.",
            "Tell me more about it.",
            "Please go on.",
        ]
    ),   
    (
        r'quit',
        [
            "Thank you for talking with me.",
            "Good-bye.",
            "Thank you, that will be $150. Have a good day!"
        ]
    )
]


def reflect(fragment):
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in reflections:
            tokens[i] = reflections[token]
    return ' '.join(tokens)


def analyze(statement):
    for pattern, responses in psychobabble:
        match = re.match(pattern, statement.rstrip(".!"))
        if match is not None:
            response = random.choice(responses)
            return response.format(*[reflect(g) for g in match.groups()])

# I feel depressed
def main():
    start = random.choice([
    "Hello. What would you like to talk about ?",
    "Hi. How are you?",
    "Hello. How are you feeling today?"
    ])
    print("ELIZA: " + start)

    while True:
        statement = input("YOU: ")
        print("ELIZA: " + analyze(statement))

        if statement == "quit":
            break


if __name__ == "__main__":
    main()
