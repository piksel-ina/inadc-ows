import pytest


REQUIRED_CFG_KEYS = {"global", "wms", "wcs", "layers"}

REQUIRED_LAYER_KEYS = {
    "name",
    "title",
    "product_name",
    "native_crs",
    "native_resolution",
    "styling",
    "bands",
    "image_processing",
    "resource_limits",
}

REQUIRED_STYLE_KEYS = {"name", "title"}

EXPECTED_LAYER_NAMES = {
    "s2_l2a",
    "s2_geomad_annual_spectral",
    "s2_geomad_annual_indices",
    "s2_geomad_annual_statistics",
    "flood_hazard_rp02",
    "flood_hazard_rp05",
    "flood_hazard_rp10",
    "flood_hazard_rp25",
    "flood_hazard_rp50",
    "ls5_c2l2_sr",
    "ls7_c2l2_sr",
    "ls8_c2l2_sr",
    "ls9_c2l2_sr",
}

EXPECTED_PRODUCT_NAMES = {
    "s2_l2a",
    "s2_geomad_annual",
    "flood_hazard",
    "ls5_c2l2_sr",
    "ls7_c2l2_sr",
    "ls8_c2l2_sr",
    "ls9_c2l2_sr",
}


def iter_named_layers(layers):
    """Yield named layers, descending into folder layers."""
    for layer in layers:
        if "layers" in layer:
            yield from iter_named_layers(layer["layers"])
        else:
            yield layer


@pytest.fixture
def ows_cfg():
    from ows_config.ows_cfg import ows_cfg

    return ows_cfg


@pytest.fixture
def named_layers(ows_cfg):
    return list(iter_named_layers(ows_cfg["layers"]))


def test_ows_cfg_imports(ows_cfg):
    assert isinstance(ows_cfg, dict)


def test_ows_cfg_top_level_keys(ows_cfg):
    missing = REQUIRED_CFG_KEYS - set(ows_cfg.keys())
    assert not missing, f"Missing top-level keys: {missing}"


def test_layers_is_list(ows_cfg):
    assert isinstance(ows_cfg["layers"], list)
    assert len(ows_cfg["layers"]) > 0


def test_expected_layer_names(named_layers):
    names = {layer["name"] for layer in named_layers}
    missing = EXPECTED_LAYER_NAMES - names
    assert not missing, f"Missing layers: {missing}"


def test_no_extra_layer_names(named_layers):
    names = {layer["name"] for layer in named_layers}
    extra = names - EXPECTED_LAYER_NAMES
    assert not extra, f"Unexpected layers: {extra}"


def test_each_layer_has_required_keys(named_layers):
    for layer in named_layers:
        missing = REQUIRED_LAYER_KEYS - set(layer.keys())
        assert not missing, f"Layer '{layer.get('name', '?')}' missing keys: {missing}"


def test_each_layer_styling_has_default_and_styles(named_layers):
    for layer in named_layers:
        styling = layer["styling"]
        assert "default_style" in styling, f"Layer '{layer['name']}' missing default_style"
        assert "styles" in styling, f"Layer '{layer['name']}' missing styles"
        assert len(styling["styles"]) > 0, f"Layer '{layer['name']}' has no styles"


def test_each_style_has_required_keys(named_layers):
    for layer in named_layers:
        for style in layer["styling"]["styles"]:
            missing = REQUIRED_STYLE_KEYS - set(style.keys())
            assert not missing, (
                f"Style in layer '{layer['name']}' missing keys: {missing}"
            )


def test_expected_product_names(named_layers):
    products = {layer["product_name"] for layer in named_layers}
    missing = EXPECTED_PRODUCT_NAMES - products
    assert not missing, f"Missing product names: {missing}"


def test_flood_hazard_layers_map_their_return_period(named_layers):
    flood_layers = [l for l in named_layers if l["name"].startswith("flood_hazard_")]
    assert len(flood_layers) == 5
    for layer in flood_layers:
        suffix = layer["name"].removeprefix("flood_hazard_")
        assert layer["product_name"] == "flood_hazard"
        assert layer["bands"] == {
            f"flood_depth_{suffix}": ["flood_depth", "depth"],
            f"flood_hazard_index_{suffix}": ["flood_hazard_index", "index", "hazard_index"],
            f"flood_hazard_class_{suffix}": ["flood_hazard_class", "classified", "hazard_class"],
        }


def test_global_has_published_crss(ows_cfg):
    crss = ows_cfg["global"].get("published_CRSs", {})
    assert len(crss) > 0, "No published CRSs defined"


def test_services_enabled(ows_cfg):
    services = ows_cfg["global"].get("services", {})
    assert services.get("wms") is True, "WMS not enabled"
    assert services.get("wcs") is True, "WCS not enabled"
