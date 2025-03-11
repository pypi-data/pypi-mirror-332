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
import json
import time
from datetime import datetime, timezone
from browserstack_sdk.sdk_cli.bstack11111l1lll_opy_ import (
    bstack1111l1l111_opy_,
    bstack1111ll111l_opy_,
    bstack11111lll11_opy_,
    bstack1111l1llll_opy_,
    bstack11111l11ll_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1l1ll1_opy_ import bstack111111l111_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1lll1ll_opy_, bstack1lll1lll11l_opy_, bstack1llll11lll1_opy_
from browserstack_sdk.sdk_cli.bstack1ll1l1111l1_opy_ import bstack1ll1l111l11_opy_
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1ll1111llll_opy_
from browserstack_sdk import sdk_pb2 as structs
from bstack_utils.measure import measure
from bstack_utils.constants import *
from typing import Tuple, List, Any
class bstack1lllll11l1l_opy_(bstack1ll1l111l11_opy_):
    bstack1l1lll11ll1_opy_ = bstack11lll_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡧࡶ࡮ࡼࡥࡳࡵࠥኪ")
    bstack1ll111lllll_opy_ = bstack11lll_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡶࡩࡸࡹࡩࡰࡰࡶࠦካ")
    bstack1l1ll1ll1ll_opy_ = bstack11lll_opy_ (u"ࠨ࡮ࡰࡰࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࡳࠣኬ")
    bstack1l1lll11l1l_opy_ = bstack11lll_opy_ (u"ࠢࡵࡧࡶࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡹࠢክ")
    bstack1l1ll1lll1l_opy_ = bstack11lll_opy_ (u"ࠣࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫࡟ࡳࡧࡩࡷࠧኮ")
    bstack1ll11l11ll1_opy_ = bstack11lll_opy_ (u"ࠤࡦࡦࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡤࡴࡨࡥࡹ࡫ࡤࠣኯ")
    bstack1l1lll11l11_opy_ = bstack11lll_opy_ (u"ࠥࡧࡧࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡰࡤࡱࡪࠨኰ")
    bstack1l1ll1l1lll_opy_ = bstack11lll_opy_ (u"ࠦࡨࡨࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡶࡸࡦࡺࡵࡴࠤ኱")
    def __init__(self):
        super().__init__(bstack1ll1l11l111_opy_=self.bstack1l1lll11ll1_opy_, frameworks=[bstack111111l111_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1ll1l1lll1l_opy_((bstack1lll1lll1ll_opy_.BEFORE_EACH, bstack1lll1lll11l_opy_.POST), self.bstack1l1l1l1lll1_opy_)
        TestFramework.bstack1ll1l1lll1l_opy_((bstack1lll1lll1ll_opy_.TEST, bstack1lll1lll11l_opy_.PRE), self.bstack1ll1lll1lll_opy_)
        TestFramework.bstack1ll1l1lll1l_opy_((bstack1lll1lll1ll_opy_.TEST, bstack1lll1lll11l_opy_.POST), self.bstack1lll111l11l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l1l1l1lll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11lll1_opy_,
        bstack1111llll11_opy_: Tuple[bstack1lll1lll1ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        bstack1ll111ll111_opy_ = self.bstack1l1l1ll1111_opy_(instance.context)
        if not bstack1ll111ll111_opy_:
            self.logger.debug(bstack11lll_opy_ (u"ࠧࡹࡥࡵࡡࡤࡧࡹ࡯ࡶࡦࡡࡧࡶ࡮ࡼࡥࡳࡵ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࠣኲ") + str(bstack1111llll11_opy_) + bstack11lll_opy_ (u"ࠨࠢኳ"))
        f.bstack1111ll11ll_opy_(instance, bstack1lllll11l1l_opy_.bstack1ll111lllll_opy_, bstack1ll111ll111_opy_)
        bstack1l1l1ll1lll_opy_ = self.bstack1l1l1ll1111_opy_(instance.context, bstack1l1l1ll1ll1_opy_=False)
        f.bstack1111ll11ll_opy_(instance, bstack1lllll11l1l_opy_.bstack1l1ll1ll1ll_opy_, bstack1l1l1ll1lll_opy_)
    def bstack1ll1lll1lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11lll1_opy_,
        bstack1111llll11_opy_: Tuple[bstack1lll1lll1ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l1l1l1lll1_opy_(f, instance, bstack1111llll11_opy_, *args, **kwargs)
        if not f.bstack11111l11l1_opy_(instance, bstack1lllll11l1l_opy_.bstack1l1lll11l11_opy_, False):
            self.__1l1l1ll1l1l_opy_(f,instance,bstack1111llll11_opy_)
    def bstack1lll111l11l_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11lll1_opy_,
        bstack1111llll11_opy_: Tuple[bstack1lll1lll1ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l1l1l1lll1_opy_(f, instance, bstack1111llll11_opy_, *args, **kwargs)
        if not f.bstack11111l11l1_opy_(instance, bstack1lllll11l1l_opy_.bstack1l1lll11l11_opy_, False):
            self.__1l1l1ll1l1l_opy_(f, instance, bstack1111llll11_opy_)
        if not f.bstack11111l11l1_opy_(instance, bstack1lllll11l1l_opy_.bstack1l1ll1l1lll_opy_, False):
            self.__1l1l1ll111l_opy_(f, instance, bstack1111llll11_opy_)
    def bstack1l1l1ll11l1_opy_(
        self,
        f: bstack111111l111_opy_,
        driver: object,
        exec: Tuple[bstack1111l1llll_opy_, str],
        bstack1111llll11_opy_: Tuple[bstack1111l1l111_opy_, bstack1111ll111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if not f.bstack1lll11111ll_opy_(instance):
            return
        if f.bstack11111l11l1_opy_(instance, bstack1lllll11l1l_opy_.bstack1l1ll1l1lll_opy_, False):
            return
        driver.execute_script(
            bstack11lll_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠧኴ").format(
                json.dumps(
                    {
                        bstack11lll_opy_ (u"ࠣࡣࡦࡸ࡮ࡵ࡮ࠣኵ"): bstack11lll_opy_ (u"ࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠧ኶"),
                        bstack11lll_opy_ (u"ࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ኷"): {bstack11lll_opy_ (u"ࠦࡸࡺࡡࡵࡷࡶࠦኸ"): result},
                    }
                )
            )
        )
        f.bstack1111ll11ll_opy_(instance, bstack1lllll11l1l_opy_.bstack1l1ll1l1lll_opy_, True)
    def bstack1l1l1ll1111_opy_(self, context: bstack11111l11ll_opy_, bstack1l1l1ll1ll1_opy_= True):
        if bstack1l1l1ll1ll1_opy_:
            bstack1ll111ll111_opy_ = self.bstack1ll1l11ll11_opy_(context, reverse=True)
        else:
            bstack1ll111ll111_opy_ = self.bstack1ll1l11111l_opy_(context, reverse=True)
        return [f for f in bstack1ll111ll111_opy_ if f[1].state != bstack1111l1l111_opy_.QUIT]
    @measure(event_name=EVENTS.bstack1lll1ll1_opy_, stage=STAGE.bstack1lll1l1l11_opy_)
    def __1l1l1ll111l_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11lll1_opy_,
        bstack1111llll11_opy_: Tuple[bstack1lll1lll1ll_opy_, bstack1lll1lll11l_opy_],
    ):
        bstack1ll111ll111_opy_ = f.bstack11111l11l1_opy_(instance, bstack1lllll11l1l_opy_.bstack1ll111lllll_opy_, [])
        if not bstack1ll111ll111_opy_:
            self.logger.debug(bstack11lll_opy_ (u"ࠧࡹࡥࡵࡡࡤࡧࡹ࡯ࡶࡦࡡࡧࡶ࡮ࡼࡥࡳࡵ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࠣኹ") + str(bstack1111llll11_opy_) + bstack11lll_opy_ (u"ࠨࠢኺ"))
            return
        driver = bstack1ll111ll111_opy_[0][0]()
        status = f.bstack11111l11l1_opy_(instance, TestFramework.bstack1l1ll1lll11_opy_, None)
        if not status:
            self.logger.debug(bstack11lll_opy_ (u"ࠢࡴࡧࡷࡣࡦࡩࡴࡪࡸࡨࡣࡩࡸࡩࡷࡧࡵࡷ࠿ࠦ࡮ࡰࠢࡶࡸࡦࡺࡵࡴࠢࡩࡳࡷࠦࡴࡦࡵࡷ࠰ࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࠤኻ") + str(bstack1111llll11_opy_) + bstack11lll_opy_ (u"ࠣࠤኼ"))
            return
        bstack1l1lll111l1_opy_ = {bstack11lll_opy_ (u"ࠤࡶࡸࡦࡺࡵࡴࠤኽ"): status.lower()}
        bstack1l1ll1ll11l_opy_ = f.bstack11111l11l1_opy_(instance, TestFramework.bstack1l1ll1l1ll1_opy_, None)
        if status.lower() == bstack11lll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪኾ") and bstack1l1ll1ll11l_opy_ is not None:
            bstack1l1lll111l1_opy_[bstack11lll_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫ኿")] = bstack1l1ll1ll11l_opy_[0][bstack11lll_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨዀ")][0] if isinstance(bstack1l1ll1ll11l_opy_, list) else str(bstack1l1ll1ll11l_opy_)
        driver.execute_script(
            bstack11lll_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠦ዁").format(
                json.dumps(
                    {
                        bstack11lll_opy_ (u"ࠢࡢࡥࡷ࡭ࡴࡴࠢዂ"): bstack11lll_opy_ (u"ࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦዃ"),
                        bstack11lll_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧዄ"): bstack1l1lll111l1_opy_,
                    }
                )
            )
        )
        f.bstack1111ll11ll_opy_(instance, bstack1lllll11l1l_opy_.bstack1l1ll1l1lll_opy_, True)
    @measure(event_name=EVENTS.bstack1111l1lll_opy_, stage=STAGE.bstack1lll1l1l11_opy_)
    def __1l1l1ll1l1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11lll1_opy_,
        bstack1111llll11_opy_: Tuple[bstack1lll1lll1ll_opy_, bstack1lll1lll11l_opy_]
    ):
        test_name = f.bstack11111l11l1_opy_(instance, TestFramework.bstack1l1l1ll1l11_opy_, None)
        if not test_name:
            self.logger.debug(bstack11lll_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡳࡩࡴࡵ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡳࡧ࡭ࡦࠤዅ"))
            return
        bstack1ll111ll111_opy_ = f.bstack11111l11l1_opy_(instance, bstack1lllll11l1l_opy_.bstack1ll111lllll_opy_, [])
        if not bstack1ll111ll111_opy_:
            self.logger.debug(bstack11lll_opy_ (u"ࠦࡸ࡫ࡴࡠࡣࡦࡸ࡮ࡼࡥࡠࡦࡵ࡭ࡻ࡫ࡲࡴ࠼ࠣࡲࡴࠦࡳࡵࡣࡷࡹࡸࠦࡦࡰࡴࠣࡸࡪࡹࡴ࠭ࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࠨ዆") + str(bstack1111llll11_opy_) + bstack11lll_opy_ (u"ࠧࠨ዇"))
            return
        for bstack1ll111111l1_opy_, bstack1l1l1l1llll_opy_ in bstack1ll111ll111_opy_:
            if not bstack111111l111_opy_.bstack1lll11111ll_opy_(bstack1l1l1l1llll_opy_):
                continue
            driver = bstack1ll111111l1_opy_()
            if not driver:
                continue
            driver.execute_script(
                bstack11lll_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠦወ").format(
                    json.dumps(
                        {
                            bstack11lll_opy_ (u"ࠢࡢࡥࡷ࡭ࡴࡴࠢዉ"): bstack11lll_opy_ (u"ࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤዊ"),
                            bstack11lll_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧዋ"): {bstack11lll_opy_ (u"ࠥࡲࡦࡳࡥࠣዌ"): test_name},
                        }
                    )
                )
            )
        f.bstack1111ll11ll_opy_(instance, bstack1lllll11l1l_opy_.bstack1l1lll11l11_opy_, True)
    def bstack1ll1111l111_opy_(
        self,
        instance: bstack1llll11lll1_opy_,
        f: TestFramework,
        bstack1111llll11_opy_: Tuple[bstack1lll1lll1ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l1l1l1lll1_opy_(f, instance, bstack1111llll11_opy_, *args, **kwargs)
        bstack1ll111ll111_opy_ = [d for d, _ in f.bstack11111l11l1_opy_(instance, bstack1lllll11l1l_opy_.bstack1ll111lllll_opy_, [])]
        if not bstack1ll111ll111_opy_:
            self.logger.debug(bstack11lll_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡵࡨࡷࡸ࡯࡯࡯ࡵࠣࡸࡴࠦ࡬ࡪࡰ࡮ࠦው"))
            return
        if not bstack1ll1111llll_opy_():
            self.logger.debug(bstack11lll_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠥዎ"))
            return
        for bstack1l1l1lll111_opy_ in bstack1ll111ll111_opy_:
            driver = bstack1l1l1lll111_opy_()
            if not driver:
                continue
            timestamp = int(time.time() * 1000)
            data = bstack11lll_opy_ (u"ࠨࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࡙ࡹ࡯ࡥ࠽ࠦዏ") + str(timestamp)
            driver.execute_script(
                bstack11lll_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠧዐ").format(
                    json.dumps(
                        {
                            bstack11lll_opy_ (u"ࠣࡣࡦࡸ࡮ࡵ࡮ࠣዑ"): bstack11lll_opy_ (u"ࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦዒ"),
                            bstack11lll_opy_ (u"ࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨዓ"): {
                                bstack11lll_opy_ (u"ࠦࡹࡿࡰࡦࠤዔ"): bstack11lll_opy_ (u"ࠧࡇ࡮࡯ࡱࡷࡥࡹ࡯࡯࡯ࠤዕ"),
                                bstack11lll_opy_ (u"ࠨࡤࡢࡶࡤࠦዖ"): data,
                                bstack11lll_opy_ (u"ࠢ࡭ࡧࡹࡩࡱࠨ዗"): bstack11lll_opy_ (u"ࠣࡦࡨࡦࡺ࡭ࠢዘ")
                            }
                        }
                    )
                )
            )
    def bstack1ll11l111ll_opy_(
        self,
        instance: bstack1llll11lll1_opy_,
        f: TestFramework,
        bstack1111llll11_opy_: Tuple[bstack1lll1lll1ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l1l1l1lll1_opy_(f, instance, bstack1111llll11_opy_, *args, **kwargs)
        bstack1ll111ll111_opy_ = [d for _, d in f.bstack11111l11l1_opy_(instance, bstack1lllll11l1l_opy_.bstack1ll111lllll_opy_, [])] + [d for _, d in f.bstack11111l11l1_opy_(instance, bstack1lllll11l1l_opy_.bstack1l1ll1ll1ll_opy_, [])]
        keys = [
            bstack1lllll11l1l_opy_.bstack1ll111lllll_opy_,
            bstack1lllll11l1l_opy_.bstack1l1ll1ll1ll_opy_,
        ]
        bstack1ll111ll111_opy_ = [
            d for key in keys for _, d in f.bstack11111l11l1_opy_(instance, key, [])
        ]
        if not bstack1ll111ll111_opy_:
            self.logger.debug(bstack11lll_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡹࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡪࡰࡧࠤࡦࡴࡹࠡࡵࡨࡷࡸ࡯࡯࡯ࡵࠣࡸࡴࠦ࡬ࡪࡰ࡮ࠦዙ"))
            return
        if f.bstack11111l11l1_opy_(instance, bstack1lllll11l1l_opy_.bstack1ll11l11ll1_opy_, False):
            self.logger.debug(bstack11lll_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡈࡈࡔࠡࡣ࡯ࡶࡪࡧࡤࡺࠢࡦࡶࡪࡧࡴࡦࡦࠥዚ"))
            return
        self.bstack111l11l11l_opy_()
        bstack11lll1l11l_opy_ = datetime.now()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.bstack11111l11l1_opy_(instance, TestFramework.bstack1ll1lll1111_opy_)
        req.test_framework_name = TestFramework.bstack11111l11l1_opy_(instance, TestFramework.bstack1ll1ll1l111_opy_)
        req.test_framework_version = TestFramework.bstack11111l11l1_opy_(instance, TestFramework.bstack1ll11l1l111_opy_)
        req.test_framework_state = bstack1111llll11_opy_[0].name
        req.test_hook_state = bstack1111llll11_opy_[1].name
        req.test_uuid = TestFramework.bstack11111l11l1_opy_(instance, TestFramework.bstack1ll1llll1l1_opy_)
        for driver in bstack1ll111ll111_opy_:
            session = req.automation_sessions.add()
            session.provider = (
                bstack11lll_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠥዛ")
                if bstack111111l111_opy_.bstack11111l11l1_opy_(driver, bstack111111l111_opy_.bstack1l1l1ll11ll_opy_, False)
                else bstack11lll_opy_ (u"ࠧࡻ࡮࡬ࡰࡲࡻࡳࡥࡧࡳ࡫ࡧࠦዜ")
            )
            session.ref = driver.ref()
            session.hub_url = bstack111111l111_opy_.bstack11111l11l1_opy_(driver, bstack111111l111_opy_.bstack1l1llll1l11_opy_, bstack11lll_opy_ (u"ࠨࠢዝ"))
            session.framework_name = driver.framework_name
            session.framework_version = driver.framework_version
            session.framework_session_id = bstack111111l111_opy_.bstack11111l11l1_opy_(driver, bstack111111l111_opy_.bstack1l1llll1l1l_opy_, bstack11lll_opy_ (u"ࠢࠣዞ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1ll1l1lllll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11lll1_opy_,
        bstack1111llll11_opy_: Tuple[bstack1lll1lll1ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs
    ):
        bstack1ll111ll111_opy_ = f.bstack11111l11l1_opy_(instance, bstack1lllll11l1l_opy_.bstack1ll111lllll_opy_, [])
        if not bstack1ll111ll111_opy_:
            self.logger.debug(bstack11lll_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦዟ") + str(kwargs) + bstack11lll_opy_ (u"ࠤࠥዠ"))
            return {}
        if len(bstack1ll111ll111_opy_) > 1:
            self.logger.debug(bstack11lll_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࢁ࡬ࡦࡰࠫࡨࡷ࡯ࡶࡦࡴࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡸ࠯ࡽࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨዡ") + str(kwargs) + bstack11lll_opy_ (u"ࠦࠧዢ"))
            return {}
        bstack1ll111111l1_opy_, bstack1l1llllll1l_opy_ = bstack1ll111ll111_opy_[0]
        driver = bstack1ll111111l1_opy_()
        if not driver:
            self.logger.debug(bstack11lll_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢዣ") + str(kwargs) + bstack11lll_opy_ (u"ࠨࠢዤ"))
            return {}
        capabilities = f.bstack11111l11l1_opy_(bstack1l1llllll1l_opy_, bstack111111l111_opy_.bstack1l1lll1l1l1_opy_)
        if not capabilities:
            self.logger.debug(bstack11lll_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠤ࡫ࡵࡵ࡯ࡦࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢዥ") + str(kwargs) + bstack11lll_opy_ (u"ࠣࠤዦ"))
            return {}
        return capabilities.get(bstack11lll_opy_ (u"ࠤࡤࡰࡼࡧࡹࡴࡏࡤࡸࡨ࡮ࠢዧ"), {})
    def bstack1ll1ll11111_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11lll1_opy_,
        bstack1111llll11_opy_: Tuple[bstack1lll1lll1ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs
    ):
        bstack1ll111ll111_opy_ = f.bstack11111l11l1_opy_(instance, bstack1lllll11l1l_opy_.bstack1ll111lllll_opy_, [])
        if not bstack1ll111ll111_opy_:
            self.logger.debug(bstack11lll_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡩࡸࡩࡷࡧࡵ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨየ") + str(kwargs) + bstack11lll_opy_ (u"ࠦࠧዩ"))
            return
        if len(bstack1ll111ll111_opy_) > 1:
            self.logger.debug(bstack11lll_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡤࡳ࡫ࡹࡩࡷࡀࠠࡼ࡮ࡨࡲ࠭ࡪࡲࡪࡸࡨࡶࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳࠪࡿࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣዪ") + str(kwargs) + bstack11lll_opy_ (u"ࠨࠢያ"))
        bstack1ll111111l1_opy_, bstack1l1llllll1l_opy_ = bstack1ll111ll111_opy_[0]
        driver = bstack1ll111111l1_opy_()
        if not driver:
            self.logger.debug(bstack11lll_opy_ (u"ࠢࡨࡧࡷࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤዬ") + str(kwargs) + bstack11lll_opy_ (u"ࠣࠤይ"))
            return
        return driver