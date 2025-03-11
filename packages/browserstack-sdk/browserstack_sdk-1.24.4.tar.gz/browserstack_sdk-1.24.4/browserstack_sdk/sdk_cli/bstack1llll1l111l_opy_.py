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
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1lll1l1l1ll_opy_ import bstack1lll1l1111l_opy_
from browserstack_sdk.sdk_cli.bstack1111llll11_opy_ import (
    bstack111l1111ll_opy_,
    bstack1111ll11l1_opy_,
    bstack11111ll11l_opy_,
)
from bstack_utils.helper import  bstack11l1ll1l_opy_
from browserstack_sdk.sdk_cli.bstack111111l1l1_opy_ import bstack1llll111lll_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll1111ll_opy_, bstack1llllll11l1_opy_, bstack1llll1lll1l_opy_, bstack1lllllllll1_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack1l1l11ll1l_opy_ import bstack1llll111l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll1ll1_opy_ import bstack1lll1l111ll_opy_
from bstack_utils.percy import bstack1l1l11ll11_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1111111111_opy_(bstack1lll1l1111l_opy_):
    def __init__(self, bstack1l1lllllll1_opy_: Dict[str, str]):
        super().__init__()
        self.bstack1l1lllllll1_opy_ = bstack1l1lllllll1_opy_
        self.percy = bstack1l1l11ll11_opy_()
        self.bstack11l1111l1_opy_ = bstack1llll111l_opy_()
        self.bstack1l1llllllll_opy_()
        bstack1llll111lll_opy_.bstack1lll111l111_opy_((bstack111l1111ll_opy_.bstack1111l11ll1_opy_, bstack1111ll11l1_opy_.PRE), self.bstack1ll11111111_opy_)
        TestFramework.bstack1lll111l111_opy_((bstack1llll1111ll_opy_.TEST, bstack1llll1lll1l_opy_.POST), self.bstack1ll1lll11l1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1ll11l1lll1_opy_(self, instance: bstack11111ll11l_opy_, driver: object):
        bstack1ll11l1111l_opy_ = TestFramework.bstack1111l1ll1l_opy_(instance.context)
        for t in bstack1ll11l1111l_opy_:
            bstack1ll111ll1l1_opy_ = TestFramework.bstack1111lll1l1_opy_(t, bstack1lll1l111ll_opy_.bstack1ll11ll11ll_opy_, [])
            if any(instance is d[1] for d in bstack1ll111ll1l1_opy_) or instance == driver:
                return t
    def bstack1ll11111111_opy_(
        self,
        f: bstack1llll111lll_opy_,
        driver: object,
        exec: Tuple[bstack11111ll11l_opy_, str],
        bstack11111ll111_opy_: Tuple[bstack111l1111ll_opy_, bstack1111ll11l1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack1llll111lll_opy_.bstack1ll1l1llll1_opy_(method_name):
                return
            platform_index = f.bstack1111lll1l1_opy_(instance, bstack1llll111lll_opy_.bstack1lll111ll1l_opy_, 0)
            bstack1ll1111ll11_opy_ = self.bstack1ll11l1lll1_opy_(instance, driver)
            bstack1l1llllll11_opy_ = TestFramework.bstack1111lll1l1_opy_(bstack1ll1111ll11_opy_, TestFramework.bstack1ll1111111l_opy_, None)
            if not bstack1l1llllll11_opy_:
                self.logger.debug(bstack11ll1l_opy_ (u"ࠥࡳࡳࡥࡰࡳࡧࡢࡩࡽ࡫ࡣࡶࡶࡨ࠾ࠥࡸࡥࡵࡷࡵࡲ࡮ࡴࡧࠡࡣࡶࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥ࡯ࡳࠡࡰࡲࡸࠥࡿࡥࡵࠢࡶࡸࡦࡸࡴࡦࡦࠥᇐ"))
                return
            driver_command = f.bstack1lll11111l1_opy_(*args)
            for command in bstack11ll1111ll_opy_:
                if command == driver_command:
                    self.bstack11l11ll1_opy_(driver, platform_index)
            bstack11ll11llll_opy_ = self.percy.bstack11l11l1ll_opy_()
            if driver_command in bstack1111l1l1l_opy_[bstack11ll11llll_opy_]:
                self.bstack11l1111l1_opy_.bstack1l1l1lll1l_opy_(bstack1l1llllll11_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack11ll1l_opy_ (u"ࠦࡴࡴ࡟ࡱࡴࡨࡣࡪࡾࡥࡤࡷࡷࡩ࠿ࠦࡥࡳࡴࡲࡶࠧᇑ"), e)
    def bstack1ll1lll11l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1llllll11l1_opy_,
        bstack11111ll111_opy_: Tuple[bstack1llll1111ll_opy_, bstack1llll1lll1l_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack1ll11ll111_opy_ import bstack1lll11ll1l1_opy_
        bstack1ll111ll1l1_opy_ = f.bstack1111lll1l1_opy_(instance, bstack1lll1l111ll_opy_.bstack1ll11ll11ll_opy_, [])
        if not bstack1ll111ll1l1_opy_:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᇒ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠨࠢᇓ"))
            return
        if len(bstack1ll111ll1l1_opy_) > 1:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡽ࡯ࡩࡳ࠮ࡤࡳ࡫ࡹࡩࡷࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡴࠫࢀࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᇔ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠣࠤᇕ"))
        bstack1ll111111ll_opy_, bstack1ll11111l11_opy_ = bstack1ll111ll1l1_opy_[0]
        driver = bstack1ll111111ll_opy_()
        if not driver:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᇖ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠥࠦᇗ"))
            return
        bstack1ll11111lll_opy_ = {
            TestFramework.bstack1ll1ll1llll_opy_: bstack11ll1l_opy_ (u"ࠦࡹ࡫ࡳࡵࠢࡱࡥࡲ࡫ࠢᇘ"),
            TestFramework.bstack1ll1l1lll1l_opy_: bstack11ll1l_opy_ (u"ࠧࡺࡥࡴࡶࠣࡹࡺ࡯ࡤࠣᇙ"),
            TestFramework.bstack1ll1111111l_opy_: bstack11ll1l_opy_ (u"ࠨࡴࡦࡵࡷࠤࡷ࡫ࡲࡶࡰࠣࡲࡦࡳࡥࠣᇚ")
        }
        bstack1ll1111l111_opy_ = { key: f.bstack1111lll1l1_opy_(instance, key) for key in bstack1ll11111lll_opy_ }
        bstack1ll11111ll1_opy_ = [key for key, value in bstack1ll1111l111_opy_.items() if not value]
        if bstack1ll11111ll1_opy_:
            for key in bstack1ll11111ll1_opy_:
                self.logger.debug(bstack11ll1l_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࠥᇛ") + str(key) + bstack11ll1l_opy_ (u"ࠣࠤᇜ"))
            return
        platform_index = f.bstack1111lll1l1_opy_(instance, bstack1llll111lll_opy_.bstack1lll111ll1l_opy_, 0)
        if self.bstack1l1lllllll1_opy_.percy_capture_mode == bstack11ll1l_opy_ (u"ࠤࡷࡩࡸࡺࡣࡢࡵࡨࠦᇝ"):
            bstack1lllll1l11_opy_ = bstack1ll1111l111_opy_.get(TestFramework.bstack1ll1111111l_opy_) + bstack11ll1l_opy_ (u"ࠥ࠱ࡹ࡫ࡳࡵࡥࡤࡷࡪࠨᇞ")
            bstack1ll1ll11l11_opy_ = bstack1lll11ll1l1_opy_.bstack1ll1l1lll11_opy_(EVENTS.bstack1ll11111l1l_opy_.value)
            PercySDK.screenshot(
                driver,
                bstack1lllll1l11_opy_,
                bstack11111111_opy_=bstack1ll1111l111_opy_[TestFramework.bstack1ll1ll1llll_opy_],
                bstack1ll1ll111l_opy_=bstack1ll1111l111_opy_[TestFramework.bstack1ll1l1lll1l_opy_],
                bstack1ll1lllll_opy_=platform_index
            )
            bstack1lll11ll1l1_opy_.end(EVENTS.bstack1ll11111l1l_opy_.value, bstack1ll1ll11l11_opy_+bstack11ll1l_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᇟ"), bstack1ll1ll11l11_opy_+bstack11ll1l_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᇠ"), True, None, None, None, None, test_name=bstack1lllll1l11_opy_)
    def bstack11l11ll1_opy_(self, driver, platform_index):
        if self.bstack11l1111l1_opy_.bstack1ll1l1111_opy_() is True or self.bstack11l1111l1_opy_.capturing() is True:
            return
        self.bstack11l1111l1_opy_.bstack1ll1111l1_opy_()
        while not self.bstack11l1111l1_opy_.bstack1ll1l1111_opy_():
            bstack1l1llllll11_opy_ = self.bstack11l1111l1_opy_.bstack11l1lllll_opy_()
            self.bstack1lll111l11_opy_(driver, bstack1l1llllll11_opy_, platform_index)
        self.bstack11l1111l1_opy_.bstack1llll1llll_opy_()
    def bstack1lll111l11_opy_(self, driver, bstack1llll11l1l_opy_, platform_index, test=None):
        from bstack_utils.bstack1ll11ll111_opy_ import bstack1lll11ll1l1_opy_
        bstack1ll1ll11l11_opy_ = bstack1lll11ll1l1_opy_.bstack1ll1l1lll11_opy_(EVENTS.bstack1llll111ll_opy_.value)
        if test != None:
            bstack11111111_opy_ = getattr(test, bstack11ll1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᇡ"), None)
            bstack1ll1ll111l_opy_ = getattr(test, bstack11ll1l_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᇢ"), None)
            PercySDK.screenshot(driver, bstack1llll11l1l_opy_, bstack11111111_opy_=bstack11111111_opy_, bstack1ll1ll111l_opy_=bstack1ll1ll111l_opy_, bstack1ll1lllll_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack1llll11l1l_opy_)
        bstack1lll11ll1l1_opy_.end(EVENTS.bstack1llll111ll_opy_.value, bstack1ll1ll11l11_opy_+bstack11ll1l_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᇣ"), bstack1ll1ll11l11_opy_+bstack11ll1l_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᇤ"), True, None, None, None, None, test_name=bstack1llll11l1l_opy_)
    def bstack1l1llllllll_opy_(self):
        os.environ[bstack11ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡉࡗࡉ࡙ࠨᇥ")] = str(self.bstack1l1lllllll1_opy_.success)
        os.environ[bstack11ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡊࡘࡃ࡚ࡡࡆࡅࡕ࡚ࡕࡓࡇࡢࡑࡔࡊࡅࠨᇦ")] = str(self.bstack1l1lllllll1_opy_.percy_capture_mode)
        self.percy.bstack1l1llllll1l_opy_(self.bstack1l1lllllll1_opy_.is_percy_auto_enabled)
        self.percy.bstack1ll111111l1_opy_(self.bstack1l1lllllll1_opy_.percy_build_id)