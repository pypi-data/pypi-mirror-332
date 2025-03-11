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
from datetime import datetime, timezone
import os
from typing import Any, Tuple, Callable, List
from browserstack_sdk.sdk_cli.bstack11111l1lll_opy_ import bstack1111l1llll_opy_, bstack1111l1l111_opy_, bstack1111ll111l_opy_
from browserstack_sdk.sdk_cli.bstack111l111lll_opy_ import bstack111l11l1ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1llll1l_opy_ import bstack1lllll11l1l_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1ll1_opy_ import bstack111111l111_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1lll1ll_opy_, bstack1llll11lll1_opy_, bstack1lll1lll11l_opy_, bstack1lll11l1ll1_opy_
from json import dumps, JSONEncoder
import grpc
from browserstack_sdk import sdk_pb2 as structs
import sys
import traceback
import time
import json
from bstack_utils.helper import bstack1ll1111llll_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
bstack1ll11lllll1_opy_ = [bstack11lll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᅫ"), bstack11lll_opy_ (u"ࠣࡲࡤࡶࡪࡴࡴࠣᅬ"), bstack11lll_opy_ (u"ࠤࡦࡳࡳ࡬ࡩࡨࠤᅭ"), bstack11lll_opy_ (u"ࠥࡷࡪࡹࡳࡪࡱࡱࠦᅮ"), bstack11lll_opy_ (u"ࠦࡵࡧࡴࡩࠤᅯ")]
bstack1ll111l1ll1_opy_ = {
    bstack11lll_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡶࡹࡵࡪࡲࡲ࠳ࡏࡴࡦ࡯ࠥᅰ"): bstack1ll11lllll1_opy_,
    bstack11lll_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴ࡰࡺࡶ࡫ࡳࡳ࠴ࡐࡢࡥ࡮ࡥ࡬࡫ࠢᅱ"): bstack1ll11lllll1_opy_,
    bstack11lll_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮ࡱࡻࡷ࡬ࡴࡴ࠮ࡎࡱࡧࡹࡱ࡫ࠢᅲ"): bstack1ll11lllll1_opy_,
    bstack11lll_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯ࡲࡼࡸ࡭ࡵ࡮࠯ࡅ࡯ࡥࡸࡹࠢᅳ"): bstack1ll11lllll1_opy_,
    bstack11lll_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡳࡽࡹ࡮࡯࡯࠰ࡉࡹࡳࡩࡴࡪࡱࡱࠦᅴ"): bstack1ll11lllll1_opy_
    + [
        bstack11lll_opy_ (u"ࠥࡳࡷ࡯ࡧࡪࡰࡤࡰࡳࡧ࡭ࡦࠤᅵ"),
        bstack11lll_opy_ (u"ࠦࡰ࡫ࡹࡸࡱࡵࡨࡸࠨᅶ"),
        bstack11lll_opy_ (u"ࠧ࡬ࡩࡹࡶࡸࡶࡪ࡯࡮ࡧࡱࠥᅷ"),
        bstack11lll_opy_ (u"ࠨ࡫ࡦࡻࡺࡳࡷࡪࡳࠣᅸ"),
        bstack11lll_opy_ (u"ࠢࡤࡣ࡯ࡰࡸࡶࡥࡤࠤᅹ"),
        bstack11lll_opy_ (u"ࠣࡥࡤࡰࡱࡵࡢ࡫ࠤᅺ"),
        bstack11lll_opy_ (u"ࠤࡶࡸࡦࡸࡴࠣᅻ"),
        bstack11lll_opy_ (u"ࠥࡷࡹࡵࡰࠣᅼ"),
        bstack11lll_opy_ (u"ࠦࡩࡻࡲࡢࡶ࡬ࡳࡳࠨᅽ"),
        bstack11lll_opy_ (u"ࠧࡽࡨࡦࡰࠥᅾ"),
    ],
    bstack11lll_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴࡭ࡢ࡫ࡱ࠲ࡘ࡫ࡳࡴ࡫ࡲࡲࠧᅿ"): [bstack11lll_opy_ (u"ࠢࡴࡶࡤࡶࡹࡶࡡࡵࡪࠥᆀ"), bstack11lll_opy_ (u"ࠣࡶࡨࡷࡹࡹࡦࡢ࡫࡯ࡩࡩࠨᆁ"), bstack11lll_opy_ (u"ࠤࡷࡩࡸࡺࡳࡤࡱ࡯ࡰࡪࡩࡴࡦࡦࠥᆂ"), bstack11lll_opy_ (u"ࠥ࡭ࡹ࡫࡭ࡴࠤᆃ")],
    bstack11lll_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡨࡵ࡮ࡧ࡫ࡪ࠲ࡈࡵ࡮ࡧ࡫ࡪࠦᆄ"): [bstack11lll_opy_ (u"ࠧ࡯࡮ࡷࡱࡦࡥࡹ࡯࡯࡯ࡡࡳࡥࡷࡧ࡭ࡴࠤᆅ"), bstack11lll_opy_ (u"ࠨࡡࡳࡩࡶࠦᆆ")],
    bstack11lll_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮ࡧ࡫ࡻࡸࡺࡸࡥࡴ࠰ࡉ࡭ࡽࡺࡵࡳࡧࡇࡩ࡫ࠨᆇ"): [bstack11lll_opy_ (u"ࠣࡵࡦࡳࡵ࡫ࠢᆈ"), bstack11lll_opy_ (u"ࠤࡤࡶ࡬ࡴࡡ࡮ࡧࠥᆉ"), bstack11lll_opy_ (u"ࠥࡪࡺࡴࡣࠣᆊ"), bstack11lll_opy_ (u"ࠦࡵࡧࡲࡢ࡯ࡶࠦᆋ"), bstack11lll_opy_ (u"ࠧࡻ࡮ࡪࡶࡷࡩࡸࡺࠢᆌ"), bstack11lll_opy_ (u"ࠨࡩࡥࡵࠥᆍ")],
    bstack11lll_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮ࡧ࡫ࡻࡸࡺࡸࡥࡴ࠰ࡖࡹࡧࡘࡥࡲࡷࡨࡷࡹࠨᆎ"): [bstack11lll_opy_ (u"ࠣࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࠨᆏ"), bstack11lll_opy_ (u"ࠤࡳࡥࡷࡧ࡭ࠣᆐ"), bstack11lll_opy_ (u"ࠥࡴࡦࡸࡡ࡮ࡡ࡬ࡲࡩ࡫ࡸࠣᆑ")],
    bstack11lll_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡷࡻ࡮࡯ࡧࡵ࠲ࡈࡧ࡬࡭ࡋࡱࡪࡴࠨᆒ"): [bstack11lll_opy_ (u"ࠧࡽࡨࡦࡰࠥᆓ"), bstack11lll_opy_ (u"ࠨࡲࡦࡵࡸࡰࡹࠨᆔ")],
    bstack11lll_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮࡮ࡣࡵ࡯࠳ࡹࡴࡳࡷࡦࡸࡺࡸࡥࡴ࠰ࡑࡳࡩ࡫ࡋࡦࡻࡺࡳࡷࡪࡳࠣᆕ"): [bstack11lll_opy_ (u"ࠣࡰࡲࡨࡪࠨᆖ"), bstack11lll_opy_ (u"ࠤࡳࡥࡷ࡫࡮ࡵࠤᆗ")],
    bstack11lll_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡱࡦࡸ࡫࠯ࡵࡷࡶࡺࡩࡴࡶࡴࡨࡷ࠳ࡓࡡࡳ࡭ࠥᆘ"): [bstack11lll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᆙ"), bstack11lll_opy_ (u"ࠧࡧࡲࡨࡵࠥᆚ"), bstack11lll_opy_ (u"ࠨ࡫ࡸࡣࡵ࡫ࡸࠨᆛ")],
}
class bstack1lll1l111ll_opy_(bstack111l11l1ll_opy_):
    bstack1ll111lll11_opy_ = bstack11lll_opy_ (u"ࠢࡵࡧࡶࡸࡤࡪࡥࡧࡧࡵࡶࡪࡪࠢᆜ")
    bstack1ll11l1llll_opy_ = bstack11lll_opy_ (u"ࠣࡋࡑࡊࡔࠨᆝ")
    bstack1ll111l11ll_opy_ = bstack11lll_opy_ (u"ࠤࡈࡖࡗࡕࡒࠣᆞ")
    bstack1ll11llll11_opy_: Callable
    bstack1ll11ll11l1_opy_: Callable
    def __init__(self, bstack1lllllllll1_opy_, bstack1llllll1ll1_opy_):
        super().__init__()
        self.bstack1ll1ll1ll1l_opy_ = bstack1llllll1ll1_opy_
        if os.getenv(bstack11lll_opy_ (u"ࠥࡗࡉࡑ࡟ࡄࡎࡌࡣࡋࡒࡁࡈࡡࡒ࠵࠶࡟ࠢᆟ"), bstack11lll_opy_ (u"ࠦ࠶ࠨᆠ")) != bstack11lll_opy_ (u"ࠧ࠷ࠢᆡ") or not self.is_enabled():
            self.logger.warning(bstack11lll_opy_ (u"ࠨࠢᆢ") + str(self.__class__.__name__) + bstack11lll_opy_ (u"ࠢࠡࡦ࡬ࡷࡦࡨ࡬ࡦࡦࠥᆣ"))
            return
        TestFramework.bstack1ll1l1lll1l_opy_((bstack1lll1lll1ll_opy_.TEST, bstack1lll1lll11l_opy_.PRE), self.bstack1ll1lll1lll_opy_)
        TestFramework.bstack1ll1l1lll1l_opy_((bstack1lll1lll1ll_opy_.TEST, bstack1lll1lll11l_opy_.POST), self.bstack1lll111l11l_opy_)
        for event in bstack1lll1lll1ll_opy_:
            for state in bstack1lll1lll11l_opy_:
                TestFramework.bstack1ll1l1lll1l_opy_((event, state), self.bstack1ll111ll1ll_opy_)
        bstack1lllllllll1_opy_.bstack1ll1l1lll1l_opy_((bstack1111l1l111_opy_.bstack1111ll1111_opy_, bstack1111ll111l_opy_.POST), self.bstack1ll11ll1ll1_opy_)
        self.bstack1ll11llll11_opy_ = sys.stdout.write
        sys.stdout.write = self.bstack1ll11l1111l_opy_(bstack1lll1l111ll_opy_.bstack1ll11l1llll_opy_, self.bstack1ll11llll11_opy_)
        self.bstack1ll11ll11l1_opy_ = sys.stderr.write
        sys.stderr.write = self.bstack1ll11l1111l_opy_(bstack1lll1l111ll_opy_.bstack1ll111l11ll_opy_, self.bstack1ll11ll11l1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1ll111ll1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11lll1_opy_,
        bstack1111llll11_opy_: Tuple[bstack1lll1lll1ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        if f.bstack1ll11111lll_opy_() and instance:
            bstack1ll11lll111_opy_ = datetime.now()
            test_framework_state, test_hook_state = bstack1111llll11_opy_
            if test_framework_state == bstack1lll1lll1ll_opy_.SETUP_FIXTURE:
                return
            elif test_framework_state == bstack1lll1lll1ll_opy_.LOG:
                bstack11lll1l11l_opy_ = datetime.now()
                entries = f.bstack1ll11ll1lll_opy_(instance, bstack1111llll11_opy_)
                if entries:
                    self.bstack1ll11l1ll11_opy_(instance, entries)
                    instance.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡦࡰࡧࡣࡱࡵࡧࡠࡥࡵࡩࡦࡺࡥࡥࡡࡨࡺࡪࡴࡴࠣᆤ"), datetime.now() - bstack11lll1l11l_opy_)
                    f.bstack1ll111l111l_opy_(instance, bstack1111llll11_opy_)
                instance.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠤࡲ࠵࠶ࡿ࠺ࡰࡰࡢࡥࡱࡲ࡟ࡵࡧࡶࡸࡤ࡫ࡶࡦࡰࡷࡷࠧᆥ"), datetime.now() - bstack1ll11lll111_opy_)
                return # do not send this event with the bstack1ll1111l1ll_opy_ bstack1ll11lll1l1_opy_
            elif (
                test_framework_state == bstack1lll1lll1ll_opy_.TEST
                and test_hook_state == bstack1lll1lll11l_opy_.POST
                and not f.bstack1111ll1l11_opy_(instance, TestFramework.bstack1ll11ll1l1l_opy_)
            ):
                self.logger.warning(bstack11lll_opy_ (u"ࠥࡨࡷࡵࡰࡱ࡫ࡱ࡫ࠥࡪࡵࡦࠢࡷࡳࠥࡲࡡࡤ࡭ࠣࡳ࡫ࠦࡲࡦࡵࡸࡰࡹࡹࠠࠣᆦ") + str(TestFramework.bstack1111ll1l11_opy_(instance, TestFramework.bstack1ll11ll1l1l_opy_)) + bstack11lll_opy_ (u"ࠦࠧᆧ"))
                f.bstack1111ll11ll_opy_(instance, bstack1lll1l111ll_opy_.bstack1ll111lll11_opy_, True)
                return # do not send this event bstack1ll11llll1l_opy_ bstack1ll111l1lll_opy_
            elif (
                f.bstack11111l11l1_opy_(instance, bstack1lll1l111ll_opy_.bstack1ll111lll11_opy_, False)
                and test_framework_state == bstack1lll1lll1ll_opy_.LOG_REPORT
                and test_hook_state == bstack1lll1lll11l_opy_.POST
                and f.bstack1111ll1l11_opy_(instance, TestFramework.bstack1ll11ll1l1l_opy_)
            ):
                self.logger.warning(bstack11lll_opy_ (u"ࠧ࡯࡮࡫ࡧࡦࡸ࡮ࡴࡧࠡࡖࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡔࡶࡤࡸࡪ࠴ࡔࡆࡕࡗ࠰࡚ࠥࡥࡴࡶࡋࡳࡴࡱࡓࡵࡣࡷࡩ࠳ࡖࡏࡔࡖࠣࠦᆨ") + str(TestFramework.bstack1111ll1l11_opy_(instance, TestFramework.bstack1ll11ll1l1l_opy_)) + bstack11lll_opy_ (u"ࠨࠢᆩ"))
                self.bstack1ll111ll1ll_opy_(f, instance, (bstack1lll1lll1ll_opy_.TEST, bstack1lll1lll11l_opy_.POST), *args, **kwargs)
            bstack11lll1l11l_opy_ = datetime.now()
            data = instance.data.copy()
            bstack1ll11l1l1ll_opy_ = sorted(
                filter(lambda x: x.get(bstack11lll_opy_ (u"ࠢࡦࡸࡨࡲࡹࡥࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠥᆪ"), None), data.pop(bstack11lll_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡪࡺࡷࡹࡷ࡫ࡳࠣᆫ"), {}).values()),
                key=lambda x: x[bstack11lll_opy_ (u"ࠤࡨࡺࡪࡴࡴࡠࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠧᆬ")],
            )
            if bstack1lllll11l1l_opy_.bstack1ll111lllll_opy_ in data:
                data.pop(bstack1lllll11l1l_opy_.bstack1ll111lllll_opy_)
            data.update({bstack11lll_opy_ (u"ࠥࡸࡪࡹࡴࡠࡨ࡬ࡼࡹࡻࡲࡦࡵࠥᆭ"): bstack1ll11l1l1ll_opy_})
            instance.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠦ࡯ࡹ࡯࡯࠼ࡷࡩࡸࡺ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡴࠤᆮ"), datetime.now() - bstack11lll1l11l_opy_)
            bstack11lll1l11l_opy_ = datetime.now()
            event_json = dumps(data, cls=bstack1ll1111lll1_opy_)
            instance.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠧࡰࡳࡰࡰ࠽ࡳࡳࡥࡡ࡭࡮ࡢࡸࡪࡹࡴࡠࡧࡹࡩࡳࡺࡳࠣᆯ"), datetime.now() - bstack11lll1l11l_opy_)
            self.bstack1ll11lll1l1_opy_(instance, bstack1111llll11_opy_, event_json=event_json)
            instance.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠨ࡯࠲࠳ࡼ࠾ࡴࡴ࡟ࡢ࡮࡯ࡣࡹ࡫ࡳࡵࡡࡨࡺࡪࡴࡴࡴࠤᆰ"), datetime.now() - bstack1ll11lll111_opy_)
    def bstack1ll1lll1lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11lll1_opy_,
        bstack1111llll11_opy_: Tuple[bstack1lll1lll1ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack11l1lll1_opy_ import bstack1lll1ll1lll_opy_
        bstack1ll1lll1l1l_opy_ = bstack1lll1ll1lll_opy_.bstack1lll111l111_opy_(EVENTS.bstack1l111111l1_opy_.value)
        self.bstack1ll1ll1ll1l_opy_.bstack1ll1111l111_opy_(instance, f, bstack1111llll11_opy_, *args, **kwargs)
        bstack1lll1ll1lll_opy_.end(EVENTS.bstack1l111111l1_opy_.value, bstack1ll1lll1l1l_opy_ + bstack11lll_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᆱ"), bstack1ll1lll1l1l_opy_ + bstack11lll_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᆲ"), status=True, failure=None, test_name=None)
    def bstack1lll111l11l_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11lll1_opy_,
        bstack1111llll11_opy_: Tuple[bstack1lll1lll1ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        req = self.bstack1ll1ll1ll1l_opy_.bstack1ll11l111ll_opy_(instance, f, bstack1111llll11_opy_, *args, **kwargs)
        self.bstack1ll1111l1l1_opy_(f, instance, req)
    @measure(event_name=EVENTS.bstack1ll11lll11l_opy_, stage=STAGE.bstack1lll1l1l11_opy_)
    def bstack1ll1111l1l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11lll1_opy_,
        req: structs.TestSessionEventRequest
    ):
        if not req:
            self.logger.debug(bstack11lll_opy_ (u"ࠤࡖ࡯࡮ࡶࡰࡪࡰࡪࠤ࡙࡫ࡳࡵࡕࡨࡷࡸ࡯࡯࡯ࡇࡹࡩࡳࡺࠠࡨࡔࡓࡇࠥࡩࡡ࡭࡮࠽ࠤࡓࡵࠠࡷࡣ࡯࡭ࡩࠦࡲࡦࡳࡸࡩࡸࡺࠠࡥࡣࡷࡥࠧᆳ"))
            return
        bstack11lll1l11l_opy_ = datetime.now()
        try:
            r = self.bstack111l11l1l1_opy_.TestSessionEvent(req)
            instance.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡨࡲࡩࡥࡴࡦࡵࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡫ࡶࡦࡰࡷࠦᆴ"), datetime.now() - bstack11lll1l11l_opy_)
            f.bstack1111ll11ll_opy_(instance, self.bstack1ll1ll1ll1l_opy_.bstack1ll11l11ll1_opy_, r.success)
            if not r.success:
                self.logger.info(bstack11lll_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨᆵ") + str(r) + bstack11lll_opy_ (u"ࠧࠨᆶ"))
        except grpc.RpcError as e:
            self.logger.error(bstack11lll_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦᆷ") + str(e) + bstack11lll_opy_ (u"ࠢࠣᆸ"))
            traceback.print_exc()
            raise e
    def bstack1ll11ll1ll1_opy_(
        self,
        f: bstack111111l111_opy_,
        _driver: object,
        exec: Tuple[bstack1111l1llll_opy_, str],
        _1ll11l1ll1l_opy_: Tuple[bstack1111l1l111_opy_, bstack1111ll111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if not bstack111111l111_opy_.bstack1lll1111111_opy_(method_name):
            return
        if f.bstack1ll1lllllll_opy_(*args) != bstack111111l111_opy_.bstack1ll111l1l1l_opy_:
            return
        bstack1ll11lll111_opy_ = datetime.now()
        screenshot = result.get(bstack11lll_opy_ (u"ࠣࡸࡤࡰࡺ࡫ࠢᆹ"), None) if isinstance(result, dict) else None
        if not isinstance(screenshot, str) or len(screenshot) <= 0:
            self.logger.warning(bstack11lll_opy_ (u"ࠤ࡬ࡲࡻࡧ࡬ࡪࡦࠣࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠠࡪ࡯ࡤ࡫ࡪࠦࡢࡢࡵࡨ࠺࠹ࠦࡳࡵࡴࠥᆺ"))
            return
        bstack1ll11lll1ll_opy_ = self.bstack1ll11ll111l_opy_(instance)
        if bstack1ll11lll1ll_opy_:
            entry = bstack1lll11l1ll1_opy_(TestFramework.bstack1ll11ll1111_opy_, screenshot)
            self.bstack1ll11l1ll11_opy_(bstack1ll11lll1ll_opy_, [entry])
            instance.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠥࡳ࠶࠷ࡹ࠻ࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡩࡽ࡫ࡣࡶࡶࡨࠦᆻ"), datetime.now() - bstack1ll11lll111_opy_)
        else:
            self.logger.warning(bstack11lll_opy_ (u"ࠦࡺࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡥࡧࡷࡩࡷࡳࡩ࡯ࡧࠣࡸࡪࡹࡴࠡࡨࡲࡶࠥࡽࡨࡪࡥ࡫ࠤࡹ࡮ࡩࡴࠢࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࠦࡷࡢࡵࠣࡸࡦࡱࡥ࡯ࠢࡥࡽࠥࡪࡲࡪࡸࡨࡶࡂࠨᆼ") + str(instance.ref()) + bstack11lll_opy_ (u"ࠧࠨᆽ"))
    @measure(event_name=EVENTS.bstack1ll1111ll11_opy_, stage=STAGE.bstack1lll1l1l11_opy_)
    def bstack1ll11l1ll11_opy_(
        self,
        bstack1ll11lll1ll_opy_: bstack1llll11lll1_opy_,
        entries: List[bstack1lll11l1ll1_opy_],
    ):
        self.bstack111l11l11l_opy_()
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.bstack11111l11l1_opy_(bstack1ll11lll1ll_opy_, TestFramework.bstack1ll1lll1111_opy_)
        req.execution_context.hash = str(bstack1ll11lll1ll_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll11lll1ll_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll11lll1ll_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.bstack11111l11l1_opy_(bstack1ll11lll1ll_opy_, TestFramework.bstack1ll1ll1l111_opy_)
            log_entry.test_framework_version = TestFramework.bstack11111l11l1_opy_(bstack1ll11lll1ll_opy_, TestFramework.bstack1ll11l1l111_opy_)
            log_entry.uuid = TestFramework.bstack11111l11l1_opy_(bstack1ll11lll1ll_opy_, TestFramework.bstack1ll1llll1l1_opy_)
            log_entry.test_framework_state = bstack1ll11lll1ll_opy_.state.name
            log_entry.message = entry.message.encode(bstack11lll_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᆾ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
        def bstack1ll11l11lll_opy_():
            bstack11lll1l11l_opy_ = datetime.now()
            try:
                self.bstack111l11l1l1_opy_.LogCreatedEvent(req)
                if entry.kind == TestFramework.bstack1ll11ll1111_opy_:
                    bstack1ll11lll1ll_opy_.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡹࡥ࡯ࡦࡢࡰࡴ࡭࡟ࡤࡴࡨࡥࡹ࡫ࡤࡠࡧࡹࡩࡳࡺ࡟ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠦᆿ"), datetime.now() - bstack11lll1l11l_opy_)
                else:
                    bstack1ll11lll1ll_opy_.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡦࡰࡧࡣࡱࡵࡧࡠࡥࡵࡩࡦࡺࡥࡥࡡࡨࡺࡪࡴࡴࡠ࡮ࡲ࡫ࠧᇀ"), datetime.now() - bstack11lll1l11l_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11lll_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢᇁ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack111l11l111_opy_.enqueue(bstack1ll11l11lll_opy_)
    @measure(event_name=EVENTS.bstack1ll111l1l11_opy_, stage=STAGE.bstack1lll1l1l11_opy_)
    def bstack1ll11lll1l1_opy_(
        self,
        instance: bstack1llll11lll1_opy_,
        bstack1111llll11_opy_: Tuple[bstack1lll1lll1ll_opy_, bstack1lll1lll11l_opy_],
        event_json=None,
    ):
        self.bstack111l11l11l_opy_()
        req = structs.TestFrameworkEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.bstack11111l11l1_opy_(instance, TestFramework.bstack1ll1lll1111_opy_)
        req.test_framework_name = TestFramework.bstack11111l11l1_opy_(instance, TestFramework.bstack1ll1ll1l111_opy_)
        req.test_framework_version = TestFramework.bstack11111l11l1_opy_(instance, TestFramework.bstack1ll11l1l111_opy_)
        req.test_framework_state = bstack1111llll11_opy_[0].name
        req.test_hook_state = bstack1111llll11_opy_[1].name
        started_at = TestFramework.bstack11111l11l1_opy_(instance, TestFramework.bstack1ll1111ll1l_opy_, None)
        if started_at:
            req.started_at = started_at.isoformat()
        ended_at = TestFramework.bstack11111l11l1_opy_(instance, TestFramework.bstack1ll111llll1_opy_, None)
        if ended_at:
            req.ended_at = ended_at.isoformat()
        req.uuid = instance.ref()
        req.event_json = (event_json if event_json else dumps(instance.data, cls=bstack1ll1111lll1_opy_)).encode(bstack11lll_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᇂ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        def bstack1ll11l11lll_opy_():
            bstack11lll1l11l_opy_ = datetime.now()
            try:
                self.bstack111l11l1l1_opy_.TestFrameworkEvent(req)
                instance.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡶࡩࡳࡪ࡟ࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡧࡹࡩࡳࡺࠢᇃ"), datetime.now() - bstack11lll1l11l_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11lll_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥᇄ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack111l11l111_opy_.enqueue(bstack1ll11l11lll_opy_)
    def bstack1ll11ll11ll_opy_(self, event_url: str, bstack111ll11l11_opy_: dict) -> bool:
        return True # always return True so that old bstack1ll111l11l1_opy_ bstack1ll1111l11l_opy_'t bstack1ll11l11l1l_opy_
    def bstack1ll11ll111l_opy_(self, instance: bstack1111l1llll_opy_):
        bstack1ll111lll1l_opy_ = TestFramework.bstack1111ll1l1l_opy_(instance.context)
        for t in bstack1ll111lll1l_opy_:
            bstack1ll111ll111_opy_ = TestFramework.bstack11111l11l1_opy_(t, bstack1lllll11l1l_opy_.bstack1ll111lllll_opy_, [])
            if any(instance is d[1] for d in bstack1ll111ll111_opy_):
                return t
    def bstack1ll11l111l1_opy_(self, message):
        self.bstack1ll11llll11_opy_(message + bstack11lll_opy_ (u"ࠨ࡜࡯ࠤᇅ"))
    def log_error(self, message):
        self.bstack1ll11ll11l1_opy_(message + bstack11lll_opy_ (u"ࠢ࡝ࡰࠥᇆ"))
    def bstack1ll11l1111l_opy_(self, level, original_func):
        def bstack1ll11l11l11_opy_(*args):
            return_value = original_func(*args)
            if not args or not isinstance(args[0], str) or not args[0].strip():
                return return_value
            message = args[0].strip()
            bstack1ll111lll1l_opy_ = TestFramework.bstack1ll111l1111_opy_()
            if not bstack1ll111lll1l_opy_:
                return return_value
            bstack1ll11lll1ll_opy_ = next(
                (
                    instance
                    for instance in bstack1ll111lll1l_opy_
                    if TestFramework.bstack1111ll1l11_opy_(instance, TestFramework.bstack1ll1llll1l1_opy_)
                ),
                None,
            )
            if not bstack1ll11lll1ll_opy_:
                return
            entry = bstack1lll11l1ll1_opy_(TestFramework.bstack1ll111ll11l_opy_, message, level)
            self.bstack1ll11l1ll11_opy_(bstack1ll11lll1ll_opy_, [entry])
            return return_value
        return bstack1ll11l11l11_opy_
class bstack1ll1111lll1_opy_(JSONEncoder):
    def __init__(self, **kwargs):
        self.bstack1ll11l11111_opy_ = set()
        kwargs[bstack11lll_opy_ (u"ࠣࡵ࡮࡭ࡵࡱࡥࡺࡵࠥᇇ")] = True
        super().__init__(**kwargs)
    def default(self, obj):
        return bstack1ll11l1l11l_opy_(obj, self.bstack1ll11l11111_opy_)
def bstack1ll11l1lll1_opy_(obj):
    return isinstance(obj, (str, int, float, bool, type(None)))
def bstack1ll11l1l11l_opy_(obj, bstack1ll11l11111_opy_=None, max_depth=3):
    if bstack1ll11l11111_opy_ is None:
        bstack1ll11l11111_opy_ = set()
    if id(obj) in bstack1ll11l11111_opy_ or max_depth <= 0:
        return None
    max_depth -= 1
    bstack1ll11l11111_opy_.add(id(obj))
    if isinstance(obj, datetime):
        return obj.isoformat()
    bstack1ll111ll1l1_opy_ = TestFramework.bstack1ll11llllll_opy_(obj)
    bstack1ll11ll1l11_opy_ = next((k.lower() in bstack1ll111ll1l1_opy_.lower() for k in bstack1ll111l1ll1_opy_.keys()), None)
    if bstack1ll11ll1l11_opy_:
        obj = TestFramework.bstack1ll11l1l1l1_opy_(obj, bstack1ll111l1ll1_opy_[bstack1ll11ll1l11_opy_])
    if not isinstance(obj, dict):
        keys = []
        if hasattr(obj, bstack11lll_opy_ (u"ࠤࡢࡣࡸࡲ࡯ࡵࡵࡢࡣࠧᇈ")):
            keys = getattr(obj, bstack11lll_opy_ (u"ࠥࡣࡤࡹ࡬ࡰࡶࡶࡣࡤࠨᇉ"), [])
        elif hasattr(obj, bstack11lll_opy_ (u"ࠦࡤࡥࡤࡪࡥࡷࡣࡤࠨᇊ")):
            keys = getattr(obj, bstack11lll_opy_ (u"ࠧࡥ࡟ࡥ࡫ࡦࡸࡤࡥࠢᇋ"), {}).keys()
        else:
            keys = dir(obj)
        obj = {k: getattr(obj, k, None) for k in keys if not str(k).startswith(bstack11lll_opy_ (u"ࠨ࡟ࠣᇌ"))}
        if not obj and bstack1ll111ll1l1_opy_ == bstack11lll_opy_ (u"ࠢࡱࡣࡷ࡬ࡱ࡯ࡢ࠯ࡒࡲࡷ࡮ࡾࡐࡢࡶ࡫ࠦᇍ"):
            obj = {bstack11lll_opy_ (u"ࠣࡲࡤࡸ࡭ࠨᇎ"): str(obj)}
    result = {}
    for key, value in obj.items():
        if not bstack1ll11l1lll1_opy_(key) or str(key).startswith(bstack11lll_opy_ (u"ࠤࡢࠦᇏ")):
            continue
        if value is not None and bstack1ll11l1lll1_opy_(value):
            result[key] = value
        elif isinstance(value, dict):
            r = bstack1ll11l1l11l_opy_(value, bstack1ll11l11111_opy_, max_depth)
            if r is not None:
                result[key] = r
        elif isinstance(value, (list, tuple, set, frozenset)):
            result[key] = list(filter(None, [bstack1ll11l1l11l_opy_(o, bstack1ll11l11111_opy_, max_depth) for o in value]))
    return result or None