# What-is-in-Common-Crawl
Machine learning project to investigate what types of data exist in Common Crawl

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
   ```bash
   conda env update --file environment.yml --prune
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
# Description of Scripts
Run scripts from the project directory: ```python3 ./scripts/script_name.py```
- get_crawl_list.py: Saves the names of all available Common Crawl crawls in a file by scraping the dropdown menu on Common Crawls [get started page] (useful for using the original CC data)
- create_sample_c4_db.py: Creates a sample database of 10,000 random entries of the c4 dataset from huggingface. Columns are: url, timestamp, content, n_tokens (number of tokens of the content). The database is saved as c4_sample inside c4_sample.db stored in the data directory.
- classify_content_db_writer.py: (Requires Google Cloud account and authentication) classifies the content of each entry in the sample database and stores the result in a seperate column (google_classifier). Classification is done with the Google Cloud NLP API and its Content Classification model. To not have to run this again, the final database with the classifications are also stored on Github to download.


[conda]: https://docs.conda.io/
[installation guide]: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html
[miniconda]: https://docs.conda.io/en/latest/miniconda.html
[mamba]: https://mamba.readthedocs.io/en/latest/installation.html#installation
[get started page]: https://commoncrawl.org/get-started
