import random
import re

starter = [
    "What would you like to talk about?",
    "How are you?",
    "How are you feeling today?",
    "How are you feeling?",
    "How do you do?"
    ]

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
    # Greetings
    (#OK
        r'(?i)[.!]*\b(hi|hey|hello|good morning|good day|good night)',
        starter
    ),
    (#OK
        r'\b([Hh]ow are you|[Hh]ow do you do|[Ww]hat\'s up)\?*',
        [
            "I'm fine, how are you today?",
            "I'm OK, how do you do?",
            "I'm fine, what would you like to talk about?",
            "I'm OK, how do you feel?"
        ]
    ),
    # Main
    (#OK
        r'.*\b([Ii] felt|[Ii] feel)\b(.*)',
        [
            "Why do {} {}?",
            "Why do you think {} {}?",
            "Where do yo think those feelings are coming from?",
            "What other feelings do you have?"
        ]
    ),
    (#OK
        r'.*\b[Ii] remember\b.*',
        [
            "What drew you to these memories?",
            "Tell me more about these memories.",
            "What else do you remember?",
            "That is interesting, please continue.",
            "What feelings do you have about this?"
        ]
    ),
    (#OK
        r'.*\b([Ii] dream about|[Ii] dream|[Ii] have a dream about)\b(.*)',
        [
            "Why do you dream about it?",
            "Is it a big dream to you?",
            "What are the other dreams you have?",
            "What feelings do you have when {} {}?",
            "What do you feel when {} {}?",
            "What do you feel when you dram about it?"
        ]
    ),
    (#OK
        r'.*\b([Ii] like|[Ii] love|[Ii] need|[Ii] want) (.*)',
        [
            "Why do {} {}?",
            "Really, do {} {}?",
            "What else do {}?",
        ]
    ),
    (#OK
        r'.*\b([Mm]y [Ff]ather|[Mm]y [Mm]other|[Mm]y [Bb]rother|[Mm]y [Ss]ister|[Mm]y [Ff]amily).*',
        [
            "{}?",
            "Please tell me more about {}.",
            "Do you often think about {}?",
            "What do you think about {}?"
        ]
    ),
    (#OK
        r'(?i).*\bam i\b(.*)\?*',
        [
        "Do you think you are {}?",
        "Do you believe you are {}?",
        "Would you want to be {}?",
        "Does it bother you?",
        "Is it important to you?",
        "Why it bothers you?",
        "What would it mean if you were {}?",
        "What would it mean if you were not {}?"
        ]
    ),
    (#OK
        r'(?i).*\bare you\b(.*)\?+',
        [
        "Why are you interested in whether I am {} or not?",
        "Would you prefer if I weren't {}?"
        ]
    ),
    (#OK
        r'(?i)[ !.?]*\byes\b(.*)',
        [
            "Why?",
            "Are you satisfied with it?",
            "Are you sure?",
            "Why do you think so?",
            "I see, what do you think about it?",
            "I see, what do you feel about it?",
        ]
    ),
    (#OK
        r'(?i)[ .!?]*\bno\b(.*)',
        [
            "Why?",
            "Why not?",
            "Are you satisfied with it?",
            "Are you sure?",
            "Why do you think so?",
            "I see, what are your thoughts about it?",
        ]
    ),
    (#OK
        r'.*\b[Ss]omeone\b.*',
        [
            "Can you be more specific?",
            "What incident are you thinking of?",
        ]
    ),
    (#OK
        r'.*\b[Ee]veryone\b.*?',
        [
            "Surely not everyone",
            "Can you think of anyone in particular?",
            "Who, for example?",
            "Are you thinking of a special person?",
            "What incident are you thinking of?",
        ],
    ),
    (#OK
        r'.*\b[Aa]lways\b.*?',
        [
            "Can you think of a specific example?",
            "Is there an incident you are thinking of?",
            "Really always?",
            "For instance..?",
            "Can you give an example?"
        ]
    ),
    (#OK
        r'.*\b([Pp]erhaps|[Mm]aybe|[Hh]opefully|I hope)\b.*?',
        [
            "You do not seem quite certain",
            "Why?",
            "Why so?",
        ],
    ),
    (#OK
        r'.*\b([Pp]robably|[Dd]efinitely|[Cc]ertainly|[Ss]ure)\b.*?',
        [
            "You seem quite certain",
            "Why?",
            "Why so?",
        ],
    ),
    (#OK
       r'.*\b[Ii] can\'t\b(.*)?',
       [
        "Maybe you could {} now",
        "Perhaps you can.",
        "Why not?",
        "Is there anything that impedes you to {}?",
        "What if you could {}?"
        ]
    ),
    (#OK
       r'.*\b[Ss]orry\b(.*)?',
       [
        "Why do you feel sorry?",
        "Why do you apologize?",
        "That's OK please don't apologize",
        "That's fine you shouldn't apologize",
        "That's fine you shouldn't be sorry"
        ]
    ),
    # Laugh
    (#OK
        r'(?i).*\b(lo+l|a*h+a+h+a+|lmao+|ke+k).*',
        [
            "Why are you laughing?",
            "Did I make you laugh?",
            "What's fun?",
            "Am I funny?"
        ]
    ),
    # Questions
    (#OK
        r'(?i)[a-z .!,\-0-9]{3,5000}\?',
        [
            "What do you think?",
            "What are your thoughts about it?",
            "What is your opinion?",
            "Can you answer it?",
            "That's hard to answer.",
            "It depends.",
        ]
    ),   
    # Quit
    (#OK
        r'[Qq]uit|[Ee]xit|[Bb]ye',
        [
            "Thank you for talking with me.",
            "Good-bye.",
            "Thank you, that will be $150. Have a good day!"
        ]
    ),
    # Other
    (#OK
        r'^( *)$',
        [
            "Any words?",
            "Let's start talking!",
            "I'd be glad to hear some of your thoughs.",
            "I'd be glad if you tell me how do you feel.",
            "Let's discuss anything you'd like to talk about.",
            "Don't be shy."
        ]
    ),
    (#OK
        r'([a-zA-Z \\\/.;,\'"()!?-]{10,100000})',
        [
            "Would you like to discuss it?",
            "What do you think about it?",
            "What do you feel about it?",
            "That's interesting, please go on.",
            "Why do you think so?",
            "Is it really true?",
            "Everything is subjective in this world."
        ]
    ),   
    (#OK
        r'([a-zA-Z \\\/.;,\'"()!?-]+)',
        [
            "Please tell me more about it.",
            "Please go on.",
            "What do you mean by {}?",
            "I'm not sure that I understand, could you tell me more?"
        ]
    ),
    (#OK
        r'.+',
        [
            "What?",
            "Sorry I don't understand.",
            "Could you explain?",
            "I'm not sure that I understand the symbols you use."
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
            # print('DEBUG:', pattern, match)
            response = random.choice(responses)
            return response.format(*[reflect(g) for g in match.groups()])

# I feel depressed
def main():
    print("ELIZA: " + random.choice(["Hi", "Hello"]) + ". " + random.choice(starter))

    while True:
        statement = input("YOU: ")
        print("ELIZA: " + analyze(statement).capitalize().replace(' i ', ' I '))

        if statement.lower() in ["quit", "exit"]:
            break


if __name__ == "__main__":
    print(len(psychobabble))
    main()
