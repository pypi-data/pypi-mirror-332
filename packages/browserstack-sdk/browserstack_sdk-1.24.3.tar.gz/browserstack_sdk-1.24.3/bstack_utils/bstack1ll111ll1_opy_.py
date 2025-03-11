# coding: UTF-8
import sys
bstack1111l1l_opy_ = sys.version_info [0] == 2
bstack1llll1l_opy_ = 2048
bstack1ll1111_opy_ = 7
def bstack11lll_opy_ (bstack11lll1_opy_):
    global bstack1lll1l_opy_
    bstack1l1l11l_opy_ = ord (bstack11lll1_opy_ [-1])
    bstack11lllll_opy_ = bstack11lll1_opy_ [:-1]
    bstack1ll1lll_opy_ = bstack1l1l11l_opy_ % len (bstack11lllll_opy_)
    bstack11l1_opy_ = bstack11lllll_opy_ [:bstack1ll1lll_opy_] + bstack11lllll_opy_ [bstack1ll1lll_opy_:]
    if bstack1111l1l_opy_:
        bstack11llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack1llll1l_opy_ - (bstack111l1l1_opy_ + bstack1l1l11l_opy_) % bstack1ll1111_opy_) for bstack111l1l1_opy_, char in enumerate (bstack11l1_opy_)])
    else:
        bstack11llll1_opy_ = str () .join ([chr (ord (char) - bstack1llll1l_opy_ - (bstack111l1l1_opy_ + bstack1l1l11l_opy_) % bstack1ll1111_opy_) for bstack111l1l1_opy_, char in enumerate (bstack11l1_opy_)])
    return eval (bstack11llll1_opy_)
import re
from bstack_utils.bstack11ll1l1l1_opy_ import bstack1l11l111l11_opy_
def bstack1l11l111lll_opy_(fixture_name):
    if fixture_name.startswith(bstack11lll_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡷࡪࡺࡵࡱࡡࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᒅ")):
        return bstack11lll_opy_ (u"ࠫࡸ࡫ࡴࡶࡲ࠰ࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᒆ")
    elif fixture_name.startswith(bstack11lll_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᒇ")):
        return bstack11lll_opy_ (u"࠭ࡳࡦࡶࡸࡴ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬᒈ")
    elif fixture_name.startswith(bstack11lll_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᒉ")):
        return bstack11lll_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰ࠰ࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᒊ")
    elif fixture_name.startswith(bstack11lll_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡷࡩࡦࡸࡤࡰࡹࡱࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᒋ")):
        return bstack11lll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬᒌ")
def bstack1l11l11l11l_opy_(fixture_name):
    return bool(re.match(bstack11lll_opy_ (u"ࠫࡣࡥࡸࡶࡰ࡬ࡸࡤ࠮ࡳࡦࡶࡸࡴࢁࡺࡥࡢࡴࡧࡳࡼࡴࠩࡠࠪࡩࡹࡳࡩࡴࡪࡱࡱࢀࡲࡵࡤࡶ࡮ࡨ࠭ࡤ࡬ࡩࡹࡶࡸࡶࡪࡥ࠮ࠫࠩᒍ"), fixture_name))
def bstack1l11l11l1ll_opy_(fixture_name):
    return bool(re.match(bstack11lll_opy_ (u"ࠬࡤ࡟ࡹࡷࡱ࡭ࡹࡥࠨࡴࡧࡷࡹࡵࢂࡴࡦࡣࡵࡨࡴࡽ࡮ࠪࡡࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࡢ࠲࠯࠭ᒎ"), fixture_name))
def bstack1l11l111l1l_opy_(fixture_name):
    return bool(re.match(bstack11lll_opy_ (u"࠭࡞ࡠࡺࡸࡲ࡮ࡺ࡟ࠩࡵࡨࡸࡺࡶࡼࡵࡧࡤࡶࡩࡵࡷ࡯ࠫࡢࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࡢ࠲࠯࠭ᒏ"), fixture_name))
def bstack1l11l11111l_opy_(fixture_name):
    if fixture_name.startswith(bstack11lll_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᒐ")):
        return bstack11lll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩᒑ"), bstack11lll_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧᒒ")
    elif fixture_name.startswith(bstack11lll_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᒓ")):
        return bstack11lll_opy_ (u"ࠫࡸ࡫ࡴࡶࡲ࠰ࡱࡴࡪࡵ࡭ࡧࠪᒔ"), bstack11lll_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡇࡌࡍࠩᒕ")
    elif fixture_name.startswith(bstack11lll_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᒖ")):
        return bstack11lll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡩࡹࡳࡩࡴࡪࡱࡱࠫᒗ"), bstack11lll_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬᒘ")
    elif fixture_name.startswith(bstack11lll_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᒙ")):
        return bstack11lll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬᒚ"), bstack11lll_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡅࡑࡒࠧᒛ")
    return None, None
def bstack1l11l11l1l1_opy_(hook_name):
    if hook_name in [bstack11lll_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫᒜ"), bstack11lll_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨᒝ")]:
        return hook_name.capitalize()
    return hook_name
def bstack1l11l11ll1l_opy_(hook_name):
    if hook_name in [bstack11lll_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨᒞ"), bstack11lll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠧᒟ")]:
        return bstack11lll_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧᒠ")
    elif hook_name in [bstack11lll_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࠩᒡ"), bstack11lll_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠩᒢ")]:
        return bstack11lll_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡇࡌࡍࠩᒣ")
    elif hook_name in [bstack11lll_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࠪᒤ"), bstack11lll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠩᒥ")]:
        return bstack11lll_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬᒦ")
    elif hook_name in [bstack11lll_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠫᒧ"), bstack11lll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫᒨ")]:
        return bstack11lll_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡅࡑࡒࠧᒩ")
    return hook_name
def bstack1l11l1111l1_opy_(node, scenario):
    if hasattr(node, bstack11lll_opy_ (u"ࠬࡩࡡ࡭࡮ࡶࡴࡪࡩࠧᒪ")):
        parts = node.nodeid.rsplit(bstack11lll_opy_ (u"ࠨ࡛ࠣᒫ"))
        params = parts[-1]
        return bstack11lll_opy_ (u"ࠢࡼࡿࠣ࡟ࢀࢃࠢᒬ").format(scenario.name, params)
    return scenario.name
def bstack1l11l1111ll_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack11lll_opy_ (u"ࠨࡥࡤࡰࡱࡹࡰࡦࡥࠪᒭ")):
            examples = list(node.callspec.params[bstack11lll_opy_ (u"ࠩࡢࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡦࡺࡤࡱࡵࡲࡥࠨᒮ")].values())
        return examples
    except:
        return []
def bstack1l11l11ll11_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack1l11l111ll1_opy_(report):
    try:
        status = bstack11lll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᒯ")
        if report.passed or (report.failed and hasattr(report, bstack11lll_opy_ (u"ࠦࡼࡧࡳࡹࡨࡤ࡭ࡱࠨᒰ"))):
            status = bstack11lll_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᒱ")
        elif report.skipped:
            status = bstack11lll_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧᒲ")
        bstack1l11l111l11_opy_(status)
    except:
        pass
def bstack1l1111l11l_opy_(status):
    try:
        bstack1l11l11l111_opy_ = bstack11lll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᒳ")
        if status == bstack11lll_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᒴ"):
            bstack1l11l11l111_opy_ = bstack11lll_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᒵ")
        elif status == bstack11lll_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫᒶ"):
            bstack1l11l11l111_opy_ = bstack11lll_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬᒷ")
        bstack1l11l111l11_opy_(bstack1l11l11l111_opy_)
    except:
        pass
def bstack1l11l11lll1_opy_(item=None, report=None, summary=None, extra=None):
    return