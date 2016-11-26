Python project bare minimum
---------------------------------------------------

## Install dependencies

```
pip install -r requirements.txt
```

## Run Test

```
python test_target.py
```

## Create Document

```
pydoc target.target
```

## Calculate coverage

```
coverage run --source target/ test_target.py
```

## Show coverage

```
coverage report
```

Result is something like this.

```
Name                 Stmts   Miss  Cover
----------------------------------------
target/__init__.py       1      0   100%
target/target.py         6      0   100%
----------------------------------------
TOTAL                    7      0   100%
```

