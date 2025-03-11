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
import threading
import logging
import bstack_utils.accessibility as bstack1lllll11ll_opy_
from bstack_utils.helper import bstack11l1ll1l_opy_
logger = logging.getLogger(__name__)
def bstack1ll1ll1111_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack1ll111l1_opy_(context, *args):
    tags = getattr(args[0], bstack11ll1l_opy_ (u"ࠩࡷࡥ࡬ࡹࠧᕏ"), [])
    bstack11llll1l1_opy_ = bstack1lllll11ll_opy_.bstack1lll1llll_opy_(tags)
    threading.current_thread().isA11yTest = bstack11llll1l1_opy_
    try:
      bstack1llllll11_opy_ = threading.current_thread().bstackSessionDriver if bstack1ll1ll1111_opy_(bstack11ll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩᕐ")) else context.browser
      if bstack1llllll11_opy_ and bstack1llllll11_opy_.session_id and bstack11llll1l1_opy_ and bstack11l1ll1l_opy_(
              threading.current_thread(), bstack11ll1l_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪᕑ"), None):
          threading.current_thread().isA11yTest = bstack1lllll11ll_opy_.bstack1ll11ll11_opy_(bstack1llllll11_opy_, bstack11llll1l1_opy_)
    except Exception as e:
       logger.debug(bstack11ll1l_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡢ࠳࠴ࡽࠥ࡯࡮ࠡࡤࡨ࡬ࡦࡼࡥ࠻ࠢࡾࢁࠬᕒ").format(str(e)))
def bstack1l11ll1l_opy_(bstack1llllll11_opy_):
    if bstack11l1ll1l_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪᕓ"), None) and bstack11l1ll1l_opy_(
      threading.current_thread(), bstack11ll1l_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ᕔ"), None) and not bstack11l1ll1l_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠨࡣ࠴࠵ࡾࡥࡳࡵࡱࡳࠫᕕ"), False):
      threading.current_thread().a11y_stop = True
      bstack1lllll11ll_opy_.bstack111lll11l_opy_(bstack1llllll11_opy_, name=bstack11ll1l_opy_ (u"ࠤࠥᕖ"), path=bstack11ll1l_opy_ (u"ࠥࠦᕗ"))