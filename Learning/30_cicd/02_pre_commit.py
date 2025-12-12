PRE_COMMIT = '''
repos:
- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: v4.4.0
  hooks:
  - id: trailing-whitespace
  - id: end-of-file-fixer
  - id: check-yaml
- repo: https://github.com/psf/black
  rev: 23.3.0
  hooks:
  - id: black
'''

PYPROJECT = '''
[tool.black]
line-length = 88
target-version = [\
