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
        r'.* ?\bI dream about\b\|bI have a dream about\b (.*)',
        [
            # "Why do you dream about it?",
            # "Is it a big dream to you?",
            # "What are the other dreams you have?",
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
        r'.* ?[Aa]m I (.*)?',
        [
        "Do you think you are {}?",
        "Do you believe you are {}?",
        "Would you want to be {}?",
        "What would it mean if you were {}?",
        ]
    ),
    (
        r'.*?[Aa]re you (.*)?',
        [
        "Why are you interested in whether I am {} or not?",
        "Would you prefer if I weren't {}?"
        ]
    ),
    (
        r'.*[Nn]o.*',
        [
            "Why not?",
            "Are you saying 'No' just to be negative?"
        ]
    ),    
    (
        r'.*([Ll][Oo][Ll]|[Hh][Aa][Hh][Aa]|[Ll][Mm][Aa][Oo]|[Kk][Ee]+[Kk]).*',
        [
            "Why are you laughing?",
            "Did I make you laugh?",
            "What's fun?",
            "Am I funny?"
        ]
    ),
    (
        r'[A-Za-z .!,\-0-9]{3,5000}\?',
        [
            "What do you think?",
            "What are your thoughts about it?",
            "What is your opinion?",
            "Can you answer it?",
            "That's hard to answer.",
            "It depends.",
        ]
    ),   
    (
        r'[Qq]uit|[Ee]xit',
        [
            "Thank you for talking with me.",
            "Good-bye.",
            "Thank you, that will be $150. Have a good day!"
        ]
    ),   
    (
        r'.{10,5000}',
        [
            "Please tell me more about it.",
            "Tell me more about it.",
            "Would you like to discuss it?",
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

        if statement.lower() in ["quit", "exit"]:
            break


if __name__ == "__main__":
    # print(len(psychobabble))
    main()
