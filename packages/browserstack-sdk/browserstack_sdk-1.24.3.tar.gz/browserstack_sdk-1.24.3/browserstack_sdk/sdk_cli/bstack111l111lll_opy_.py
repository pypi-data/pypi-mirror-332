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
import logging
import abc
from browserstack_sdk.sdk_cli.bstack111l11l111_opy_ import bstack111l111l1l_opy_
class bstack111l11l1ll_opy_(abc.ABC):
    bin_session_id: str
    bstack111l11l111_opy_: bstack111l111l1l_opy_
    def __init__(self):
        self.bstack111l11l1l1_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack111l11l111_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack111l111ll1_opy_(self):
        return (self.bstack111l11l1l1_opy_ != None and self.bin_session_id != None and self.bstack111l11l111_opy_ != None)
    def configure(self, bstack111l11l1l1_opy_, config, bin_session_id: str, bstack111l11l111_opy_: bstack111l111l1l_opy_):
        self.bstack111l11l1l1_opy_ = bstack111l11l1l1_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack111l11l111_opy_ = bstack111l11l111_opy_
        if self.bin_session_id:
            self.logger.debug(bstack11lll_opy_ (u"ࠧࡡࡻࡪࡦࠫࡷࡪࡲࡦࠪࡿࡠࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷ࡫ࡤࠡ࡯ࡲࡨࡺࡲࡥࠡࡽࡶࡩࡱ࡬࠮ࡠࡡࡦࡰࡦࡹࡳࡠࡡ࠱ࡣࡤࡴࡡ࡮ࡧࡢࡣࢂࡀࠠࡣ࡫ࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤ࠾ࠤ࿌") + str(self.bin_session_id) + bstack11lll_opy_ (u"ࠨࠢ࿍"))
    def bstack111l11l11l_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack11lll_opy_ (u"ࠢࡣ࡫ࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤࠡࡥࡤࡲࡳࡵࡴࠡࡤࡨࠤࡓࡵ࡮ࡦࠤ࿎"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False