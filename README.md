# Coding Assessment
## TextShuttle Internship 2021

### Getting started

You have 90 minutes to work on this assignment. Don't worry should you not
manage to complete all tasks.

Clone this repository and edit any code on your own machine. Once the time is up,
compress your local repository (with your modified code) into a `.zip` or `.tar.gz`
archive and send it to furrer@textshuttle.ai.

Please complete the tasks in order, i.e. do not work on task 2 before having completed task 1, etc.

### Task 1: Corpus Cleaning

A corpus is a collection of text segments, each consisting of a single string. On disk, corpora are often stored in line-delimited plain text files containing one segment per line.

Before training NLP models, corpora – often crawled from the web and thus containing noise – must be cleaned. Your task is to implement two cleaning methods: filtering and punctuation normalization. Implement the `filter` and `normalize` methods in `preprocess_corpus.py` according to their docstring specifications. You may use the file stored in `data/corpus.fr.txt` for testing.

### Task 2: Use of REST API

Some NLP models operate on the level of sentences, but a segment in a corpus may contain multiple sentences. Implement the `split` method in `preprocess_corpus.py` to split up such segments into single sentences, as specified in the docstring.

Sentence splitting can be a nasty business. Rather than implementing your own algorithm, use our REST API as described at https://stg.tait.ts.mt/api/v2/docs.

We recommend using the [`requests` module](https://pypi.org/project/requests/) to communicate with the online service. This module is not part of Python's standard library; you may need to install it.

### Task 3: Command Line Interface

Implement a command line interface (CLI) in `preprocess_corpus.py` to conveniently apply the functionality implemented in tasks 1 and 2 to a corpus stored on disk. The CLI should load a corpus; then apply (1) sentence splitting, (2) filtering, (3) normalization, and finally write all processed segments to the standard output. The CLI should accept two options `--min-alpha` and `--language` to control the respective parameters.

Examples:

```
$ python3 preprocess_corpus.py data/corpus.de.txt
Wie geht's?
Ausgezeichnet.
Und dir?
...
$ python3 preprocess_corpus.py --min-alpha 0.9 data/corpus.de.txt
Ausgezeichnet.
...
```
