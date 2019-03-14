
## SETUP

### Solvers for LP, IP, MILP, etc.

* Create a local `solvers` directory
* Download solvers from AMPL site (e.g. https://ampl.com/dl/open/couenne/couenne-osx.zip) into that directory
* Unzip
* Run the following command to add the solvers directory to path:

```bash
export PATH=$PATH:`pwd`/solvers
```

### Jupyter Notebook w/ Anaconda

See https://stackoverflow.com/a/44786736/150568 for more details.

```bash
source activate supply-chain-python

python -m ipykernel install \
  --user \
  --name supply-chain-python \
  --display-name "Python (supply-chain-python)"

jupyter notebook
```


## TESTING

* basic, with linting:

`pytest --pylama --tb=short`

* including coverage:

`pytest --pylama --cov=. --tb=short`


## TODO

* package / module 

