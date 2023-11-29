# Biocontainers + RSEPedia MPI

![https://raw.githubusercontent.com/vsoch/contributor-ci/main/docs/assets/img/contributor-ci.png](https://raw.githubusercontent.com/vsoch/contributor-ci/main/docs/assets/img/contributor-ci.png)

This repository contains [Contributor CI](https://github.com/vsoch/contributor-ci) results for a set of (mostly manually) curated Biocontainers and RSEPedia repositories that have MPI. I likely missed some (or have a false positive or two).
For the action itself, if you need to get information on users, a traditional `GITHUB_TOKEN` in the action
is not sufficient and you'll need to set a personal access token to `CCI_GITHUB_TOKEN`.

## Usage

To generate data:

```bash
$ cci --out-dir _cci extract releases repos activity_commits topics activity_lines repo_metadata stars repo_dependencies dependencies languages
```
Note we are leaving out metrics for users (because we don't care). You will need a `GITHUB_TOKEN` or personal access token exported in the environment. You can update the [_data](_data) with:

```bash
$ pip install contributor-ci
$ cci ui update
```
