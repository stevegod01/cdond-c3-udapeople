# Historical HNG9 Docker exercise

This folder preserves a historical internship exercise from [stevegod01/hng9-stage2-docker-task at commit 6efae0d](https://github.com/stevegod01/hng9-stage2-docker-task/tree/6efae0dab5d9bbe2afae4ba94da9b583540cebcf). The original Git history remains in the source repository; inherited license notices and the original submission record are retained here. [SOURCE.md](SOURCE.md) records the baseline and consolidation changes.

Generated node_modules and Python bytecode are excluded; install from the checked-in manifests/lockfile. Compose builds the checked-in sources, binds development ports only to localhost, and requires a disposable Django secret from the environment. A committed demo key is no longer used by the code. The SQLite database path now resolves inside the API project directory.

## Local learning setup

These historical Python/Django/React/Node versions are obsolete. This is not a production-ready application and no current image-build result is claimed.

~~~sh
export DJANGO_SECRET_KEY=$(python -c "import secrets; print(secrets.token_urlsafe(48))")
docker compose config --quiet
docker compose up --build
docker compose down
~~~

PowerShell: assign the generated value to $env:DJANGO_SECRET_KEY before the Compose commands.

Inspect localhost:3000 and localhost:8000 after successful startup. The Django project is a scaffold, not an integrated marketplace API. No cloud deployment is needed. Do not expose these development servers publicly; modernization is a separate project.

The frontend and API Dockerfiles describe development servers explicitly. Both build contexts exclude dependencies, credentials and generated artifacts. Generated dependency files remain recoverable from Git history.

[Historical submission record](HISTORICAL-README.md) preserves the original server/image references without asserting current availability. LICENSE.md contains inherited public-domain/US-government language; this copy does not assert that newly written material has that provenance. No new license or authorship claim is added.
