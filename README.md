ADS_COVID-19
==============================

applied data science on COVID-19 data

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

## Objectives:
To develop a prototype for COVID-19 analysis using the learnt best practices of data science.
To create an interactive dashboard using industry standard CRISP-DM.
Plotting confirmed cases, doubling rate and SIR Model for all countries.
To generate COVID-19 infection statistics by implementing SIR Model.

## How to run:
- Clone the repository. 
- Use the Final_Submission.ipynb Jupiter notebook from folder Final_Project_Delivery folder from the cloned repository.

## First Delivery:
Plotting graph for three countries showing cases and vaccinations relative to population with respect to time. The countries chosen for this exercise were Australia, United Kingdom and Hong Kong. Following plots were generated:
![419148_Relative_Cases_COVID](https://user-images.githubusercontent.com/54177686/181649180-43db358c-ee12-44d6-ab74-4fadd8aad53a.png)

![419148_RelativeVax_perPop](https://user-images.githubusercontent.com/54177686/181649247-d7b7a241-596c-4de9-b309-7857615a337d.png)

## Pitch Video:
Watch the video uploaded in pitch_video folder.

## Final Delivery:
### The created Dashboard has following sections:

- Confirmed cases for all countries. The country/ies can be selected from the dropdown menu. Doubling rate: The time taken for the cases to double. Doubling rate filtered: Doubling rate using Savgol filter for better forecast.
![newplot](https://user-images.githubusercontent.com/54177686/181651888-6985636b-17fb-431f-857f-c9d55d92ca46.png)

- Plot for relative Vaccinations w.r.t. to population of the country. The plots are the ones shown in first delivery.

- An SIR model; S: Susceptible Population, I: Infected and R: Recovered, over period of time and the real cases plotted along with it for better understanding.
![newplot-2](https://user-images.githubusercontent.com/54177686/181651929-a722cd64-b165-4dfc-a290-7d5056d9c7a6.png)

- World Map for all countries.
![newplot-3](https://user-images.githubusercontent.com/54177686/181651973-2309dd1d-25ad-4cd1-b68c-518dbb8dd49b.png)

## FIN

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
