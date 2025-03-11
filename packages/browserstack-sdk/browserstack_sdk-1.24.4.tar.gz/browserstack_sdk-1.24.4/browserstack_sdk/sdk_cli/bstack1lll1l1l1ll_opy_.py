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
import logging
import abc
from browserstack_sdk.sdk_cli.bstack111l11l11l_opy_ import bstack111l11l1l1_opy_
class bstack1lll1l1111l_opy_(abc.ABC):
    bin_session_id: str
    bstack111l11l11l_opy_: bstack111l11l1l1_opy_
    def __init__(self):
        self.bstack1lll11ll11l_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack111l11l11l_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack1lll1l111l1_opy_(self):
        return (self.bstack1lll11ll11l_opy_ != None and self.bin_session_id != None and self.bstack111l11l11l_opy_ != None)
    def configure(self, bstack1lll11ll11l_opy_, config, bin_session_id: str, bstack111l11l11l_opy_: bstack111l11l1l1_opy_):
        self.bstack1lll11ll11l_opy_ = bstack1lll11ll11l_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack111l11l11l_opy_ = bstack111l11l11l_opy_
        if self.bin_session_id:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡧࡴࡴࡦࡪࡩࡸࡶࡪࡪࠠ࡮ࡱࡧࡹࡱ࡫ࠠࡼࡵࡨࡰ࡫࠴࡟ࡠࡥ࡯ࡥࡸࡹ࡟ࡠ࠰ࡢࡣࡳࡧ࡭ࡦࡡࡢࢁ࠿ࠦࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪ࠽ࠣᅚ") + str(self.bin_session_id) + bstack11ll1l_opy_ (u"ࠧࠨᅛ"))
    def bstack1ll1ll1111l_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack11ll1l_opy_ (u"ࠨࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠠࡤࡣࡱࡲࡴࡺࠠࡣࡧࠣࡒࡴࡴࡥࠣᅜ"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False