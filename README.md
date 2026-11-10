# inadc-ows

[![Tests](https://github.com/piksel-ina/inadc-ows/actions/workflows/test.yml/badge.svg)](https://github.com/piksel-ina/inadc-ows/actions/workflows/test.yml)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Build-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![OGC](https://img.shields.io/badge/OGC-WMS%20%2F%20WCS-blue)](https://www.ogc.org/)

OWS (OGC Web Services) for the Indonesia datacube platform, powered by [datacube-ows](https://github.com/opendatacube/datacube-ows).

Requires a PostGIS database with ODC initialised and products indexed. For a quick setup with pre-configured products, use [inadc-odc](https://github.com/piksel-ina/inadc-odc) — once it's running:

    make build
    make up
    # Export env vars to connect to local ODC DB.
    make init
    # ows workers cache layer ranges at boot; must restart to pick up
    # data added/ranges updated by `make init` (or any later `datacube-ows-update` run).
    make restart

## CI

Push a tag matching `inadc-ows-vYYYYMMDD-HHMM` to trigger an image build to ECR.
