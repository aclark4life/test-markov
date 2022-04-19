import csv

import pymc3 as pm
import requests

# Via https://stackoverflow.com/a/35371451
CSV_URL = "http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv"
with requests.Session() as s:
    download = s.get(CSV_URL)

    decoded_content = download.content.decode("utf-8")

    cr = csv.reader(decoded_content.splitlines(), delimiter=",")
    my_list = list(cr)
    for row in my_list:
        print(row)


# Via https://docs.pymc.io/en/v3/
X, y = linear_training_data()
with pm.Model() as linear_model:
    weights = pm.Normal("weights", mu=0, sigma=1)
    noise = pm.Gamma("noise", alpha=2, beta=1)
    y_observed = pm.Normal(
        "y_observed",
        mu=X @ weights,
        sigma=noise,
        observed=y,
    )

    prior = pm.sample_prior_predictive()
    posterior = pm.sample()
    posterior_pred = pm.sample_posterior_predictive(posterior)
