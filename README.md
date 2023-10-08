# What-is-in-Common-Crawl
Machine learning project to investigate what types of data exist in Common Crawl

# September 12
Figured out next steps and what to complete for next class. Started looking at the requirements for the project proposal. Assigned tasks to complete before next class. Add to proposal document with thoughts from literature review. Try querying common crawl to figure out how to use it.

# September 14
Tried pulling data from Common Crawl, but were not yet successful. Added to the literature review. Allocated proposal paper sections with the intention to be done with a first draft of the proposal by next class. 

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

1. Update environment:
   ```
   conda env update --prefix ./env --file environment.yml  --pruneconda env update --prefix ./env --file environment.yml  --prune
   ```

2. Create concrete dependencies as `environment.lock.yml` for the exact reproduction of your
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
