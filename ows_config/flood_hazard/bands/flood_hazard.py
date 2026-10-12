"""
Band definitions for the Flood Hazard (Bahaya Banjir 2025) products
"""

FLOOD_HAZARD_BANDS_INFO = {
    "flood_depth": "Kedalaman banjir (meter)",
    "flood_hazard_index": "Indeks bahaya banjir (0–1)",
    "flood_hazard_class": "Kelas bahaya banjir (rendah/sedang/tinggi)",
}

_BAND_ALIASES = {
    "flood_depth": ["flood_depth", "depth"],
    "flood_hazard_index": ["flood_hazard_index", "index", "hazard_index"],
    "flood_hazard_class": ["flood_hazard_class", "classified", "hazard_class"],
}


def flood_hazard_bands(suffix):
    return {
        f"{variable}_{suffix}": aliases
        for variable, aliases in _BAND_ALIASES.items()
    }
