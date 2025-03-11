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
import threading
from bstack_utils.helper import bstack1l1ll1llll_opy_
from bstack_utils.constants import bstack1l11111l1ll_opy_, EVENTS, STAGE
from bstack_utils.bstack111l11ll_opy_ import get_logger
logger = get_logger(__name__)
class bstack11l1ll1l1_opy_:
    bstack11l1111l11l_opy_ = None
    @classmethod
    def bstack11ll11l1_opy_(cls):
        if cls.on() and os.getenv(bstack11lll_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠤ᷵")):
            logger.info(
                bstack11lll_opy_ (u"ࠬ࡜ࡩࡴ࡫ࡷࠤ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀࠤࡹࡵࠠࡷ࡫ࡨࡻࠥࡨࡵࡪ࡮ࡧࠤࡷ࡫ࡰࡰࡴࡷ࠰ࠥ࡯࡮ࡴ࡫ࡪ࡬ࡹࡹࠬࠡࡣࡱࡨࠥࡳࡡ࡯ࡻࠣࡱࡴࡸࡥࠡࡦࡨࡦࡺ࡭ࡧࡪࡰࡪࠤ࡮ࡴࡦࡰࡴࡰࡥࡹ࡯࡯࡯ࠢࡤࡰࡱࠦࡡࡵࠢࡲࡲࡪࠦࡰ࡭ࡣࡦࡩࠦࡢ࡮ࠨ᷶").format(os.getenv(bstack11lll_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇ᷷ࠦ"))))
    @classmethod
    def on(cls):
        if os.environ.get(bstack11lll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗ᷸ࠫ"), None) is None or os.environ[bstack11lll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘ᷹ࠬ")] == bstack11lll_opy_ (u"ࠤࡱࡹࡱࡲ᷺ࠢ"):
            return False
        return True
    @classmethod
    def bstack111ll11l1ll_opy_(cls, bs_config, framework=bstack11lll_opy_ (u"ࠥࠦ᷻")):
        bstack1l1111ll1l1_opy_ = False
        for fw in bstack1l11111l1ll_opy_:
            if fw in framework:
                bstack1l1111ll1l1_opy_ = True
        return bstack1l1ll1llll_opy_(bs_config.get(bstack11lll_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ᷼"), bstack1l1111ll1l1_opy_))
    @classmethod
    def bstack111ll111l1l_opy_(cls, framework):
        return framework in bstack1l11111l1ll_opy_
    @classmethod
    def bstack111lll11l11_opy_(cls, bs_config, framework):
        return cls.bstack111ll11l1ll_opy_(bs_config, framework) is True and cls.bstack111ll111l1l_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack11lll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥ᷽ࠩ"), None)
    @staticmethod
    def bstack11l11l1l11_opy_():
        if getattr(threading.current_thread(), bstack11lll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪ᷾"), None):
            return {
                bstack11lll_opy_ (u"ࠧࡵࡻࡳࡩ᷿ࠬ"): bstack11lll_opy_ (u"ࠨࡶࡨࡷࡹ࠭Ḁ"),
                bstack11lll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩḁ"): getattr(threading.current_thread(), bstack11lll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧḂ"), None)
            }
        if getattr(threading.current_thread(), bstack11lll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨḃ"), None):
            return {
                bstack11lll_opy_ (u"ࠬࡺࡹࡱࡧࠪḄ"): bstack11lll_opy_ (u"࠭ࡨࡰࡱ࡮ࠫḅ"),
                bstack11lll_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧḆ"): getattr(threading.current_thread(), bstack11lll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬḇ"), None)
            }
        return None
    @staticmethod
    def bstack111ll111l11_opy_(func):
        def wrap(*args, **kwargs):
            if bstack11l1ll1l1_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack111llll1ll_opy_(test, hook_name=None):
        bstack111ll1111ll_opy_ = test.parent
        if hook_name in [bstack11lll_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠧḈ"), bstack11lll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫḉ"), bstack11lll_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࠪḊ"), bstack11lll_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫ࠧḋ")]:
            bstack111ll1111ll_opy_ = test
        scope = []
        while bstack111ll1111ll_opy_ is not None:
            scope.append(bstack111ll1111ll_opy_.name)
            bstack111ll1111ll_opy_ = bstack111ll1111ll_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack111ll1111l1_opy_(hook_type):
        if hook_type == bstack11lll_opy_ (u"ࠨࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠦḌ"):
            return bstack11lll_opy_ (u"ࠢࡔࡧࡷࡹࡵࠦࡨࡰࡱ࡮ࠦḍ")
        elif hook_type == bstack11lll_opy_ (u"ࠣࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠧḎ"):
            return bstack11lll_opy_ (u"ࠤࡗࡩࡦࡸࡤࡰࡹࡱࠤ࡭ࡵ࡯࡬ࠤḏ")
    @staticmethod
    def bstack111ll11111l_opy_(bstack1l11ll111l_opy_):
        try:
            if not bstack11l1ll1l1_opy_.on():
                return bstack1l11ll111l_opy_
            if os.environ.get(bstack11lll_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࠣḐ"), None) == bstack11lll_opy_ (u"ࠦࡹࡸࡵࡦࠤḑ"):
                tests = os.environ.get(bstack11lll_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࡢࡘࡊ࡙ࡔࡔࠤḒ"), None)
                if tests is None or tests == bstack11lll_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦḓ"):
                    return bstack1l11ll111l_opy_
                bstack1l11ll111l_opy_ = tests.split(bstack11lll_opy_ (u"ࠧ࠭ࠩḔ"))
                return bstack1l11ll111l_opy_
        except Exception as exc:
            logger.debug(bstack11lll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡳࡧࡵࡹࡳࠦࡨࡢࡰࡧࡰࡪࡸ࠺ࠡࠤḕ") + str(str(exc)) + bstack11lll_opy_ (u"ࠤࠥḖ"))
        return bstack1l11ll111l_opy_