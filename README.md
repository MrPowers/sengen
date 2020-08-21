# sengen: Python Sensor Data Generator

## Welcome

sengen is a fork of the Mandrova open-source python library for scientific data generation.  The code was forked so it could be uploaded to PyPi.

It supports stationary, non-stationary, and even user-specified generation schemes.

## Simple Start

Importing Sensor Data Generator

```python
from sengen.data_generator import SensorDataGenerator as sdg
```

Decleration of Important Variables For Generation

```python
seed = 20171221
sample_size = 1000
dg = sdg()
```

Generation Options

```python
dg.generation_input.add_option(sensor_names="Hello", distribution="normal", mu=0, sigma=1)
dg.generation_input.add_option(sensor_names="World", eq="x",
                               initial={"x":0}, step={"x":1})
```

Generate

```python
dg.generate(sample_size=sample_size, seed=seed)
```

Save Data Table

1. As .csv
```python
dg.save_as_csv(file_name="hello_world")
```

2. As .xlsx
```python
dg.save_as_excel(file_name="hello", sheet_name="world")
```

## Tutorials

- [Chapter1: Data Generation](tutorials/chapter1_data_generation.ipynb)
- [Chapter2: Data Modification](tutorials/chapter2_data_modification.ipynb)
- [Chapter3: Stationary Examples](tutorials/chapter3_stationary_examples.ipynb)
- [Chapter4: Non-Stationary Examples](tutorials/chapter4_non_stationary_examples.ipynb)
- [Chapter5: Complex Generation Example](tutorials/chapter5_complex_generation_example.ipynb)
- [Appendix A: Playing With Lorenz Attractor](tutorials/appendix_a_playing_with_lorenz_attractor.ipynb)

## Contributor
- Jong Duk Shinn

### Special Thanks to:
Development:
- Andre Yoon
- Sangwoo Shim
- Yongsub Lim
- Ki Hyun Kim
- Byungchan Kim (kbc8894@makinarocks.ai)

Logo Design:
- Yujin Han

