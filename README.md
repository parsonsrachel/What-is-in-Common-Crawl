# What-is-in-Common-Crawl
Machine learning project to investigate what types of data exist in Common Crawl

# September 12
Figured out next steps and what to complete for next class. Started looking at the requirements for the project proposal. Assigned tasks to complete before next class. Add to proposal document with thoughts from literature review. Try querying common crawl to figure out how to use it.

# September 14
Tried pulling data from Common Crawl, but were not yet successful. Added to the literature review. Allocated proposal paper sections with the intention to be done with a first draft of the proposal by next class. 

# September 19
Started the proposal presentation and assigned slides. Still need to edit the paper and fix formating. Still have not figured out how to query Common Crawl.

# September 28
Presented proposal. Notes we got back
- create a filtering method based on the types of data we see
- currated datasets already exist so filtering method that filters out all bad data and not just specific types would be good
- try running some of the filtering methods we looked at to see what is left over from filtering and what was filtered out that maybe shouldn't have been
- won't really have to worry a lot about large data storage because a few thousand is not too large

## Installation

In order to set up the necessary environment:

1. If [conda] is not yet installed, follow the [installation guide] for your operating system.
   > Note: [miniconda] or [mamba] are faster options
2. From the projects root directory create the environment with:
   ```
   conda env create -f environment.yml
   ```
3. Activate the new environment with:
   ```
   conda activate whatsincc
   ```
   > Note: The environment should always be activated before working on this project
#### Troubleshoot
- Make sure to restart your terminal after installing conda. Or run ```source ~/.bashrc```
- If ```conda activate``` fails, try ```conda init``` and then ```conda activate``` again


## Dependency Management & Reproducibility

1. Create concrete dependencies as `environment.lock.yml` for the exact reproduction of your
   environment with:
   ```bash
   conda env export -n whatsincc -f environment.lock.yml
   ```
   For multi-OS development, consider using `--no-builds` during the export.
3. Update your current environment with respect to a new `environment.lock.yml` using:
   ```bash
   conda env update -f environment.lock.yml --prune
   ```

[conda]: https://docs.conda.io/
[installation guide]: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html
[miniconda]: https://docs.conda.io/en/latest/miniconda.html
[mamba]: https://mamba.readthedocs.io/en/latest/installation.html#installation
