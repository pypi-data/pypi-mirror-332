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
import json
import requests
import logging
import threading
from urllib.parse import urlparse
from bstack_utils.constants import bstack1l111lll11l_opy_ as bstack1l11l111111_opy_, EVENTS
from bstack_utils.bstack11l11ll11_opy_ import bstack11l11ll11_opy_
from bstack_utils.helper import bstack11111lll1_opy_, bstack11l111ll1l_opy_, bstack1l1l1ll11l_opy_, bstack1l111llllll_opy_, \
  bstack1l111ll11ll_opy_, bstack1l1ll1l11l_opy_, get_host_info, bstack1l111lll1ll_opy_, bstack1l1l11l1l1_opy_, bstack11l111llll_opy_
from browserstack_sdk._version import __version__
from bstack_utils.bstack111l11ll_opy_ import get_logger
from bstack_utils.bstack11l1lll1_opy_ import bstack1lll1ll1lll_opy_
logger = get_logger(__name__)
bstack11l1lll1_opy_ = bstack1lll1ll1lll_opy_()
@bstack11l111llll_opy_(class_method=False)
def _1l111l1ll1l_opy_(driver, bstack111l1l11ll_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack11lll_opy_ (u"ࠬࡵࡳࡠࡰࡤࡱࡪ࠭ᒸ"): caps.get(bstack11lll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠬᒹ"), None),
        bstack11lll_opy_ (u"ࠧࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠫᒺ"): bstack111l1l11ll_opy_.get(bstack11lll_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫᒻ"), None),
        bstack11lll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡲࡦࡳࡥࠨᒼ"): caps.get(bstack11lll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨᒽ"), None),
        bstack11lll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ᒾ"): caps.get(bstack11lll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᒿ"), None)
    }
  except Exception as error:
    logger.debug(bstack11lll_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡬ࡥࡵࡥ࡫࡭ࡳ࡭ࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠢࡧࡩࡹࡧࡩ࡭ࡵࠣࡻ࡮ࡺࡨࠡࡧࡵࡶࡴࡸࠠ࠻ࠢࠪᓀ") + str(error))
  return response
def on():
    if os.environ.get(bstack11lll_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬᓁ"), None) is None or os.environ[bstack11lll_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ᓂ")] == bstack11lll_opy_ (u"ࠤࡱࡹࡱࡲࠢᓃ"):
        return False
    return True
def bstack1l111llll11_opy_(config):
  return config.get(bstack11lll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪᓄ"), False) or any([p.get(bstack11lll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᓅ"), False) == True for p in config.get(bstack11lll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨᓆ"), [])])
def bstack1llll1ll1_opy_(config, bstack11ll1l1l11_opy_):
  try:
    if not bstack1l1l1ll11l_opy_(config):
      return False
    bstack1l111l1l1ll_opy_ = config.get(bstack11lll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᓇ"), False)
    if int(bstack11ll1l1l11_opy_) < len(config.get(bstack11lll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪᓈ"), [])) and config[bstack11lll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫᓉ")][bstack11ll1l1l11_opy_]:
      bstack1l111lll1l1_opy_ = config[bstack11lll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬᓊ")][bstack11ll1l1l11_opy_].get(bstack11lll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪᓋ"), None)
    else:
      bstack1l111lll1l1_opy_ = config.get(bstack11lll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᓌ"), None)
    if bstack1l111lll1l1_opy_ != None:
      bstack1l111l1l1ll_opy_ = bstack1l111lll1l1_opy_
    bstack1l111ll111l_opy_ = os.getenv(bstack11lll_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪᓍ")) is not None and len(os.getenv(bstack11lll_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫᓎ"))) > 0 and os.getenv(bstack11lll_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬᓏ")) != bstack11lll_opy_ (u"ࠨࡰࡸࡰࡱ࠭ᓐ")
    return bstack1l111l1l1ll_opy_ and bstack1l111ll111l_opy_
  except Exception as error:
    logger.debug(bstack11lll_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡸࡨࡶ࡮࡬ࡹࡪࡰࡪࠤࡹ࡮ࡥࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡺ࡭ࡹ࡮ࠠࡦࡴࡵࡳࡷࠦ࠺ࠡࠩᓑ") + str(error))
  return False
def bstack11l1l1lll_opy_(test_tags):
  bstack1ll1ll1llll_opy_ = os.getenv(bstack11lll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫᓒ"))
  if bstack1ll1ll1llll_opy_ is None:
    return True
  bstack1ll1ll1llll_opy_ = json.loads(bstack1ll1ll1llll_opy_)
  try:
    include_tags = bstack1ll1ll1llll_opy_[bstack11lll_opy_ (u"ࠫ࡮ࡴࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩᓓ")] if bstack11lll_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪᓔ") in bstack1ll1ll1llll_opy_ and isinstance(bstack1ll1ll1llll_opy_[bstack11lll_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫᓕ")], list) else []
    exclude_tags = bstack1ll1ll1llll_opy_[bstack11lll_opy_ (u"ࠧࡦࡺࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬᓖ")] if bstack11lll_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ᓗ") in bstack1ll1ll1llll_opy_ and isinstance(bstack1ll1ll1llll_opy_[bstack11lll_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧᓘ")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack11lll_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡸࡤࡰ࡮ࡪࡡࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡨࡲࡶࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡨࡥࡧࡱࡵࡩࠥࡹࡣࡢࡰࡱ࡭ࡳ࡭࠮ࠡࡇࡵࡶࡴࡸࠠ࠻ࠢࠥᓙ") + str(error))
  return False
def bstack1l111l1l111_opy_(config, bstack1l111l1l1l1_opy_, bstack1l111ll11l1_opy_, bstack1l111l11lll_opy_):
  bstack1l111ll1ll1_opy_ = bstack1l111llllll_opy_(config)
  bstack1l111l1ll11_opy_ = bstack1l111ll11ll_opy_(config)
  if bstack1l111ll1ll1_opy_ is None or bstack1l111l1ll11_opy_ is None:
    logger.error(bstack11lll_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡲࡶࡰࠣࡪࡴࡸࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰ࠽ࠤࡒ࡯ࡳࡴ࡫ࡱ࡫ࠥࡧࡵࡵࡪࡨࡲࡹ࡯ࡣࡢࡶ࡬ࡳࡳࠦࡴࡰ࡭ࡨࡲࠬᓚ"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack11lll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭ᓛ"), bstack11lll_opy_ (u"࠭ࡻࡾࠩᓜ")))
    data = {
        bstack11lll_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬᓝ"): config[bstack11lll_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭ᓞ")],
        bstack11lll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬᓟ"): config.get(bstack11lll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ᓠ"), os.path.basename(os.getcwd())),
        bstack11lll_opy_ (u"ࠫࡸࡺࡡࡳࡶࡗ࡭ࡲ࡫ࠧᓡ"): bstack11111lll1_opy_(),
        bstack11lll_opy_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪᓢ"): config.get(bstack11lll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡉ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩᓣ"), bstack11lll_opy_ (u"ࠧࠨᓤ")),
        bstack11lll_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨᓥ"): {
            bstack11lll_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡓࡧ࡭ࡦࠩᓦ"): bstack1l111l1l1l1_opy_,
            bstack11lll_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᓧ"): bstack1l111ll11l1_opy_,
            bstack11lll_opy_ (u"ࠫࡸࡪ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨᓨ"): __version__,
            bstack11lll_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫ࠧᓩ"): bstack11lll_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ᓪ"),
            bstack11lll_opy_ (u"ࠧࡵࡧࡶࡸࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࠧᓫ"): bstack11lll_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯ࠪᓬ"),
            bstack11lll_opy_ (u"ࠩࡷࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩᓭ"): bstack1l111l11lll_opy_
        },
        bstack11lll_opy_ (u"ࠪࡷࡪࡺࡴࡪࡰࡪࡷࠬᓮ"): settings,
        bstack11lll_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࡈࡵ࡮ࡵࡴࡲࡰࠬᓯ"): bstack1l111lll1ll_opy_(),
        bstack11lll_opy_ (u"ࠬࡩࡩࡊࡰࡩࡳࠬᓰ"): bstack1l1ll1l11l_opy_(),
        bstack11lll_opy_ (u"࠭ࡨࡰࡵࡷࡍࡳ࡬࡯ࠨᓱ"): get_host_info(),
        bstack11lll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᓲ"): bstack1l1l1ll11l_opy_(config)
    }
    headers = {
        bstack11lll_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧᓳ"): bstack11lll_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬᓴ"),
    }
    config = {
        bstack11lll_opy_ (u"ࠪࡥࡺࡺࡨࠨᓵ"): (bstack1l111ll1ll1_opy_, bstack1l111l1ll11_opy_),
        bstack11lll_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬᓶ"): headers
    }
    response = bstack1l1l11l1l1_opy_(bstack11lll_opy_ (u"ࠬࡖࡏࡔࡖࠪᓷ"), bstack1l11l111111_opy_ + bstack11lll_opy_ (u"࠭࠯ࡷ࠴࠲ࡸࡪࡹࡴࡠࡴࡸࡲࡸ࠭ᓸ"), data, config)
    bstack1l111l1l11l_opy_ = response.json()
    if bstack1l111l1l11l_opy_[bstack11lll_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨᓹ")]:
      parsed = json.loads(os.getenv(bstack11lll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩᓺ"), bstack11lll_opy_ (u"ࠩࡾࢁࠬᓻ")))
      parsed[bstack11lll_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫᓼ")] = bstack1l111l1l11l_opy_[bstack11lll_opy_ (u"ࠫࡩࡧࡴࡢࠩᓽ")][bstack11lll_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᓾ")]
      os.environ[bstack11lll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧᓿ")] = json.dumps(parsed)
      bstack11l11ll11_opy_.bstack1l111l11ll1_opy_(bstack1l111l1l11l_opy_[bstack11lll_opy_ (u"ࠧࡥࡣࡷࡥࠬᔀ")][bstack11lll_opy_ (u"ࠨࡵࡦࡶ࡮ࡶࡴࡴࠩᔁ")])
      bstack11l11ll11_opy_.bstack1l111lllll1_opy_(bstack1l111l1l11l_opy_[bstack11lll_opy_ (u"ࠩࡧࡥࡹࡧࠧᔂ")][bstack11lll_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡷࠬᔃ")])
      bstack11l11ll11_opy_.store()
      return bstack1l111l1l11l_opy_[bstack11lll_opy_ (u"ࠫࡩࡧࡴࡢࠩᔄ")][bstack11lll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽ࡙ࡵ࡫ࡦࡰࠪᔅ")], bstack1l111l1l11l_opy_[bstack11lll_opy_ (u"࠭ࡤࡢࡶࡤࠫᔆ")][bstack11lll_opy_ (u"ࠧࡪࡦࠪᔇ")]
    else:
      logger.error(bstack11lll_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡶࡺࡴ࡮ࡪࡰࡪࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࠺ࠡࠩᔈ") + bstack1l111l1l11l_opy_[bstack11lll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᔉ")])
      if bstack1l111l1l11l_opy_[bstack11lll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᔊ")] == bstack11lll_opy_ (u"ࠫࡎࡴࡶࡢ࡮࡬ࡨࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠥࡶࡡࡴࡵࡨࡨ࠳࠭ᔋ"):
        for bstack1l111ll1l1l_opy_ in bstack1l111l1l11l_opy_[bstack11lll_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࡷࠬᔌ")]:
          logger.error(bstack1l111ll1l1l_opy_[bstack11lll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᔍ")])
      return None, None
  except Exception as error:
    logger.error(bstack11lll_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡵࡹࡳࠦࡦࡰࡴࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡀࠠࠣᔎ") +  str(error))
    return None, None
def bstack1l111llll1l_opy_():
  if os.getenv(bstack11lll_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ᔏ")) is None:
    return {
        bstack11lll_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᔐ"): bstack11lll_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩᔑ"),
        bstack11lll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᔒ"): bstack11lll_opy_ (u"ࠬࡈࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦࡨࡢࡦࠣࡪࡦ࡯࡬ࡦࡦ࠱ࠫᔓ")
    }
  data = {bstack11lll_opy_ (u"࠭ࡥ࡯ࡦࡗ࡭ࡲ࡫ࠧᔔ"): bstack11111lll1_opy_()}
  headers = {
      bstack11lll_opy_ (u"ࠧࡂࡷࡷ࡬ࡴࡸࡩࡻࡣࡷ࡭ࡴࡴࠧᔕ"): bstack11lll_opy_ (u"ࠨࡄࡨࡥࡷ࡫ࡲࠡࠩᔖ") + os.getenv(bstack11lll_opy_ (u"ࠤࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠢᔗ")),
      bstack11lll_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩᔘ"): bstack11lll_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧᔙ")
  }
  response = bstack1l1l11l1l1_opy_(bstack11lll_opy_ (u"ࠬࡖࡕࡕࠩᔚ"), bstack1l11l111111_opy_ + bstack11lll_opy_ (u"࠭࠯ࡵࡧࡶࡸࡤࡸࡵ࡯ࡵ࠲ࡷࡹࡵࡰࠨᔛ"), data, { bstack11lll_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨᔜ"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack11lll_opy_ (u"ࠣࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤ࡙࡫ࡳࡵࠢࡕࡹࡳࠦ࡭ࡢࡴ࡮ࡩࡩࠦࡡࡴࠢࡦࡳࡲࡶ࡬ࡦࡶࡨࡨࠥࡧࡴࠡࠤᔝ") + bstack11l111ll1l_opy_().isoformat() + bstack11lll_opy_ (u"ࠩ࡝ࠫᔞ"))
      return {bstack11lll_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪᔟ"): bstack11lll_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬᔠ"), bstack11lll_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᔡ"): bstack11lll_opy_ (u"࠭ࠧᔢ")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack11lll_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡰࡥࡷࡱࡩ࡯ࡩࠣࡧࡴࡳࡰ࡭ࡧࡷ࡭ࡴࡴࠠࡰࡨࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡔࡦࡵࡷࠤࡗࡻ࡮࠻ࠢࠥᔣ") + str(error))
    return {
        bstack11lll_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨᔤ"): bstack11lll_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᔥ"),
        bstack11lll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᔦ"): str(error)
    }
def bstack1l11l1lll_opy_(caps, options, desired_capabilities={}):
  try:
    bstack1ll1ll11l1l_opy_ = caps.get(bstack11lll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᔧ"), {}).get(bstack11lll_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠩᔨ"), caps.get(bstack11lll_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭ᔩ"), bstack11lll_opy_ (u"ࠧࠨᔪ")))
    if bstack1ll1ll11l1l_opy_:
      logger.warn(bstack11lll_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡆࡨࡷࡰࡺ࡯ࡱࠢࡥࡶࡴࡽࡳࡦࡴࡶ࠲ࠧᔫ"))
      return False
    if options:
      bstack1l111ll1lll_opy_ = options.to_capabilities()
    elif desired_capabilities:
      bstack1l111ll1lll_opy_ = desired_capabilities
    else:
      bstack1l111ll1lll_opy_ = {}
    browser = caps.get(bstack11lll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧᔬ"), bstack11lll_opy_ (u"ࠪࠫᔭ")).lower() or bstack1l111ll1lll_opy_.get(bstack11lll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩᔮ"), bstack11lll_opy_ (u"ࠬ࠭ᔯ")).lower()
    if browser != bstack11lll_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭ᔰ"):
      logger.warning(bstack11lll_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡵࡹࡳࠦ࡯࡯࡮ࡼࠤࡴࡴࠠࡄࡪࡵࡳࡲ࡫ࠠࡣࡴࡲࡻࡸ࡫ࡲࡴ࠰ࠥᔱ"))
      return False
    browser_version = caps.get(bstack11lll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᔲ")) or caps.get(bstack11lll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫᔳ")) or bstack1l111ll1lll_opy_.get(bstack11lll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫᔴ")) or bstack1l111ll1lll_opy_.get(bstack11lll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᔵ"), {}).get(bstack11lll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᔶ")) or bstack1l111ll1lll_opy_.get(bstack11lll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᔷ"), {}).get(bstack11lll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩᔸ"))
    if browser_version and browser_version != bstack11lll_opy_ (u"ࠨ࡮ࡤࡸࡪࡹࡴࠨᔹ") and int(browser_version.split(bstack11lll_opy_ (u"ࠩ࠱ࠫᔺ"))[0]) <= 98:
      logger.warning(bstack11lll_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡇ࡭ࡸ࡯࡮ࡧࠣࡦࡷࡵࡷࡴࡧࡵࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥ࡭ࡲࡦࡣࡷࡩࡷࠦࡴࡩࡣࡱࠤ࠾࠾࠮ࠣᔻ"))
      return False
    if not options:
      bstack1ll1lll111l_opy_ = caps.get(bstack11lll_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩᔼ")) or bstack1l111ll1lll_opy_.get(bstack11lll_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪᔽ"), {})
      if bstack11lll_opy_ (u"࠭࠭࠮ࡪࡨࡥࡩࡲࡥࡴࡵࠪᔾ") in bstack1ll1lll111l_opy_.get(bstack11lll_opy_ (u"ࠧࡢࡴࡪࡷࠬᔿ"), []):
        logger.warn(bstack11lll_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡲࡴࡺࠠࡳࡷࡱࠤࡴࡴࠠ࡭ࡧࡪࡥࡨࡿࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫࠮ࠡࡕࡺ࡭ࡹࡩࡨࠡࡶࡲࠤࡳ࡫ࡷࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥࠡࡱࡵࠤࡦࡼ࡯ࡪࡦࠣࡹࡸ࡯࡮ࡨࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠥᕀ"))
        return False
    return True
  except Exception as error:
    logger.debug(bstack11lll_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡸࡤࡰ࡮ࡪࡡࡵࡧࠣࡥ࠶࠷ࡹࠡࡵࡸࡴࡵࡵࡲࡵࠢ࠽ࠦᕁ") + str(error))
    return False
def set_capabilities(caps, config):
  try:
    bstack1lll11ll1ll_opy_ = config.get(bstack11lll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪᕂ"), {})
    bstack1lll11ll1ll_opy_[bstack11lll_opy_ (u"ࠫࡦࡻࡴࡩࡖࡲ࡯ࡪࡴࠧᕃ")] = os.getenv(bstack11lll_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪᕄ"))
    bstack1l111l1lll1_opy_ = json.loads(os.getenv(bstack11lll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧᕅ"), bstack11lll_opy_ (u"ࠧࡼࡿࠪᕆ"))).get(bstack11lll_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᕇ"))
    caps[bstack11lll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᕈ")] = True
    if bstack11lll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᕉ") in caps:
      caps[bstack11lll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᕊ")][bstack11lll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬᕋ")] = bstack1lll11ll1ll_opy_
      caps[bstack11lll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᕌ")][bstack11lll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᕍ")][bstack11lll_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᕎ")] = bstack1l111l1lll1_opy_
    else:
      caps[bstack11lll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨᕏ")] = bstack1lll11ll1ll_opy_
      caps[bstack11lll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩᕐ")][bstack11lll_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬᕑ")] = bstack1l111l1lll1_opy_
  except Exception as error:
    logger.debug(bstack11lll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶ࠲ࠥࡋࡲࡳࡱࡵ࠾ࠥࠨᕒ") +  str(error))
def bstack1l1l1llll1_opy_(driver, bstack1l111ll1l11_opy_):
  try:
    setattr(driver, bstack11lll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ࠭ᕓ"), True)
    session = driver.session_id
    if session:
      bstack1l111ll1111_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack1l111ll1111_opy_ = False
      bstack1l111ll1111_opy_ = url.scheme in [bstack11lll_opy_ (u"ࠢࡩࡶࡷࡴࠧᕔ"), bstack11lll_opy_ (u"ࠣࡪࡷࡸࡵࡹࠢᕕ")]
      if bstack1l111ll1111_opy_:
        if bstack1l111ll1l11_opy_:
          logger.info(bstack11lll_opy_ (u"ࠤࡖࡩࡹࡻࡰࠡࡨࡲࡶࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡺࡥࡴࡶ࡬ࡲ࡬ࠦࡨࡢࡵࠣࡷࡹࡧࡲࡵࡧࡧ࠲ࠥࡇࡵࡵࡱࡰࡥࡹ࡫ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡧ࡫ࡧࡪࡰࠣࡱࡴࡳࡥ࡯ࡶࡤࡶ࡮ࡲࡹ࠯ࠤᕖ"))
      return bstack1l111ll1l11_opy_
  except Exception as e:
    logger.error(bstack11lll_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡸࡦࡸࡴࡪࡰࡪࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡵࡦࡥࡳࠦࡦࡰࡴࠣࡸ࡭࡯ࡳࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨ࠾ࠥࠨᕗ") + str(e))
    return False
def bstack11lll111l_opy_(driver, name, path):
  try:
    bstack1lll111l1l1_opy_ = {
        bstack11lll_opy_ (u"ࠫࡹ࡮ࡔࡦࡵࡷࡖࡺࡴࡕࡶ࡫ࡧࠫᕘ"): threading.current_thread().current_test_uuid,
        bstack11lll_opy_ (u"ࠬࡺࡨࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪᕙ"): os.environ.get(bstack11lll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫᕚ"), bstack11lll_opy_ (u"ࠧࠨᕛ")),
        bstack11lll_opy_ (u"ࠨࡶ࡫ࡎࡼࡺࡔࡰ࡭ࡨࡲࠬᕜ"): os.environ.get(bstack11lll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ᕝ"), bstack11lll_opy_ (u"ࠪࠫᕞ"))
    }
    bstack1ll1lll1l1l_opy_ = bstack11l1lll1_opy_.bstack1lll111l111_opy_(EVENTS.bstack1l1lllll1l_opy_.value)
    logger.debug(bstack11lll_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡢࡦࡨࡲࡶࡪࠦࡳࡢࡸ࡬ࡲ࡬ࠦࡲࡦࡵࡸࡰࡹࡹࠧᕟ"))
    try:
      logger.debug(driver.execute_async_script(bstack11l11ll11_opy_.perform_scan, {bstack11lll_opy_ (u"ࠧࡳࡥࡵࡪࡲࡨࠧᕠ"): name}))
      bstack11l1lll1_opy_.end(EVENTS.bstack1l1lllll1l_opy_.value, bstack1ll1lll1l1l_opy_ + bstack11lll_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᕡ"), bstack1ll1lll1l1l_opy_ + bstack11lll_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᕢ"), True, None)
    except Exception as error:
      bstack11l1lll1_opy_.end(EVENTS.bstack1l1lllll1l_opy_.value, bstack1ll1lll1l1l_opy_ + bstack11lll_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᕣ"), bstack1ll1lll1l1l_opy_ + bstack11lll_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᕤ"), False, str(error))
    bstack1ll1lll1l1l_opy_ = bstack11l1lll1_opy_.bstack1l111lll111_opy_(EVENTS.bstack1ll1llll1ll_opy_.value)
    bstack11l1lll1_opy_.mark(bstack1ll1lll1l1l_opy_ + bstack11lll_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᕥ"))
    try:
      logger.debug(driver.execute_async_script(bstack11l11ll11_opy_.bstack1l111l1llll_opy_, bstack1lll111l1l1_opy_))
      bstack11l1lll1_opy_.end(bstack1ll1lll1l1l_opy_, bstack1ll1lll1l1l_opy_ + bstack11lll_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᕦ"), bstack1ll1lll1l1l_opy_ + bstack11lll_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᕧ"),True, None)
    except Exception as error:
      bstack11l1lll1_opy_.end(bstack1ll1lll1l1l_opy_, bstack1ll1lll1l1l_opy_ + bstack11lll_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᕨ"), bstack1ll1lll1l1l_opy_ + bstack11lll_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᕩ"),False, str(error))
    logger.info(bstack11lll_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡶࡨࡷࡹ࡯࡮ࡨࠢࡩࡳࡷࠦࡴࡩ࡫ࡶࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡩࡣࡶࠤࡪࡴࡤࡦࡦ࠱ࠦᕪ"))
  except Exception as bstack1ll1lllll11_opy_:
    logger.error(bstack11lll_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࡧࡴࡻ࡬ࡥࠢࡱࡳࡹࠦࡢࡦࠢࡳࡶࡴࡩࡥࡴࡵࡨࡨࠥ࡬࡯ࡳࠢࡷ࡬ࡪࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦ࠼ࠣࠦᕫ") + str(path) + bstack11lll_opy_ (u"ࠥࠤࡊࡸࡲࡰࡴࠣ࠾ࠧᕬ") + str(bstack1ll1lllll11_opy_))