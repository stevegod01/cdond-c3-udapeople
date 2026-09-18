# Udapeople deployment runbook

## Before enabling the cloud workflow

1. Use a dedicated AWS test environment and review all three CloudFormation templates.
2. Supply AWS_DEFAULT_REGION and AWS authentication through CircleCI's protected project/context configuration. Never commit credentials.
3. Supply BACKEND_AMI_ID (current Ubuntu x86_64 AMI in that region), EC2_KEY_PAIR_NAME, and SSH_CIDR. Install the corresponding private SSH key in CircleCI and replace the historical fingerprint in configuration. The old default AMI/key name is no longer used.
4. Provision a PostgreSQL database reachable from the new backend and set TYPEORM_HOST, TYPEORM_PORT, TYPEORM_USERNAME, TYPEORM_PASSWORD, TYPEORM_DATABASE, TYPEORM_CONNECTION, TYPEORM_ENTITIES, TYPEORM_MIGRATIONS and TYPEORM_MIGRATIONS_DIR appropriately. Review backend/.env.sample. Database provisioning is outside this pipeline.
5. Confirm the Ubuntu image can download the pinned Node.js distribution, that community.general can be installed, and that PM2/node-exporter requirements fit the host. The configuration targets x86_64 and the ubuntu user.
6. Decide backup/restore and migration-reversal procedures before any schema changes. Migrations cannot safely be undone merely by deleting EC2/S3.
7. Run local checks and examine the dependency-audit jobs. Audit jobs report issues and do not mutate package files. A failing audit blocks deployment.
8. Trigger a CircleCI pipeline with boolean deploy=true, inspect the plan/settings, and approve approve-deployment. A normal push does not enable the cloud workflow.

No cloud deployment, account credentials, live endpoints, database migrations, or Ansible remote execution were used during the September 2026 cleanup.

## Changes in the repaired workflow

- A workflow-local marker records whether migration output reports an applied migration, replacing the external kvdb.io service.
- Backend smoke checks require a successful HTTP response containing JSON status=ok. Frontend checks require a successful response containing the actual root element, rather than an unrelated Welcome string.
- Each endpoint probe has a ten-second request timeout and at most twelve attempts with five-second delays.
- The Ansible deployment updates only the named udapeople PM2 process.
- The previous environment ID must be a seven-character lowercase hexadecimal workflow prefix before cleanup. Missing or current IDs are skipped; malformed IDs fail instead of being used in a deletion command.
- npm ci consumes repaired lockfiles. Cloud executors and targets still need runtime/environment verification; the historical application libraries were not fully upgraded.

## Failure handling and rollback

If infrastructure/configuration fails, the failure cleanup command removes that workflow's frontend objects and stacks. Inspect the console if cleanup itself fails. Avoid running concurrent deployments against the same shared database and CDN.

Database rollback is **manual**: the pipeline records a migration marker but does not automatically revert migrations from parallel application jobs. Review which migrations ran, verify backups, and use the repository's migrations:revert command only after determining that reversing the latest migration is appropriate. A workflow can apply multiple migrations; a single revert is not a complete restore.

If an endpoint probe fails, the workflow stops before the CDN update. If the CDN update fails, do not remove the previous environment until the distribution state is understood. Automatic previous-environment cleanup runs only after CloudFormation reports the CDN stack update complete.

For intentional teardown, identify the exact workflow ID and the shared InitialStack CDN, database, monitoring and IAM resources. Delete only resources belonging to the test deployment after checking dependencies. The repository does not contain a universal account-wide teardown command.

## Remaining validation

Local application build/unit tests and pipeline-helper tests pass. AWS template semantics, account permissions, runtime image downloads, Ansible collection installation, AMI bootstrap, real HTTP endpoints, migrations and restoration remain unverified against a live test environment. There is no production-readiness claim.
