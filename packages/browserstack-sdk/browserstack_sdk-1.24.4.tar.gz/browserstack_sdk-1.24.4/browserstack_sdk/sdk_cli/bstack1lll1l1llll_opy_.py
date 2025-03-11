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
import json
import time
import os
import threading
import asyncio
from browserstack_sdk.sdk_cli.bstack1111llll11_opy_ import (
    bstack111l1111ll_opy_,
    bstack1111ll11l1_opy_,
    bstack11111ll11l_opy_,
    bstack111l11111l_opy_,
)
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1ll11ll111l_opy_, bstack11ll111l11_opy_
from browserstack_sdk.sdk_cli.bstack111111l1l1_opy_ import bstack1llll111lll_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll1111ll_opy_, bstack1llll1lll1l_opy_, bstack1llllll11l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1ll1l_opy_ import bstack11111111l1_opy_
from browserstack_sdk.sdk_cli.bstack1ll1l111ll1_opy_ import bstack1ll1l11l1l1_opy_
from typing import Tuple, List, Any
from bstack_utils.bstack1l1ll1l1ll_opy_ import bstack1ll1l11ll1_opy_, bstack11lll1lll_opy_, bstack11l1llll_opy_
from browserstack_sdk import sdk_pb2 as structs
class bstack1llll111111_opy_(bstack1ll1l11l1l1_opy_):
    bstack1l1ll1ll1ll_opy_ = bstack11ll1l_opy_ (u"ࠣࡶࡨࡷࡹࡥࡤࡳ࡫ࡹࡩࡷࡹࠢሆ")
    bstack1ll11ll11ll_opy_ = bstack11ll1l_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࡳࠣሇ")
    bstack1l1lll11ll1_opy_ = bstack11ll1l_opy_ (u"ࠥࡲࡴࡴ࡟ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡷࡪࡹࡳࡪࡱࡱࡷࠧለ")
    bstack1l1lll1111l_opy_ = bstack11ll1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡶࡩࡸࡹࡩࡰࡰࡶࠦሉ")
    bstack1l1lll1l111_opy_ = bstack11ll1l_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡣࡷ࡫ࡦࡴࠤሊ")
    bstack1ll1l111111_opy_ = bstack11ll1l_opy_ (u"ࠨࡣࡣࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡨࡸࡥࡢࡶࡨࡨࠧላ")
    bstack1l1lll111ll_opy_ = bstack11ll1l_opy_ (u"ࠢࡤࡤࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡴࡡ࡮ࡧࠥሌ")
    bstack1l1lll11111_opy_ = bstack11ll1l_opy_ (u"ࠣࡥࡥࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡳࡵࡣࡷࡹࡸࠨል")
    def __init__(self):
        super().__init__(bstack1ll1l11ll11_opy_=self.bstack1l1ll1ll1ll_opy_, frameworks=[bstack1llll111lll_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1lll111l111_opy_((bstack1llll1111ll_opy_.BEFORE_EACH, bstack1llll1lll1l_opy_.POST), self.bstack1l1ll1lll11_opy_)
        if bstack11ll111l11_opy_():
            TestFramework.bstack1lll111l111_opy_((bstack1llll1111ll_opy_.TEST, bstack1llll1lll1l_opy_.POST), self.bstack1ll1lll1ll1_opy_)
        else:
            TestFramework.bstack1lll111l111_opy_((bstack1llll1111ll_opy_.TEST, bstack1llll1lll1l_opy_.PRE), self.bstack1ll1lll1ll1_opy_)
        TestFramework.bstack1lll111l111_opy_((bstack1llll1111ll_opy_.TEST, bstack1llll1lll1l_opy_.POST), self.bstack1ll1lll11l1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l1ll1lll11_opy_(
        self,
        f: TestFramework,
        instance: bstack1llllll11l1_opy_,
        bstack11111ll111_opy_: Tuple[bstack1llll1111ll_opy_, bstack1llll1lll1l_opy_],
        *args,
        **kwargs,
    ):
        bstack1l1ll1ll1l1_opy_ = self.bstack1l1lll11l1l_opy_(instance.context)
        if not bstack1l1ll1ll1l1_opy_:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠤࡶࡩࡹࡥࡡࡤࡶ࡬ࡺࡪࡥࡰࡢࡩࡨ࠾ࠥࡴ࡯ࠡࡲࡤ࡫ࡪࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࠢሎ") + str(bstack11111ll111_opy_) + bstack11ll1l_opy_ (u"ࠥࠦሏ"))
            return
        f.bstack111l111111_opy_(instance, bstack1llll111111_opy_.bstack1ll11ll11ll_opy_, bstack1l1ll1ll1l1_opy_)
    def bstack1l1lll11l1l_opy_(self, context: bstack111l11111l_opy_, bstack1l1lll11lll_opy_= True):
        if bstack1l1lll11lll_opy_:
            bstack1l1ll1ll1l1_opy_ = self.bstack1ll1l11l11l_opy_(context, reverse=True)
        else:
            bstack1l1ll1ll1l1_opy_ = self.bstack1ll1l111l11_opy_(context, reverse=True)
        return [f for f in bstack1l1ll1ll1l1_opy_ if f[1].state != bstack111l1111ll_opy_.QUIT]
    def bstack1ll1lll1ll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1llllll11l1_opy_,
        bstack11111ll111_opy_: Tuple[bstack1llll1111ll_opy_, bstack1llll1lll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l1ll1lll11_opy_(f, instance, bstack11111ll111_opy_, *args, **kwargs)
        if not bstack1ll11ll111l_opy_:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢሐ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠧࠨሑ"))
            return
        bstack1l1ll1ll1l1_opy_ = f.bstack1111lll1l1_opy_(instance, bstack1llll111111_opy_.bstack1ll11ll11ll_opy_, [])
        if not bstack1l1ll1ll1l1_opy_:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤሒ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠢࠣሓ"))
            return
        if len(bstack1l1ll1ll1l1_opy_) > 1:
            self.logger.debug(
                bstack1llllllll1l_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡿࡱ࡫࡮ࠩࡲࡤ࡫ࡪࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡴࠫࢀࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࡽ࡮ࡻࡦࡸࡧࡴࡿࠥሔ"))
        bstack1l1ll1ll11l_opy_, bstack1ll11111l11_opy_ = bstack1l1ll1ll1l1_opy_[0]
        page = bstack1l1ll1ll11l_opy_()
        if not page:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡱࡣࡪࡩࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤሕ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠥࠦሖ"))
            return
        bstack1l1l11l111_opy_ = getattr(args[0], bstack11ll1l_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦሗ"), None)
        try:
            page.evaluate(bstack11ll1l_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨመ"),
                        bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠪሙ") + json.dumps(
                            bstack1l1l11l111_opy_) + bstack11ll1l_opy_ (u"ࠢࡾࡿࠥሚ"))
        except Exception as e:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣࡿࢂࠨማ"), e)
    def bstack1ll1lll11l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1llllll11l1_opy_,
        bstack11111ll111_opy_: Tuple[bstack1llll1111ll_opy_, bstack1llll1lll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l1ll1lll11_opy_(f, instance, bstack11111ll111_opy_, *args, **kwargs)
        if not bstack1ll11ll111l_opy_:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧሜ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠥࠦም"))
            return
        bstack1l1ll1ll1l1_opy_ = f.bstack1111lll1l1_opy_(instance, bstack1llll111111_opy_.bstack1ll11ll11ll_opy_, [])
        if not bstack1l1ll1ll1l1_opy_:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢሞ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠧࠨሟ"))
            return
        if len(bstack1l1ll1ll1l1_opy_) > 1:
            self.logger.debug(
                bstack1llllllll1l_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡽ࡯ࡩࡳ࠮ࡰࡢࡩࡨࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡹࠩࡾࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࡻ࡬ࡹࡤࡶ࡬ࡹࡽࠣሠ"))
        bstack1l1ll1ll11l_opy_, bstack1ll11111l11_opy_ = bstack1l1ll1ll1l1_opy_[0]
        page = bstack1l1ll1ll11l_opy_()
        if not page:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡶࡡࡨࡧࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢሡ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠣࠤሢ"))
            return
        status = f.bstack1111lll1l1_opy_(instance, TestFramework.bstack1l1ll1llll1_opy_, None)
        if not status:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠤࡱࡳࠥࡹࡴࡢࡶࡸࡷࠥ࡬࡯ࡳࠢࡷࡩࡸࡺࠬࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࠧሣ") + str(bstack11111ll111_opy_) + bstack11ll1l_opy_ (u"ࠥࠦሤ"))
            return
        bstack1l1ll1lllll_opy_ = {bstack11ll1l_opy_ (u"ࠦࡸࡺࡡࡵࡷࡶࠦሥ"): status.lower()}
        bstack1l1ll1lll1l_opy_ = f.bstack1111lll1l1_opy_(instance, TestFramework.bstack1l1ll1l1lll_opy_, None)
        if status.lower() == bstack11ll1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬሦ") and bstack1l1ll1lll1l_opy_ is not None:
            bstack1l1ll1lllll_opy_[bstack11ll1l_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭ሧ")] = bstack1l1ll1lll1l_opy_[0][bstack11ll1l_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧࠪረ")][0] if isinstance(bstack1l1ll1lll1l_opy_, list) else str(bstack1l1ll1lll1l_opy_)
        try:
              page.evaluate(
                    bstack11ll1l_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤሩ"),
                    bstack11ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࠧሪ")
                    + json.dumps(bstack1l1ll1lllll_opy_)
                    + bstack11ll1l_opy_ (u"ࠥࢁࠧራ")
                )
        except Exception as e:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡵࡷࡥࡹࡻࡳࠡࡽࢀࠦሬ"), e)
    def bstack1ll11ll11l1_opy_(
        self,
        instance: bstack1llllll11l1_opy_,
        f: TestFramework,
        bstack11111ll111_opy_: Tuple[bstack1llll1111ll_opy_, bstack1llll1lll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l1ll1lll11_opy_(f, instance, bstack11111ll111_opy_, *args, **kwargs)
        if not bstack1ll11ll111l_opy_:
            self.logger.debug(
                bstack1llllllll1l_opy_ (u"ࠧࡳࡡࡳ࡭ࡢࡳ࠶࠷ࡹࡠࡵࡼࡲࡨࡀࠠ࡯ࡱࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࢀࡱࡷࡢࡴࡪࡷࢂࠨር"))
            return
        bstack1l1ll1ll1l1_opy_ = f.bstack1111lll1l1_opy_(instance, bstack1llll111111_opy_.bstack1ll11ll11ll_opy_, [])
        if not bstack1l1ll1ll1l1_opy_:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤሮ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠢࠣሯ"))
            return
        if len(bstack1l1ll1ll1l1_opy_) > 1:
            self.logger.debug(
                bstack1llllllll1l_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡿࡱ࡫࡮ࠩࡲࡤ࡫ࡪࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡴࠫࢀࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࡽ࡮ࡻࡦࡸࡧࡴࡿࠥሰ"))
        bstack1l1ll1ll11l_opy_, bstack1ll11111l11_opy_ = bstack1l1ll1ll1l1_opy_[0]
        page = bstack1l1ll1ll11l_opy_()
        if not page:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠤࡰࡥࡷࡱ࡟ࡰ࠳࠴ࡽࡤࡹࡹ࡯ࡥ࠽ࠤࡳࡵࠠࡱࡣࡪࡩࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤሱ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠥࠦሲ"))
            return
        timestamp = int(time.time() * 1000)
        data = bstack11ll1l_opy_ (u"ࠦࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࡗࡾࡴࡣ࠻ࠤሳ") + str(timestamp)
        try:
            page.evaluate(
                bstack11ll1l_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨሴ"),
                bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫስ").format(
                    json.dumps(
                        {
                            bstack11ll1l_opy_ (u"ࠢࡢࡥࡷ࡭ࡴࡴࠢሶ"): bstack11ll1l_opy_ (u"ࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥሷ"),
                            bstack11ll1l_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧሸ"): {
                                bstack11ll1l_opy_ (u"ࠥࡸࡾࡶࡥࠣሹ"): bstack11ll1l_opy_ (u"ࠦࡆࡴ࡮ࡰࡶࡤࡸ࡮ࡵ࡮ࠣሺ"),
                                bstack11ll1l_opy_ (u"ࠧࡪࡡࡵࡣࠥሻ"): data,
                                bstack11ll1l_opy_ (u"ࠨ࡬ࡦࡸࡨࡰࠧሼ"): bstack11ll1l_opy_ (u"ࠢࡥࡧࡥࡹ࡬ࠨሽ")
                            }
                        }
                    )
                )
            )
        except Exception as e:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡴ࠷࠱ࡺࠢࡤࡲࡳࡵࡴࡢࡶ࡬ࡳࡳࠦ࡭ࡢࡴ࡮࡭ࡳ࡭ࠠࡼࡿࠥሾ"), e)
    def bstack1ll111ll1ll_opy_(
        self,
        instance: bstack1llllll11l1_opy_,
        f: TestFramework,
        bstack11111ll111_opy_: Tuple[bstack1llll1111ll_opy_, bstack1llll1lll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l1ll1lll11_opy_(f, instance, bstack11111ll111_opy_, *args, **kwargs)
        if f.bstack1111lll1l1_opy_(instance, bstack1llll111111_opy_.bstack1ll1l111111_opy_, False):
            return
        self.bstack1ll1ll1111l_opy_()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.bstack1111lll1l1_opy_(instance, TestFramework.bstack1lll111ll1l_opy_)
        req.test_framework_name = TestFramework.bstack1111lll1l1_opy_(instance, TestFramework.bstack1ll1lllll1l_opy_)
        req.test_framework_version = TestFramework.bstack1111lll1l1_opy_(instance, TestFramework.bstack1ll11l1l111_opy_)
        req.test_framework_state = bstack11111ll111_opy_[0].name
        req.test_hook_state = bstack11111ll111_opy_[1].name
        req.test_uuid = TestFramework.bstack1111lll1l1_opy_(instance, TestFramework.bstack1ll1l1lll1l_opy_)
        for bstack1l1lll111l1_opy_ in bstack11111111l1_opy_.bstack1111l1l11l_opy_.values():
            session = req.automation_sessions.add()
            session.provider = (
                bstack11ll1l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠣሿ")
                if bstack1ll11ll111l_opy_
                else bstack11ll1l_opy_ (u"ࠥࡹࡳࡱ࡮ࡰࡹࡱࡣ࡬ࡸࡩࡥࠤቀ")
            )
            session.ref = bstack1l1lll111l1_opy_.ref()
            session.hub_url = bstack11111111l1_opy_.bstack1111lll1l1_opy_(bstack1l1lll111l1_opy_, bstack11111111l1_opy_.bstack1l1llll11l1_opy_, bstack11ll1l_opy_ (u"ࠦࠧቁ"))
            session.framework_name = bstack1l1lll111l1_opy_.framework_name
            session.framework_version = bstack1l1lll111l1_opy_.framework_version
            session.framework_session_id = bstack11111111l1_opy_.bstack1111lll1l1_opy_(bstack1l1lll111l1_opy_, bstack11111111l1_opy_.bstack1l1lll1ll1l_opy_, bstack11ll1l_opy_ (u"ࠧࠨቂ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll111ll11_opy_(
        self,
        f: TestFramework,
        instance: bstack1llllll11l1_opy_,
        bstack11111ll111_opy_: Tuple[bstack1llll1111ll_opy_, bstack1llll1lll1l_opy_],
        *args,
        **kwargs
    ):
        bstack1l1ll1ll1l1_opy_ = f.bstack1111lll1l1_opy_(instance, bstack1llll111111_opy_.bstack1ll11ll11ll_opy_, [])
        if not bstack1l1ll1ll1l1_opy_:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠨࡧࡦࡶࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡰࡲࠤࡵࡧࡧࡦࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢቃ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠢࠣቄ"))
            return
        if len(bstack1l1ll1ll1l1_opy_) > 1:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠣࡩࡨࡸࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡧࡶ࡮ࡼࡥࡳ࠼ࠣࡿࡱ࡫࡮ࠩࡲࡤ࡫ࡪࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡴࠫࢀࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤቅ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠤࠥቆ"))
        bstack1l1ll1ll11l_opy_, bstack1ll11111l11_opy_ = bstack1l1ll1ll1l1_opy_[0]
        page = bstack1l1ll1ll11l_opy_()
        if not page:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡩࡸࡩࡷࡧࡵ࠾ࠥࡴ࡯ࠡࡲࡤ࡫ࡪࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥቇ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠦࠧቈ"))
            return
        return page
    def bstack1ll1ll111ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llllll11l1_opy_,
        bstack11111ll111_opy_: Tuple[bstack1llll1111ll_opy_, bstack1llll1lll1l_opy_],
        *args,
        **kwargs
    ):
        caps = {}
        bstack1l1lll11l11_opy_ = {}
        for bstack1l1lll111l1_opy_ in bstack11111111l1_opy_.bstack1111l1l11l_opy_.values():
            caps = bstack11111111l1_opy_.bstack1111lll1l1_opy_(bstack1l1lll111l1_opy_, bstack11111111l1_opy_.bstack1l1llll11ll_opy_, bstack11ll1l_opy_ (u"ࠧࠨ቉"))
        bstack1l1lll11l11_opy_[bstack11ll1l_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠦቊ")] = caps.get(bstack11ll1l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࠣቋ"), bstack11ll1l_opy_ (u"ࠣࠤቌ"))
        bstack1l1lll11l11_opy_[bstack11ll1l_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠣቍ")] = caps.get(bstack11ll1l_opy_ (u"ࠥࡳࡸࠨ቎"), bstack11ll1l_opy_ (u"ࠦࠧ቏"))
        bstack1l1lll11l11_opy_[bstack11ll1l_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢቐ")] = caps.get(bstack11ll1l_opy_ (u"ࠨ࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠥቑ"), bstack11ll1l_opy_ (u"ࠢࠣቒ"))
        bstack1l1lll11l11_opy_[bstack11ll1l_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠤቓ")] = caps.get(bstack11ll1l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠦቔ"), bstack11ll1l_opy_ (u"ࠥࠦቕ"))
        return bstack1l1lll11l11_opy_
    def bstack1lll1111l11_opy_(self, page: object, bstack1ll1ll11l1l_opy_, args={}):
        try:
            bstack1l1ll1ll111_opy_ = bstack11ll1l_opy_ (u"ࠦࠧࠨࠨࡧࡷࡱࡧࡹ࡯࡯࡯ࠢࠫ࠲࠳࠴ࡢࡴࡶࡤࡧࡰ࡙ࡤ࡬ࡃࡵ࡫ࡸ࠯ࠠࡼࡽࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡸࡥࡵࡷࡵࡲࠥࡴࡥࡸࠢࡓࡶࡴࡳࡩࡴࡧࠫࠬࡷ࡫ࡳࡰ࡮ࡹࡩ࠱ࠦࡲࡦ࡬ࡨࡧࡹ࠯ࠠ࠾ࡀࠣࡿࢀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡨࡳࡵࡣࡦ࡯ࡘࡪ࡫ࡂࡴࡪࡷ࠳ࡶࡵࡴࡪࠫࡶࡪࡹ࡯࡭ࡸࡨ࠭ࡀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢁࡦ࡯ࡡࡥࡳࡩࡿࡽࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࢂ࠯࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽࡾࠫࠫࡿࡦࡸࡧࡠ࡬ࡶࡳࡳࢃࠩࠣࠤࠥቖ")
            bstack1ll1ll11l1l_opy_ = bstack1ll1ll11l1l_opy_.replace(bstack11ll1l_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ቗"), bstack11ll1l_opy_ (u"ࠨࡢࡴࡶࡤࡧࡰ࡙ࡤ࡬ࡃࡵ࡫ࡸࠨቘ"))
            script = bstack1l1ll1ll111_opy_.format(fn_body=bstack1ll1ll11l1l_opy_, arg_json=json.dumps(args))
            return page.evaluate(script)
        except Exception as e:
            self.logger.error(bstack11ll1l_opy_ (u"ࠢࡢ࠳࠴ࡽࡤࡹࡣࡳ࡫ࡳࡸࡤ࡫ࡸࡦࡥࡸࡸࡪࡀࠠࡆࡴࡵࡳࡷࠦࡥࡹࡧࡦࡹࡹ࡯࡮ࡨࠢࡷ࡬ࡪࠦࡡ࠲࠳ࡼࠤࡸࡩࡲࡪࡲࡷ࠰ࠥࠨ቙") + str(e) + bstack11ll1l_opy_ (u"ࠣࠤቚ"))