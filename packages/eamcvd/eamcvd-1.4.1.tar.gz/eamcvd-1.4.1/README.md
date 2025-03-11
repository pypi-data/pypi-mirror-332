# EAMCVD

A library to fetch EAMCVD(elefant ai mod comp. and vulnerabilities database) incompatibility reports.

## Installation

 `pip install eamcvd`

## Usage

```python
from eamcvd import requlib

# Search by ID
posts = requlib.getByID('id(witout 'eai-')')

# Search by name
posts = requlib.getByName('mod-name')
