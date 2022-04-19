import csv

import pymc3 as pm
import requests

# Via https://stackoverflow.com/a/35371451
CSV_URL = "https://raw.githubusercontent.com/Kaushik-Varma/linear_regression_model_python/main/Company_data.csv"
with requests.Session() as s:
    download = s.get(CSV_URL)

    decoded_content = download.content.decode("utf-8")

    cr = csv.reader(decoded_content.splitlines(), delimiter=",")
    my_list = list(cr)
    count = 0
    for row in my_list:
        count += 1


        # Via https://docs.pymc.io/en/v3/
        # x, y = linear_training_data()
        if count > 1:
            print(row)
            x, y = row[0], row[1]
            with pm.Model() as linear_model:
                weights = pm.Normal("weights", mu=0, sigma=1)
                noise = pm.Gamma("noise", alpha=2, beta=1)
                y_observed = pm.Normal(
                    "y_observed",
                    mu=x @ weights,
                    sigma=noise,
                    observed=y,
                )

                prior = pm.sample_prior_predictive()
                posterior = pm.sample()
                posterior_pred = pm.sample_posterior_predictive(posterior)
