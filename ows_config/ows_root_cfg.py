"""
Root OWS configuration - global settings
"""

service_title = "DE Indonesia (Piksel) Web Services"
service_abstract = """
Data penginderaan jauh dan produk turunannya dari Digital Earth Indonesia (Piksel).
"""

service_keywords = [
    "digital earth",
    "digital earth indonesia",
    "datacube ows",
    "flood",
    "banjir",
    "penginderaan jauh",
    "geospasial",
    "bahaya banjir",
    "indonesia",
    "piksel",
]

contact_info = {
    "person": "Muhammad Taufik",
    "organisation": "Badan Informasi Geospasial",
    "position": "",
    "address": {
        "type": "postal",
        "address": "Badan Informasi Geospasial",
        "city": "Bogor",
        "state": "Jawa Barat",
        "postcode": "16920",
        "country": "Indonesia",
    },
    "email": "muhammad.taufik@big.go.id",
    "telephone": "",
    "fax": ""
}

published_CRSs = {
    "EPSG:3857": {
        "geographic": False,
        "horizontal_coord": "x",
        "vertical_coord": "y",
    },
    "EPSG:4326": {
        "geographic": True,
        "vertical_coord_first": True
    },
    "EPSG:3577": {
        "geographic": False,
        "horizontal_coord": "x",
        "vertical_coord": "y",
    },
    "EPSG:6933": {
        "geographic": False,
        "horizontal_coord": "x",
        "vertical_coord": "y",
    }
}

allowed_urls = [
    "https://ows.piksel.big.go.id",
    "https://ows-uncached.piksel.big.go.id",
    "https://ows.staging.piksel.big.go.id",
    "https://ows-uncached.staging.piksel.big.go.id",
    "https://*.staging.piksel.big.go.id",
]


services = {
    "wms": True,
    "wcs": True,
    "wmts": True,
}

wms = {
    "max_width": 512,
    "max_height": 512,
    "caps_cache_maxage": 60 * 60 * 24,
}

wcs = {
    "default_geographic_CRS": "EPSG:4326",
    "formats": {
        "GeoTIFF": {
            "renderers": {
                "1": "datacube_ows.wcs1_utils.get_tiff",
                "2": "datacube_ows.wcs2_utils.get_tiff",
            },
            "mime": "image/geotiff",
            "extension": "tif",
            "multi-time": False,
        },
        "netCDF": {
            "renderers": {
                "1": "datacube_ows.wcs1_utils.get_netcdf",
                "2": "datacube_ows.wcs2_utils.get_netcdf",
            },
            "mime": "application/x-netcdf",
            "extension": "nc",
            "multi-time": True,
        },
    },
    "native_format": "GeoTIFF",
}

ENABLE_SURFACE_REFLECTANCE = True
ENABLE_FLOOD_HAZARD = True
