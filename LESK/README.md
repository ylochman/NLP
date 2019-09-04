# Word sense disambiguation with Simplified Lesk for Ukrainian

Please see [Lesk.ipynb](./Lesk.ipynb)

## Task Description
Choose a word with multiple meanings.

1. Collect real-world sentences for the word.

2. Implement Simplified Lesk for disambiguating the meanings of the word.

3. Set aside 50 sentences as a test set and manually fix the disambiguation errors that Lesk made. Calculate the quality of WSD by Lesk.

4. Improve the quality of WSD by:

- taking into account word count
- counting IDF score (log of total number of senses divided by the number of senses where the word was used)
- extending the word lists for senses in a semi-supervised manner (using the context of words that were disambiguated with high confidence)

Describe your observations and results obtained in a separate document.