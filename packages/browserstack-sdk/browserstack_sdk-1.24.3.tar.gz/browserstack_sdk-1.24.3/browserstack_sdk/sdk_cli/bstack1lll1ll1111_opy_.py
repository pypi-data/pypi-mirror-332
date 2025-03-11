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
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack111l111lll_opy_ import bstack111l11l1ll_opy_
from browserstack_sdk.sdk_cli.bstack11111l1lll_opy_ import (
    bstack1111l1l111_opy_,
    bstack1111ll111l_opy_,
    bstack1111l1llll_opy_,
)
from bstack_utils.helper import  bstack1l11lllll_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1ll1_opy_ import bstack111111l111_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1lll1ll_opy_, bstack1llll11lll1_opy_, bstack1lll1lll11l_opy_, bstack1lll11l1ll1_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack111llll1_opy_ import bstack1l1l11ll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1llll1l_opy_ import bstack1lllll11l1l_opy_
from bstack_utils.percy import bstack1ll1l111l_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1lll1llllll_opy_(bstack111l11l1ll_opy_):
    def __init__(self, bstack1l1llllll11_opy_: Dict[str, str]):
        super().__init__()
        self.bstack1l1llllll11_opy_ = bstack1l1llllll11_opy_
        self.percy = bstack1ll1l111l_opy_()
        self.bstack1lll111111_opy_ = bstack1l1l11ll1_opy_()
        self.bstack1l1lllll1l1_opy_()
        bstack111111l111_opy_.bstack1ll1l1lll1l_opy_((bstack1111l1l111_opy_.bstack1111ll1111_opy_, bstack1111ll111l_opy_.PRE), self.bstack1ll111111ll_opy_)
        TestFramework.bstack1ll1l1lll1l_opy_((bstack1lll1lll1ll_opy_.TEST, bstack1lll1lll11l_opy_.POST), self.bstack1lll111l11l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1ll11ll111l_opy_(self, instance: bstack1111l1llll_opy_, driver: object):
        bstack1ll111lll1l_opy_ = TestFramework.bstack1111ll1l1l_opy_(instance.context)
        for t in bstack1ll111lll1l_opy_:
            bstack1ll111ll111_opy_ = TestFramework.bstack11111l11l1_opy_(t, bstack1lllll11l1l_opy_.bstack1ll111lllll_opy_, [])
            if any(instance is d[1] for d in bstack1ll111ll111_opy_) or instance == driver:
                return t
    def bstack1ll111111ll_opy_(
        self,
        f: bstack111111l111_opy_,
        driver: object,
        exec: Tuple[bstack1111l1llll_opy_, str],
        bstack1111llll11_opy_: Tuple[bstack1111l1l111_opy_, bstack1111ll111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack111111l111_opy_.bstack1lll1111111_opy_(method_name):
                return
            platform_index = f.bstack11111l11l1_opy_(instance, bstack111111l111_opy_.bstack1ll1lll1111_opy_, 0)
            bstack1ll11lll1ll_opy_ = self.bstack1ll11ll111l_opy_(instance, driver)
            bstack1ll11111111_opy_ = TestFramework.bstack11111l11l1_opy_(bstack1ll11lll1ll_opy_, TestFramework.bstack1l1lllll1ll_opy_, None)
            if not bstack1ll11111111_opy_:
                self.logger.debug(bstack11lll_opy_ (u"ࠥࡳࡳࡥࡰࡳࡧࡢࡩࡽ࡫ࡣࡶࡶࡨ࠾ࠥࡸࡥࡵࡷࡵࡲ࡮ࡴࡧࠡࡣࡶࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥ࡯ࡳࠡࡰࡲࡸࠥࡿࡥࡵࠢࡶࡸࡦࡸࡴࡦࡦࠥᇐ"))
                return
            driver_command = f.bstack1ll1lllllll_opy_(*args)
            for command in bstack1l1lll111_opy_:
                if command == driver_command:
                    self.bstack1l1l1l111l_opy_(driver, platform_index)
            bstack1lll1111l_opy_ = self.percy.bstack11lll1lll1_opy_()
            if driver_command in bstack11l1l1111_opy_[bstack1lll1111l_opy_]:
                self.bstack1lll111111_opy_.bstack1l1l11ll1l_opy_(bstack1ll11111111_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack11lll_opy_ (u"ࠦࡴࡴ࡟ࡱࡴࡨࡣࡪࡾࡥࡤࡷࡷࡩ࠿ࠦࡥࡳࡴࡲࡶࠧᇑ"), e)
    def bstack1lll111l11l_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11lll1_opy_,
        bstack1111llll11_opy_: Tuple[bstack1lll1lll1ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack11l1lll1_opy_ import bstack1lll1ll1lll_opy_
        bstack1ll111ll111_opy_ = f.bstack11111l11l1_opy_(instance, bstack1lllll11l1l_opy_.bstack1ll111lllll_opy_, [])
        if not bstack1ll111ll111_opy_:
            self.logger.debug(bstack11lll_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᇒ") + str(kwargs) + bstack11lll_opy_ (u"ࠨࠢᇓ"))
            return
        if len(bstack1ll111ll111_opy_) > 1:
            self.logger.debug(bstack11lll_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡽ࡯ࡩࡳ࠮ࡤࡳ࡫ࡹࡩࡷࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡴࠫࢀࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᇔ") + str(kwargs) + bstack11lll_opy_ (u"ࠣࠤᇕ"))
        bstack1ll111111l1_opy_, bstack1l1llllll1l_opy_ = bstack1ll111ll111_opy_[0]
        driver = bstack1ll111111l1_opy_()
        if not driver:
            self.logger.debug(bstack11lll_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᇖ") + str(kwargs) + bstack11lll_opy_ (u"ࠥࠦᇗ"))
            return
        bstack1l1llllllll_opy_ = {
            TestFramework.bstack1ll1lll1l11_opy_: bstack11lll_opy_ (u"ࠦࡹ࡫ࡳࡵࠢࡱࡥࡲ࡫ࠢᇘ"),
            TestFramework.bstack1ll1llll1l1_opy_: bstack11lll_opy_ (u"ࠧࡺࡥࡴࡶࠣࡹࡺ࡯ࡤࠣᇙ"),
            TestFramework.bstack1l1lllll1ll_opy_: bstack11lll_opy_ (u"ࠨࡴࡦࡵࡷࠤࡷ࡫ࡲࡶࡰࠣࡲࡦࡳࡥࠣᇚ")
        }
        bstack1ll1111111l_opy_ = { key: f.bstack11111l11l1_opy_(instance, key) for key in bstack1l1llllllll_opy_ }
        bstack1ll11111l11_opy_ = [key for key, value in bstack1ll1111111l_opy_.items() if not value]
        if bstack1ll11111l11_opy_:
            for key in bstack1ll11111l11_opy_:
                self.logger.debug(bstack11lll_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࠥᇛ") + str(key) + bstack11lll_opy_ (u"ࠣࠤᇜ"))
            return
        platform_index = f.bstack11111l11l1_opy_(instance, bstack111111l111_opy_.bstack1ll1lll1111_opy_, 0)
        if self.bstack1l1llllll11_opy_.percy_capture_mode == bstack11lll_opy_ (u"ࠤࡷࡩࡸࡺࡣࡢࡵࡨࠦᇝ"):
            bstack1ll11l1l1_opy_ = bstack1ll1111111l_opy_.get(TestFramework.bstack1l1lllll1ll_opy_) + bstack11lll_opy_ (u"ࠥ࠱ࡹ࡫ࡳࡵࡥࡤࡷࡪࠨᇞ")
            bstack1ll1lll1l1l_opy_ = bstack1lll1ll1lll_opy_.bstack1lll111l111_opy_(EVENTS.bstack1ll11111ll1_opy_.value)
            PercySDK.screenshot(
                driver,
                bstack1ll11l1l1_opy_,
                bstack1l111ll1ll_opy_=bstack1ll1111111l_opy_[TestFramework.bstack1ll1lll1l11_opy_],
                bstack1l1lll111l_opy_=bstack1ll1111111l_opy_[TestFramework.bstack1ll1llll1l1_opy_],
                bstack111llll11_opy_=platform_index
            )
            bstack1lll1ll1lll_opy_.end(EVENTS.bstack1ll11111ll1_opy_.value, bstack1ll1lll1l1l_opy_+bstack11lll_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᇟ"), bstack1ll1lll1l1l_opy_+bstack11lll_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᇠ"), True, None, None, None, None, test_name=bstack1ll11l1l1_opy_)
    def bstack1l1l1l111l_opy_(self, driver, platform_index):
        if self.bstack1lll111111_opy_.bstack11ll1l1l_opy_() is True or self.bstack1lll111111_opy_.capturing() is True:
            return
        self.bstack1lll111111_opy_.bstack1111l1ll1_opy_()
        while not self.bstack1lll111111_opy_.bstack11ll1l1l_opy_():
            bstack1ll11111111_opy_ = self.bstack1lll111111_opy_.bstack1lllll1l11_opy_()
            self.bstack1l11111lll_opy_(driver, bstack1ll11111111_opy_, platform_index)
        self.bstack1lll111111_opy_.bstack1l1l1l11_opy_()
    def bstack1l11111lll_opy_(self, driver, bstack1l11lll1l_opy_, platform_index, test=None):
        from bstack_utils.bstack11l1lll1_opy_ import bstack1lll1ll1lll_opy_
        bstack1ll1lll1l1l_opy_ = bstack1lll1ll1lll_opy_.bstack1lll111l111_opy_(EVENTS.bstack11111l1l_opy_.value)
        if test != None:
            bstack1l111ll1ll_opy_ = getattr(test, bstack11lll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᇡ"), None)
            bstack1l1lll111l_opy_ = getattr(test, bstack11lll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᇢ"), None)
            PercySDK.screenshot(driver, bstack1l11lll1l_opy_, bstack1l111ll1ll_opy_=bstack1l111ll1ll_opy_, bstack1l1lll111l_opy_=bstack1l1lll111l_opy_, bstack111llll11_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack1l11lll1l_opy_)
        bstack1lll1ll1lll_opy_.end(EVENTS.bstack11111l1l_opy_.value, bstack1ll1lll1l1l_opy_+bstack11lll_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᇣ"), bstack1ll1lll1l1l_opy_+bstack11lll_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᇤ"), True, None, None, None, None, test_name=bstack1l11lll1l_opy_)
    def bstack1l1lllll1l1_opy_(self):
        os.environ[bstack11lll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡉࡗࡉ࡙ࠨᇥ")] = str(self.bstack1l1llllll11_opy_.success)
        os.environ[bstack11lll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡊࡘࡃ࡚ࡡࡆࡅࡕ࡚ࡕࡓࡇࡢࡑࡔࡊࡅࠨᇦ")] = str(self.bstack1l1llllll11_opy_.percy_capture_mode)
        self.percy.bstack1l1lllllll1_opy_(self.bstack1l1llllll11_opy_.is_percy_auto_enabled)
        self.percy.bstack1ll11111l1l_opy_(self.bstack1l1llllll11_opy_.percy_build_id)