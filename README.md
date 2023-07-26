Term Discovery Evaluation
=========================

[![Upload Python Package](https://github.com/zerospeech/tdev2/actions/workflows/pipy-publish.yaml/badge.svg)](https://github.com/zerospeech/tdev2/actions/workflows/pipy-publish.yaml) [![PyPI version](https://badge.fury.io/py/zerospeech-tde.svg)](https://badge.fury.io/py/zerospeech-tde) ![ANACONDA-VER](https://anaconda.org/coml/zerospeech-tde/badges/version.svg
) ![LICENCE](https://anaconda.org/coml/zerospeech-tde/badges/license.svg
)

Toolbox to evaluate  Term Discovery systems.


## Install

You can install using pip (`pip install zerospeech-tde`) or using conda (`conda install -c coml zerospeech-tde`)


## Info

* Complete Documentation and metrics description ar
  available at https://docs.cognitive-ml.fr/tde/

This toolbox transcribed phonetical each discovered interval, then applies
NLP evaluation to judge the quality of the discovery.
The metrics are:
- NED : mean of the edit distance between all the discovered pairs
- coverage: percentage of the corpus covered
- token/type: measure how good the system was at finding gold tokens and gold types
- boundary: measure how good the system was at finding gold boundaries
- grouping: judge the purity of the clusters formed by the system


## [Zerospeech Challenge](https://zerospeech.com)

This is used for the [task 2](https://zerospeech.com/tasks/task_2/tasks_goals/) of the zerospeech challenge, for this purpose it has been packaged into the [zerospeech evaluation toolkit](https://github.com/zerospeech/benchmarks)
