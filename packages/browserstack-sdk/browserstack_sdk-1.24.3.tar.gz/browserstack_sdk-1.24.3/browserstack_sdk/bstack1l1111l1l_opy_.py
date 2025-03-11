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
import multiprocessing
import os
import json
from time import sleep
import bstack_utils.accessibility as bstack1ll11llll1_opy_
from browserstack_sdk.bstack11llll1l11_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack1l111l1lll_opy_
class bstack11l111ll_opy_:
    def __init__(self, args, logger, bstack111l1l11l1_opy_, bstack111l1lll1l_opy_):
        self.args = args
        self.logger = logger
        self.bstack111l1l11l1_opy_ = bstack111l1l11l1_opy_
        self.bstack111l1lll1l_opy_ = bstack111l1lll1l_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack1l11ll111l_opy_ = []
        self.bstack111l1ll1l1_opy_ = None
        self.bstack1l1lll1l11_opy_ = []
        self.bstack111l1l1ll1_opy_ = self.bstack11ll111111_opy_()
        self.bstack1ll1l1l11_opy_ = -1
    def bstack1111lll1_opy_(self, bstack111l1l1111_opy_):
        self.parse_args()
        self.bstack111l1ll111_opy_()
        self.bstack111l1l1lll_opy_(bstack111l1l1111_opy_)
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack111l1l1l1l_opy_():
        import importlib
        if getattr(importlib, bstack11lll_opy_ (u"ࠪࡪ࡮ࡴࡤࡠ࡮ࡲࡥࡩ࡫ࡲࠨྦྷ"), False):
            bstack111l1l1l11_opy_ = importlib.find_loader(bstack11lll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭ྨ"))
        else:
            bstack111l1l1l11_opy_ = importlib.util.find_spec(bstack11lll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧྩ"))
    def bstack111l1ll1ll_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack1ll1l1l11_opy_ = -1
        if self.bstack111l1lll1l_opy_ and bstack11lll_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭ྪ") in self.bstack111l1l11l1_opy_:
            self.bstack1ll1l1l11_opy_ = int(self.bstack111l1l11l1_opy_[bstack11lll_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧྫ")])
        try:
            bstack111l1llll1_opy_ = [bstack11lll_opy_ (u"ࠨ࠯࠰ࡨࡷ࡯ࡶࡦࡴࠪྫྷ"), bstack11lll_opy_ (u"ࠩ࠰࠱ࡵࡲࡵࡨ࡫ࡱࡷࠬྭ"), bstack11lll_opy_ (u"ࠪ࠱ࡵ࠭ྮ")]
            if self.bstack1ll1l1l11_opy_ >= 0:
                bstack111l1llll1_opy_.extend([bstack11lll_opy_ (u"ࠫ࠲࠳࡮ࡶ࡯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬྯ"), bstack11lll_opy_ (u"ࠬ࠳࡮ࠨྰ")])
            for arg in bstack111l1llll1_opy_:
                self.bstack111l1ll1ll_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack111l1ll111_opy_(self):
        bstack111l1ll1l1_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack111l1ll1l1_opy_ = bstack111l1ll1l1_opy_
        return bstack111l1ll1l1_opy_
    def bstack111111111_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack111l1l1l1l_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack1l111l1lll_opy_)
    def bstack111l1l1lll_opy_(self, bstack111l1l1111_opy_):
        bstack11lll111l1_opy_ = Config.bstack1ll1ll1l1l_opy_()
        if bstack111l1l1111_opy_:
            self.bstack111l1ll1l1_opy_.append(bstack11lll_opy_ (u"࠭࠭࠮ࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪྱ"))
            self.bstack111l1ll1l1_opy_.append(bstack11lll_opy_ (u"ࠧࡕࡴࡸࡩࠬྲ"))
        if bstack11lll111l1_opy_.bstack111l1l111l_opy_():
            self.bstack111l1ll1l1_opy_.append(bstack11lll_opy_ (u"ࠨ࠯࠰ࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧླ"))
            self.bstack111l1ll1l1_opy_.append(bstack11lll_opy_ (u"ࠩࡗࡶࡺ࡫ࠧྴ"))
        self.bstack111l1ll1l1_opy_.append(bstack11lll_opy_ (u"ࠪ࠱ࡵ࠭ྵ"))
        self.bstack111l1ll1l1_opy_.append(bstack11lll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡳࡰࡺ࡭ࡩ࡯ࠩྶ"))
        self.bstack111l1ll1l1_opy_.append(bstack11lll_opy_ (u"ࠬ࠳࠭ࡥࡴ࡬ࡺࡪࡸࠧྷ"))
        self.bstack111l1ll1l1_opy_.append(bstack11lll_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭ྸ"))
        if self.bstack1ll1l1l11_opy_ > 1:
            self.bstack111l1ll1l1_opy_.append(bstack11lll_opy_ (u"ࠧ࠮ࡰࠪྐྵ"))
            self.bstack111l1ll1l1_opy_.append(str(self.bstack1ll1l1l11_opy_))
    def bstack111l1lll11_opy_(self):
        bstack1l1lll1l11_opy_ = []
        for spec in self.bstack1l11ll111l_opy_:
            bstack1lll11l1_opy_ = [spec]
            bstack1lll11l1_opy_ += self.bstack111l1ll1l1_opy_
            bstack1l1lll1l11_opy_.append(bstack1lll11l1_opy_)
        self.bstack1l1lll1l11_opy_ = bstack1l1lll1l11_opy_
        return bstack1l1lll1l11_opy_
    def bstack11ll111111_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack111l1l1ll1_opy_ = True
            return True
        except Exception as e:
            self.bstack111l1l1ll1_opy_ = False
        return self.bstack111l1l1ll1_opy_
    def bstack11lll11l1l_opy_(self, bstack111l1ll11l_opy_, bstack1111lll1_opy_):
        bstack1111lll1_opy_[bstack11lll_opy_ (u"ࠨࡅࡒࡒࡋࡏࡇࠨྺ")] = self.bstack111l1l11l1_opy_
        multiprocessing.set_start_method(bstack11lll_opy_ (u"ࠩࡶࡴࡦࡽ࡮ࠨྻ"))
        bstack1llll11l11_opy_ = []
        manager = multiprocessing.Manager()
        bstack11111l1l1_opy_ = manager.list()
        if bstack11lll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ྼ") in self.bstack111l1l11l1_opy_:
            for index, platform in enumerate(self.bstack111l1l11l1_opy_[bstack11lll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ྽")]):
                bstack1llll11l11_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack111l1ll11l_opy_,
                                                            args=(self.bstack111l1ll1l1_opy_, bstack1111lll1_opy_, bstack11111l1l1_opy_)))
            bstack111ll11111_opy_ = len(self.bstack111l1l11l1_opy_[bstack11lll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ྾")])
        else:
            bstack1llll11l11_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack111l1ll11l_opy_,
                                                        args=(self.bstack111l1ll1l1_opy_, bstack1111lll1_opy_, bstack11111l1l1_opy_)))
            bstack111ll11111_opy_ = 1
        i = 0
        for t in bstack1llll11l11_opy_:
            os.environ[bstack11lll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭྿")] = str(i)
            if bstack11lll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ࿀") in self.bstack111l1l11l1_opy_:
                os.environ[bstack11lll_opy_ (u"ࠨࡅࡘࡖࡗࡋࡎࡕࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡉࡇࡔࡂࠩ࿁")] = json.dumps(self.bstack111l1l11l1_opy_[bstack11lll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ࿂")][i % bstack111ll11111_opy_])
            i += 1
            t.start()
        for t in bstack1llll11l11_opy_:
            t.join()
        return list(bstack11111l1l1_opy_)
    @staticmethod
    def bstack1l1ll1ll1l_opy_(driver, bstack111l1l11ll_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack11lll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧ࿃"), None)
        if item and getattr(item, bstack11lll_opy_ (u"ࠫࡤࡧ࠱࠲ࡻࡢࡸࡪࡹࡴࡠࡥࡤࡷࡪ࠭࿄"), None) and not getattr(item, bstack11lll_opy_ (u"ࠬࡥࡡ࠲࠳ࡼࡣࡸࡺ࡯ࡱࡡࡧࡳࡳ࡫ࠧ࿅"), False):
            logger.info(
                bstack11lll_opy_ (u"ࠨࡁࡶࡶࡲࡱࡦࡺࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤࡪࡾࡥࡤࡷࡷ࡭ࡴࡴࠠࡩࡣࡶࠤࡪࡴࡤࡦࡦ࠱ࠤࡕࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡨࡲࡶࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡺࡥࡴࡶ࡬ࡲ࡬ࠦࡩࡴࠢࡸࡲࡩ࡫ࡲࡸࡣࡼ࠲࿆ࠧ"))
            bstack111l1lllll_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack1ll11llll1_opy_.bstack11lll111l_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)