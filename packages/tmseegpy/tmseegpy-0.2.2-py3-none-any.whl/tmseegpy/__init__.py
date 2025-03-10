"""TMS-EEG Analysis Package"""


def _is_in_jupyter():
    """Check if we're running in a Jupyter notebook"""
    try:
        from IPython import get_ipython
        if get_ipython() is not None:
            return True
        return False
    except ImportError:
        return False


# Configure backends based on environment
import matplotlib
import matplotlib.pyplot as plt
import mne

if _is_in_jupyter():
    matplotlib.use('module://matplotlib_inline.backend_inline')
    mne.viz.set_browser_backend("matplotlib")
else:
    matplotlib.use('QtAgg')
    mne.viz.set_browser_backend("qt")
    plt.rcParams['figure.figsize'] = [8, 6]

# Now import all components

from .clean import *
from .pcist import *
from .preproc import *
from .preproc_vis import *
from .run import *
from .validate_tep import *
from .dataloader import *
from .cli import main as cli_main
from .ica_topo_classifier import ICATopographyClassifier
from .ica_nn_classifier import *

__version__ = "0.2.1"

__all__ = [
    'cli_main',
    'ICATopographyClassifier'
]


# Define entry points for command line tools
def run_cli():
    """Entry point for the tmseegpy command line tool"""
    cli_main()

