"""Offline YAML and workflow checks. This does not validate an AWS deployment."""
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


class CloudFormationLoader(yaml.SafeLoader):
    pass


def construct_intrinsic(loader, suffix, node):
    if isinstance(node, yaml.ScalarNode):
        return {suffix: loader.construct_scalar(node)}
    if isinstance(node, yaml.SequenceNode):
        return {suffix: loader.construct_sequence(node)}
    return {suffix: loader.construct_mapping(node)}


CloudFormationLoader.add_multi_constructor("!", construct_intrinsic)


def validate():
    config = yaml.safe_load((ROOT / ".circleci/config.yml").read_text())
    assert config["parameters"]["deploy"]["default"] is False
    assert config["workflows"]["deploy"]["when"] == "<< pipeline.parameters.deploy >>"
    assert config["workflows"]["validate"]["jobs"] == ["offline-checks", "application-checks"]
    deploy_jobs = config["workflows"]["deploy"]["jobs"]
    assert any(isinstance(job, dict) and job.get("approve-deployment", {}).get("type") == "approval"
               for job in deploy_jobs)
    assert not (ROOT / ".github/workflows/manual.yml").exists(), "Inherited Jira automation is active"
    for path in (ROOT / ".circleci").rglob("*.yml"):
        yaml.load(path.read_text(), Loader=CloudFormationLoader)
    print("CircleCI deployment opt-in, approval gate, and YAML parse checks passed")


if __name__ == "__main__":
    validate()
