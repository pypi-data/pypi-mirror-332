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
class RobotHandler():
    def __init__(self, args, logger, bstack111l1l1ll1_opy_, bstack111l1ll111_opy_):
        self.args = args
        self.logger = logger
        self.bstack111l1l1ll1_opy_ = bstack111l1l1ll1_opy_
        self.bstack111l1ll111_opy_ = bstack111l1ll111_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack111ll1111l_opy_(bstack111l11lll1_opy_):
        bstack111l11ll11_opy_ = []
        if bstack111l11lll1_opy_:
            tokens = str(os.path.basename(bstack111l11lll1_opy_)).split(bstack11ll1l_opy_ (u"ࠢࡠࠤ࿇"))
            camelcase_name = bstack11ll1l_opy_ (u"ࠣࠢࠥ࿈").join(t.title() for t in tokens)
            suite_name, bstack111l11llll_opy_ = os.path.splitext(camelcase_name)
            bstack111l11ll11_opy_.append(suite_name)
        return bstack111l11ll11_opy_
    @staticmethod
    def bstack111l11ll1l_opy_(typename):
        if bstack11ll1l_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࠧ࿉") in typename:
            return bstack11ll1l_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࡋࡲࡳࡱࡵࠦ࿊")
        return bstack11ll1l_opy_ (u"࡚ࠦࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠧ࿋")