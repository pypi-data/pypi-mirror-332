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
import os
import threading
import asyncio
from browserstack_sdk.sdk_cli.bstack11111l1lll_opy_ import (
    bstack1111l1l111_opy_,
    bstack1111ll111l_opy_,
    bstack1111l1llll_opy_,
    bstack11111l11ll_opy_,
)
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1ll1111llll_opy_, bstack11l111111_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1ll1_opy_ import bstack111111l111_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1lll1ll_opy_, bstack1lll1lll11l_opy_, bstack1llll11lll1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1111l1_opy_ import bstack1lll1l11l1l_opy_
from browserstack_sdk.sdk_cli.bstack1ll1l1111l1_opy_ import bstack1ll1l111l11_opy_
from typing import Tuple, List, Any
from bstack_utils.bstack11ll1l1l1_opy_ import bstack1l1111ll11_opy_, bstack111111ll1_opy_, bstack1lll1lllll_opy_
from browserstack_sdk import sdk_pb2 as structs
class bstack1111111l11_opy_(bstack1ll1l111l11_opy_):
    bstack1l1lll11ll1_opy_ = bstack11lll_opy_ (u"ࠣࡶࡨࡷࡹࡥࡤࡳ࡫ࡹࡩࡷࡹࠢሆ")
    bstack1ll111lllll_opy_ = bstack11lll_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࡳࠣሇ")
    bstack1l1ll1ll1ll_opy_ = bstack11lll_opy_ (u"ࠥࡲࡴࡴ࡟ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡷࡪࡹࡳࡪࡱࡱࡷࠧለ")
    bstack1l1lll11l1l_opy_ = bstack11lll_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡶࡩࡸࡹࡩࡰࡰࡶࠦሉ")
    bstack1l1ll1lll1l_opy_ = bstack11lll_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡣࡷ࡫ࡦࡴࠤሊ")
    bstack1ll11l11ll1_opy_ = bstack11lll_opy_ (u"ࠨࡣࡣࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡨࡸࡥࡢࡶࡨࡨࠧላ")
    bstack1l1lll11l11_opy_ = bstack11lll_opy_ (u"ࠢࡤࡤࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡴࡡ࡮ࡧࠥሌ")
    bstack1l1ll1l1lll_opy_ = bstack11lll_opy_ (u"ࠣࡥࡥࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡳࡵࡣࡷࡹࡸࠨል")
    def __init__(self):
        super().__init__(bstack1ll1l11l111_opy_=self.bstack1l1lll11ll1_opy_, frameworks=[bstack111111l111_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1ll1l1lll1l_opy_((bstack1lll1lll1ll_opy_.BEFORE_EACH, bstack1lll1lll11l_opy_.POST), self.bstack1l1ll1lllll_opy_)
        if bstack11l111111_opy_():
            TestFramework.bstack1ll1l1lll1l_opy_((bstack1lll1lll1ll_opy_.TEST, bstack1lll1lll11l_opy_.POST), self.bstack1ll1lll1lll_opy_)
        else:
            TestFramework.bstack1ll1l1lll1l_opy_((bstack1lll1lll1ll_opy_.TEST, bstack1lll1lll11l_opy_.PRE), self.bstack1ll1lll1lll_opy_)
        TestFramework.bstack1ll1l1lll1l_opy_((bstack1lll1lll1ll_opy_.TEST, bstack1lll1lll11l_opy_.POST), self.bstack1lll111l11l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l1ll1lllll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11lll1_opy_,
        bstack1111llll11_opy_: Tuple[bstack1lll1lll1ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        bstack1l1ll1ll1l1_opy_ = self.bstack1l1ll1ll111_opy_(instance.context)
        if not bstack1l1ll1ll1l1_opy_:
            self.logger.debug(bstack11lll_opy_ (u"ࠤࡶࡩࡹࡥࡡࡤࡶ࡬ࡺࡪࡥࡰࡢࡩࡨ࠾ࠥࡴ࡯ࠡࡲࡤ࡫ࡪࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࠢሎ") + str(bstack1111llll11_opy_) + bstack11lll_opy_ (u"ࠥࠦሏ"))
            return
        f.bstack1111ll11ll_opy_(instance, bstack1111111l11_opy_.bstack1ll111lllll_opy_, bstack1l1ll1ll1l1_opy_)
    def bstack1l1ll1ll111_opy_(self, context: bstack11111l11ll_opy_, bstack1l1ll1llll1_opy_= True):
        if bstack1l1ll1llll1_opy_:
            bstack1l1ll1ll1l1_opy_ = self.bstack1ll1l11ll11_opy_(context, reverse=True)
        else:
            bstack1l1ll1ll1l1_opy_ = self.bstack1ll1l11111l_opy_(context, reverse=True)
        return [f for f in bstack1l1ll1ll1l1_opy_ if f[1].state != bstack1111l1l111_opy_.QUIT]
    def bstack1ll1lll1lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11lll1_opy_,
        bstack1111llll11_opy_: Tuple[bstack1lll1lll1ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l1ll1lllll_opy_(f, instance, bstack1111llll11_opy_, *args, **kwargs)
        if not bstack1ll1111llll_opy_:
            self.logger.debug(bstack11lll_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢሐ") + str(kwargs) + bstack11lll_opy_ (u"ࠧࠨሑ"))
            return
        bstack1l1ll1ll1l1_opy_ = f.bstack11111l11l1_opy_(instance, bstack1111111l11_opy_.bstack1ll111lllll_opy_, [])
        if not bstack1l1ll1ll1l1_opy_:
            self.logger.debug(bstack11lll_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤሒ") + str(kwargs) + bstack11lll_opy_ (u"ࠢࠣሓ"))
            return
        if len(bstack1l1ll1ll1l1_opy_) > 1:
            self.logger.debug(
                bstack1lll11lllll_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡿࡱ࡫࡮ࠩࡲࡤ࡫ࡪࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡴࠫࢀࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࡽ࡮ࡻࡦࡸࡧࡴࡿࠥሔ"))
        bstack1l1lll1111l_opy_, bstack1l1llllll1l_opy_ = bstack1l1ll1ll1l1_opy_[0]
        page = bstack1l1lll1111l_opy_()
        if not page:
            self.logger.debug(bstack11lll_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡱࡣࡪࡩࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤሕ") + str(kwargs) + bstack11lll_opy_ (u"ࠥࠦሖ"))
            return
        bstack11lllllll_opy_ = getattr(args[0], bstack11lll_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦሗ"), None)
        try:
            page.evaluate(bstack11lll_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨመ"),
                        bstack11lll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠪሙ") + json.dumps(
                            bstack11lllllll_opy_) + bstack11lll_opy_ (u"ࠢࡾࡿࠥሚ"))
        except Exception as e:
            self.logger.debug(bstack11lll_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣࡿࢂࠨማ"), e)
    def bstack1lll111l11l_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11lll1_opy_,
        bstack1111llll11_opy_: Tuple[bstack1lll1lll1ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l1ll1lllll_opy_(f, instance, bstack1111llll11_opy_, *args, **kwargs)
        if not bstack1ll1111llll_opy_:
            self.logger.debug(bstack11lll_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧሜ") + str(kwargs) + bstack11lll_opy_ (u"ࠥࠦም"))
            return
        bstack1l1ll1ll1l1_opy_ = f.bstack11111l11l1_opy_(instance, bstack1111111l11_opy_.bstack1ll111lllll_opy_, [])
        if not bstack1l1ll1ll1l1_opy_:
            self.logger.debug(bstack11lll_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢሞ") + str(kwargs) + bstack11lll_opy_ (u"ࠧࠨሟ"))
            return
        if len(bstack1l1ll1ll1l1_opy_) > 1:
            self.logger.debug(
                bstack1lll11lllll_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡽ࡯ࡩࡳ࠮ࡰࡢࡩࡨࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡹࠩࡾࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࡻ࡬ࡹࡤࡶ࡬ࡹࡽࠣሠ"))
        bstack1l1lll1111l_opy_, bstack1l1llllll1l_opy_ = bstack1l1ll1ll1l1_opy_[0]
        page = bstack1l1lll1111l_opy_()
        if not page:
            self.logger.debug(bstack11lll_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡶࡡࡨࡧࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢሡ") + str(kwargs) + bstack11lll_opy_ (u"ࠣࠤሢ"))
            return
        status = f.bstack11111l11l1_opy_(instance, TestFramework.bstack1l1ll1lll11_opy_, None)
        if not status:
            self.logger.debug(bstack11lll_opy_ (u"ࠤࡱࡳࠥࡹࡴࡢࡶࡸࡷࠥ࡬࡯ࡳࠢࡷࡩࡸࡺࠬࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࠧሣ") + str(bstack1111llll11_opy_) + bstack11lll_opy_ (u"ࠥࠦሤ"))
            return
        bstack1l1lll111l1_opy_ = {bstack11lll_opy_ (u"ࠦࡸࡺࡡࡵࡷࡶࠦሥ"): status.lower()}
        bstack1l1ll1ll11l_opy_ = f.bstack11111l11l1_opy_(instance, TestFramework.bstack1l1ll1l1ll1_opy_, None)
        if status.lower() == bstack11lll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬሦ") and bstack1l1ll1ll11l_opy_ is not None:
            bstack1l1lll111l1_opy_[bstack11lll_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭ሧ")] = bstack1l1ll1ll11l_opy_[0][bstack11lll_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧࠪረ")][0] if isinstance(bstack1l1ll1ll11l_opy_, list) else str(bstack1l1ll1ll11l_opy_)
        try:
              page.evaluate(
                    bstack11lll_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤሩ"),
                    bstack11lll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࠧሪ")
                    + json.dumps(bstack1l1lll111l1_opy_)
                    + bstack11lll_opy_ (u"ࠥࢁࠧራ")
                )
        except Exception as e:
            self.logger.debug(bstack11lll_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡵࡷࡥࡹࡻࡳࠡࡽࢀࠦሬ"), e)
    def bstack1ll1111l111_opy_(
        self,
        instance: bstack1llll11lll1_opy_,
        f: TestFramework,
        bstack1111llll11_opy_: Tuple[bstack1lll1lll1ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l1ll1lllll_opy_(f, instance, bstack1111llll11_opy_, *args, **kwargs)
        if not bstack1ll1111llll_opy_:
            self.logger.debug(
                bstack1lll11lllll_opy_ (u"ࠧࡳࡡࡳ࡭ࡢࡳ࠶࠷ࡹࡠࡵࡼࡲࡨࡀࠠ࡯ࡱࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࢀࡱࡷࡢࡴࡪࡷࢂࠨር"))
            return
        bstack1l1ll1ll1l1_opy_ = f.bstack11111l11l1_opy_(instance, bstack1111111l11_opy_.bstack1ll111lllll_opy_, [])
        if not bstack1l1ll1ll1l1_opy_:
            self.logger.debug(bstack11lll_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤሮ") + str(kwargs) + bstack11lll_opy_ (u"ࠢࠣሯ"))
            return
        if len(bstack1l1ll1ll1l1_opy_) > 1:
            self.logger.debug(
                bstack1lll11lllll_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡿࡱ࡫࡮ࠩࡲࡤ࡫ࡪࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡴࠫࢀࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࡽ࡮ࡻࡦࡸࡧࡴࡿࠥሰ"))
        bstack1l1lll1111l_opy_, bstack1l1llllll1l_opy_ = bstack1l1ll1ll1l1_opy_[0]
        page = bstack1l1lll1111l_opy_()
        if not page:
            self.logger.debug(bstack11lll_opy_ (u"ࠤࡰࡥࡷࡱ࡟ࡰ࠳࠴ࡽࡤࡹࡹ࡯ࡥ࠽ࠤࡳࡵࠠࡱࡣࡪࡩࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤሱ") + str(kwargs) + bstack11lll_opy_ (u"ࠥࠦሲ"))
            return
        timestamp = int(time.time() * 1000)
        data = bstack11lll_opy_ (u"ࠦࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࡗࡾࡴࡣ࠻ࠤሳ") + str(timestamp)
        try:
            page.evaluate(
                bstack11lll_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨሴ"),
                bstack11lll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫስ").format(
                    json.dumps(
                        {
                            bstack11lll_opy_ (u"ࠢࡢࡥࡷ࡭ࡴࡴࠢሶ"): bstack11lll_opy_ (u"ࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥሷ"),
                            bstack11lll_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧሸ"): {
                                bstack11lll_opy_ (u"ࠥࡸࡾࡶࡥࠣሹ"): bstack11lll_opy_ (u"ࠦࡆࡴ࡮ࡰࡶࡤࡸ࡮ࡵ࡮ࠣሺ"),
                                bstack11lll_opy_ (u"ࠧࡪࡡࡵࡣࠥሻ"): data,
                                bstack11lll_opy_ (u"ࠨ࡬ࡦࡸࡨࡰࠧሼ"): bstack11lll_opy_ (u"ࠢࡥࡧࡥࡹ࡬ࠨሽ")
                            }
                        }
                    )
                )
            )
        except Exception as e:
            self.logger.debug(bstack11lll_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡴ࠷࠱ࡺࠢࡤࡲࡳࡵࡴࡢࡶ࡬ࡳࡳࠦ࡭ࡢࡴ࡮࡭ࡳ࡭ࠠࡼࡿࠥሾ"), e)
    def bstack1ll11l111ll_opy_(
        self,
        instance: bstack1llll11lll1_opy_,
        f: TestFramework,
        bstack1111llll11_opy_: Tuple[bstack1lll1lll1ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l1ll1lllll_opy_(f, instance, bstack1111llll11_opy_, *args, **kwargs)
        if f.bstack11111l11l1_opy_(instance, bstack1111111l11_opy_.bstack1ll11l11ll1_opy_, False):
            return
        self.bstack111l11l11l_opy_()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.bstack11111l11l1_opy_(instance, TestFramework.bstack1ll1lll1111_opy_)
        req.test_framework_name = TestFramework.bstack11111l11l1_opy_(instance, TestFramework.bstack1ll1ll1l111_opy_)
        req.test_framework_version = TestFramework.bstack11111l11l1_opy_(instance, TestFramework.bstack1ll11l1l111_opy_)
        req.test_framework_state = bstack1111llll11_opy_[0].name
        req.test_hook_state = bstack1111llll11_opy_[1].name
        req.test_uuid = TestFramework.bstack11111l11l1_opy_(instance, TestFramework.bstack1ll1llll1l1_opy_)
        for bstack1l1lll11111_opy_ in bstack1lll1l11l1l_opy_.bstack1111l11lll_opy_.values():
            session = req.automation_sessions.add()
            session.provider = (
                bstack11lll_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠣሿ")
                if bstack1ll1111llll_opy_
                else bstack11lll_opy_ (u"ࠥࡹࡳࡱ࡮ࡰࡹࡱࡣ࡬ࡸࡩࡥࠤቀ")
            )
            session.ref = bstack1l1lll11111_opy_.ref()
            session.hub_url = bstack1lll1l11l1l_opy_.bstack11111l11l1_opy_(bstack1l1lll11111_opy_, bstack1lll1l11l1l_opy_.bstack1l1llll1l11_opy_, bstack11lll_opy_ (u"ࠦࠧቁ"))
            session.framework_name = bstack1l1lll11111_opy_.framework_name
            session.framework_version = bstack1l1lll11111_opy_.framework_version
            session.framework_session_id = bstack1lll1l11l1l_opy_.bstack11111l11l1_opy_(bstack1l1lll11111_opy_, bstack1lll1l11l1l_opy_.bstack1l1llll1l1l_opy_, bstack11lll_opy_ (u"ࠧࠨቂ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1ll1ll11111_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11lll1_opy_,
        bstack1111llll11_opy_: Tuple[bstack1lll1lll1ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs
    ):
        bstack1l1ll1ll1l1_opy_ = f.bstack11111l11l1_opy_(instance, bstack1111111l11_opy_.bstack1ll111lllll_opy_, [])
        if not bstack1l1ll1ll1l1_opy_:
            self.logger.debug(bstack11lll_opy_ (u"ࠨࡧࡦࡶࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡰࡲࠤࡵࡧࡧࡦࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢቃ") + str(kwargs) + bstack11lll_opy_ (u"ࠢࠣቄ"))
            return
        if len(bstack1l1ll1ll1l1_opy_) > 1:
            self.logger.debug(bstack11lll_opy_ (u"ࠣࡩࡨࡸࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡧࡶ࡮ࡼࡥࡳ࠼ࠣࡿࡱ࡫࡮ࠩࡲࡤ࡫ࡪࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡴࠫࢀࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤቅ") + str(kwargs) + bstack11lll_opy_ (u"ࠤࠥቆ"))
        bstack1l1lll1111l_opy_, bstack1l1llllll1l_opy_ = bstack1l1ll1ll1l1_opy_[0]
        page = bstack1l1lll1111l_opy_()
        if not page:
            self.logger.debug(bstack11lll_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡩࡸࡩࡷࡧࡵ࠾ࠥࡴ࡯ࠡࡲࡤ࡫ࡪࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥቇ") + str(kwargs) + bstack11lll_opy_ (u"ࠦࠧቈ"))
            return
        return page
    def bstack1ll1l1lllll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11lll1_opy_,
        bstack1111llll11_opy_: Tuple[bstack1lll1lll1ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs
    ):
        caps = {}
        bstack1l1ll1l1l1l_opy_ = {}
        for bstack1l1lll11111_opy_ in bstack1lll1l11l1l_opy_.bstack1111l11lll_opy_.values():
            caps = bstack1lll1l11l1l_opy_.bstack11111l11l1_opy_(bstack1l1lll11111_opy_, bstack1lll1l11l1l_opy_.bstack1l1lll1l1l1_opy_, bstack11lll_opy_ (u"ࠧࠨ቉"))
        bstack1l1ll1l1l1l_opy_[bstack11lll_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠦቊ")] = caps.get(bstack11lll_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࠣቋ"), bstack11lll_opy_ (u"ࠣࠤቌ"))
        bstack1l1ll1l1l1l_opy_[bstack11lll_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠣቍ")] = caps.get(bstack11lll_opy_ (u"ࠥࡳࡸࠨ቎"), bstack11lll_opy_ (u"ࠦࠧ቏"))
        bstack1l1ll1l1l1l_opy_[bstack11lll_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢቐ")] = caps.get(bstack11lll_opy_ (u"ࠨ࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠥቑ"), bstack11lll_opy_ (u"ࠢࠣቒ"))
        bstack1l1ll1l1l1l_opy_[bstack11lll_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠤቓ")] = caps.get(bstack11lll_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠦቔ"), bstack11lll_opy_ (u"ࠥࠦቕ"))
        return bstack1l1ll1l1l1l_opy_
    def bstack1ll1l1llll1_opy_(self, page: object, bstack1lll111l1ll_opy_, args={}):
        try:
            bstack1l1lll111ll_opy_ = bstack11lll_opy_ (u"ࠦࠧࠨࠨࡧࡷࡱࡧࡹ࡯࡯࡯ࠢࠫ࠲࠳࠴ࡢࡴࡶࡤࡧࡰ࡙ࡤ࡬ࡃࡵ࡫ࡸ࠯ࠠࡼࡽࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡸࡥࡵࡷࡵࡲࠥࡴࡥࡸࠢࡓࡶࡴࡳࡩࡴࡧࠫࠬࡷ࡫ࡳࡰ࡮ࡹࡩ࠱ࠦࡲࡦ࡬ࡨࡧࡹ࠯ࠠ࠾ࡀࠣࡿࢀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡨࡳࡵࡣࡦ࡯ࡘࡪ࡫ࡂࡴࡪࡷ࠳ࡶࡵࡴࡪࠫࡶࡪࡹ࡯࡭ࡸࡨ࠭ࡀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢁࡦ࡯ࡡࡥࡳࡩࡿࡽࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࢂ࠯࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽࡾࠫࠫࡿࡦࡸࡧࡠ࡬ࡶࡳࡳࢃࠩࠣࠤࠥቖ")
            bstack1lll111l1ll_opy_ = bstack1lll111l1ll_opy_.replace(bstack11lll_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ቗"), bstack11lll_opy_ (u"ࠨࡢࡴࡶࡤࡧࡰ࡙ࡤ࡬ࡃࡵ࡫ࡸࠨቘ"))
            script = bstack1l1lll111ll_opy_.format(fn_body=bstack1lll111l1ll_opy_, arg_json=json.dumps(args))
            return page.evaluate(script)
        except Exception as e:
            self.logger.error(bstack11lll_opy_ (u"ࠢࡢ࠳࠴ࡽࡤࡹࡣࡳ࡫ࡳࡸࡤ࡫ࡸࡦࡥࡸࡸࡪࡀࠠࡆࡴࡵࡳࡷࠦࡥࡹࡧࡦࡹࡹ࡯࡮ࡨࠢࡷ࡬ࡪࠦࡡ࠲࠳ࡼࠤࡸࡩࡲࡪࡲࡷ࠰ࠥࠨ቙") + str(e) + bstack11lll_opy_ (u"ࠣࠤቚ"))