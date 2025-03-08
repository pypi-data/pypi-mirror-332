# Quickstart

## Hydra application

The following example demonstrates how to use Hydraflow with a Hydra application.
There are two main steps to using Hydraflow:

1. Set the MLflow experiment using the Hydra job name.
2. Start a new MLflow run that logs the Hydra configuration.

```python title="apps/quickstart.py" linenums="1" hl_lines="24 26"
--8<-- "apps/quickstart.py"
```

### Start a new MLflow run

[`hydraflow.start_run`][] starts a new MLflow run that logs the Hydra configuration.
It returns the started run so that it can be used to log metrics, parameters, and artifacts
within the context of the run.

```python
with hydraflow.start_run(cfg) as run:
    pass
```

## Run the application

```bash exec="on"
rm -rf mlruns outputs multirun
```

### Single-run

Run the Hydra application as a normal Python script.

```console exec="1" source="console"
$ python apps/quickstart.py
```

Check the MLflow CLI to view the experiment.

```console exec="1" source="console"
$ mlflow experiments search
```

### Multi-run

```console exec="1" source="console"
$ python apps/quickstart.py -m width=400,600 height=100,200,300
```

## Use Hydraflow API

### Run collection

```pycon exec="1" source="console" session="quickstart"
>>> import hydraflow
>>> rc = hydraflow.list_runs("quickstart")
>>> print(rc)
```

### Retrieve a run

```pycon exec="1" source="console" session="quickstart"
>>> run = rc.first()
>>> print(type(run))
```

```pycon exec="1" source="console" session="quickstart"
>>> cfg = hydraflow.load_config(run)
>>> print(type(cfg))
>>> print(cfg)
```

```pycon exec="1" source="console" session="quickstart"
>>> run = rc.last()
>>> cfg = hydraflow.load_config(run)
>>> print(cfg)
```

### Filter runs

```pycon exec="1" source="console" session="quickstart"
>>> filtered = rc.filter(width=400)
>>> print(filtered)
```

```pycon exec="1" source="console" session="quickstart"
>>> filtered = rc.filter(height=[100, 300])
>>> print(filtered)
```

```pycon exec="1" source="console" session="quickstart"
>>> filtered = rc.filter(height=(100, 300))
>>> print(filtered)
```

### Group runs

```pycon exec="1" source="console" session="quickstart"
>>> grouped = rc.groupby("width")
>>> for key, group in grouped.items():
...     print(key, group)
```

```pycon exec="1" source="console" session="quickstart"
>>> grouped = rc.groupby(["height"])
>>> for key, group in grouped.items():
...     print(key, group)
```

### Config dataframe

```pycon exec="1" source="console" session="quickstart"
>>> print(rc.data.config)
```
