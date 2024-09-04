import pytest
from src.LLM import review_code
from src.utils.review_utils import load_file

def test_review_yaml():
    yaml_content = load_file('code_files/test.yaml', 'yaml')
    review = review_code(yaml_content if isinstance(yaml_content, str) else yaml.dump(yaml_content), 'yaml')
    assert isinstance(review, str)
    assert "Best practices" in review  # Example assertion

def test_review_docker():
    docker_content = load_file('code_files/test.Dockerfile', 'docker')
    review = review_code(docker_content, 'docker')
    assert isinstance(review, str)
    assert "Best practices" in review  # Example assertion

def test_review_jenkins():
    jenkins_content = load_file('code_files/test.Jenkinsfile', 'jenkins')
    review = review_code(jenkins_content, 'jenkins')
    assert isinstance(review, str)
    assert "Best practices" in review  # Example assertion

def test_review_travis():
    travis_content = load_file('code_files/test.travis.yml', 'travis')
    review = review_code(travis_content, 'travis')
    assert isinstance(review, str)
    assert "Best practices" in review  # Example assertion

def test_review_github_actions():
    github_actions_content = load_file('code_files/test.github.yml', 'github_actions')
    review = review_code(github_actions_content, 'github_actions')
    assert isinstance(review, str)
    assert "Best practices" in review  # Example assertion
