import argparse
import re


def download_vocabulary(file="words.txt"):
    with open(file, "r") as f:
        vocabulary = f.read().split('\n')
    vocabulary = [v.lower() for v in vocabulary]
    return vocabulary

def remove_beginnings(text):
    beginnings = [r"#", r"http://", r"https://", r"www."]
    for beginning in beginnings:
        text = re.sub(beginning, "", text)
    return text

def remove_endings(text):
    return re.split("\.[a-zA-z]+", text)[0]

def split_into_words(text, vocabulary):
    """Returns a list of tokens for the input text constructed
       from concatanating words from vocabulary.
    """
    # print(text)
    if text == "":
        return True, [""]
    else:
        matched = False
        words = [text]
        for i in range(len(text)):
            potential_word = text[:i+1]
            ismatched, next_words = False, []
            if potential_word.lower() in vocabulary:
                # print(potential_word)
                ismatched, next_words = split_into_words(text[i+1:], vocabulary)
                if ismatched:
                    matched = True
                    potential_word = [potential_word]
                    words = potential_word + next_words if next_words != [""] else potential_word
                    # print('GOTCHA:', words)
        return matched, words

def segment_text(text, vocabulary_file="words.txt"):
    processed = remove_endings(remove_beginnings(text))
    
    # Separate numbers and text
    separated = [i for i in re.split(r'([a-z]+)', processed) if i]

    # Separate words
    vocabulary = download_vocabulary(vocabulary_file)
    final = []
    for text in separated:
        matched, words = split_into_words(text, vocabulary)
        final.extend(words if matched else [text])
        # processed_final.extend(words if matched else ["ERROR"])
    return " ".join(final)

def run(input_example=None, input_file=None, output_file=None):
    """ Main function that does everything.
    """
    if input_file is not None:
        with open(input_file, "r") as f:
            inputs = f.read().split('\n')
        outputs = [segment_text(input) for input in inputs]
        if output_file is not None:
            with open(output_file, "w") as f:
                for output in outputs:
                    f.write("{}\n".format(output))
    else:
        assert input_example is not None
        print(input_example, '->', segment_text(input_example))


if __name__=="__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="input file", type=str, default="input.txt")
    parser.add_argument("-o", "--output", help="output file", type=str, default="output.txt")
    args = parser.parse_args()

    run(input_file=args.input, output_file=args.output)
    run("https://www.myownexample21justforfun42hahaha.com.ua")