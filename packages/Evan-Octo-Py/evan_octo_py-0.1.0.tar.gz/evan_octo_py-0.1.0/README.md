# OctoPy

OctoPy is a Python library that provides a comprehensive interface to GitHub's API, specifically focused on managing GitHub Copilot, Rulesets, and Custom Properties for organizations and repositories.

## Features

### GitHub Copilot Management
- Get Copilot metrics for enterprises, organizations, and teams
- Retrieve Copilot usage summaries
- Manage Copilot seat assignments for users and teams
- Add/remove users and teams from Copilot subscriptions

### Rulesets Management
- Create, read, update, and delete rulesets for organizations
- Manage repository-specific rulesets
- List and query ruleset configurations

### Custom Properties Management
- Manage custom properties for organizations and repositories
- Create, update, and delete custom property definitions
- Query custom property configurations

## Installation

```bash
pip install octopy
```

## Usage

### Basic Setup

```python
from octopy import OctoPy

# Initialize with a personal access token
octopy = OctoPy(
    token="your_github_token",
    org="your_organization",
    enterprise="your_enterprise"  # Optional
)
```

### GitHub App Authentication

```python
from octopy import OctoPy

# Initialize with GitHub App credentials
octopy = OctoPy(
    app_id="your_app_id",
    org="your_organization"
)
```

### Examples

#### Managing Copilot

```python
# Get Copilot metrics for an organization
metrics = octopy.get_copilot_metrics_org()

# Add users to Copilot
octopy.add_users_to_copilot(["username1", "username2"])

# Get usage summary for a team
usage = octopy.get_copilot_usage_team("team-slug")
```

#### Managing Rulesets

```python
# List organization rulesets
rulesets = octopy.list_org_rulesets()

# Create a new ruleset
ruleset_data = {
    "name": "My Ruleset",
    "target": "branch",
    "enforcement": "active"
}
octopy.create_org_ruleset(ruleset_data)
```

#### Managing Custom Properties

```python
# List organization custom properties
properties = octopy.list_org_custom_properties()

# Create a new custom property
property_data = {
    "value_type": "string",
    "required": True
}
octopy.create_org_custom_property("property_name", property_data)
```

## Requirements

- Python 3.6+
- `requests` library
- GitHub Personal Access Token or GitHub App credentials
- Appropriate GitHub permissions for the operations you want to perform

## Authentication

OctoPy supports two authentication methods:
1. Personal Access Token (PAT)
2. GitHub App authentication

For GitHub App authentication, you'll need:
- App ID
- Private key file (app_key.pem)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. # Octo-Py