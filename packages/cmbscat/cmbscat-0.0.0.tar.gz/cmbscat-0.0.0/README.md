# CMBSCAT: fast map-based emulator for CMB systematics


`cmbscat` is a pip installable package that can synthesize new map samples (called **emulations**) which are both visually and statistically similar to the ones found in an (eventually) small dataset of simulations. 

## Install with pip
You can install it simply doing:
```
pip install cmbscat
```

## Usage
You can then set generate a new dataset of CMB systematics maps by doing:

```python
from cmbscat import cmbscat_pipe

# Set emulator parameters
params = {
    'NNN'          : 10,             # Number of input reference maps
    'gauss_real'   : True,             # Generate new input data as Gaussian realizations from pixel covariance of original data
    'NGEN'         : 10,               # Batch size for gradient descent
    'n_samples'    : 10,               # Samples in the input dataset
    'nside'        : 16,               # N_side of input maps
    'NORIENT'      : 4,                # Orientations in the SC
    'nstep'        : 50,              # Steps in gradient descent
    'KERNELSZ'     : 3,                # Wavelet kernel size
    'outname'      : 'example',        # Output name
    'outpath'      : './data/',        # Output path
    'data'         : 'variable_gain_sims.npy'  # Input data path
}

# Initialize pipeline...
pipeline = cmbscat_pipe(params)

#...and run! This generates NGEN new maps for each of the n_samples input maps
pipeline.run()
```

## Tutorial Notebook
You can find an introductory notebook explaining all features of the `cmbscat` package [here](https://github.com/pcampeti/CMBSCAT/blob/main/notebook/CMBSCAT_demo.ipynb)
