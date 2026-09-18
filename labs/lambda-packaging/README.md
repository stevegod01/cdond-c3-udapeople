# Offline Lambda packaging lab

Adapted from [stevegod01's linuxacademy course fork](https://github.com/stevegod01/content-github-actions-deep-dive-lesson/tree/496f966742cc3960a5ea96cdd96e3a437222d330). The original history stays in that archive; this folder contains the repaired small exercise.

The handler returns World for an input field equal to Hello and rejects malformed events. No AWS account, network or credentials are used. This is a packaging exercise, not a deployed Lambda.

~~~sh
python -m unittest discover -s tests -v
python -m zipfile -c lambda-example.zip function/lambda_function.py
~~~

The repository-level lab-quality workflow checks and packages the handler at the zip root, as required for a lambda_function.lambda_handler entrypoint. workflow.example.yml records the standalone form and must have paths adapted if reused.

No third-party runtime dependencies remain. Original course attribution and applicable notices are retained; no new license is granted.
