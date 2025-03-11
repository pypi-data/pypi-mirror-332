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
import threading
import logging
import bstack_utils.accessibility as bstack1ll11llll1_opy_
from bstack_utils.helper import bstack1l11lllll_opy_
logger = logging.getLogger(__name__)
def bstack1l1lll1111_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack11l1l1l1l_opy_(context, *args):
    tags = getattr(args[0], bstack11lll_opy_ (u"ࠫࡹࡧࡧࡴࠩᖂ"), [])
    bstack111l111l_opy_ = bstack1ll11llll1_opy_.bstack11l1l1lll_opy_(tags)
    threading.current_thread().isA11yTest = bstack111l111l_opy_
    try:
      bstack1l1ll11111_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1lll1111_opy_(bstack11lll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫᖃ")) else context.browser
      if bstack1l1ll11111_opy_ and bstack1l1ll11111_opy_.session_id and bstack111l111l_opy_ and bstack1l11lllll_opy_(
              threading.current_thread(), bstack11lll_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬᖄ"), None):
          threading.current_thread().isA11yTest = bstack1ll11llll1_opy_.bstack1l1l1llll1_opy_(bstack1l1ll11111_opy_, bstack111l111l_opy_)
    except Exception as e:
       logger.debug(bstack11lll_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡤ࠵࠶ࡿࠠࡪࡰࠣࡦࡪ࡮ࡡࡷࡧ࠽ࠤࢀࢃࠧᖅ").format(str(e)))
def bstack11lll1111_opy_(bstack1l1ll11111_opy_):
    if bstack1l11lllll_opy_(threading.current_thread(), bstack11lll_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬᖆ"), None) and bstack1l11lllll_opy_(
      threading.current_thread(), bstack11lll_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨᖇ"), None) and not bstack1l11lllll_opy_(threading.current_thread(), bstack11lll_opy_ (u"ࠪࡥ࠶࠷ࡹࡠࡵࡷࡳࡵ࠭ᖈ"), False):
      threading.current_thread().a11y_stop = True
      bstack1ll11llll1_opy_.bstack11lll111l_opy_(bstack1l1ll11111_opy_, name=bstack11lll_opy_ (u"ࠦࠧᖉ"), path=bstack11lll_opy_ (u"ࠧࠨᖊ"))