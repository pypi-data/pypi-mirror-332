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
import os
import re
from enum import Enum
bstack1llllll111_opy_ = {
  bstack11lll_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨᖙ"): bstack11lll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡵࡴࡧࡵࠫᖚ"),
  bstack11lll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫᖛ"): bstack11lll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡭ࡨࡽࠬᖜ"),
  bstack11lll_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᖝ"): bstack11lll_opy_ (u"ࠫࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᖞ"),
  bstack11lll_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬᖟ"): bstack11lll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡻࡳࡦࡡࡺ࠷ࡨ࠭ᖠ"),
  bstack11lll_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬᖡ"): bstack11lll_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࠩᖢ"),
  bstack11lll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬᖣ"): bstack11lll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࠩᖤ"),
  bstack11lll_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩᖥ"): bstack11lll_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᖦ"),
  bstack11lll_opy_ (u"࠭ࡤࡦࡤࡸ࡫ࠬᖧ"): bstack11lll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡤࡦࡤࡸ࡫ࠬᖨ"),
  bstack11lll_opy_ (u"ࠨࡥࡲࡲࡸࡵ࡬ࡦࡎࡲ࡫ࡸ࠭ᖩ"): bstack11lll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡲࡸࡵ࡬ࡦࠩᖪ"),
  bstack11lll_opy_ (u"ࠪࡲࡪࡺࡷࡰࡴ࡮ࡐࡴ࡭ࡳࠨᖫ"): bstack11lll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡲࡪࡺࡷࡰࡴ࡮ࡐࡴ࡭ࡳࠨᖬ"),
  bstack11lll_opy_ (u"ࠬࡧࡰࡱ࡫ࡸࡱࡑࡵࡧࡴࠩᖭ"): bstack11lll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡰࡱ࡫ࡸࡱࡑࡵࡧࡴࠩᖮ"),
  bstack11lll_opy_ (u"ࠧࡷ࡫ࡧࡩࡴ࠭ᖯ"): bstack11lll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡷ࡫ࡧࡩࡴ࠭ᖰ"),
  bstack11lll_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰࡐࡴ࡭ࡳࠨᖱ"): bstack11lll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡶࡩࡱ࡫࡮ࡪࡷࡰࡐࡴ࡭ࡳࠨᖲ"),
  bstack11lll_opy_ (u"ࠫࡹ࡫࡬ࡦ࡯ࡨࡸࡷࡿࡌࡰࡩࡶࠫᖳ"): bstack11lll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡹ࡫࡬ࡦ࡯ࡨࡸࡷࡿࡌࡰࡩࡶࠫᖴ"),
  bstack11lll_opy_ (u"࠭ࡧࡦࡱࡏࡳࡨࡧࡴࡪࡱࡱࠫᖵ"): bstack11lll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡧࡦࡱࡏࡳࡨࡧࡴࡪࡱࡱࠫᖶ"),
  bstack11lll_opy_ (u"ࠨࡶ࡬ࡱࡪࢀ࡯࡯ࡧࠪᖷ"): bstack11lll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡶ࡬ࡱࡪࢀ࡯࡯ࡧࠪᖸ"),
  bstack11lll_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬᖹ"): bstack11lll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡷࡪࡲࡥ࡯࡫ࡸࡱࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ᖺ"),
  bstack11lll_opy_ (u"ࠬࡳࡡࡴ࡭ࡆࡳࡲࡳࡡ࡯ࡦࡶࠫᖻ"): bstack11lll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡳࡡࡴ࡭ࡆࡳࡲࡳࡡ࡯ࡦࡶࠫᖼ"),
  bstack11lll_opy_ (u"ࠧࡪࡦ࡯ࡩ࡙࡯࡭ࡦࡱࡸࡸࠬᖽ"): bstack11lll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡪࡦ࡯ࡩ࡙࡯࡭ࡦࡱࡸࡸࠬᖾ"),
  bstack11lll_opy_ (u"ࠩࡰࡥࡸࡱࡂࡢࡵ࡬ࡧࡆࡻࡴࡩࠩᖿ"): bstack11lll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡰࡥࡸࡱࡂࡢࡵ࡬ࡧࡆࡻࡴࡩࠩᗀ"),
  bstack11lll_opy_ (u"ࠫࡸ࡫࡮ࡥࡍࡨࡽࡸ࠭ᗁ"): bstack11lll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡸ࡫࡮ࡥࡍࡨࡽࡸ࠭ᗂ"),
  bstack11lll_opy_ (u"࠭ࡡࡶࡶࡲ࡛ࡦ࡯ࡴࠨᗃ"): bstack11lll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡶࡶࡲ࡛ࡦ࡯ࡴࠨᗄ"),
  bstack11lll_opy_ (u"ࠨࡪࡲࡷࡹࡹࠧᗅ"): bstack11lll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡪࡲࡷࡹࡹࠧᗆ"),
  bstack11lll_opy_ (u"ࠪࡦ࡫ࡩࡡࡤࡪࡨࠫᗇ"): bstack11lll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦ࡫ࡩࡡࡤࡪࡨࠫᗈ"),
  bstack11lll_opy_ (u"ࠬࡽࡳࡍࡱࡦࡥࡱ࡙ࡵࡱࡲࡲࡶࡹ࠭ᗉ"): bstack11lll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡽࡳࡍࡱࡦࡥࡱ࡙ࡵࡱࡲࡲࡶࡹ࠭ᗊ"),
  bstack11lll_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡄࡱࡵࡷࡗ࡫ࡳࡵࡴ࡬ࡧࡹ࡯࡯࡯ࡵࠪᗋ"): bstack11lll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡥ࡫ࡶࡥࡧࡲࡥࡄࡱࡵࡷࡗ࡫ࡳࡵࡴ࡬ࡧࡹ࡯࡯࡯ࡵࠪᗌ"),
  bstack11lll_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭ᗍ"): bstack11lll_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࠪᗎ"),
  bstack11lll_opy_ (u"ࠫࡷ࡫ࡡ࡭ࡏࡲࡦ࡮ࡲࡥࠨᗏ"): bstack11lll_opy_ (u"ࠬࡸࡥࡢ࡮ࡢࡱࡴࡨࡩ࡭ࡧࠪᗐ"),
  bstack11lll_opy_ (u"࠭ࡡࡱࡲ࡬ࡹࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᗑ"): bstack11lll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡱࡲ࡬ࡹࡲࡥࡶࡦࡴࡶ࡭ࡴࡴࠧᗒ"),
  bstack11lll_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡏࡧࡷࡻࡴࡸ࡫ࠨᗓ"): bstack11lll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡸࡷࡹࡵ࡭ࡏࡧࡷࡻࡴࡸ࡫ࠨᗔ"),
  bstack11lll_opy_ (u"ࠪࡲࡪࡺࡷࡰࡴ࡮ࡔࡷࡵࡦࡪ࡮ࡨࠫᗕ"): bstack11lll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡲࡪࡺࡷࡰࡴ࡮ࡔࡷࡵࡦࡪ࡮ࡨࠫᗖ"),
  bstack11lll_opy_ (u"ࠬࡧࡣࡤࡧࡳࡸࡎࡴࡳࡦࡥࡸࡶࡪࡉࡥࡳࡶࡶࠫᗗ"): bstack11lll_opy_ (u"࠭ࡡࡤࡥࡨࡴࡹ࡙ࡳ࡭ࡅࡨࡶࡹࡹࠧᗘ"),
  bstack11lll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩᗙ"): bstack11lll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩᗚ"),
  bstack11lll_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩᗛ"): bstack11lll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡶࡳࡺࡸࡣࡦࠩᗜ"),
  bstack11lll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ᗝ"): bstack11lll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ᗞ"),
  bstack11lll_opy_ (u"࠭ࡨࡰࡵࡷࡒࡦࡳࡥࠨᗟ"): bstack11lll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡨࡰࡵࡷࡒࡦࡳࡥࠨᗠ"),
  bstack11lll_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡔ࡫ࡰࠫᗡ"): bstack11lll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡧࡱࡥࡧࡲࡥࡔ࡫ࡰࠫᗢ"),
  bstack11lll_opy_ (u"ࠪࡷ࡮ࡳࡏࡱࡶ࡬ࡳࡳࡹࠧᗣ"): bstack11lll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡷ࡮ࡳࡏࡱࡶ࡬ࡳࡳࡹࠧᗤ"),
  bstack11lll_opy_ (u"ࠬࡻࡰ࡭ࡱࡤࡨࡒ࡫ࡤࡪࡣࠪᗥ"): bstack11lll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡻࡰ࡭ࡱࡤࡨࡒ࡫ࡤࡪࡣࠪᗦ"),
  bstack11lll_opy_ (u"ࠧࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪᗧ"): bstack11lll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪᗨ"),
  bstack11lll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫᗩ"): bstack11lll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫᗪ")
}
bstack11llllll1ll_opy_ = [
  bstack11lll_opy_ (u"ࠫࡴࡹࠧᗫ"),
  bstack11lll_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨᗬ"),
  bstack11lll_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨᗭ"),
  bstack11lll_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬᗮ"),
  bstack11lll_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬᗯ"),
  bstack11lll_opy_ (u"ࠩࡵࡩࡦࡲࡍࡰࡤ࡬ࡰࡪ࠭ᗰ"),
  bstack11lll_opy_ (u"ࠪࡥࡵࡶࡩࡶ࡯࡙ࡩࡷࡹࡩࡰࡰࠪᗱ"),
]
bstack1l11l1l1ll_opy_ = {
  bstack11lll_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ᗲ"): [bstack11lll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡚࡙ࡅࡓࡐࡄࡑࡊ࠭ᗳ"), bstack11lll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡛ࡓࡆࡔࡢࡒࡆࡓࡅࠨᗴ")],
  bstack11lll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪᗵ"): bstack11lll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡅࡆࡉࡘ࡙࡟ࡌࡇ࡜ࠫᗶ"),
  bstack11lll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬᗷ"): bstack11lll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅ࡙ࡎࡒࡄࡠࡐࡄࡑࡊ࠭ᗸ"),
  bstack11lll_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩᗹ"): bstack11lll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡘࡏࡋࡇࡆࡘࡤࡔࡁࡎࡇࠪᗺ"),
  bstack11lll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᗻ"): bstack11lll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡖࡋࡏࡈࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩᗼ"),
  bstack11lll_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨᗽ"): bstack11lll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡄࡖࡆࡒࡌࡆࡎࡖࡣࡕࡋࡒࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࠪᗾ"),
  bstack11lll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧᗿ"): bstack11lll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࠩᘀ"),
  bstack11lll_opy_ (u"ࠬࡸࡥࡳࡷࡱࡘࡪࡹࡴࡴࠩᘁ"): bstack11lll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࡣ࡙ࡋࡓࡕࡕࠪᘂ"),
  bstack11lll_opy_ (u"ࠧࡢࡲࡳࠫᘃ"): [bstack11lll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡒࡓࡣࡎࡊࠧᘄ"), bstack11lll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡓࡔࠬᘅ")],
  bstack11lll_opy_ (u"ࠪࡰࡴ࡭ࡌࡦࡸࡨࡰࠬᘆ"): bstack11lll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡗࡉࡑ࡟ࡍࡑࡊࡐࡊ࡜ࡅࡍࠩᘇ"),
  bstack11lll_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᘈ"): bstack11lll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩᘉ"),
  bstack11lll_opy_ (u"ࠧࡵࡧࡶࡸࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫᘊ"): bstack11lll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡕࡂࡔࡇࡕ࡚ࡆࡈࡉࡍࡋࡗ࡝ࠬᘋ"),
  bstack11lll_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ᘌ"): bstack11lll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗ࡙ࡗࡈࡏࡔࡅࡄࡐࡊ࠭ᘍ")
}
bstack1ll11l1l_opy_ = {
  bstack11lll_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ᘎ"): [bstack11lll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡺࡹࡥࡳࡡࡱࡥࡲ࡫ࠧᘏ"), bstack11lll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡻࡳࡦࡴࡑࡥࡲ࡫ࠧᘐ")],
  bstack11lll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪᘑ"): [bstack11lll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹ࡟࡬ࡧࡼࠫᘒ"), bstack11lll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫᘓ")],
  bstack11lll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ᘔ"): bstack11lll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ᘕ"),
  bstack11lll_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪᘖ"): bstack11lll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪᘗ"),
  bstack11lll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩᘘ"): bstack11lll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩᘙ"),
  bstack11lll_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩᘚ"): [bstack11lll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡳࡴࡵ࠭ᘛ"), bstack11lll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪᘜ")],
  bstack11lll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩᘝ"): bstack11lll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡤࡣ࡯ࠫᘞ"),
  bstack11lll_opy_ (u"ࠧࡳࡧࡵࡹࡳ࡚ࡥࡴࡶࡶࠫᘟ"): bstack11lll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡳࡧࡵࡹࡳ࡚ࡥࡴࡶࡶࠫᘠ"),
  bstack11lll_opy_ (u"ࠩࡤࡴࡵ࠭ᘡ"): bstack11lll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡴࡵ࠭ᘢ"),
  bstack11lll_opy_ (u"ࠫࡱࡵࡧࡍࡧࡹࡩࡱ࠭ᘣ"): bstack11lll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡱࡵࡧࡍࡧࡹࡩࡱ࠭ᘤ"),
  bstack11lll_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᘥ"): bstack11lll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᘦ")
}
bstack1llll1l1l1_opy_ = {
  bstack11lll_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫᘧ"): bstack11lll_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ᘨ"),
  bstack11lll_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬᘩ"): [bstack11lll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡷࡪࡲࡥ࡯࡫ࡸࡱࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ᘪ"), bstack11lll_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᘫ")],
  bstack11lll_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫᘬ"): bstack11lll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᘭ"),
  bstack11lll_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬᘮ"): bstack11lll_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩᘯ"),
  bstack11lll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨᘰ"): [bstack11lll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬᘱ"), bstack11lll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥ࡮ࡢ࡯ࡨࠫᘲ")],
  bstack11lll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᘳ"): bstack11lll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩᘴ"),
  bstack11lll_opy_ (u"ࠨࡴࡨࡥࡱࡓ࡯ࡣ࡫࡯ࡩࠬᘵ"): bstack11lll_opy_ (u"ࠩࡵࡩࡦࡲ࡟࡮ࡱࡥ࡭ࡱ࡫ࠧᘶ"),
  bstack11lll_opy_ (u"ࠪࡥࡵࡶࡩࡶ࡯࡙ࡩࡷࡹࡩࡰࡰࠪᘷ"): [bstack11lll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡵࡶࡩࡶ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠫᘸ"), bstack11lll_opy_ (u"ࠬࡧࡰࡱ࡫ࡸࡱࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ᘹ")],
  bstack11lll_opy_ (u"࠭ࡡࡤࡥࡨࡴࡹࡏ࡮ࡴࡧࡦࡹࡷ࡫ࡃࡦࡴࡷࡷࠬᘺ"): [bstack11lll_opy_ (u"ࠧࡢࡥࡦࡩࡵࡺࡓࡴ࡮ࡆࡩࡷࡺࡳࠨᘻ"), bstack11lll_opy_ (u"ࠨࡣࡦࡧࡪࡶࡴࡔࡵ࡯ࡇࡪࡸࡴࠨᘼ")]
}
bstack1l1ll1lll1_opy_ = [
  bstack11lll_opy_ (u"ࠩࡤࡧࡨ࡫ࡰࡵࡋࡱࡷࡪࡩࡵࡳࡧࡆࡩࡷࡺࡳࠨᘽ"),
  bstack11lll_opy_ (u"ࠪࡴࡦ࡭ࡥࡍࡱࡤࡨࡘࡺࡲࡢࡶࡨ࡫ࡾ࠭ᘾ"),
  bstack11lll_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪᘿ"),
  bstack11lll_opy_ (u"ࠬࡹࡥࡵ࡙࡬ࡲࡩࡵࡷࡓࡧࡦࡸࠬᙀ"),
  bstack11lll_opy_ (u"࠭ࡴࡪ࡯ࡨࡳࡺࡺࡳࠨᙁ"),
  bstack11lll_opy_ (u"ࠧࡴࡶࡵ࡭ࡨࡺࡆࡪ࡮ࡨࡍࡳࡺࡥࡳࡣࡦࡸࡦࡨࡩ࡭࡫ࡷࡽࠬᙂ"),
  bstack11lll_opy_ (u"ࠨࡷࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡔࡷࡵ࡭ࡱࡶࡅࡩ࡭ࡧࡶࡪࡱࡵࠫᙃ"),
  bstack11lll_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧᙄ"),
  bstack11lll_opy_ (u"ࠪࡱࡴࢀ࠺ࡧ࡫ࡵࡩ࡫ࡵࡸࡐࡲࡷ࡭ࡴࡴࡳࠨᙅ"),
  bstack11lll_opy_ (u"ࠫࡲࡹ࠺ࡦࡦࡪࡩࡔࡶࡴࡪࡱࡱࡷࠬᙆ"),
  bstack11lll_opy_ (u"ࠬࡹࡥ࠻࡫ࡨࡓࡵࡺࡩࡰࡰࡶࠫᙇ"),
  bstack11lll_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮࠴࡯ࡱࡶ࡬ࡳࡳࡹࠧᙈ"),
]
bstack1ll11llll_opy_ = [
  bstack11lll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫᙉ"),
  bstack11lll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬᙊ"),
  bstack11lll_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨᙋ"),
  bstack11lll_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪᙌ"),
  bstack11lll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧᙍ"),
  bstack11lll_opy_ (u"ࠬࡲ࡯ࡨࡎࡨࡺࡪࡲࠧᙎ"),
  bstack11lll_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩᙏ"),
  bstack11lll_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫᙐ"),
  bstack11lll_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫᙑ"),
  bstack11lll_opy_ (u"ࠩࡷࡩࡸࡺࡃࡰࡰࡷࡩࡽࡺࡏࡱࡶ࡬ࡳࡳࡹࠧᙒ"),
  bstack11lll_opy_ (u"ࠪࡸࡪࡹࡴࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧᙓ"),
  bstack11lll_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰ࡚ࡦࡸࡩࡢࡤ࡯ࡩࡸ࠭ᙔ"),
  bstack11lll_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱ࡙ࡧࡧࠨᙕ"),
  bstack11lll_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᙖ"),
  bstack11lll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᙗ"),
  bstack11lll_opy_ (u"ࠨࡴࡨࡶࡺࡴࡔࡦࡵࡷࡷࠬᙘ"),
  bstack11lll_opy_ (u"ࠩࡆ࡙ࡘ࡚ࡏࡎࡡࡗࡅࡌࡥ࠱ࠨᙙ"),
  bstack11lll_opy_ (u"ࠪࡇ࡚࡙ࡔࡐࡏࡢࡘࡆࡍ࡟࠳ࠩᙚ"),
  bstack11lll_opy_ (u"ࠫࡈ࡛ࡓࡕࡑࡐࡣ࡙ࡇࡇࡠ࠵ࠪᙛ"),
  bstack11lll_opy_ (u"ࠬࡉࡕࡔࡖࡒࡑࡤ࡚ࡁࡈࡡ࠷ࠫᙜ"),
  bstack11lll_opy_ (u"࠭ࡃࡖࡕࡗࡓࡒࡥࡔࡂࡉࡢ࠹ࠬᙝ"),
  bstack11lll_opy_ (u"ࠧࡄࡗࡖࡘࡔࡓ࡟ࡕࡃࡊࡣ࠻࠭ᙞ"),
  bstack11lll_opy_ (u"ࠨࡅࡘࡗ࡙ࡕࡍࡠࡖࡄࡋࡤ࠽ࠧᙟ"),
  bstack11lll_opy_ (u"ࠩࡆ࡙ࡘ࡚ࡏࡎࡡࡗࡅࡌࡥ࠸ࠨᙠ"),
  bstack11lll_opy_ (u"ࠪࡇ࡚࡙ࡔࡐࡏࡢࡘࡆࡍ࡟࠺ࠩᙡ"),
  bstack11lll_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪᙢ"),
  bstack11lll_opy_ (u"ࠬࡶࡥࡳࡥࡼࡓࡵࡺࡩࡰࡰࡶࠫᙣ"),
  bstack11lll_opy_ (u"࠭ࡰࡦࡴࡦࡽࡈࡧࡰࡵࡷࡵࡩࡒࡵࡤࡦࠩᙤ"),
  bstack11lll_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡂࡷࡷࡳࡈࡧࡰࡵࡷࡵࡩࡑࡵࡧࡴࠩᙥ"),
  bstack11lll_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬᙦ"),
  bstack11lll_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ᙧ")
]
bstack1l11111lll1_opy_ = [
  bstack11lll_opy_ (u"ࠪࡹࡵࡲ࡯ࡢࡦࡐࡩࡩ࡯ࡡࠨᙨ"),
  bstack11lll_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ᙩ"),
  bstack11lll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨᙪ"),
  bstack11lll_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫᙫ"),
  bstack11lll_opy_ (u"ࠧࡵࡧࡶࡸࡕࡸࡩࡰࡴ࡬ࡸࡾ࠭ᙬ"),
  bstack11lll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ᙭"),
  bstack11lll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡕࡣࡪࠫ᙮"),
  bstack11lll_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨᙯ"),
  bstack11lll_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᙰ"),
  bstack11lll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪᙱ"),
  bstack11lll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᙲ"),
  bstack11lll_opy_ (u"ࠧ࡭ࡱࡦࡥࡱ࠭ᙳ"),
  bstack11lll_opy_ (u"ࠨࡱࡶࠫᙴ"),
  bstack11lll_opy_ (u"ࠩࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬᙵ"),
  bstack11lll_opy_ (u"ࠪ࡬ࡴࡹࡴࡴࠩᙶ"),
  bstack11lll_opy_ (u"ࠫࡦࡻࡴࡰ࡙ࡤ࡭ࡹ࠭ᙷ"),
  bstack11lll_opy_ (u"ࠬࡸࡥࡨ࡫ࡲࡲࠬᙸ"),
  bstack11lll_opy_ (u"࠭ࡴࡪ࡯ࡨࡾࡴࡴࡥࠨᙹ"),
  bstack11lll_opy_ (u"ࠧ࡮ࡣࡦ࡬࡮ࡴࡥࠨᙺ"),
  bstack11lll_opy_ (u"ࠨࡴࡨࡷࡴࡲࡵࡵ࡫ࡲࡲࠬᙻ"),
  bstack11lll_opy_ (u"ࠩ࡬ࡨࡱ࡫ࡔࡪ࡯ࡨࡳࡺࡺࠧᙼ"),
  bstack11lll_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡒࡶ࡮࡫࡮ࡵࡣࡷ࡭ࡴࡴࠧᙽ"),
  bstack11lll_opy_ (u"ࠫࡻ࡯ࡤࡦࡱࠪᙾ"),
  bstack11lll_opy_ (u"ࠬࡴ࡯ࡑࡣࡪࡩࡑࡵࡡࡥࡖ࡬ࡱࡪࡵࡵࡵࠩᙿ"),
  bstack11lll_opy_ (u"࠭ࡢࡧࡥࡤࡧ࡭࡫ࠧ "),
  bstack11lll_opy_ (u"ࠧࡥࡧࡥࡹ࡬࠭ᚁ"),
  bstack11lll_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡔࡥࡵࡩࡪࡴࡳࡩࡱࡷࡷࠬᚂ"),
  bstack11lll_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡕࡨࡲࡩࡑࡥࡺࡵࠪᚃ"),
  bstack11lll_opy_ (u"ࠪࡶࡪࡧ࡬ࡎࡱࡥ࡭ࡱ࡫ࠧᚄ"),
  bstack11lll_opy_ (u"ࠫࡳࡵࡐࡪࡲࡨࡰ࡮ࡴࡥࠨᚅ"),
  bstack11lll_opy_ (u"ࠬࡩࡨࡦࡥ࡮࡙ࡗࡒࠧᚆ"),
  bstack11lll_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᚇ"),
  bstack11lll_opy_ (u"ࠧࡢࡥࡦࡩࡵࡺࡃࡰࡱ࡮࡭ࡪࡹࠧᚈ"),
  bstack11lll_opy_ (u"ࠨࡥࡤࡴࡹࡻࡲࡦࡅࡵࡥࡸ࡮ࠧᚉ"),
  bstack11lll_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭ᚊ"),
  bstack11lll_opy_ (u"ࠪࡥࡵࡶࡩࡶ࡯࡙ࡩࡷࡹࡩࡰࡰࠪᚋ"),
  bstack11lll_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡗࡧࡵࡷ࡮ࡵ࡮ࠨᚌ"),
  bstack11lll_opy_ (u"ࠬࡴ࡯ࡃ࡮ࡤࡲࡰࡖ࡯࡭࡮࡬ࡲ࡬࠭ᚍ"),
  bstack11lll_opy_ (u"࠭࡭ࡢࡵ࡮ࡗࡪࡴࡤࡌࡧࡼࡷࠬᚎ"),
  bstack11lll_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡌࡰࡩࡶࠫᚏ"),
  bstack11lll_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡊࡦࠪᚐ"),
  bstack11lll_opy_ (u"ࠩࡧࡩࡩ࡯ࡣࡢࡶࡨࡨࡉ࡫ࡶࡪࡥࡨࠫᚑ"),
  bstack11lll_opy_ (u"ࠪ࡬ࡪࡧࡤࡦࡴࡓࡥࡷࡧ࡭ࡴࠩᚒ"),
  bstack11lll_opy_ (u"ࠫࡵ࡮࡯࡯ࡧࡑࡹࡲࡨࡥࡳࠩᚓ"),
  bstack11lll_opy_ (u"ࠬࡴࡥࡵࡹࡲࡶࡰࡒ࡯ࡨࡵࠪᚔ"),
  bstack11lll_opy_ (u"࠭࡮ࡦࡶࡺࡳࡷࡱࡌࡰࡩࡶࡓࡵࡺࡩࡰࡰࡶࠫᚕ"),
  bstack11lll_opy_ (u"ࠧࡤࡱࡱࡷࡴࡲࡥࡍࡱࡪࡷࠬᚖ"),
  bstack11lll_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨᚗ"),
  bstack11lll_opy_ (u"ࠩࡤࡴࡵ࡯ࡵ࡮ࡎࡲ࡫ࡸ࠭ᚘ"),
  bstack11lll_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡅ࡭ࡴࡳࡥࡵࡴ࡬ࡧࠬᚙ"),
  bstack11lll_opy_ (u"ࠫࡻ࡯ࡤࡦࡱ࡙࠶ࠬᚚ"),
  bstack11lll_opy_ (u"ࠬࡳࡩࡥࡕࡨࡷࡸ࡯࡯࡯ࡋࡱࡷࡹࡧ࡬࡭ࡃࡳࡴࡸ࠭᚛"),
  bstack11lll_opy_ (u"࠭ࡥࡴࡲࡵࡩࡸࡹ࡯ࡔࡧࡵࡺࡪࡸࠧ᚜"),
  bstack11lll_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡎࡲ࡫ࡸ࠭᚝"),
  bstack11lll_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯ࡆࡨࡵ࠭᚞"),
  bstack11lll_opy_ (u"ࠩࡷࡩࡱ࡫࡭ࡦࡶࡵࡽࡑࡵࡧࡴࠩ᚟"),
  bstack11lll_opy_ (u"ࠪࡷࡾࡴࡣࡕ࡫ࡰࡩ࡜࡯ࡴࡩࡐࡗࡔࠬᚠ"),
  bstack11lll_opy_ (u"ࠫ࡬࡫࡯ࡍࡱࡦࡥࡹ࡯࡯࡯ࠩᚡ"),
  bstack11lll_opy_ (u"ࠬ࡭ࡰࡴࡎࡲࡧࡦࡺࡩࡰࡰࠪᚢ"),
  bstack11lll_opy_ (u"࠭࡮ࡦࡶࡺࡳࡷࡱࡐࡳࡱࡩ࡭ࡱ࡫ࠧᚣ"),
  bstack11lll_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡎࡦࡶࡺࡳࡷࡱࠧᚤ"),
  bstack11lll_opy_ (u"ࠨࡨࡲࡶࡨ࡫ࡃࡩࡣࡱ࡫ࡪࡐࡡࡳࠩᚥ"),
  bstack11lll_opy_ (u"ࠩࡻࡱࡸࡐࡡࡳࠩᚦ"),
  bstack11lll_opy_ (u"ࠪࡼࡲࡾࡊࡢࡴࠪᚧ"),
  bstack11lll_opy_ (u"ࠫࡲࡧࡳ࡬ࡅࡲࡱࡲࡧ࡮ࡥࡵࠪᚨ"),
  bstack11lll_opy_ (u"ࠬࡳࡡࡴ࡭ࡅࡥࡸ࡯ࡣࡂࡷࡷ࡬ࠬᚩ"),
  bstack11lll_opy_ (u"࠭ࡷࡴࡎࡲࡧࡦࡲࡓࡶࡲࡳࡳࡷࡺࠧᚪ"),
  bstack11lll_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡄࡱࡵࡷࡗ࡫ࡳࡵࡴ࡬ࡧࡹ࡯࡯࡯ࡵࠪᚫ"),
  bstack11lll_opy_ (u"ࠨࡣࡳࡴ࡛࡫ࡲࡴ࡫ࡲࡲࠬᚬ"),
  bstack11lll_opy_ (u"ࠩࡤࡧࡨ࡫ࡰࡵࡋࡱࡷࡪࡩࡵࡳࡧࡆࡩࡷࡺࡳࠨᚭ"),
  bstack11lll_opy_ (u"ࠪࡶࡪࡹࡩࡨࡰࡄࡴࡵ࠭ᚮ"),
  bstack11lll_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩࡆࡴࡩ࡮ࡣࡷ࡭ࡴࡴࡳࠨᚯ"),
  bstack11lll_opy_ (u"ࠬࡩࡡ࡯ࡣࡵࡽࠬᚰ"),
  bstack11lll_opy_ (u"࠭ࡦࡪࡴࡨࡪࡴࡾࠧᚱ"),
  bstack11lll_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧᚲ"),
  bstack11lll_opy_ (u"ࠨ࡫ࡨࠫᚳ"),
  bstack11lll_opy_ (u"ࠩࡨࡨ࡬࡫ࠧᚴ"),
  bstack11lll_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࠪᚵ"),
  bstack11lll_opy_ (u"ࠫࡶࡻࡥࡶࡧࠪᚶ"),
  bstack11lll_opy_ (u"ࠬ࡯࡮ࡵࡧࡵࡲࡦࡲࠧᚷ"),
  bstack11lll_opy_ (u"࠭ࡡࡱࡲࡖࡸࡴࡸࡥࡄࡱࡱࡪ࡮࡭ࡵࡳࡣࡷ࡭ࡴࡴࠧᚸ"),
  bstack11lll_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡃࡢ࡯ࡨࡶࡦࡏ࡭ࡢࡩࡨࡍࡳࡰࡥࡤࡶ࡬ࡳࡳ࠭ᚹ"),
  bstack11lll_opy_ (u"ࠨࡰࡨࡸࡼࡵࡲ࡬ࡎࡲ࡫ࡸࡋࡸࡤ࡮ࡸࡨࡪࡎ࡯ࡴࡶࡶࠫᚺ"),
  bstack11lll_opy_ (u"ࠩࡱࡩࡹࡽ࡯ࡳ࡭ࡏࡳ࡬ࡹࡉ࡯ࡥ࡯ࡹࡩ࡫ࡈࡰࡵࡷࡷࠬᚻ"),
  bstack11lll_opy_ (u"ࠪࡹࡵࡪࡡࡵࡧࡄࡴࡵ࡙ࡥࡵࡶ࡬ࡲ࡬ࡹࠧᚼ"),
  bstack11lll_opy_ (u"ࠫࡷ࡫ࡳࡦࡴࡹࡩࡉ࡫ࡶࡪࡥࡨࠫᚽ"),
  bstack11lll_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬᚾ"),
  bstack11lll_opy_ (u"࠭ࡳࡦࡰࡧࡏࡪࡿࡳࠨᚿ"),
  bstack11lll_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡐࡢࡵࡶࡧࡴࡪࡥࠨᛀ"),
  bstack11lll_opy_ (u"ࠨࡷࡳࡨࡦࡺࡥࡊࡱࡶࡈࡪࡼࡩࡤࡧࡖࡩࡹࡺࡩ࡯ࡩࡶࠫᛁ"),
  bstack11lll_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡃࡸࡨ࡮ࡵࡉ࡯࡬ࡨࡧࡹ࡯࡯࡯ࠩᛂ"),
  bstack11lll_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡄࡴࡵࡲࡥࡑࡣࡼࠫᛃ"),
  bstack11lll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬᛄ"),
  bstack11lll_opy_ (u"ࠬࡽࡤࡪࡱࡖࡩࡷࡼࡩࡤࡧࠪᛅ"),
  bstack11lll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨᛆ"),
  bstack11lll_opy_ (u"ࠧࡱࡴࡨࡺࡪࡴࡴࡄࡴࡲࡷࡸ࡙ࡩࡵࡧࡗࡶࡦࡩ࡫ࡪࡰࡪࠫᛇ"),
  bstack11lll_opy_ (u"ࠨࡪ࡬࡫࡭ࡉ࡯࡯ࡶࡵࡥࡸࡺࠧᛈ"),
  bstack11lll_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡒࡵࡩ࡫࡫ࡲࡦࡰࡦࡩࡸ࠭ᛉ"),
  bstack11lll_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡖ࡭ࡲ࠭ᛊ"),
  bstack11lll_opy_ (u"ࠫࡸ࡯࡭ࡐࡲࡷ࡭ࡴࡴࡳࠨᛋ"),
  bstack11lll_opy_ (u"ࠬࡸࡥ࡮ࡱࡹࡩࡎࡕࡓࡂࡲࡳࡗࡪࡺࡴࡪࡰࡪࡷࡑࡵࡣࡢ࡮࡬ࡾࡦࡺࡩࡰࡰࠪᛌ"),
  bstack11lll_opy_ (u"࠭ࡨࡰࡵࡷࡒࡦࡳࡥࠨᛍ"),
  bstack11lll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩᛎ"),
  bstack11lll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪᛏ"),
  bstack11lll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠨᛐ"),
  bstack11lll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬᛑ"),
  bstack11lll_opy_ (u"ࠫࡵࡧࡧࡦࡎࡲࡥࡩ࡙ࡴࡳࡣࡷࡩ࡬ࡿࠧᛒ"),
  bstack11lll_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫᛓ"),
  bstack11lll_opy_ (u"࠭ࡴࡪ࡯ࡨࡳࡺࡺࡳࠨᛔ"),
  bstack11lll_opy_ (u"ࠧࡶࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡓࡶࡴࡳࡰࡵࡄࡨ࡬ࡦࡼࡩࡰࡴࠪᛕ")
]
bstack1lllll1lll_opy_ = {
  bstack11lll_opy_ (u"ࠨࡸࠪᛖ"): bstack11lll_opy_ (u"ࠩࡹࠫᛗ"),
  bstack11lll_opy_ (u"ࠪࡪࠬᛘ"): bstack11lll_opy_ (u"ࠫ࡫࠭ᛙ"),
  bstack11lll_opy_ (u"ࠬ࡬࡯ࡳࡥࡨࠫᛚ"): bstack11lll_opy_ (u"࠭ࡦࡰࡴࡦࡩࠬᛛ"),
  bstack11lll_opy_ (u"ࠧࡰࡰ࡯ࡽࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ᛜ"): bstack11lll_opy_ (u"ࠨࡱࡱࡰࡾࡇࡵࡵࡱࡰࡥࡹ࡫ࠧᛝ"),
  bstack11lll_opy_ (u"ࠩࡩࡳࡷࡩࡥ࡭ࡱࡦࡥࡱ࠭ᛞ"): bstack11lll_opy_ (u"ࠪࡪࡴࡸࡣࡦ࡮ࡲࡧࡦࡲࠧᛟ"),
  bstack11lll_opy_ (u"ࠫࡵࡸ࡯ࡹࡻ࡫ࡳࡸࡺࠧᛠ"): bstack11lll_opy_ (u"ࠬࡶࡲࡰࡺࡼࡌࡴࡹࡴࠨᛡ"),
  bstack11lll_opy_ (u"࠭ࡰࡳࡱࡻࡽࡵࡵࡲࡵࠩᛢ"): bstack11lll_opy_ (u"ࠧࡱࡴࡲࡼࡾࡖ࡯ࡳࡶࠪᛣ"),
  bstack11lll_opy_ (u"ࠨࡲࡵࡳࡽࡿࡵࡴࡧࡵࠫᛤ"): bstack11lll_opy_ (u"ࠩࡳࡶࡴࡾࡹࡖࡵࡨࡶࠬᛥ"),
  bstack11lll_opy_ (u"ࠪࡴࡷࡵࡸࡺࡲࡤࡷࡸ࠭ᛦ"): bstack11lll_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡥࡸࡹࠧᛧ"),
  bstack11lll_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡴࡷࡵࡸࡺࡪࡲࡷࡹ࠭ᛨ"): bstack11lll_opy_ (u"࠭࡬ࡰࡥࡤࡰࡕࡸ࡯ࡹࡻࡋࡳࡸࡺࠧᛩ"),
  bstack11lll_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡶࡲࡰࡺࡼࡴࡴࡸࡴࠨᛪ"): bstack11lll_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡐࡳࡱࡻࡽࡕࡵࡲࡵࠩ᛫"),
  bstack11lll_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡱࡴࡲࡼࡾࡻࡳࡦࡴࠪ᛬"): bstack11lll_opy_ (u"ࠪ࠱ࡱࡵࡣࡢ࡮ࡓࡶࡴࡾࡹࡖࡵࡨࡶࠬ᛭"),
  bstack11lll_opy_ (u"ࠫ࠲ࡲ࡯ࡤࡣ࡯ࡴࡷࡵࡸࡺࡷࡶࡩࡷ࠭ᛮ"): bstack11lll_opy_ (u"ࠬ࠳࡬ࡰࡥࡤࡰࡕࡸ࡯ࡹࡻࡘࡷࡪࡸࠧᛯ"),
  bstack11lll_opy_ (u"࠭࡬ࡰࡥࡤࡰࡵࡸ࡯ࡹࡻࡳࡥࡸࡹࠧᛰ"): bstack11lll_opy_ (u"ࠧ࠮࡮ࡲࡧࡦࡲࡐࡳࡱࡻࡽࡕࡧࡳࡴࠩᛱ"),
  bstack11lll_opy_ (u"ࠨ࠯࡯ࡳࡨࡧ࡬ࡱࡴࡲࡼࡾࡶࡡࡴࡵࠪᛲ"): bstack11lll_opy_ (u"ࠩ࠰ࡰࡴࡩࡡ࡭ࡒࡵࡳࡽࡿࡐࡢࡵࡶࠫᛳ"),
  bstack11lll_opy_ (u"ࠪࡦ࡮ࡴࡡࡳࡻࡳࡥࡹ࡮ࠧᛴ"): bstack11lll_opy_ (u"ࠫࡧ࡯࡮ࡢࡴࡼࡴࡦࡺࡨࠨᛵ"),
  bstack11lll_opy_ (u"ࠬࡶࡡࡤࡨ࡬ࡰࡪ࠭ᛶ"): bstack11lll_opy_ (u"࠭࠭ࡱࡣࡦ࠱࡫࡯࡬ࡦࠩᛷ"),
  bstack11lll_opy_ (u"ࠧࡱࡣࡦ࠱࡫࡯࡬ࡦࠩᛸ"): bstack11lll_opy_ (u"ࠨ࠯ࡳࡥࡨ࠳ࡦࡪ࡮ࡨࠫ᛹"),
  bstack11lll_opy_ (u"ࠩ࠰ࡴࡦࡩ࠭ࡧ࡫࡯ࡩࠬ᛺"): bstack11lll_opy_ (u"ࠪ࠱ࡵࡧࡣ࠮ࡨ࡬ࡰࡪ࠭᛻"),
  bstack11lll_opy_ (u"ࠫࡱࡵࡧࡧ࡫࡯ࡩࠬ᛼"): bstack11lll_opy_ (u"ࠬࡲ࡯ࡨࡨ࡬ࡰࡪ࠭᛽"),
  bstack11lll_opy_ (u"࠭࡬ࡰࡥࡤࡰ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ᛾"): bstack11lll_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ᛿"),
  bstack11lll_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭࠮ࡴࡨࡴࡪࡧࡴࡦࡴࠪᜀ"): bstack11lll_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡔࡨࡴࡪࡧࡴࡦࡴࠪᜁ")
}
bstack1l1111111ll_opy_ = bstack11lll_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳࡬࡯ࡴࡩࡷࡥ࠲ࡨࡵ࡭࠰ࡲࡨࡶࡨࡿ࠯ࡤ࡮࡬࠳ࡷ࡫࡬ࡦࡣࡶࡩࡸ࠵࡬ࡢࡶࡨࡷࡹ࠵ࡤࡰࡹࡱࡰࡴࡧࡤࠣᜂ")
bstack1l1111l11l1_opy_ = bstack11lll_opy_ (u"ࠦ࠴ࡶࡥࡳࡥࡼ࠳࡭࡫ࡡ࡭ࡶ࡫ࡧ࡭࡫ࡣ࡬ࠤᜃ")
bstack11lll1l1l1_opy_ = bstack11lll_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡥࡥࡵ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡳࡦࡰࡧࡣࡸࡪ࡫ࡠࡧࡹࡩࡳࡺࡳࠣᜄ")
bstack11l11lll_opy_ = bstack11lll_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡩࡷࡥ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡸࡦ࠲࡬ࡺࡨࠧᜅ")
bstack11llllll1_opy_ = bstack11lll_opy_ (u"ࠧࡩࡶࡷࡴ࠿࠵࠯ࡩࡷࡥ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠺࠹࠲࠲ࡻࡩ࠵ࡨࡶࡤࠪᜆ")
bstack1ll1llllll_opy_ = bstack11lll_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱࡫ࡹࡧ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡱࡩࡽࡺ࡟ࡩࡷࡥࡷࠬᜇ")
bstack11llllllll1_opy_ = {
  bstack11lll_opy_ (u"ࠩࡦࡶ࡮ࡺࡩࡤࡣ࡯ࠫᜈ"): 50,
  bstack11lll_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩᜉ"): 40,
  bstack11lll_opy_ (u"ࠫࡼࡧࡲ࡯࡫ࡱ࡫ࠬᜊ"): 30,
  bstack11lll_opy_ (u"ࠬ࡯࡮ࡧࡱࠪᜋ"): 20,
  bstack11lll_opy_ (u"࠭ࡤࡦࡤࡸ࡫ࠬᜌ"): 10
}
bstack1lll1ll1l_opy_ = bstack11llllllll1_opy_[bstack11lll_opy_ (u"ࠧࡪࡰࡩࡳࠬᜍ")]
bstack1ll1l1111_opy_ = bstack11lll_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮࠮ࡲࡼࡸ࡭ࡵ࡮ࡢࡩࡨࡲࡹ࠵ࠧᜎ")
bstack1111llll1_opy_ = bstack11lll_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮ࡲࡼࡸ࡭ࡵ࡮ࡢࡩࡨࡲࡹ࠵ࠧᜏ")
bstack1111l1l1_opy_ = bstack11lll_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧ࠰ࡴࡾࡺࡨࡰࡰࡤ࡫ࡪࡴࡴ࠰ࠩᜐ")
bstack1l111l111_opy_ = bstack11lll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷ࠱ࡵࡿࡴࡩࡱࡱࡥ࡬࡫࡮ࡵ࠱ࠪᜑ")
bstack1l111l1lll_opy_ = bstack11lll_opy_ (u"ࠬࡖ࡬ࡦࡣࡶࡩࠥ࡯࡮ࡴࡶࡤࡰࡱࠦࡰࡺࡶࡨࡷࡹࠦࡡ࡯ࡦࠣࡴࡾࡺࡥࡴࡶ࠰ࡷࡪࡲࡥ࡯࡫ࡸࡱࠥࡶࡡࡤ࡭ࡤ࡫ࡪࡹ࠮ࠡࡢࡳ࡭ࡵࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡱࡻࡷࡩࡸࡺࠠࡱࡻࡷࡩࡸࡺ࠭ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡢࠪᜒ")
bstack1l1111ll111_opy_ = [bstack11lll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡛ࡓࡆࡔࡑࡅࡒࡋࠧᜓ"), bstack11lll_opy_ (u"࡚ࠧࡑࡘࡖࡤ࡛ࡓࡆࡔࡑࡅࡒࡋ᜔ࠧ")]
bstack1l1111l1111_opy_ = [bstack11lll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡅࡆࡉࡘ࡙࡟ࡌࡇ࡜᜕ࠫ"), bstack11lll_opy_ (u"ࠩ࡜ࡓ࡚ࡘ࡟ࡂࡅࡆࡉࡘ࡙࡟ࡌࡇ࡜ࠫ᜖")]
bstack1l1l1l1ll1_opy_ = re.compile(bstack11lll_opy_ (u"ࠪࡢࡠࡢ࡜ࡸ࠯ࡠ࠯࠿࠴ࠪࠥࠩ᜗"))
bstack1llllll11l_opy_ = [
  bstack11lll_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡏࡣࡰࡩࠬ᜘"),
  bstack11lll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧ᜙"),
  bstack11lll_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪ᜚"),
  bstack11lll_opy_ (u"ࠧ࡯ࡧࡺࡇࡴࡳ࡭ࡢࡰࡧࡘ࡮ࡳࡥࡰࡷࡷࠫ᜛"),
  bstack11lll_opy_ (u"ࠨࡣࡳࡴࠬ᜜"),
  bstack11lll_opy_ (u"ࠩࡸࡨ࡮ࡪࠧ᜝"),
  bstack11lll_opy_ (u"ࠪࡰࡦࡴࡧࡶࡣࡪࡩࠬ᜞"),
  bstack11lll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡨࠫᜟ"),
  bstack11lll_opy_ (u"ࠬࡵࡲࡪࡧࡱࡸࡦࡺࡩࡰࡰࠪᜠ"),
  bstack11lll_opy_ (u"࠭ࡡࡶࡶࡲ࡛ࡪࡨࡶࡪࡧࡺࠫᜡ"),
  bstack11lll_opy_ (u"ࠧ࡯ࡱࡕࡩࡸ࡫ࡴࠨᜢ"), bstack11lll_opy_ (u"ࠨࡨࡸࡰࡱࡘࡥࡴࡧࡷࠫᜣ"),
  bstack11lll_opy_ (u"ࠩࡦࡰࡪࡧࡲࡔࡻࡶࡸࡪࡳࡆࡪ࡮ࡨࡷࠬᜤ"),
  bstack11lll_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡖ࡬ࡱ࡮ࡴࡧࡴࠩᜥ"),
  bstack11lll_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡔࡪࡸࡦࡰࡴࡰࡥࡳࡩࡥࡍࡱࡪ࡫࡮ࡴࡧࠨᜦ"),
  bstack11lll_opy_ (u"ࠬࡵࡴࡩࡧࡵࡅࡵࡶࡳࠨᜧ"),
  bstack11lll_opy_ (u"࠭ࡰࡳ࡫ࡱࡸࡕࡧࡧࡦࡕࡲࡹࡷࡩࡥࡐࡰࡉ࡭ࡳࡪࡆࡢ࡫࡯ࡹࡷ࡫ࠧᜨ"),
  bstack11lll_opy_ (u"ࠧࡢࡲࡳࡅࡨࡺࡩࡷ࡫ࡷࡽࠬᜩ"), bstack11lll_opy_ (u"ࠨࡣࡳࡴࡕࡧࡣ࡬ࡣࡪࡩࠬᜪ"), bstack11lll_opy_ (u"ࠩࡤࡴࡵ࡝ࡡࡪࡶࡄࡧࡹ࡯ࡶࡪࡶࡼࠫᜫ"), bstack11lll_opy_ (u"ࠪࡥࡵࡶࡗࡢ࡫ࡷࡔࡦࡩ࡫ࡢࡩࡨࠫᜬ"), bstack11lll_opy_ (u"ࠫࡦࡶࡰࡘࡣ࡬ࡸࡉࡻࡲࡢࡶ࡬ࡳࡳ࠭ᜭ"),
  bstack11lll_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡗ࡫ࡡࡥࡻࡗ࡭ࡲ࡫࡯ࡶࡶࠪᜮ"),
  bstack11lll_opy_ (u"࠭ࡡ࡭࡮ࡲࡻ࡙࡫ࡳࡵࡒࡤࡧࡰࡧࡧࡦࡵࠪᜯ"),
  bstack11lll_opy_ (u"ࠧࡢࡰࡧࡶࡴ࡯ࡤࡄࡱࡹࡩࡷࡧࡧࡦࠩᜰ"), bstack11lll_opy_ (u"ࠨࡣࡱࡨࡷࡵࡩࡥࡅࡲࡺࡪࡸࡡࡨࡧࡈࡲࡩࡏ࡮ࡵࡧࡱࡸࠬᜱ"),
  bstack11lll_opy_ (u"ࠩࡤࡲࡩࡸ࡯ࡪࡦࡇࡩࡻ࡯ࡣࡦࡔࡨࡥࡩࡿࡔࡪ࡯ࡨࡳࡺࡺࠧᜲ"),
  bstack11lll_opy_ (u"ࠪࡥࡩࡨࡐࡰࡴࡷࠫᜳ"),
  bstack11lll_opy_ (u"ࠫࡦࡴࡤࡳࡱ࡬ࡨࡉ࡫ࡶࡪࡥࡨࡗࡴࡩ࡫ࡦࡶ᜴ࠪ"),
  bstack11lll_opy_ (u"ࠬࡧ࡮ࡥࡴࡲ࡭ࡩࡏ࡮ࡴࡶࡤࡰࡱ࡚ࡩ࡮ࡧࡲࡹࡹ࠭᜵"),
  bstack11lll_opy_ (u"࠭ࡡ࡯ࡦࡵࡳ࡮ࡪࡉ࡯ࡵࡷࡥࡱࡲࡐࡢࡶ࡫ࠫ᜶"),
  bstack11lll_opy_ (u"ࠧࡢࡸࡧࠫ᜷"), bstack11lll_opy_ (u"ࠨࡣࡹࡨࡑࡧࡵ࡯ࡥ࡫ࡘ࡮ࡳࡥࡰࡷࡷࠫ᜸"), bstack11lll_opy_ (u"ࠩࡤࡺࡩࡘࡥࡢࡦࡼࡘ࡮ࡳࡥࡰࡷࡷࠫ᜹"), bstack11lll_opy_ (u"ࠪࡥࡻࡪࡁࡳࡩࡶࠫ᜺"),
  bstack11lll_opy_ (u"ࠫࡺࡹࡥࡌࡧࡼࡷࡹࡵࡲࡦࠩ᜻"), bstack11lll_opy_ (u"ࠬࡱࡥࡺࡵࡷࡳࡷ࡫ࡐࡢࡶ࡫ࠫ᜼"), bstack11lll_opy_ (u"࠭࡫ࡦࡻࡶࡸࡴࡸࡥࡑࡣࡶࡷࡼࡵࡲࡥࠩ᜽"),
  bstack11lll_opy_ (u"ࠧ࡬ࡧࡼࡅࡱ࡯ࡡࡴࠩ᜾"), bstack11lll_opy_ (u"ࠨ࡭ࡨࡽࡕࡧࡳࡴࡹࡲࡶࡩ࠭᜿"),
  bstack11lll_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡦࡵ࡭ࡻ࡫ࡲࡆࡺࡨࡧࡺࡺࡡࡣ࡮ࡨࠫᝀ"), bstack11lll_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡧࡶ࡮ࡼࡥࡳࡃࡵ࡫ࡸ࠭ᝁ"), bstack11lll_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡨࡷ࡯ࡶࡦࡴࡈࡼࡪࡩࡵࡵࡣࡥࡰࡪࡊࡩࡳࠩᝂ"), bstack11lll_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡩࡸࡩࡷࡧࡵࡇ࡭ࡸ࡯࡮ࡧࡐࡥࡵࡶࡩ࡯ࡩࡉ࡭ࡱ࡫ࠧᝃ"), bstack11lll_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪࡪࡲࡪࡸࡨࡶ࡚ࡹࡥࡔࡻࡶࡸࡪࡳࡅࡹࡧࡦࡹࡹࡧࡢ࡭ࡧࠪᝄ"),
  bstack11lll_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࡤࡳ࡫ࡹࡩࡷࡖ࡯ࡳࡶࠪᝅ"), bstack11lll_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࡥࡴ࡬ࡺࡪࡸࡐࡰࡴࡷࡷࠬᝆ"),
  bstack11lll_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡦࡵ࡭ࡻ࡫ࡲࡅ࡫ࡶࡥࡧࡲࡥࡃࡷ࡬ࡰࡩࡉࡨࡦࡥ࡮ࠫᝇ"),
  bstack11lll_opy_ (u"ࠪࡥࡺࡺ࡯ࡘࡧࡥࡺ࡮࡫ࡷࡕ࡫ࡰࡩࡴࡻࡴࠨᝈ"),
  bstack11lll_opy_ (u"ࠫ࡮ࡴࡴࡦࡰࡷࡅࡨࡺࡩࡰࡰࠪᝉ"), bstack11lll_opy_ (u"ࠬ࡯࡮ࡵࡧࡱࡸࡈࡧࡴࡦࡩࡲࡶࡾ࠭ᝊ"), bstack11lll_opy_ (u"࠭ࡩ࡯ࡶࡨࡲࡹࡌ࡬ࡢࡩࡶࠫᝋ"), bstack11lll_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡡ࡭ࡋࡱࡸࡪࡴࡴࡂࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᝌ"),
  bstack11lll_opy_ (u"ࠨࡦࡲࡲࡹ࡙ࡴࡰࡲࡄࡴࡵࡕ࡮ࡓࡧࡶࡩࡹ࠭ᝍ"),
  bstack11lll_opy_ (u"ࠩࡸࡲ࡮ࡩ࡯ࡥࡧࡎࡩࡾࡨ࡯ࡢࡴࡧࠫᝎ"), bstack11lll_opy_ (u"ࠪࡶࡪࡹࡥࡵࡍࡨࡽࡧࡵࡡࡳࡦࠪᝏ"),
  bstack11lll_opy_ (u"ࠫࡳࡵࡓࡪࡩࡱࠫᝐ"),
  bstack11lll_opy_ (u"ࠬ࡯ࡧ࡯ࡱࡵࡩ࡚ࡴࡩ࡮ࡲࡲࡶࡹࡧ࡮ࡵࡘ࡬ࡩࡼࡹࠧᝑ"),
  bstack11lll_opy_ (u"࠭ࡤࡪࡵࡤࡦࡱ࡫ࡁ࡯ࡦࡵࡳ࡮ࡪࡗࡢࡶࡦ࡬ࡪࡸࡳࠨᝒ"),
  bstack11lll_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧᝓ"),
  bstack11lll_opy_ (u"ࠨࡴࡨࡧࡷ࡫ࡡࡵࡧࡆ࡬ࡷࡵ࡭ࡦࡆࡵ࡭ࡻ࡫ࡲࡔࡧࡶࡷ࡮ࡵ࡮ࡴࠩ᝔"),
  bstack11lll_opy_ (u"ࠩࡱࡥࡹ࡯ࡶࡦ࡙ࡨࡦࡘࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠨ᝕"),
  bstack11lll_opy_ (u"ࠪࡥࡳࡪࡲࡰ࡫ࡧࡗࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡐࡢࡶ࡫ࠫ᝖"),
  bstack11lll_opy_ (u"ࠫࡳ࡫ࡴࡸࡱࡵ࡯ࡘࡶࡥࡦࡦࠪ᝗"),
  bstack11lll_opy_ (u"ࠬ࡭ࡰࡴࡇࡱࡥࡧࡲࡥࡥࠩ᝘"),
  bstack11lll_opy_ (u"࠭ࡩࡴࡊࡨࡥࡩࡲࡥࡴࡵࠪ᝙"),
  bstack11lll_opy_ (u"ࠧࡢࡦࡥࡉࡽ࡫ࡣࡕ࡫ࡰࡩࡴࡻࡴࠨ᝚"),
  bstack11lll_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡥࡔࡥࡵ࡭ࡵࡺࠧ᝛"),
  bstack11lll_opy_ (u"ࠩࡶ࡯࡮ࡶࡄࡦࡸ࡬ࡧࡪࡏ࡮ࡪࡶ࡬ࡥࡱ࡯ࡺࡢࡶ࡬ࡳࡳ࠭᝜"),
  bstack11lll_opy_ (u"ࠪࡥࡺࡺ࡯ࡈࡴࡤࡲࡹࡖࡥࡳ࡯࡬ࡷࡸ࡯࡯࡯ࡵࠪ᝝"),
  bstack11lll_opy_ (u"ࠫࡦࡴࡤࡳࡱ࡬ࡨࡓࡧࡴࡶࡴࡤࡰࡔࡸࡩࡦࡰࡷࡥࡹ࡯࡯࡯ࠩ᝞"),
  bstack11lll_opy_ (u"ࠬࡹࡹࡴࡶࡨࡱࡕࡵࡲࡵࠩ᝟"),
  bstack11lll_opy_ (u"࠭ࡲࡦ࡯ࡲࡸࡪࡇࡤࡣࡊࡲࡷࡹ࠭ᝠ"),
  bstack11lll_opy_ (u"ࠧࡴ࡭࡬ࡴ࡚ࡴ࡬ࡰࡥ࡮ࠫᝡ"), bstack11lll_opy_ (u"ࠨࡷࡱࡰࡴࡩ࡫ࡕࡻࡳࡩࠬᝢ"), bstack11lll_opy_ (u"ࠩࡸࡲࡱࡵࡣ࡬ࡍࡨࡽࠬᝣ"),
  bstack11lll_opy_ (u"ࠪࡥࡺࡺ࡯ࡍࡣࡸࡲࡨ࡮ࠧᝤ"),
  bstack11lll_opy_ (u"ࠫࡸࡱࡩࡱࡎࡲ࡫ࡨࡧࡴࡄࡣࡳࡸࡺࡸࡥࠨᝥ"),
  bstack11lll_opy_ (u"ࠬࡻ࡮ࡪࡰࡶࡸࡦࡲ࡬ࡐࡶ࡫ࡩࡷࡖࡡࡤ࡭ࡤ࡫ࡪࡹࠧᝦ"),
  bstack11lll_opy_ (u"࠭ࡤࡪࡵࡤࡦࡱ࡫ࡗࡪࡰࡧࡳࡼࡇ࡮ࡪ࡯ࡤࡸ࡮ࡵ࡮ࠨᝧ"),
  bstack11lll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩ࡚࡯ࡰ࡮ࡶ࡚ࡪࡸࡳࡪࡱࡱࠫᝨ"),
  bstack11lll_opy_ (u"ࠨࡧࡱࡪࡴࡸࡣࡦࡃࡳࡴࡎࡴࡳࡵࡣ࡯ࡰࠬᝩ"),
  bstack11lll_opy_ (u"ࠩࡨࡲࡸࡻࡲࡦ࡙ࡨࡦࡻ࡯ࡥࡸࡵࡋࡥࡻ࡫ࡐࡢࡩࡨࡷࠬᝪ"), bstack11lll_opy_ (u"ࠪࡻࡪࡨࡶࡪࡧࡺࡈࡪࡼࡴࡰࡱ࡯ࡷࡕࡵࡲࡵࠩᝫ"), bstack11lll_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨ࡛ࡪࡨࡶࡪࡧࡺࡈࡪࡺࡡࡪ࡮ࡶࡇࡴࡲ࡬ࡦࡥࡷ࡭ࡴࡴࠧᝬ"),
  bstack11lll_opy_ (u"ࠬࡸࡥ࡮ࡱࡷࡩࡆࡶࡰࡴࡅࡤࡧ࡭࡫ࡌࡪ࡯࡬ࡸࠬ᝭"),
  bstack11lll_opy_ (u"࠭ࡣࡢ࡮ࡨࡲࡩࡧࡲࡇࡱࡵࡱࡦࡺࠧᝮ"),
  bstack11lll_opy_ (u"ࠧࡣࡷࡱࡨࡱ࡫ࡉࡥࠩᝯ"),
  bstack11lll_opy_ (u"ࠨ࡮ࡤࡹࡳࡩࡨࡕ࡫ࡰࡩࡴࡻࡴࠨᝰ"),
  bstack11lll_opy_ (u"ࠩ࡯ࡳࡨࡧࡴࡪࡱࡱࡗࡪࡸࡶࡪࡥࡨࡷࡊࡴࡡࡣ࡮ࡨࡨࠬ᝱"), bstack11lll_opy_ (u"ࠪࡰࡴࡩࡡࡵ࡫ࡲࡲࡘ࡫ࡲࡷ࡫ࡦࡩࡸࡇࡵࡵࡪࡲࡶ࡮ࢀࡥࡥࠩᝲ"),
  bstack11lll_opy_ (u"ࠫࡦࡻࡴࡰࡃࡦࡧࡪࡶࡴࡂ࡮ࡨࡶࡹࡹࠧᝳ"), bstack11lll_opy_ (u"ࠬࡧࡵࡵࡱࡇ࡭ࡸࡳࡩࡴࡵࡄࡰࡪࡸࡴࡴࠩ᝴"),
  bstack11lll_opy_ (u"࠭࡮ࡢࡶ࡬ࡺࡪࡏ࡮ࡴࡶࡵࡹࡲ࡫࡮ࡵࡵࡏ࡭ࡧ࠭᝵"),
  bstack11lll_opy_ (u"ࠧ࡯ࡣࡷ࡭ࡻ࡫ࡗࡦࡤࡗࡥࡵ࠭᝶"),
  bstack11lll_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࡊࡰ࡬ࡸ࡮ࡧ࡬ࡖࡴ࡯ࠫ᝷"), bstack11lll_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪࡃ࡯ࡰࡴࡽࡐࡰࡲࡸࡴࡸ࠭᝸"), bstack11lll_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࡌ࡫ࡳࡵࡲࡦࡈࡵࡥࡺࡪࡗࡢࡴࡱ࡭ࡳ࡭ࠧ᝹"), bstack11lll_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࡓࡵ࡫࡮ࡍ࡫ࡱ࡯ࡸࡏ࡮ࡃࡣࡦ࡯࡬ࡸ࡯ࡶࡰࡧࠫ᝺"),
  bstack11lll_opy_ (u"ࠬࡱࡥࡦࡲࡎࡩࡾࡉࡨࡢ࡫ࡱࡷࠬ᝻"),
  bstack11lll_opy_ (u"࠭࡬ࡰࡥࡤࡰ࡮ࢀࡡࡣ࡮ࡨࡗࡹࡸࡩ࡯ࡩࡶࡈ࡮ࡸࠧ᝼"),
  bstack11lll_opy_ (u"ࠧࡱࡴࡲࡧࡪࡹࡳࡂࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ᝽"),
  bstack11lll_opy_ (u"ࠨ࡫ࡱࡸࡪࡸࡋࡦࡻࡇࡩࡱࡧࡹࠨ᝾"),
  bstack11lll_opy_ (u"ࠩࡶ࡬ࡴࡽࡉࡐࡕࡏࡳ࡬࠭᝿"),
  bstack11lll_opy_ (u"ࠪࡷࡪࡴࡤࡌࡧࡼࡗࡹࡸࡡࡵࡧࡪࡽࠬក"),
  bstack11lll_opy_ (u"ࠫࡼ࡫ࡢ࡬࡫ࡷࡖࡪࡹࡰࡰࡰࡶࡩ࡙࡯࡭ࡦࡱࡸࡸࠬខ"), bstack11lll_opy_ (u"ࠬࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵ࡙ࡤ࡭ࡹ࡚ࡩ࡮ࡧࡲࡹࡹ࠭គ"),
  bstack11lll_opy_ (u"࠭ࡲࡦ࡯ࡲࡸࡪࡊࡥࡣࡷࡪࡔࡷࡵࡸࡺࠩឃ"),
  bstack11lll_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡁࡴࡻࡱࡧࡊࡾࡥࡤࡷࡷࡩࡋࡸ࡯࡮ࡊࡷࡸࡵࡹࠧង"),
  bstack11lll_opy_ (u"ࠨࡵ࡮࡭ࡵࡒ࡯ࡨࡅࡤࡴࡹࡻࡲࡦࠩច"),
  bstack11lll_opy_ (u"ࠩࡺࡩࡧࡱࡩࡵࡆࡨࡦࡺ࡭ࡐࡳࡱࡻࡽࡕࡵࡲࡵࠩឆ"),
  bstack11lll_opy_ (u"ࠪࡪࡺࡲ࡬ࡄࡱࡱࡸࡪࡾࡴࡍ࡫ࡶࡸࠬជ"),
  bstack11lll_opy_ (u"ࠫࡼࡧࡩࡵࡈࡲࡶࡆࡶࡰࡔࡥࡵ࡭ࡵࡺࠧឈ"),
  bstack11lll_opy_ (u"ࠬࡽࡥࡣࡸ࡬ࡩࡼࡉ࡯࡯ࡰࡨࡧࡹࡘࡥࡵࡴ࡬ࡩࡸ࠭ញ"),
  bstack11lll_opy_ (u"࠭ࡡࡱࡲࡑࡥࡲ࡫ࠧដ"),
  bstack11lll_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡓࡔࡎࡆࡩࡷࡺࠧឋ"),
  bstack11lll_opy_ (u"ࠨࡶࡤࡴ࡜࡯ࡴࡩࡕ࡫ࡳࡷࡺࡐࡳࡧࡶࡷࡉࡻࡲࡢࡶ࡬ࡳࡳ࠭ឌ"),
  bstack11lll_opy_ (u"ࠩࡶࡧࡦࡲࡥࡇࡣࡦࡸࡴࡸࠧឍ"),
  bstack11lll_opy_ (u"ࠪࡻࡩࡧࡌࡰࡥࡤࡰࡕࡵࡲࡵࠩណ"),
  bstack11lll_opy_ (u"ࠫࡸ࡮࡯ࡸ࡚ࡦࡳࡩ࡫ࡌࡰࡩࠪត"),
  bstack11lll_opy_ (u"ࠬ࡯࡯ࡴࡋࡱࡷࡹࡧ࡬࡭ࡒࡤࡹࡸ࡫ࠧថ"),
  bstack11lll_opy_ (u"࠭ࡸࡤࡱࡧࡩࡈࡵ࡮ࡧ࡫ࡪࡊ࡮ࡲࡥࠨទ"),
  bstack11lll_opy_ (u"ࠧ࡬ࡧࡼࡧ࡭ࡧࡩ࡯ࡒࡤࡷࡸࡽ࡯ࡳࡦࠪធ"),
  bstack11lll_opy_ (u"ࠨࡷࡶࡩࡕࡸࡥࡣࡷ࡬ࡰࡹ࡝ࡄࡂࠩន"),
  bstack11lll_opy_ (u"ࠩࡳࡶࡪࡼࡥ࡯ࡶ࡚ࡈࡆࡇࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠪប"),
  bstack11lll_opy_ (u"ࠪࡻࡪࡨࡄࡳ࡫ࡹࡩࡷࡇࡧࡦࡰࡷ࡙ࡷࡲࠧផ"),
  bstack11lll_opy_ (u"ࠫࡰ࡫ࡹࡤࡪࡤ࡭ࡳࡖࡡࡵࡪࠪព"),
  bstack11lll_opy_ (u"ࠬࡻࡳࡦࡐࡨࡻ࡜ࡊࡁࠨភ"),
  bstack11lll_opy_ (u"࠭ࡷࡥࡣࡏࡥࡺࡴࡣࡩࡖ࡬ࡱࡪࡵࡵࡵࠩម"), bstack11lll_opy_ (u"ࠧࡸࡦࡤࡇࡴࡴ࡮ࡦࡥࡷ࡭ࡴࡴࡔࡪ࡯ࡨࡳࡺࡺࠧយ"),
  bstack11lll_opy_ (u"ࠨࡺࡦࡳࡩ࡫ࡏࡳࡩࡌࡨࠬរ"), bstack11lll_opy_ (u"ࠩࡻࡧࡴࡪࡥࡔ࡫ࡪࡲ࡮ࡴࡧࡊࡦࠪល"),
  bstack11lll_opy_ (u"ࠪࡹࡵࡪࡡࡵࡧࡧ࡛ࡉࡇࡂࡶࡰࡧࡰࡪࡏࡤࠨវ"),
  bstack11lll_opy_ (u"ࠫࡷ࡫ࡳࡦࡶࡒࡲࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡳࡶࡒࡲࡱࡿࠧឝ"),
  bstack11lll_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩ࡚ࡩ࡮ࡧࡲࡹࡹࡹࠧឞ"),
  bstack11lll_opy_ (u"࠭ࡷࡥࡣࡖࡸࡦࡸࡴࡶࡲࡕࡩࡹࡸࡩࡦࡵࠪស"), bstack11lll_opy_ (u"ࠧࡸࡦࡤࡗࡹࡧࡲࡵࡷࡳࡖࡪࡺࡲࡺࡋࡱࡸࡪࡸࡶࡢ࡮ࠪហ"),
  bstack11lll_opy_ (u"ࠨࡥࡲࡲࡳ࡫ࡣࡵࡊࡤࡶࡩࡽࡡࡳࡧࡎࡩࡾࡨ࡯ࡢࡴࡧࠫឡ"),
  bstack11lll_opy_ (u"ࠩࡰࡥࡽ࡚ࡹࡱ࡫ࡱ࡫ࡋࡸࡥࡲࡷࡨࡲࡨࡿࠧអ"),
  bstack11lll_opy_ (u"ࠪࡷ࡮ࡳࡰ࡭ࡧࡌࡷ࡛࡯ࡳࡪࡤ࡯ࡩࡈ࡮ࡥࡤ࡭ࠪឣ"),
  bstack11lll_opy_ (u"ࠫࡺࡹࡥࡄࡣࡵࡸ࡭ࡧࡧࡦࡕࡶࡰࠬឤ"),
  bstack11lll_opy_ (u"ࠬࡹࡨࡰࡷ࡯ࡨ࡚ࡹࡥࡔ࡫ࡱ࡫ࡱ࡫ࡴࡰࡰࡗࡩࡸࡺࡍࡢࡰࡤ࡫ࡪࡸࠧឥ"),
  bstack11lll_opy_ (u"࠭ࡳࡵࡣࡵࡸࡎ࡝ࡄࡑࠩឦ"),
  bstack11lll_opy_ (u"ࠧࡢ࡮࡯ࡳࡼ࡚࡯ࡶࡥ࡫ࡍࡩࡋ࡮ࡳࡱ࡯ࡰࠬឧ"),
  bstack11lll_opy_ (u"ࠨ࡫ࡪࡲࡴࡸࡥࡉ࡫ࡧࡨࡪࡴࡁࡱ࡫ࡓࡳࡱ࡯ࡣࡺࡇࡵࡶࡴࡸࠧឨ"),
  bstack11lll_opy_ (u"ࠩࡰࡳࡨࡱࡌࡰࡥࡤࡸ࡮ࡵ࡮ࡂࡲࡳࠫឩ"),
  bstack11lll_opy_ (u"ࠪࡰࡴ࡭ࡣࡢࡶࡉࡳࡷࡳࡡࡵࠩឪ"), bstack11lll_opy_ (u"ࠫࡱࡵࡧࡤࡣࡷࡊ࡮ࡲࡴࡦࡴࡖࡴࡪࡩࡳࠨឫ"),
  bstack11lll_opy_ (u"ࠬࡧ࡬࡭ࡱࡺࡈࡪࡲࡡࡺࡃࡧࡦࠬឬ"),
  bstack11lll_opy_ (u"࠭ࡤࡪࡵࡤࡦࡱ࡫ࡉࡥࡎࡲࡧࡦࡺ࡯ࡳࡃࡸࡸࡴࡩ࡯࡮ࡲ࡯ࡩࡹ࡯࡯࡯ࠩឭ")
]
bstack1l111111l_opy_ = bstack11lll_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡣࡳ࡭࠲ࡩ࡬ࡰࡷࡧ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠵ࡵࡱ࡮ࡲࡥࡩ࠭ឮ")
bstack11llll111l_opy_ = [bstack11lll_opy_ (u"ࠨ࠰ࡤࡴࡰ࠭ឯ"), bstack11lll_opy_ (u"ࠩ࠱ࡥࡦࡨࠧឰ"), bstack11lll_opy_ (u"ࠪ࠲࡮ࡶࡡࠨឱ")]
bstack1l111l11ll_opy_ = [bstack11lll_opy_ (u"ࠫ࡮ࡪࠧឲ"), bstack11lll_opy_ (u"ࠬࡶࡡࡵࡪࠪឳ"), bstack11lll_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡥࡩࡥࠩ឴"), bstack11lll_opy_ (u"ࠧࡴࡪࡤࡶࡪࡧࡢ࡭ࡧࡢ࡭ࡩ࠭឵")]
bstack11l1lllll_opy_ = {
  bstack11lll_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨា"): bstack11lll_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧិ"),
  bstack11lll_opy_ (u"ࠪࡪ࡮ࡸࡥࡧࡱࡻࡓࡵࡺࡩࡰࡰࡶࠫី"): bstack11lll_opy_ (u"ࠫࡲࡵࡺ࠻ࡨ࡬ࡶࡪ࡬࡯ࡹࡑࡳࡸ࡮ࡵ࡮ࡴࠩឹ"),
  bstack11lll_opy_ (u"ࠬ࡫ࡤࡨࡧࡒࡴࡹ࡯࡯࡯ࡵࠪឺ"): bstack11lll_opy_ (u"࠭࡭ࡴ࠼ࡨࡨ࡬࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧុ"),
  bstack11lll_opy_ (u"ࠧࡪࡧࡒࡴࡹ࡯࡯࡯ࡵࠪូ"): bstack11lll_opy_ (u"ࠨࡵࡨ࠾࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧួ"),
  bstack11lll_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪࡑࡳࡸ࡮ࡵ࡮ࡴࠩើ"): bstack11lll_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫࠱ࡳࡵࡺࡩࡰࡰࡶࠫឿ")
}
bstack11l1l1ll1_opy_ = [
  bstack11lll_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩៀ"),
  bstack11lll_opy_ (u"ࠬࡳ࡯ࡻ࠼ࡩ࡭ࡷ࡫ࡦࡰࡺࡒࡴࡹ࡯࡯࡯ࡵࠪេ"),
  bstack11lll_opy_ (u"࠭࡭ࡴ࠼ࡨࡨ࡬࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧែ"),
  bstack11lll_opy_ (u"ࠧࡴࡧ࠽࡭ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ៃ"),
  bstack11lll_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩ࠯ࡱࡳࡸ࡮ࡵ࡮ࡴࠩោ"),
]
bstack1ll1lllll_opy_ = bstack1ll11llll_opy_ + bstack1l11111lll1_opy_ + bstack1llllll11l_opy_
bstack1l11l1l1l_opy_ = [
  bstack11lll_opy_ (u"ࠩࡡࡰࡴࡩࡡ࡭ࡪࡲࡷࡹࠪࠧៅ"),
  bstack11lll_opy_ (u"ࠪࡢࡧࡹ࠭࡭ࡱࡦࡥࡱ࠴ࡣࡰ࡯ࠧࠫំ"),
  bstack11lll_opy_ (u"ࠫࡣ࠷࠲࠸࠰ࠪះ"),
  bstack11lll_opy_ (u"ࠬࡤ࠱࠱࠰ࠪៈ"),
  bstack11lll_opy_ (u"࠭࡞࠲࠹࠵࠲࠶ࡡ࠶࠮࠻ࡠ࠲ࠬ៉"),
  bstack11lll_opy_ (u"ࠧ࡟࠳࠺࠶࠳࠸࡛࠱࠯࠼ࡡ࠳࠭៊"),
  bstack11lll_opy_ (u"ࠨࡠ࠴࠻࠷࠴࠳࡜࠲࠰࠵ࡢ࠴ࠧ់"),
  bstack11lll_opy_ (u"ࠩࡡ࠵࠾࠸࠮࠲࠸࠻࠲ࠬ៌")
]
bstack1l111111lll_opy_ = bstack11lll_opy_ (u"ࠪ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡦࡶࡩ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫ៍")
bstack11llll1ll1_opy_ = bstack11lll_opy_ (u"ࠫࡸࡪ࡫࠰ࡸ࠴࠳ࡪࡼࡥ࡯ࡶࠪ៎")
bstack1l1l1111_opy_ = [ bstack11lll_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧ៏") ]
bstack1111111l_opy_ = [ bstack11lll_opy_ (u"࠭ࡡࡱࡲ࠰ࡥࡺࡺ࡯࡮ࡣࡷࡩࠬ័") ]
bstack1l111l111l_opy_ = [bstack11lll_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ៑")]
bstack1l1l1ll11_opy_ = [ bstack11lll_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ្") ]
bstack1l1l11l11_opy_ = bstack11lll_opy_ (u"ࠩࡖࡈࡐ࡙ࡥࡵࡷࡳࠫ៓")
bstack11l111l11_opy_ = bstack11lll_opy_ (u"ࠪࡗࡉࡑࡔࡦࡵࡷࡅࡹࡺࡥ࡮ࡲࡷࡩࡩ࠭។")
bstack11l1ll11_opy_ = bstack11lll_opy_ (u"ࠫࡘࡊࡋࡕࡧࡶࡸࡘࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬ࠨ៕")
bstack111l11l1l_opy_ = bstack11lll_opy_ (u"ࠬ࠺࠮࠱࠰࠳ࠫ៖")
bstack1llllll1l_opy_ = [
  bstack11lll_opy_ (u"࠭ࡅࡓࡔࡢࡊࡆࡏࡌࡆࡆࠪៗ"),
  bstack11lll_opy_ (u"ࠧࡆࡔࡕࡣ࡙ࡏࡍࡆࡆࡢࡓ࡚࡚ࠧ៘"),
  bstack11lll_opy_ (u"ࠨࡇࡕࡖࡤࡈࡌࡐࡅࡎࡉࡉࡥࡂ࡚ࡡࡆࡐࡎࡋࡎࡕࠩ៙"),
  bstack11lll_opy_ (u"ࠩࡈࡖࡗࡥࡎࡆࡖ࡚ࡓࡗࡑ࡟ࡄࡊࡄࡒࡌࡋࡄࠨ៚"),
  bstack11lll_opy_ (u"ࠪࡉࡗࡘ࡟ࡔࡑࡆࡏࡊ࡚࡟ࡏࡑࡗࡣࡈࡕࡎࡏࡇࡆࡘࡊࡊࠧ៛"),
  bstack11lll_opy_ (u"ࠫࡊࡘࡒࡠࡅࡒࡒࡓࡋࡃࡕࡋࡒࡒࡤࡉࡌࡐࡕࡈࡈࠬៜ"),
  bstack11lll_opy_ (u"ࠬࡋࡒࡓࡡࡆࡓࡓࡔࡅࡄࡖࡌࡓࡓࡥࡒࡆࡕࡈࡘࠬ៝"),
  bstack11lll_opy_ (u"࠭ࡅࡓࡔࡢࡇࡔࡔࡎࡆࡅࡗࡍࡔࡔ࡟ࡓࡇࡉ࡙ࡘࡋࡄࠨ៞"),
  bstack11lll_opy_ (u"ࠧࡆࡔࡕࡣࡈࡕࡎࡏࡇࡆࡘࡎࡕࡎࡠࡃࡅࡓࡗ࡚ࡅࡅࠩ៟"),
  bstack11lll_opy_ (u"ࠨࡇࡕࡖࡤࡉࡏࡏࡐࡈࡇ࡙ࡏࡏࡏࡡࡉࡅࡎࡒࡅࡅࠩ០"),
  bstack11lll_opy_ (u"ࠩࡈࡖࡗࡥࡎࡂࡏࡈࡣࡓࡕࡔࡠࡔࡈࡗࡔࡒࡖࡆࡆࠪ១"),
  bstack11lll_opy_ (u"ࠪࡉࡗࡘ࡟ࡂࡆࡇࡖࡊ࡙ࡓࡠࡋࡑ࡚ࡆࡒࡉࡅࠩ២"),
  bstack11lll_opy_ (u"ࠫࡊࡘࡒࡠࡃࡇࡈࡗࡋࡓࡔࡡࡘࡒࡗࡋࡁࡄࡊࡄࡆࡑࡋࠧ៣"),
  bstack11lll_opy_ (u"ࠬࡋࡒࡓࡡࡗ࡙ࡓࡔࡅࡍࡡࡆࡓࡓࡔࡅࡄࡖࡌࡓࡓࡥࡆࡂࡋࡏࡉࡉ࠭៤"),
  bstack11lll_opy_ (u"࠭ࡅࡓࡔࡢࡇࡔࡔࡎࡆࡅࡗࡍࡔࡔ࡟ࡕࡋࡐࡉࡉࡥࡏࡖࡖࠪ៥"),
  bstack11lll_opy_ (u"ࠧࡆࡔࡕࡣࡘࡕࡃࡌࡕࡢࡇࡔࡔࡎࡆࡅࡗࡍࡔࡔ࡟ࡇࡃࡌࡐࡊࡊࠧ៦"),
  bstack11lll_opy_ (u"ࠨࡇࡕࡖࡤ࡙ࡏࡄࡍࡖࡣࡈࡕࡎࡏࡇࡆࡘࡎࡕࡎࡠࡊࡒࡗ࡙ࡥࡕࡏࡔࡈࡅࡈࡎࡁࡃࡎࡈࠫ៧"),
  bstack11lll_opy_ (u"ࠩࡈࡖࡗࡥࡐࡓࡑ࡛࡝ࡤࡉࡏࡏࡐࡈࡇ࡙ࡏࡏࡏࡡࡉࡅࡎࡒࡅࡅࠩ៨"),
  bstack11lll_opy_ (u"ࠪࡉࡗࡘ࡟ࡏࡃࡐࡉࡤࡔࡏࡕࡡࡕࡉࡘࡕࡌࡗࡇࡇࠫ៩"),
  bstack11lll_opy_ (u"ࠫࡊࡘࡒࡠࡐࡄࡑࡊࡥࡒࡆࡕࡒࡐ࡚࡚ࡉࡐࡐࡢࡊࡆࡏࡌࡆࡆࠪ៪"),
  bstack11lll_opy_ (u"ࠬࡋࡒࡓࡡࡐࡅࡓࡊࡁࡕࡑࡕ࡝ࡤࡖࡒࡐ࡚࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣࡋࡇࡉࡍࡇࡇࠫ៫"),
]
bstack1l1ll1ll_opy_ = bstack11lll_opy_ (u"࠭࠮࠰ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠭ࡢࡴࡷ࡭࡫ࡧࡣࡵࡵ࠲ࠫ៬")
bstack1l1llll1ll_opy_ = os.path.join(os.path.expanduser(bstack11lll_opy_ (u"ࠧࡿࠩ៭")), bstack11lll_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ៮"), bstack11lll_opy_ (u"ࠩ࠱ࡦࡸࡺࡡࡤ࡭࠰ࡧࡴࡴࡦࡪࡩ࠱࡮ࡸࡵ࡮ࠨ៯"))
bstack1l111lll11l_opy_ = bstack11lll_opy_ (u"ࠪ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡢࡲ࡬ࠫ៰")
bstack1l11111l1ll_opy_ = [ bstack11lll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ៱"), bstack11lll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ៲"), bstack11lll_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬ៳"), bstack11lll_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ៴")]
bstack11l1111ll_opy_ = [ bstack11lll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ៵"), bstack11lll_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ៶"), bstack11lll_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩ៷"), bstack11lll_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ៸") ]
bstack11l111l111_opy_ = {
  bstack11lll_opy_ (u"ࠬࡖࡁࡔࡕࠪ៹"): bstack11lll_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭៺"),
  bstack11lll_opy_ (u"ࠧࡇࡃࡌࡐࠬ៻"): bstack11lll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ៼"),
  bstack11lll_opy_ (u"ࠩࡖࡏࡎࡖࠧ៽"): bstack11lll_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫ៾")
}
bstack1l1lll111_opy_ = [
  bstack11lll_opy_ (u"ࠦ࡬࡫ࡴࠣ៿"),
  bstack11lll_opy_ (u"ࠧ࡭࡯ࡃࡣࡦ࡯ࠧ᠀"),
  bstack11lll_opy_ (u"ࠨࡧࡰࡈࡲࡶࡼࡧࡲࡥࠤ᠁"),
  bstack11lll_opy_ (u"ࠢࡳࡧࡩࡶࡪࡹࡨࠣ᠂"),
  bstack11lll_opy_ (u"ࠣࡥ࡯࡭ࡨࡱࡅ࡭ࡧࡰࡩࡳࡺࠢ᠃"),
  bstack11lll_opy_ (u"ࠤࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࠨ᠄"),
  bstack11lll_opy_ (u"ࠥࡷࡺࡨ࡭ࡪࡶࡈࡰࡪࡳࡥ࡯ࡶࠥ᠅"),
  bstack11lll_opy_ (u"ࠦࡸ࡫࡮ࡥࡍࡨࡽࡸ࡚࡯ࡆ࡮ࡨࡱࡪࡴࡴࠣ᠆"),
  bstack11lll_opy_ (u"ࠧࡹࡥ࡯ࡦࡎࡩࡾࡹࡔࡰࡃࡦࡸ࡮ࡼࡥࡆ࡮ࡨࡱࡪࡴࡴࠣ᠇"),
  bstack11lll_opy_ (u"ࠨࡣ࡭ࡧࡤࡶࡊࡲࡥ࡮ࡧࡱࡸࠧ᠈"),
  bstack11lll_opy_ (u"ࠢࡢࡥࡷ࡭ࡴࡴࡳࠣ᠉"),
  bstack11lll_opy_ (u"ࠣࡧࡻࡩࡨࡻࡴࡦࡕࡦࡶ࡮ࡶࡴࠣ᠊"),
  bstack11lll_opy_ (u"ࠤࡨࡼࡪࡩࡵࡵࡧࡄࡷࡾࡴࡣࡔࡥࡵ࡭ࡵࡺࠢ᠋"),
  bstack11lll_opy_ (u"ࠥࡧࡱࡵࡳࡦࠤ᠌"),
  bstack11lll_opy_ (u"ࠦࡶࡻࡩࡵࠤ᠍"),
  bstack11lll_opy_ (u"ࠧࡶࡥࡳࡨࡲࡶࡲ࡚࡯ࡶࡥ࡫ࡅࡨࡺࡩࡰࡰࠥ᠎"),
  bstack11lll_opy_ (u"ࠨࡰࡦࡴࡩࡳࡷࡳࡍࡶ࡮ࡷ࡭࡙ࡵࡵࡤࡪࠥ᠏"),
  bstack11lll_opy_ (u"ࠢࡴࡪࡤ࡯ࡪࠨ᠐"),
  bstack11lll_opy_ (u"ࠣࡥ࡯ࡳࡸ࡫ࡁࡱࡲࠥ᠑")
]
bstack11lllll1ll1_opy_ = [
  bstack11lll_opy_ (u"ࠤࡦࡰ࡮ࡩ࡫ࠣ᠒"),
  bstack11lll_opy_ (u"ࠥࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠢ᠓"),
  bstack11lll_opy_ (u"ࠦࡦࡻࡴࡰࠤ᠔"),
  bstack11lll_opy_ (u"ࠧࡳࡡ࡯ࡷࡤࡰࠧ᠕"),
  bstack11lll_opy_ (u"ࠨࡴࡦࡵࡷࡧࡦࡹࡥࠣ᠖")
]
bstack11l1l1111_opy_ = {
  bstack11lll_opy_ (u"ࠢࡤ࡮࡬ࡧࡰࠨ᠗"): [bstack11lll_opy_ (u"ࠣࡥ࡯࡭ࡨࡱࡅ࡭ࡧࡰࡩࡳࡺࠢ᠘")],
  bstack11lll_opy_ (u"ࠤࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࠨ᠙"): [bstack11lll_opy_ (u"ࠥࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠢ᠚")],
  bstack11lll_opy_ (u"ࠦࡦࡻࡴࡰࠤ᠛"): [bstack11lll_opy_ (u"ࠧࡹࡥ࡯ࡦࡎࡩࡾࡹࡔࡰࡇ࡯ࡩࡲ࡫࡮ࡵࠤ᠜"), bstack11lll_opy_ (u"ࠨࡳࡦࡰࡧࡏࡪࡿࡳࡕࡱࡄࡧࡹ࡯ࡶࡦࡇ࡯ࡩࡲ࡫࡮ࡵࠤ᠝"), bstack11lll_opy_ (u"ࠢࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠦ᠞"), bstack11lll_opy_ (u"ࠣࡥ࡯࡭ࡨࡱࡅ࡭ࡧࡰࡩࡳࡺࠢ᠟")],
  bstack11lll_opy_ (u"ࠤࡰࡥࡳࡻࡡ࡭ࠤᠠ"): [bstack11lll_opy_ (u"ࠥࡱࡦࡴࡵࡢ࡮ࠥᠡ")],
  bstack11lll_opy_ (u"ࠦࡹ࡫ࡳࡵࡥࡤࡷࡪࠨᠢ"): [bstack11lll_opy_ (u"ࠧࡺࡥࡴࡶࡦࡥࡸ࡫ࠢᠣ")],
}
bstack1l11111ll1l_opy_ = {
  bstack11lll_opy_ (u"ࠨࡣ࡭࡫ࡦ࡯ࡊࡲࡥ࡮ࡧࡱࡸࠧᠤ"): bstack11lll_opy_ (u"ࠢࡤ࡮࡬ࡧࡰࠨᠥ"),
  bstack11lll_opy_ (u"ࠣࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠧᠦ"): bstack11lll_opy_ (u"ࠤࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࠨᠧ"),
  bstack11lll_opy_ (u"ࠥࡷࡪࡴࡤࡌࡧࡼࡷ࡙ࡵࡅ࡭ࡧࡰࡩࡳࡺࠢᠨ"): bstack11lll_opy_ (u"ࠦࡸ࡫࡮ࡥࡍࡨࡽࡸࠨᠩ"),
  bstack11lll_opy_ (u"ࠧࡹࡥ࡯ࡦࡎࡩࡾࡹࡔࡰࡃࡦࡸ࡮ࡼࡥࡆ࡮ࡨࡱࡪࡴࡴࠣᠪ"): bstack11lll_opy_ (u"ࠨࡳࡦࡰࡧࡏࡪࡿࡳࠣᠫ"),
  bstack11lll_opy_ (u"ࠢࡵࡧࡶࡸࡨࡧࡳࡦࠤᠬ"): bstack11lll_opy_ (u"ࠣࡶࡨࡷࡹࡩࡡࡴࡧࠥᠭ")
}
bstack111ll1ll11_opy_ = {
  bstack11lll_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑ࠭ᠮ"): bstack11lll_opy_ (u"ࠪࡗࡺ࡯ࡴࡦࠢࡖࡩࡹࡻࡰࠨᠯ"),
  bstack11lll_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡅࡑࡒࠧᠰ"): bstack11lll_opy_ (u"࡙ࠬࡵࡪࡶࡨࠤ࡙࡫ࡡࡳࡦࡲࡻࡳ࠭ᠱ"),
  bstack11lll_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫᠲ"): bstack11lll_opy_ (u"ࠧࡕࡧࡶࡸ࡙ࠥࡥࡵࡷࡳࠫᠳ"),
  bstack11lll_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬᠴ"): bstack11lll_opy_ (u"ࠩࡗࡩࡸࡺࠠࡕࡧࡤࡶࡩࡵࡷ࡯ࠩᠵ")
}
bstack1l1111l11ll_opy_ = 65536
bstack11llllll1l1_opy_ = bstack11lll_opy_ (u"ࠪ࠲࠳࠴࡛ࡕࡔࡘࡒࡈࡇࡔࡆࡆࡠࠫᠶ")
bstack11llllll11l_opy_ = [
      bstack11lll_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ᠷ"), bstack11lll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨᠸ"), bstack11lll_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩᠹ"), bstack11lll_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫᠺ"), bstack11lll_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡗࡣࡵ࡭ࡦࡨ࡬ࡦࡵࠪᠻ"),
      bstack11lll_opy_ (u"ࠩࡳࡶࡴࡾࡹࡖࡵࡨࡶࠬᠼ"), bstack11lll_opy_ (u"ࠪࡴࡷࡵࡸࡺࡒࡤࡷࡸ࠭ᠽ"), bstack11lll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡓࡶࡴࡾࡹࡖࡵࡨࡶࠬᠾ"), bstack11lll_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡔࡷࡵࡸࡺࡒࡤࡷࡸ࠭ᠿ"),
      bstack11lll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡻࡳࡦࡴࡑࡥࡲ࡫ࠧᡀ"), bstack11lll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩᡁ"), bstack11lll_opy_ (u"ࠨࡣࡸࡸ࡭࡚࡯࡬ࡧࡱࠫᡂ")
    ]
bstack11lllll1l1l_opy_= {
  bstack11lll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ᡃ"): bstack11lll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧᡄ"),
  bstack11lll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨᡅ"): bstack11lll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩᡆ"),
  bstack11lll_opy_ (u"࠭࡬ࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬᡇ"): bstack11lll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫᡈ"),
  bstack11lll_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨᡉ"): bstack11lll_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩᡊ"),
  bstack11lll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ᡋ"): bstack11lll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧᡌ"),
  bstack11lll_opy_ (u"ࠬࡲ࡯ࡨࡎࡨࡺࡪࡲࠧᡍ"): bstack11lll_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨᡎ"),
  bstack11lll_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪᡏ"): bstack11lll_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫᡐ"),
  bstack11lll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ᡑ"): bstack11lll_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧᡒ"),
  bstack11lll_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧᡓ"): bstack11lll_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨᡔ"),
  bstack11lll_opy_ (u"࠭ࡴࡦࡵࡷࡇࡴࡴࡴࡦࡺࡷࡓࡵࡺࡩࡰࡰࡶࠫᡕ"): bstack11lll_opy_ (u"ࠧࡵࡧࡶࡸࡈࡵ࡮ࡵࡧࡻࡸࡔࡶࡴࡪࡱࡱࡷࠬᡖ"),
  bstack11lll_opy_ (u"ࠨࡶࡨࡷࡹࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬᡗ"): bstack11lll_opy_ (u"ࠩࡷࡩࡸࡺࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ᡘ"),
  bstack11lll_opy_ (u"ࠪࡸࡪࡹࡴࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᡙ"): bstack11lll_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨᡚ"),
  bstack11lll_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱ࡛ࡧࡲࡪࡣࡥࡰࡪࡹࠧᡛ"): bstack11lll_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲ࡜ࡡࡳ࡫ࡤࡦࡱ࡫ࡳࠨᡜ"),
  bstack11lll_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᡝ"): bstack11lll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᡞ"),
  bstack11lll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᡟ"): bstack11lll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᡠ"),
  bstack11lll_opy_ (u"ࠫࡷ࡫ࡲࡶࡰࡗࡩࡸࡺࡳࠨᡡ"): bstack11lll_opy_ (u"ࠬࡸࡥࡳࡷࡱࡘࡪࡹࡴࡴࠩᡢ"),
  bstack11lll_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬᡣ"): bstack11lll_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭ᡤ"),
  bstack11lll_opy_ (u"ࠨࡲࡨࡶࡨࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᡥ"): bstack11lll_opy_ (u"ࠩࡳࡩࡷࡩࡹࡐࡲࡷ࡭ࡴࡴࡳࠨᡦ"),
  bstack11lll_opy_ (u"ࠪࡴࡪࡸࡣࡺࡅࡤࡴࡹࡻࡲࡦࡏࡲࡨࡪ࠭ᡧ"): bstack11lll_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡆࡥࡵࡺࡵࡳࡧࡐࡳࡩ࡫ࠧᡨ"),
  bstack11lll_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪࡇࡵࡵࡱࡆࡥࡵࡺࡵࡳࡧࡏࡳ࡬ࡹࠧᡩ"): bstack11lll_opy_ (u"࠭ࡤࡪࡵࡤࡦࡱ࡫ࡁࡶࡶࡲࡇࡦࡶࡴࡶࡴࡨࡐࡴ࡭ࡳࠨᡪ"),
  bstack11lll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧᡫ"): bstack11lll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨᡬ"),
  bstack11lll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩᡭ"): bstack11lll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪᡮ"),
  bstack11lll_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨᡯ"): bstack11lll_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩᡰ"),
  bstack11lll_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪᡱ"): bstack11lll_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࡓࡵࡺࡩࡰࡰࡶࠫᡲ"),
  bstack11lll_opy_ (u"ࠨࡲࡵࡳࡽࡿࡓࡦࡶࡷ࡭ࡳ࡭ࡳࠨᡳ"): bstack11lll_opy_ (u"ࠩࡳࡶࡴࡾࡹࡔࡧࡷࡸ࡮ࡴࡧࡴࠩᡴ")
}
bstack11lllllllll_opy_ = [bstack11lll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪᡵ"), bstack11lll_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪᡶ")]
bstack111l1l1ll_opy_ = (bstack11lll_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸࠧᡷ"),)
bstack1l11111l111_opy_ = bstack11lll_opy_ (u"࠭ࡳࡥ࡭࠲ࡺ࠶࠵ࡵࡱࡦࡤࡸࡪࡥࡣ࡭࡫ࠪᡸ")
bstack1l1111lll_opy_ = bstack11lll_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࡣࡳ࡭࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡣࡸࡸࡴࡳࡡࡵࡧ࠰ࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫࠯ࡷ࠳࠲࡫ࡷ࡯ࡤࡴ࠱ࠥ᡹")
bstack11llllllll_opy_ = bstack11lll_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࡪࡶ࡮ࡪ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡨࡦࡹࡨࡣࡱࡤࡶࡩ࠵ࡢࡶ࡫࡯ࡨࡸ࠵ࠢ᡺")
bstack1ll1ll1lll_opy_ = bstack11lll_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡥࡵ࡯࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡥࡺࡺ࡯࡮ࡣࡷࡩ࠲ࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦ࠱ࡹ࠵࠴ࡨࡵࡪ࡮ࡧࡷ࠳ࡰࡳࡰࡰࠥ᡻")
class EVENTS(Enum):
  bstack1l1111l1lll_opy_ = bstack11lll_opy_ (u"ࠪࡷࡩࡱ࠺ࡰ࠳࠴ࡽ࠿ࡶࡲࡪࡰࡷ࠱ࡧࡻࡩ࡭ࡦ࡯࡭ࡳࡱࠧ᡼")
  bstack111l11l1_opy_ = bstack11lll_opy_ (u"ࠫࡸࡪ࡫࠻ࡥ࡯ࡩࡦࡴࡵࡱࠩ᡽") # final bstack1l11111111l_opy_
  bstack1l11111llll_opy_ = bstack11lll_opy_ (u"ࠬࡹࡤ࡬࠼ࡶࡩࡳࡪ࡬ࡰࡩࡶࠫ᡾")
  bstack1l11ll1ll1_opy_ = bstack11lll_opy_ (u"࠭ࡳࡥ࡭࠽ࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫࠺ࡱࡴ࡬ࡲࡹ࠳ࡢࡶ࡫࡯ࡨࡱ࡯࡮࡬ࠩ᡿") #shift post bstack1l11111l11l_opy_
  bstack1ll1l1l1l1_opy_ = bstack11lll_opy_ (u"ࠧࡴࡦ࡮࠾ࡦࡻࡴࡰ࡯ࡤࡸࡪࡀࡰࡳ࡫ࡱࡸ࠲ࡨࡵࡪ࡮ࡧࡰ࡮ࡴ࡫ࠨᢀ") #shift post bstack1l11111l11l_opy_
  bstack1l1111l1ll1_opy_ = bstack11lll_opy_ (u"ࠨࡵࡧ࡯࠿ࡺࡥࡴࡶ࡫ࡹࡧ࠭ᢁ") #shift
  bstack1l111111l11_opy_ = bstack11lll_opy_ (u"ࠩࡶࡨࡰࡀࡰࡦࡴࡦࡽ࠿ࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠧᢂ") #shift
  bstack11ll11l1l_opy_ = bstack11lll_opy_ (u"ࠪࡷࡩࡱ࠺ࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨ࠾࡭ࡻࡢ࠮࡯ࡤࡲࡦ࡭ࡥ࡮ࡧࡱࡸࠬᢃ")
  bstack1ll1llll1ll_opy_ = bstack11lll_opy_ (u"ࠫࡸࡪ࡫࠻ࡣ࠴࠵ࡾࡀࡳࡢࡸࡨ࠱ࡷ࡫ࡳࡶ࡮ࡷࡷࠬᢄ")
  bstack1l1lllll1l_opy_ = bstack11lll_opy_ (u"ࠬࡹࡤ࡬࠼ࡤ࠵࠶ࡿ࠺ࡥࡴ࡬ࡺࡪࡸ࠭ࡱࡧࡵࡪࡴࡸ࡭ࡴࡥࡤࡲࠬᢅ")
  bstack1l1l111ll1_opy_ = bstack11lll_opy_ (u"࠭ࡳࡥ࡭࠽ࡥࡺࡺ࡯࡮ࡣࡷࡩ࠿ࡲ࡯ࡤࡣ࡯ࠫᢆ") #shift
  bstack11lll111_opy_ = bstack11lll_opy_ (u"ࠧࡴࡦ࡮࠾ࡦࡶࡰ࠮ࡣࡸࡸࡴࡳࡡࡵࡧ࠽ࡥࡵࡶ࠭ࡶࡲ࡯ࡳࡦࡪࠧᢇ") #shift
  bstack1l1lll11_opy_ = bstack11lll_opy_ (u"ࠨࡵࡧ࡯࠿ࡧࡵࡵࡱࡰࡥࡹ࡫࠺ࡤ࡫࠰ࡥࡷࡺࡩࡧࡣࡦࡸࡸ࠭ᢈ")
  bstack1lll11ll_opy_ = bstack11lll_opy_ (u"ࠩࡶࡨࡰࡀࡡ࠲࠳ࡼ࠾࡬࡫ࡴ࠮ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹ࠮ࡴࡨࡷࡺࡲࡴࡴ࠯ࡶࡹࡲࡳࡡࡳࡻࠪᢉ") #shift
  bstack1l1l11ll11_opy_ = bstack11lll_opy_ (u"ࠪࡷࡩࡱ࠺ࡢ࠳࠴ࡽ࠿࡭ࡥࡵ࠯ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺ࠯ࡵࡩࡸࡻ࡬ࡵࡵࠪᢊ") #shift
  bstack1l11111ll11_opy_ = bstack11lll_opy_ (u"ࠫࡸࡪ࡫࠻ࡲࡨࡶࡨࡿࠧᢋ") #shift
  bstack1ll11111ll1_opy_ = bstack11lll_opy_ (u"ࠬࡹࡤ࡬࠼ࡳࡩࡷࡩࡹ࠻ࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠬᢌ")
  bstack1lll1ll1_opy_ = bstack11lll_opy_ (u"࠭ࡳࡥ࡭࠽ࡥࡺࡺ࡯࡮ࡣࡷࡩ࠿ࡹࡥࡴࡵ࡬ࡳࡳ࠳ࡳࡵࡣࡷࡹࡸ࠭ᢍ") #shift
  bstack1ll1ll11ll_opy_ = bstack11lll_opy_ (u"ࠧࡴࡦ࡮࠾ࡦࡻࡴࡰ࡯ࡤࡸࡪࡀࡨࡶࡤ࠰ࡱࡦࡴࡡࡨࡧࡰࡩࡳࡺࠧᢎ")
  bstack1l111111l1l_opy_ = bstack11lll_opy_ (u"ࠨࡵࡧ࡯࠿ࡶࡲࡰࡺࡼ࠱ࡸ࡫ࡴࡶࡲࠪᢏ") #shift
  bstack1l1l1lll11_opy_ = bstack11lll_opy_ (u"ࠩࡶࡨࡰࡀࡳࡦࡶࡸࡴࠬᢐ")
  bstack1l111111ll1_opy_ = bstack11lll_opy_ (u"ࠪࡷࡩࡱ࠺ࡱࡧࡵࡧࡾࡀࡳ࡯ࡣࡳࡷ࡭ࡵࡴࠨᢑ") # not bstack1l111111111_opy_ in python
  bstack1lllll11l_opy_ = bstack11lll_opy_ (u"ࠫࡸࡪ࡫࠻ࡦࡵ࡭ࡻ࡫ࡲ࠻ࡳࡸ࡭ࡹ࠭ᢒ") # used in bstack1l1111l111l_opy_
  bstack1l1lll1ll1_opy_ = bstack11lll_opy_ (u"ࠬࡹࡤ࡬࠼ࡧࡶ࡮ࡼࡥࡳ࠼ࡪࡩࡹ࠭ᢓ") # used in bstack1l1111l111l_opy_
  bstack11llll11l_opy_ = bstack11lll_opy_ (u"࠭ࡳࡥ࡭࠽࡬ࡴࡵ࡫ࠨᢔ")
  bstack1111l1lll_opy_ = bstack11lll_opy_ (u"ࠧࡴࡦ࡮࠾ࡦࡻࡴࡰ࡯ࡤࡸࡪࡀࡳࡦࡵࡶ࡭ࡴࡴ࠭࡯ࡣࡰࡩࠬᢕ")
  bstack1l111111l1_opy_ = bstack11lll_opy_ (u"ࠨࡵࡧ࡯࠿ࡧࡵࡵࡱࡰࡥࡹ࡫࠺ࡴࡧࡶࡷ࡮ࡵ࡮࠮ࡣࡱࡲࡴࡺࡡࡵ࡫ࡲࡲࠬᢖ") #
  bstack1l1l111lll_opy_ = bstack11lll_opy_ (u"ࠩࡶࡨࡰࡀ࡯࠲࠳ࡼ࠾ࡩࡸࡩࡷࡧࡵ࠱ࡹࡧ࡫ࡦࡕࡦࡶࡪ࡫࡮ࡔࡪࡲࡸࠬᢗ")
  bstack11111l1l_opy_ = bstack11lll_opy_ (u"ࠪࡷࡩࡱ࠺ࡱࡧࡵࡧࡾࡀࡡࡶࡶࡲ࠱ࡨࡧࡰࡵࡷࡵࡩࠬᢘ")
  bstack1ll1ll1l1_opy_ = bstack11lll_opy_ (u"ࠫࡸࡪ࡫࠻ࡲࡵࡩ࠲ࡺࡥࡴࡶࠪᢙ")
  bstack1ll111ll_opy_ = bstack11lll_opy_ (u"ࠬࡹࡤ࡬࠼ࡳࡳࡸࡺ࠭ࡵࡧࡶࡸࠬᢚ")
  bstack11l1llllll_opy_ = bstack11lll_opy_ (u"࠭ࡳࡥ࡭࠽ࡨࡷ࡯ࡶࡦࡴ࠽ࡴࡷ࡫࠭ࡪࡰ࡬ࡸ࡮ࡧ࡬ࡪࡼࡤࡸ࡮ࡵ࡮ࠨᢛ") #shift
  bstack1llllll1ll_opy_ = bstack11lll_opy_ (u"ࠧࡴࡦ࡮࠾ࡩࡸࡩࡷࡧࡵ࠾ࡵࡵࡳࡵ࠯࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡦࡺࡩࡰࡰࠪᢜ") #shift
  bstack1l1111111l1_opy_ = bstack11lll_opy_ (u"ࠨࡵࡧ࡯࠿ࡧࡵࡵࡱ࠰ࡧࡦࡶࡴࡶࡴࡨࠫᢝ")
  bstack11lllllll11_opy_ = bstack11lll_opy_ (u"ࠩࡶࡨࡰࡀࡡࡶࡶࡲࡱࡦࡺࡥ࠻࡫ࡧࡰࡪ࠳ࡴࡪ࡯ࡨࡳࡺࡺࠧᢞ")
  bstack111111ll1l_opy_ = bstack11lll_opy_ (u"ࠪࡷࡩࡱ࠺ࡤ࡮࡬࠾ࡸࡺࡡࡳࡶࠪᢟ")
  bstack1l1111l1l11_opy_ = bstack11lll_opy_ (u"ࠫࡸࡪ࡫࠻ࡥ࡯࡭࠿ࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠧᢠ")
  bstack11llllll111_opy_ = bstack11lll_opy_ (u"ࠬࡹࡤ࡬࠼ࡦࡰ࡮ࡀࡣࡩࡧࡦ࡯࠲ࡻࡰࡥࡣࡷࡩࠬᢡ")
  bstack1lll1ll1l1l_opy_ = bstack11lll_opy_ (u"࠭ࡳࡥ࡭࠽ࡧࡱ࡯࠺ࡰࡰ࠰ࡦࡴࡵࡴࡴࡶࡵࡥࡵ࠭ᢢ")
  bstack1llll1l1111_opy_ = bstack11lll_opy_ (u"ࠧࡴࡦ࡮࠾ࡨࡲࡩ࠻ࡱࡱ࠱ࡨࡵ࡮࡯ࡧࡦࡸࠬᢣ")
  bstack1lllll1l111_opy_ = bstack11lll_opy_ (u"ࠨࡵࡧ࡯࠿ࡩ࡬ࡪ࠼ࡲࡲ࠲ࡹࡴࡰࡲࠪᢤ")
  bstack1llll111111_opy_ = bstack11lll_opy_ (u"ࠩࡶࡨࡰࡀࡳࡵࡣࡵࡸࡇ࡯࡮ࡔࡧࡶࡷ࡮ࡵ࡮ࠨᢥ")
  bstack1llllll111l_opy_ = bstack11lll_opy_ (u"ࠪࡷࡩࡱ࠺ࡤࡱࡱࡲࡪࡩࡴࡃ࡫ࡱࡗࡪࡹࡳࡪࡱࡱࠫᢦ")
  bstack1l1111l1l1l_opy_ = bstack11lll_opy_ (u"ࠫࡸࡪ࡫࠻ࡦࡵ࡭ࡻ࡫ࡲࡊࡰ࡬ࡸࠬᢧ")
  bstack1l11111l1l1_opy_ = bstack11lll_opy_ (u"ࠬࡹࡤ࡬࠼ࡩ࡭ࡳࡪࡎࡦࡣࡵࡩࡸࡺࡈࡶࡤࠪᢨ")
  bstack1l1ll1111l1_opy_ = bstack11lll_opy_ (u"࠭ࡳࡥ࡭࠽ࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࡋࡱ࡭ࡹᢩ࠭")
  bstack1l1ll11llll_opy_ = bstack11lll_opy_ (u"ࠧࡴࡦ࡮࠾ࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡖࡸࡦࡸࡴࠨᢪ")
  bstack1ll1lllll1l_opy_ = bstack11lll_opy_ (u"ࠨࡵࡧ࡯࠿ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡈࡵ࡮ࡧ࡫ࡪࠫ᢫")
  bstack11lllll1lll_opy_ = bstack11lll_opy_ (u"ࠩࡶࡨࡰࡀ࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾࡉ࡯࡯ࡨ࡬࡫ࠬ᢬")
  bstack1ll1l1l11l1_opy_ = bstack11lll_opy_ (u"ࠪࡷࡩࡱ࠺ࡢ࡫ࡖࡩࡱ࡬ࡈࡦࡣ࡯ࡗࡹ࡫ࡰࠨ᢭")
  bstack1ll1l11ll1l_opy_ = bstack11lll_opy_ (u"ࠫࡸࡪ࡫࠻ࡣ࡬ࡗࡪࡲࡦࡉࡧࡤࡰࡌ࡫ࡴࡓࡧࡶࡹࡱࡺࠧ᢮")
  bstack1ll111l1l11_opy_ = bstack11lll_opy_ (u"ࠬࡹࡤ࡬࠼ࡷࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࡇࡹࡩࡳࡺࠧ᢯")
  bstack1ll11lll11l_opy_ = bstack11lll_opy_ (u"࠭ࡳࡥ࡭࠽ࡸࡪࡹࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡆࡸࡨࡲࡹ࠭ᢰ")
  bstack1ll1111ll11_opy_ = bstack11lll_opy_ (u"ࠧࡴࡦ࡮࠾ࡨࡲࡩ࠻࡮ࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࡊࡼࡥ࡯ࡶࠪᢱ")
  bstack11lllllll1l_opy_ = bstack11lll_opy_ (u"ࠨࡵࡧ࡯࠿ࡩ࡬ࡪ࠼ࡨࡲࡶࡻࡥࡶࡧࡗࡩࡸࡺࡅࡷࡧࡱࡸࠬᢲ")
  bstack1l1ll111lll_opy_ = bstack11lll_opy_ (u"ࠩࡶࡨࡰࡀࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࡘࡺ࡯ࡱࠩᢳ")
  bstack11111l111l_opy_ = bstack11lll_opy_ (u"ࠪࡷࡩࡱ࠺ࡰࡰࡖࡸࡴࡶࠧᢴ")
class STAGE(Enum):
  bstack111ll11l_opy_ = bstack11lll_opy_ (u"ࠫࡸࡺࡡࡳࡶࠪᢵ")
  END = bstack11lll_opy_ (u"ࠬ࡫࡮ࡥࠩᢶ")
  bstack1lll1l1l11_opy_ = bstack11lll_opy_ (u"࠭ࡳࡪࡰࡪࡰࡪ࠭ᢷ")
bstack1ll11l1lll_opy_ = {
  bstack11lll_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚ࠧᢸ"): bstack11lll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨᢹ"),
  bstack11lll_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕ࠯ࡅࡈࡉ࠭ᢺ"): bstack11lll_opy_ (u"ࠪࡔࡾࡺࡥࡴࡶ࠰ࡧࡺࡩࡵ࡮ࡤࡨࡶࠬᢻ")
}
PLAYWRIGHT_HUB_URL = bstack11lll_opy_ (u"ࠦࡼࡹࡳ࠻࠱࠲ࡧࡩࡶ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠿ࡤࡣࡳࡷࡂࠨᢼ")