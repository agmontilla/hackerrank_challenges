# Hackerrank Challenges

[![continuos integration](https://github.com/agmontilla/hackerrank_challenges/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/agmontilla/hackerrank_challenges/actions/workflows/ci.yml) [![codecov](https://codecov.io/gh/agmontilla/hackerrank_challenges/branch/main/graph/badge.svg?token=VMDQQ8F4FQ)](https://codecov.io/gh/agmontilla/hackerrank_challenges)

---

These are my personal solutions for [hackerrank challenges](https://www.hackerrank.com/domains/python).

## Continuos Integration workflow

I've added a GitHub action workflow to run unit tests automatically. My workflow is based on [Install Poetry Action](https://github.com/marketplace/actions/install-poetry-action)

## Coverage

I've added the integration with [Codecov](https://docs.codecov.com/docs) to check coverage. This was built using [this](https://github.com/marketplace/actions/install-poetry-action#codecov-upload)

TODO:

- Check [coverage](https://coverage.readthedocs.io/en/latest/config.html) to improve coverage status

Other posibilities are: [1](https://www.freecodecamp.org/news/how-to-generate-code-coverage-report-with-codecov-and-github-actions/), [2](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python#testing-with-pytest-and-pytest-cov), [3](https://nedbatchelder.com/blog/202209/making_a_coverage_badge.html)

Note:
- I added a conditional step<sup>[1](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-environment-variable),[2](https://stackoverflow.com/questions/59882715/use-environment-variable-in-github-action-if?rq=3)</sup> to run upload code coverage (if I'm executing GH actions locally, it ignores uploading code coverage to CODECOV)
- I'm running GH actions locally using [act](https://github.com/nektos/act)