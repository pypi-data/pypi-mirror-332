bioScience: A new Python science library for High-Performance Computing Bioinformatics Analytics
=================================================================================================

**Deployment & Documentation & Stats**

.. image:: https://img.shields.io/badge/pypi-v0.1.4-brightgreen
   :target: https://pypi.org/project/bioscience/
   :alt: PyPI version


.. image:: https://readthedocs.org/projects/bioscience/badge/?version=latest
   :target: https://bioscience.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status


.. image:: https://img.shields.io/github/stars/aureliolfdez/bioscience.svg
   :target: https://github.com/aureliolfdez/bioscience/stargazers
   :alt: GitHub stars


.. image:: https://img.shields.io/github/forks/aureliolfdez/bioscience.svg?color=blue
   :target: https://github.com/aureliolfdez/bioscience/network
   :alt: GitHub forks


.. image:: https://img.shields.io/badge/License-BSD_3--Clause-blue.svg
   :target: https://github.com/aureliolfdez/bioscience/blob/main/LICENSE
   :alt: License

----


BioScience is an advanced Python library designed to satisfy the growing data analysis needs in the field of bioinformatics by leveraging High-Performance Computing (HPC). This library encompasses a vast multitude of functionalities, from loading specialised gene expression datasets (microarrays, RNA-Seq, etc.) to pre-processing techniques and data mining algorithms suitable for this type of datasets. BioScience is distinguished by its capacity to manage large amounts of biological data, providing users with efficient and scalable tools for the analysis of genomic and transcriptomic data through the use of parallel architectures for clusters composed of CPUs and GPUs.


**BioScience** is featured for:

* **Unified APIs, detailed documentation, and interactive examples** available to the community.
* **Complete coverage** for generate biological results from gene co-expression datasets.
* **Optimized models** to generate results in the shortest possible time.
* **Optimization of a High-Performance Computing (HPC) and Big Data ecosystem**.

----

Installation
============

It is recommended to use **pip** for installation. Please make sure
**the latest version** is installed, as bioScience is updated frequently:

.. code-block:: bash

   pip install bioscience            # normal install
   pip install --upgrade bioscience  # or update if needed
   pip install --pre bioscience      # or include pre-release version for new features

Alternatively, you could clone and run setup.py file:

.. code-block:: bash

   git clone https://github.com/aureliolfdez/bioscience.git
   pip install .

**Required Dependencies**\ :

* **Python**>=3.11
* **numpy**>=2.0.1
* **pandas**>=2.2.2
* **scikit-learn**>=1.5.1
* **numba**>=0.60.0
* **seaborn**>=0.13.2
* **matplotlib**>=3.9.0
* **setuptools**>=75.1.0
* **requests**>=2.32.3

----

API demo
========

.. code-block:: python


      import bioscience as bs

      if __name__ == "__main__":
         
         # RNA-Seq dataset load
         dataset = load(path="datasets/rnaseq.txt", index_gene=0, index_lengths=1 ,naFilter=True, head = 0)

         # RNA-Seq preprocessing
         bs.tpm(dataset)

         # Binary preprocessing
         bs.binarize(dataset)

         # Data mining phase
         listModels = bs.bibit(dataset, cMnr=2, cMnc=2, mode=3, deviceCount=1, debug = True)

         # Save results
         bs.saveGenes(path="/path/", models=listModels, data=dataset)

**Citing bioScience**\ :

`bioScience <https://www.sciencedirect.com/science/article/pii/S2352711024000372>`_ is published in
`SoftwareX <https://www.sciencedirect.com/science/article/pii/S2352711024000372>`_.
If you use bioScience in a scientific publication, we would appreciate citations to the following paper::

   López-Fernández, A., Gómez-Vela, F. A., Gonzalez-Dominguez, J., & Bidare-Divakarachari, P. (2024). bioScience: A new python science library for high-performance computing bioinformatics analytics. SoftwareX, 26, 101666.

**Key Links and Resources**\ :

* `View the latest codes on Github <https://github.com/aureliolfdez/bioscience>`_
* `View the documentation & API <https://bioscience.readthedocs.io/>`_
* `View all examples <https://github.com/aureliolfdez/bioscience/tree/main/tests/test_integration>`_