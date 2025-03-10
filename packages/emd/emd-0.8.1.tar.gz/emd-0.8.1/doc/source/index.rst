.. emd documentation master file, created by
   sphinx-quickstart on Sun Jan 27 23:11:40 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
:html_theme.sidebar_secondary.remove:

Empirical Mode Decomposition in Python
======================================

Python tools for the extraction and analysis of non-linear and non-stationary oscillatory signals.

.. grid:: 2
    :gutter: 3 3 4 5

    .. grid-item-card:: Sift Oscillations
        :img-bottom: _static/emd_logo_no_head_short.png

    .. grid-item-card:: Non-Linear Power Spectra
        :img-bottom: _static/hht_snippet_short.png


    .. grid-item-card:: Cross-Frequency Coupling
        :img-bottom: _static/single_cycle_array.jpg


    .. grid-item-card:: Single Cycle Waveform Shape
        :img-bottom: _static/waveform_array_short.png



Features
========

* Sift algorithms including the ensemble sift, complete ensemble sift and mask sift
* Instantaneous phase, frequency and amplitude computation
* Cycle detection and analysis
* Hilbert-Huang spectrum estimation (1d frequency spectrum or 2d time-frequency spectrum)
* Second layer sift to quantify structure in amplitude modulations
* Holospectrum estimation (3d instantaneous frequency x amplitude modulation frequency x time spectrum)

Sitemap
=======

.. toctree::
   :maxdepth: 2

   Install<install>
   Cite<cite>
   Tutorials<emd_tutorials/index>
   Reference<api>
   Contribute<contribute>
   Changelog<changelog>
