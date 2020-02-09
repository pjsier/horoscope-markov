# Horoscope Markov Chains

Using [`markovify`](https://github.com/jsvine/markovify/) to create a Markov chain from daily horoscopes.

## Examples

> You may discover that what seems practical today could motivate you today, Taurus. While your ears and that the status quo. Deep inside you know the best you can. Although your approach assertive and not on the nuances of conversations and fascinating new information. But if you can, put it off for the last few months!

> If your partner out to be accurate, which might be to push yourself to something that interests you, Pisces. Do some serious decisions about anything could happen. Follow that instinct and get things going again in a while. If you find what you think, Sagittarius. Take an afternoon film.

## Setup

```bash
make install
make input/targets.txt
make -j 3 data/corpus.txt
pipenv run python scripts/run_model.py data/corpus.txt
```
