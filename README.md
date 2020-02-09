# Horoscope Markov Chains

Using [`markovify`](https://github.com/jsvine/markovify/) to create a Markov chain from daily horoscopes like this:

> You may discover that what seems practical today could motivate you today, Taurus. While your ears and that the status quo. Deep inside you know the best you can. Although your approach assertive and not on the nuances of conversations and fascinating new information. But if you can, put it off for the last few months!

## Setup

```bash
make install
make input/targets.txt
make -j 3 data/corpus.txt
pipenv run python scripts/run_model.py
```
