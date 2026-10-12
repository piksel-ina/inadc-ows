"""
Flood Hazard (Bahaya Banjir 2025) product configuration.
"""

from ...common.resource_limits import FLOOD_HAZARD_LIMIT
from ..bands.flood_hazard import FLOOD_HAZARD_BANDS_INFO, flood_hazard_bands
from ..styles.flood_hazard import FLOOD_HAZARD_STYLES

_FLOOD_HAZARD_ABSTRACT = """
Bahaya banjir untuk {label} ({aep} AEP), diturunkan dari Modified Geomorphic
Flood Index berbasis data model elevasi FABDEM v1.2 dan data curah hujan BMKG.
Data satu periode, tahun 2025.

Tersedia tiga informasi/layer, yaitu kelas bahaya (rendah/sedang/tinggi),
kedalaman banjir hasil pemodelan dalam meter, dan indeks bahaya relatif.

Cakupan: ini adalah rilis yang hanya mencakup beberapa wilayah di Pulau Jawa
yang telah divalidasi pada tahun 2025.
"""

_RETURN_PERIODS = [
    (2, "rp02", "periode ulang 2 tahun", "50%"),
    (5, "rp05", "periode ulang 5 tahun", "20%"),
    (10, "rp10", "periode ulang 10 tahun", "10%"),
    (25, "rp25", "periode ulang 25 tahun", "4%"),
    (50, "rp50", "periode ulang 50 tahun", "2%"),
]


def _build_layer(return_period, suffix, label, aep):
    return {
        "title": f"Bahaya Banjir 2025 - Periode Ulang {return_period} Tahun ({aep} AEP)",
        "name": f"flood_hazard_{suffix}",
        "abstract": _FLOOD_HAZARD_ABSTRACT.format(label=label, aep=aep),
        "product_name": "flood_hazard",
        "bands": flood_hazard_bands(suffix),
        "resource_limits": FLOOD_HAZARD_LIMIT,
        "dynamic": False,
        "time_resolution": "summary",
        "default_time": "latest",
        "native_crs": "EPSG:6933",
        "native_resolution": [30, -30],
        "image_processing": {
            "extent_mask_func": ["ows_config.common.band_utils.mask_by_nan"],
            "always_fetch_bands": [],
            "manual_merge": False,
            "apply_solar_corrections": False,
        },
        "feature_info": {
            "include_utc_dates": False,
            "include_bands": FLOOD_HAZARD_BANDS_INFO,
        },
        "styling": {
            "default_style": "hazard_class",
            "styles": FLOOD_HAZARD_STYLES,
        },
    }


flood_hazard_layers = [
    _build_layer(rp, suffix, label, aep)
    for rp, suffix, label, aep in _RETURN_PERIODS
]

flood_hazard_folder = {
    "title": "Bahaya Banjir 2025",
    "abstract": """
                Skenario bahaya banjir Indonesia yang diproduksi pada tahun 2025
                dengan lima periode ulang (2, 5, 10, 25, dan 50 tahun). Setiap
                periode ulang diterbitkan sebagai produk tersendiri yang
                masing-masing menyediakan kelas bahaya, kedalaman banjir, dan
                indeks bahaya.
                """,
    "keywords": [
        "banjir",
        "flood",
        "bahaya",
        "hazard",
        "genangan",
        "inundation",
        "periode ulang",
    ],
    "layers": flood_hazard_layers,
}
