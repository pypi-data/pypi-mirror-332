# coding: UTF-8
import sys
bstack1111ll1_opy_ = sys.version_info [0] == 2
bstack1ll11l_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11ll1l_opy_ (bstack111l1l1_opy_):
    global bstack1l111_opy_
    bstack1l1lll_opy_ = ord (bstack111l1l1_opy_ [-1])
    bstack1l1llll_opy_ = bstack111l1l1_opy_ [:-1]
    bstack1l11ll1_opy_ = bstack1l1lll_opy_ % len (bstack1l1llll_opy_)
    bstack1l11ll_opy_ = bstack1l1llll_opy_ [:bstack1l11ll1_opy_] + bstack1l1llll_opy_ [bstack1l11ll1_opy_:]
    if bstack1111ll1_opy_:
        bstack11l1111_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll11l_opy_ - (bstack111ll_opy_ + bstack1l1lll_opy_) % bstack11lllll_opy_) for bstack111ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack11l1111_opy_ = str () .join ([chr (ord (char) - bstack1ll11l_opy_ - (bstack111ll_opy_ + bstack1l1lll_opy_) % bstack11lllll_opy_) for bstack111ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack11l1111_opy_)
import os
import json
import logging
import datetime
import threading
from bstack_utils.helper import bstack1l111lll11l_opy_, bstack11l1l1ll1l_opy_, get_host_info, bstack11lll11l11l_opy_, \
 bstack11lll1ll11_opy_, bstack11l1ll1l_opy_, bstack111ll1l1ll_opy_, bstack11lll1l1lll_opy_, bstack1l1ll1111l_opy_
import bstack_utils.accessibility as bstack1lllll11ll_opy_
from bstack_utils.bstack11l1l1111l_opy_ import bstack111111ll_opy_
from bstack_utils.percy import bstack1l1l11ll11_opy_
from bstack_utils.config import Config
bstack1l1l11lll_opy_ = Config.bstack11l1lll11_opy_()
logger = logging.getLogger(__name__)
percy = bstack1l1l11ll11_opy_()
@bstack111ll1l1ll_opy_(class_method=False)
def bstack111lll1l1l1_opy_(bs_config, bstack1ll111l11l_opy_):
  try:
    data = {
        bstack11ll1l_opy_ (u"ࠬ࡬࡯ࡳ࡯ࡤࡸࠬᶷ"): bstack11ll1l_opy_ (u"࠭ࡪࡴࡱࡱࠫᶸ"),
        bstack11ll1l_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡠࡰࡤࡱࡪ࠭ᶹ"): bs_config.get(bstack11ll1l_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭ᶺ"), bstack11ll1l_opy_ (u"ࠩࠪᶻ")),
        bstack11ll1l_opy_ (u"ࠪࡲࡦࡳࡥࠨᶼ"): bs_config.get(bstack11ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧᶽ"), os.path.basename(os.path.abspath(os.getcwd()))),
        bstack11ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᶾ"): bs_config.get(bstack11ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᶿ")),
        bstack11ll1l_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬ᷀"): bs_config.get(bstack11ll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡄࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫ᷁"), bstack11ll1l_opy_ (u"᷂ࠩࠪ")),
        bstack11ll1l_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ᷃"): bstack1l1ll1111l_opy_(),
        bstack11ll1l_opy_ (u"ࠫࡹࡧࡧࡴࠩ᷄"): bstack11lll11l11l_opy_(bs_config),
        bstack11ll1l_opy_ (u"ࠬ࡮࡯ࡴࡶࡢ࡭ࡳ࡬࡯ࠨ᷅"): get_host_info(),
        bstack11ll1l_opy_ (u"࠭ࡣࡪࡡ࡬ࡲ࡫ࡵࠧ᷆"): bstack11l1l1ll1l_opy_(),
        bstack11ll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡲࡶࡰࡢ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ᷇"): os.environ.get(bstack11ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡗࡌࡐࡉࡥࡒࡖࡐࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧ᷈")),
        bstack11ll1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࡡࡷࡩࡸࡺࡳࡠࡴࡨࡶࡺࡴࠧ᷉"): os.environ.get(bstack11ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࠨ᷊"), False),
        bstack11ll1l_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࡤࡩ࡯࡯ࡶࡵࡳࡱ࠭᷋"): bstack1l111lll11l_opy_(),
        bstack11ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ᷌"): bstack111ll1l1111_opy_(),
        bstack11ll1l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡧࡩࡹࡧࡩ࡭ࡵࠪ᷍"): bstack111ll1l11l1_opy_(bstack1ll111l11l_opy_),
        bstack11ll1l_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࡠ࡯ࡤࡴ᷎ࠬ"): bstack1ll1l1llll_opy_(bs_config, bstack1ll111l11l_opy_.get(bstack11ll1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡺࡹࡥࡥ᷏ࠩ"), bstack11ll1l_opy_ (u"᷐ࠩࠪ"))),
        bstack11ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬ᷑"): bstack11lll1ll11_opy_(bs_config),
    }
    return data
  except Exception as error:
    logger.error(bstack11ll1l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡲࡤࡽࡱࡵࡡࡥࠢࡩࡳࡷࠦࡔࡦࡵࡷࡌࡺࡨ࠺ࠡࠢࡾࢁࠧ᷒").format(str(error)))
    return None
def bstack111ll1l11l1_opy_(framework):
  return {
    bstack11ll1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡏࡣࡰࡩࠬᷓ"): framework.get(bstack11ll1l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࠧᷔ"), bstack11ll1l_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺࠧᷕ")),
    bstack11ll1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮࡚ࡪࡸࡳࡪࡱࡱࠫᷖ"): framework.get(bstack11ll1l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ᷗ")),
    bstack11ll1l_opy_ (u"ࠪࡷࡩࡱࡖࡦࡴࡶ࡭ࡴࡴࠧᷘ"): framework.get(bstack11ll1l_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩᷙ")),
    bstack11ll1l_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫ࠧᷚ"): bstack11ll1l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ᷛ"),
    bstack11ll1l_opy_ (u"ࠧࡵࡧࡶࡸࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࠧᷜ"): framework.get(bstack11ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨᷝ"))
  }
def bstack1ll1l1llll_opy_(bs_config, framework):
  bstack11l111l11_opy_ = False
  bstack11ll1lll1_opy_ = False
  bstack111ll11ll11_opy_ = False
  if bstack11ll1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ᷞ") in bs_config:
    bstack111ll11ll11_opy_ = True
  elif bstack11ll1l_opy_ (u"ࠪࡥࡵࡶࠧᷟ") in bs_config:
    bstack11l111l11_opy_ = True
  else:
    bstack11ll1lll1_opy_ = True
  bstack1l1l11ll1_opy_ = {
    bstack11ll1l_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫᷠ"): bstack111111ll_opy_.bstack111ll11l11l_opy_(bs_config, framework),
    bstack11ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᷡ"): bstack1lllll11ll_opy_.bstack1l111lll1l1_opy_(bs_config),
    bstack11ll1l_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬᷢ"): bs_config.get(bstack11ll1l_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭ᷣ"), False),
    bstack11ll1l_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪᷤ"): bstack11ll1lll1_opy_,
    bstack11ll1l_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨᷥ"): bstack11l111l11_opy_,
    bstack11ll1l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫ࠧᷦ"): bstack111ll11ll11_opy_
  }
  return bstack1l1l11ll1_opy_
@bstack111ll1l1ll_opy_(class_method=False)
def bstack111ll1l1111_opy_():
  try:
    bstack111ll11llll_opy_ = json.loads(os.getenv(bstack11ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬᷧ"), bstack11ll1l_opy_ (u"ࠬࢁࡽࠨᷨ")))
    return {
        bstack11ll1l_opy_ (u"࠭ࡳࡦࡶࡷ࡭ࡳ࡭ࡳࠨᷩ"): bstack111ll11llll_opy_
    }
  except Exception as error:
    logger.error(bstack11ll1l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤ࡬࡫ࡴࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡵࡨࡸࡹ࡯࡮ࡨࡵࠣࡪࡴࡸࠠࡕࡧࡶࡸࡍࡻࡢ࠻ࠢࠣࡿࢂࠨᷪ").format(str(error)))
    return {}
def bstack111lll1l1ll_opy_(array, bstack111ll11l1l1_opy_, bstack111ll1l111l_opy_):
  result = {}
  for o in array:
    key = o[bstack111ll11l1l1_opy_]
    result[key] = o[bstack111ll1l111l_opy_]
  return result
def bstack111lll11ll1_opy_(bstack11111ll1_opy_=bstack11ll1l_opy_ (u"ࠨࠩᷫ")):
  bstack111ll11l111_opy_ = bstack1lllll11ll_opy_.on()
  bstack111ll11ll1l_opy_ = bstack111111ll_opy_.on()
  bstack111ll11lll1_opy_ = percy.bstack1l1l1l1l1_opy_()
  if bstack111ll11lll1_opy_ and not bstack111ll11ll1l_opy_ and not bstack111ll11l111_opy_:
    return bstack11111ll1_opy_ not in [bstack11ll1l_opy_ (u"ࠩࡆࡆ࡙࡙ࡥࡴࡵ࡬ࡳࡳࡉࡲࡦࡣࡷࡩࡩ࠭ᷬ"), bstack11ll1l_opy_ (u"ࠪࡐࡴ࡭ࡃࡳࡧࡤࡸࡪࡪࠧᷭ")]
  elif bstack111ll11l111_opy_ and not bstack111ll11ll1l_opy_:
    return bstack11111ll1_opy_ not in [bstack11ll1l_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬᷮ"), bstack11ll1l_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧᷯ"), bstack11ll1l_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪᷰ")]
  return bstack111ll11l111_opy_ or bstack111ll11ll1l_opy_ or bstack111ll11lll1_opy_
@bstack111ll1l1ll_opy_(class_method=False)
def bstack111lll1lll1_opy_(bstack11111ll1_opy_, test=None):
  bstack111ll11l1ll_opy_ = bstack1lllll11ll_opy_.on()
  if not bstack111ll11l1ll_opy_ or bstack11111ll1_opy_ not in [bstack11ll1l_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩᷱ")] or test == None:
    return None
  return {
    bstack11ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨᷲ"): bstack111ll11l1ll_opy_ and bstack11l1ll1l_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨᷳ"), None) == True and bstack1lllll11ll_opy_.bstack1lll1llll_opy_(test[bstack11ll1l_opy_ (u"ࠪࡸࡦ࡭ࡳࠨᷴ")])
  }