# Experiment Runner
 

- [Experiment Runner](#experiment-runner)
  - [Working Requirements](#working-requirements)
  - [Usage](#usage)


## Working Requirements
- [ ] should be able to “enter” into a running experiment and single step.
- [ ] should log data columns from each iteration into something
- [ ] should be able to easily find all the data logs for a single exp
- [ ] no webapps, apis or databases
- [ ] Logs should be plain and easy to transport
- [ ] Data ingest should be easy by pointing to files or directories
- [ ] Where a validation or test set is given, it should be easy to collate the resulting outputs (logs, files, plots) for each sample across fixtures, for example to see what effect a certain hparam has on each test sample.
- [ ] it should be imagined that this solution will not be the whole project, rather a subfolder in a research project wherein other code is written out of scope. Thus we should support both the “testcases model” where expts are confined to a directory as well as expts being written within the code, or in runner files.
- [ ] be able to write expts and training loops such that setup on remote machines is easy, what with different paths needed etc.

## Usage
1. Testcases Style
    ```python
    # experiments/lr.py
    from .fixtures import lr

    def best_lr(lr: float):
        for l in lr:
            ...
            yield l, loss, ...

    def circular_lr(lr: float):
        ...
    ```


2. Runner Style
    ```python
    # main.py
    from .models import Model

    @experiment
    def best_lr(lr: float):
        ...
    ```

