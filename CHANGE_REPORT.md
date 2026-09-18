# Change report — 18 September 2026

Original HEAD: `58798071bd411060373e5dbe6aa3f619444857ed`.

## Implemented

- Repaired backend/frontend npm lockfiles to agree with their existing manifests; retained the original application framework versions.
- Added ordinary cloud-free CircleCI build/test jobs and GitHub helper checks. Cloud delivery requires deploy=true and a separate approval job.
- Added a GitHub Actions frontend/backend matrix on Node.js 24.16.0 using `npm ci --ignore-scripts --legacy-peer-deps`, the existing unit-test commands and application builds. Frontend jobs set the retained Webpack OpenSSL compatibility option and a loopback API URL; no live API or cloud service is called by the mocked unit tests.
- Preserved the original deployment config and inherited Jira workflow under docs/legacy; the Jira workflow cannot run from that directory.
- Replaced failing/unbounded smoke shell logic with a tested Python helper requiring HTTP success and the actual API/frontend response.
- Replaced external kvdb migration coordination with a workflow-local marker. Removed automatic database reversal from parallel jobs; manual migration rollback is documented.
- Changed dependency scans from mutating npm audit fix to reporting npm audit. No dependency audit was run during this work.
- Required deployment-specific AMI, key pair and SSH CIDR inputs; replaced fixed sleep with wait_for_connection; pinned the Node runtime on the target host; scoped PM2 restarts to udapeople; changed exporter executable mode to 0755.
- Guarded previous-environment cleanup with exact workflow-ID validation.
- Added the operator runbook, case-study README, and immutable consolidation manifest identifying all 23 non-identical files in the older variant. Its full Git history is preserved separately.

## Consolidated learning material

- Added `labs/lambda-packaging` from the linuxacademy course fork at `496f966742cc3960a5ea96cdd96e3a437222d330`. The repaired handler validates its event, has offline tests, needs no third-party runtime packages, and is packaged at the zip root. The standalone workflow example is retained with its path-adaptation requirement documented.
- Added `labs/docker-compose` from the HNG9 exercise at `6efae0dab5d9bbe2afae4ba94da9b583540cebcf`. Generated dependencies and bytecode are excluded. Compose builds local sources, binds ports to localhost, and requires an environment-provided demo secret. The SQLite path is joined correctly inside the API project directory. The original submission record and inherited license notices remain alongside a source record.
- Added two byte-identical screenshots from `proof` at `9486584093f487db3b3d1323c6acdbb16541d578` under `docs/contributions/todoassistant`. Their context explicitly distinguishes historical team contributions from sole authorship, successful checks, or a current deployment.
- Added `.github/workflows/lab-quality.yml` for offline Lambda tests, zip packaging and Compose configuration validation. The workflow does not launch containers or deploy to AWS.
- Added successor notices to the three source repositories while preserving their history. The HNG source cleanup removes 21,302 tracked generated files; original history and its verified local Git bundle preserve recovery evidence.

## Local verification

Python 3.12.14, Node.js 24.16.0 on Windows:

- Backend: 51 suites, 79 tests passed; TypeScript build passed.
- Frontend: 5 suites, 12 tests passed; Webpack build passed with the legacy OpenSSL compatibility option.
- New endpoint helper: 5 tests passed with injected HTTP responses, without network access.
- YAML parsing and deployment-default/approval checks passed.
- Repaired npm lockfiles were checked with offline npm ci dry runs. The v1 lockfile format is retained to keep diffs focused; modern npm prints old-lockfile metadata notices.
- git diff --check passed after line-ending normalization.
- Lambda tests passed in both the original fork and consolidated copy: two tests per copy, including six invalid-event subcases.
- Both HNG Compose configurations passed `docker compose config --quiet` with exit 0 using a new empty `DOCKER_CONFIG` directory and a disposable validation placeholder. No user Docker configuration or daemon operation was needed.
- Both SQLite path expressions were parsed and checked against the API project directory. Consolidation headings passed strict UTF-8 decoding; copied contribution images matched their source SHA-256 hashes and were visually reviewed.
- GitHub application/lab workflow YAML parsed successfully. Matrix paths, existing package scripts/lockfiles, Node 24.16.0, frontend environment and exact test/build commands were checked against the locally verified instructions. The OpenSSL compatibility setting also passed a local Node 24.19.0 runtime check; no additional full application test run is implied by that check.

## Remaining limits

No cloud resource, database migration, real HTTP endpoint, Ansible remote host or remote CI workflow was exercised. Ansible/Python YAML parse checks are not a complete Ansible semantic or AWS validation. The retained historical dependencies produce deprecation notices and still need deliberate modernization; the frontend build needs the compatibility option and API_URL. The backend's separate end-to-end suite was not run. Current AMI availability, SSH key fingerprints and account/environment configuration remain operator inputs. Node distribution and Ansible collection installation were authored but not remotely tested.

The consolidated HNG exercise retains obsolete framework/runtime versions and development servers. Compose configuration parsing does not prove that its images currently build or its services start; neither was attempted. Lambda packaging was checked locally, but no Lambda deployment or remote workflow run is claimed. The screenshots remain historical evidence with visible failed checks.

No remote commit, push, archival or deployment was performed by this lane.
