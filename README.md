
## SETUP

### Solvers for LP, IP, MILP, etc.

* Create a local `solvers` directory
* Download solvers from AMPL site (e.g. https://ampl.com/dl/open/couenne/couenne-osx.zip) into that directory
* Unzip
* Run the following command to add the solvers directory to path:

```
export PATH=$PATH:`pwd`/solvers
```

## TESTING

* basic, with linting:

`pytest --pylama --tb=short`

* including coverage:

`pytest --pylama --cov=. --tb=short`


## TODO

* package / module 

