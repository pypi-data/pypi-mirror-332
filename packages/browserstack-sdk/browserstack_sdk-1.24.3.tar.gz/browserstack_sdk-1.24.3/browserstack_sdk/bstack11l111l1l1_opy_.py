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
class RobotHandler():
    def __init__(self, args, logger, bstack111l1l11l1_opy_, bstack111l1lll1l_opy_):
        self.args = args
        self.logger = logger
        self.bstack111l1l11l1_opy_ = bstack111l1l11l1_opy_
        self.bstack111l1lll1l_opy_ = bstack111l1lll1l_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack111llll1ll_opy_(bstack111l11lll1_opy_):
        bstack111l11ll11_opy_ = []
        if bstack111l11lll1_opy_:
            tokens = str(os.path.basename(bstack111l11lll1_opy_)).split(bstack11lll_opy_ (u"ࠢࡠࠤ࿇"))
            camelcase_name = bstack11lll_opy_ (u"ࠣࠢࠥ࿈").join(t.title() for t in tokens)
            suite_name, bstack111l11llll_opy_ = os.path.splitext(camelcase_name)
            bstack111l11ll11_opy_.append(suite_name)
        return bstack111l11ll11_opy_
    @staticmethod
    def bstack111l11ll1l_opy_(typename):
        if bstack11lll_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࠧ࿉") in typename:
            return bstack11lll_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࡋࡲࡳࡱࡵࠦ࿊")
        return bstack11lll_opy_ (u"࡚ࠦࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠧ࿋")