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
import logging
import os
import datetime
import threading
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack1l11l11ll1l_opy_, bstack1l11l11l1l1_opy_, bstack1lll111l_opy_, bstack111ll1l1ll_opy_, bstack11lll1111ll_opy_, bstack11lllll1111_opy_, bstack11lll1l1lll_opy_, bstack1l1ll1111l_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11l1111ll11_opy_ import bstack11l1111l11l_opy_
import bstack_utils.bstack1l1l11l1_opy_ as bstack1llll1ll_opy_
from bstack_utils.bstack11l1l1111l_opy_ import bstack111111ll_opy_
import bstack_utils.accessibility as bstack1lllll11ll_opy_
from bstack_utils.bstack1111ll1l1_opy_ import bstack1111ll1l1_opy_
from bstack_utils.bstack11l11l1ll1_opy_ import bstack111llll1ll_opy_
bstack111ll1lll11_opy_ = bstack11ll1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡥࡲࡰࡱ࡫ࡣࡵࡱࡵ࠱ࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧᲽ")
logger = logging.getLogger(__name__)
class bstack1ll11l1l11_opy_:
    bstack11l1111ll11_opy_ = None
    bs_config = None
    bstack1ll111l11l_opy_ = None
    @classmethod
    @bstack111ll1l1ll_opy_(class_method=True)
    @measure(event_name=EVENTS.bstack1l111l11l1l_opy_, stage=STAGE.bstack1111l111_opy_)
    def launch(cls, bs_config, bstack1ll111l11l_opy_):
        cls.bs_config = bs_config
        cls.bstack1ll111l11l_opy_ = bstack1ll111l11l_opy_
        try:
            cls.bstack111lll111l1_opy_()
            bstack1l11l111lll_opy_ = bstack1l11l11ll1l_opy_(bs_config)
            bstack1l111ll1ll1_opy_ = bstack1l11l11l1l1_opy_(bs_config)
            data = bstack1llll1ll_opy_.bstack111lll1l1l1_opy_(bs_config, bstack1ll111l11l_opy_)
            config = {
                bstack11ll1l_opy_ (u"ࠨࡣࡸࡸ࡭࠭Ჾ"): (bstack1l11l111lll_opy_, bstack1l111ll1ll1_opy_),
                bstack11ll1l_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪᲿ"): cls.default_headers()
            }
            response = bstack1lll111l_opy_(bstack11ll1l_opy_ (u"ࠪࡔࡔ࡙ࡔࠨ᳀"), cls.request_url(bstack11ll1l_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠵࠳ࡧࡻࡩ࡭ࡦࡶࠫ᳁")), data, config)
            if response.status_code != 200:
                bstack1111111lll_opy_ = response.json()
                if bstack1111111lll_opy_[bstack11ll1l_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭᳂")] == False:
                    cls.bstack111ll1llll1_opy_(bstack1111111lll_opy_)
                    return
                cls.bstack111ll1ll1l1_opy_(bstack1111111lll_opy_[bstack11ll1l_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭᳃")])
                cls.bstack111lll11111_opy_(bstack1111111lll_opy_[bstack11ll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ᳄")])
                return None
            bstack111lll1l11l_opy_ = cls.bstack111ll1l11ll_opy_(response)
            return bstack111lll1l11l_opy_
        except Exception as error:
            logger.error(bstack11ll1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥࡨࡵࡪ࡮ࡧࠤ࡫ࡵࡲࠡࡖࡨࡷࡹࡎࡵࡣ࠼ࠣࡿࢂࠨ᳅").format(str(error)))
            return None
    @classmethod
    @bstack111ll1l1ll_opy_(class_method=True)
    def stop(cls, bstack111ll1l1l11_opy_=None):
        if not bstack111111ll_opy_.on() and not bstack1lllll11ll_opy_.on():
            return
        if os.environ.get(bstack11ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭᳆")) == bstack11ll1l_opy_ (u"ࠥࡲࡺࡲ࡬ࠣ᳇") or os.environ.get(bstack11ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ᳈")) == bstack11ll1l_opy_ (u"ࠧࡴࡵ࡭࡮ࠥ᳉"):
            logger.error(bstack11ll1l_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡴࡰࡲࠣࡦࡺ࡯࡬ࡥࠢࡵࡩࡶࡻࡥࡴࡶࠣࡸࡴࠦࡔࡦࡵࡷࡌࡺࡨ࠺ࠡࡏ࡬ࡷࡸ࡯࡮ࡨࠢࡤࡹࡹ࡮ࡥ࡯ࡶ࡬ࡧࡦࡺࡩࡰࡰࠣࡸࡴࡱࡥ࡯ࠩ᳊"))
            return {
                bstack11ll1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ᳋"): bstack11ll1l_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ᳌"),
                bstack11ll1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ᳍"): bstack11ll1l_opy_ (u"ࠪࡘࡴࡱࡥ࡯࠱ࡥࡹ࡮ࡲࡤࡊࡆࠣ࡭ࡸࠦࡵ࡯ࡦࡨࡪ࡮ࡴࡥࡥ࠮ࠣࡦࡺ࡯࡬ࡥࠢࡦࡶࡪࡧࡴࡪࡱࡱࠤࡲ࡯ࡧࡩࡶࠣ࡬ࡦࡼࡥࠡࡨࡤ࡭ࡱ࡫ࡤࠨ᳎")
            }
        try:
            cls.bstack11l1111ll11_opy_.shutdown()
            data = {
                bstack11ll1l_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ᳏"): bstack1l1ll1111l_opy_()
            }
            if not bstack111ll1l1l11_opy_ is None:
                data[bstack11ll1l_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟࡮ࡧࡷࡥࡩࡧࡴࡢࠩ᳐")] = [{
                    bstack11ll1l_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭᳑"): bstack11ll1l_opy_ (u"ࠧࡶࡵࡨࡶࡤࡱࡩ࡭࡮ࡨࡨࠬ᳒"),
                    bstack11ll1l_opy_ (u"ࠨࡵ࡬࡫ࡳࡧ࡬ࠨ᳓"): bstack111ll1l1l11_opy_
                }]
            config = {
                bstack11ll1l_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵ᳔ࠪ"): cls.default_headers()
            }
            bstack11lll1lll1l_opy_ = bstack11ll1l_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂ࠵ࡳࡵࡱࡳ᳕ࠫ").format(os.environ[bstack11ll1l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠤ᳖")])
            bstack111ll1lllll_opy_ = cls.request_url(bstack11lll1lll1l_opy_)
            response = bstack1lll111l_opy_(bstack11ll1l_opy_ (u"ࠬࡖࡕࡕ᳗ࠩ"), bstack111ll1lllll_opy_, data, config)
            if not response.ok:
                raise Exception(bstack11ll1l_opy_ (u"ࠨࡓࡵࡱࡳࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡴ࡯ࡵࠢࡲ࡯᳘ࠧ"))
        except Exception as error:
            logger.error(bstack11ll1l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡵࡱࡳࠤࡧࡻࡩ࡭ࡦࠣࡶࡪࡷࡵࡦࡵࡷࠤࡹࡵࠠࡕࡧࡶࡸࡍࡻࡢ࠻࠼᳙ࠣࠦ") + str(error))
            return {
                bstack11ll1l_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ᳚"): bstack11ll1l_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ᳛"),
                bstack11ll1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨ᳜ࠫ"): str(error)
            }
    @classmethod
    @bstack111ll1l1ll_opy_(class_method=True)
    def bstack111ll1l11ll_opy_(cls, response):
        bstack1111111lll_opy_ = response.json() if not isinstance(response, dict) else response
        bstack111lll1l11l_opy_ = {}
        if bstack1111111lll_opy_.get(bstack11ll1l_opy_ (u"ࠫ࡯ࡽࡴࠨ᳝")) is None:
            os.environ[bstack11ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕ᳞ࠩ")] = bstack11ll1l_opy_ (u"࠭࡮ࡶ࡮࡯᳟ࠫ")
        else:
            os.environ[bstack11ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ᳠")] = bstack1111111lll_opy_.get(bstack11ll1l_opy_ (u"ࠨ࡬ࡺࡸࠬ᳡"), bstack11ll1l_opy_ (u"ࠩࡱࡹࡱࡲ᳢ࠧ"))
        os.environ[bstack11ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ᳣")] = bstack1111111lll_opy_.get(bstack11ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ᳤࠭"), bstack11ll1l_opy_ (u"ࠬࡴࡵ࡭࡮᳥ࠪ"))
        logger.info(bstack11ll1l_opy_ (u"࠭ࡔࡦࡵࡷ࡬ࡺࡨࠠࡴࡶࡤࡶࡹ࡫ࡤࠡࡹ࡬ࡸ࡭ࠦࡩࡥ࠼᳦ࠣࠫ") + os.getenv(bstack11ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈ᳧ࠬ")));
        if bstack111111ll_opy_.bstack111lll11lll_opy_(cls.bs_config, cls.bstack1ll111l11l_opy_.get(bstack11ll1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡺࡹࡥࡥ᳨ࠩ"), bstack11ll1l_opy_ (u"ࠩࠪᳩ"))) is True:
            bstack111ll1ll111_opy_, build_hashed_id, bstack111lll1ll11_opy_ = cls.bstack111ll1l1lll_opy_(bstack1111111lll_opy_)
            if bstack111ll1ll111_opy_ != None and build_hashed_id != None:
                bstack111lll1l11l_opy_[bstack11ll1l_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪᳪ")] = {
                    bstack11ll1l_opy_ (u"ࠫ࡯ࡽࡴࡠࡶࡲ࡯ࡪࡴࠧᳫ"): bstack111ll1ll111_opy_,
                    bstack11ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧᳬ"): build_hashed_id,
                    bstack11ll1l_opy_ (u"࠭ࡡ࡭࡮ࡲࡻࡤࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵ᳭ࠪ"): bstack111lll1ll11_opy_
                }
            else:
                bstack111lll1l11l_opy_[bstack11ll1l_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧᳮ")] = {}
        else:
            bstack111lll1l11l_opy_[bstack11ll1l_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨᳯ")] = {}
        if bstack1lllll11ll_opy_.bstack1l111lll1l1_opy_(cls.bs_config) is True:
            bstack111ll1ll11l_opy_, build_hashed_id = cls.bstack111lll1111l_opy_(bstack1111111lll_opy_)
            if bstack111ll1ll11l_opy_ != None and build_hashed_id != None:
                bstack111lll1l11l_opy_[bstack11ll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᳰ")] = {
                    bstack11ll1l_opy_ (u"ࠪࡥࡺࡺࡨࡠࡶࡲ࡯ࡪࡴࠧᳱ"): bstack111ll1ll11l_opy_,
                    bstack11ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ᳲ"): build_hashed_id,
                }
            else:
                bstack111lll1l11l_opy_[bstack11ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᳳ")] = {}
        else:
            bstack111lll1l11l_opy_[bstack11ll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭᳴")] = {}
        if bstack111lll1l11l_opy_[bstack11ll1l_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧᳵ")].get(bstack11ll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪᳶ")) != None or bstack111lll1l11l_opy_[bstack11ll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ᳷")].get(bstack11ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ᳸")) != None:
            cls.bstack111lll11l11_opy_(bstack1111111lll_opy_.get(bstack11ll1l_opy_ (u"ࠫ࡯ࡽࡴࠨ᳹")), bstack1111111lll_opy_.get(bstack11ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧᳺ")))
        return bstack111lll1l11l_opy_
    @classmethod
    def bstack111ll1l1lll_opy_(cls, bstack1111111lll_opy_):
        if bstack1111111lll_opy_.get(bstack11ll1l_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭᳻")) == None:
            cls.bstack111ll1ll1l1_opy_()
            return [None, None, None]
        if bstack1111111lll_opy_[bstack11ll1l_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧ᳼")][bstack11ll1l_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩ᳽")] != True:
            cls.bstack111ll1ll1l1_opy_(bstack1111111lll_opy_[bstack11ll1l_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ᳾")])
            return [None, None, None]
        logger.debug(bstack11ll1l_opy_ (u"ࠪࡘࡪࡹࡴࠡࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠡࡄࡸ࡭ࡱࡪࠠࡤࡴࡨࡥࡹ࡯࡯࡯ࠢࡖࡹࡨࡩࡥࡴࡵࡩࡹࡱࠧࠧ᳿"))
        os.environ[bstack11ll1l_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡄࡑࡐࡔࡑࡋࡔࡆࡆࠪᴀ")] = bstack11ll1l_opy_ (u"ࠬࡺࡲࡶࡧࠪᴁ")
        if bstack1111111lll_opy_.get(bstack11ll1l_opy_ (u"࠭ࡪࡸࡶࠪᴂ")):
            os.environ[bstack11ll1l_opy_ (u"ࠧࡄࡔࡈࡈࡊࡔࡔࡊࡃࡏࡗࡤࡌࡏࡓࡡࡆࡖࡆ࡙ࡈࡠࡔࡈࡔࡔࡘࡔࡊࡐࡊࠫᴃ")] = json.dumps({
                bstack11ll1l_opy_ (u"ࠨࡷࡶࡩࡷࡴࡡ࡮ࡧࠪᴄ"): bstack1l11l11ll1l_opy_(cls.bs_config),
                bstack11ll1l_opy_ (u"ࠩࡳࡥࡸࡹࡷࡰࡴࡧࠫᴅ"): bstack1l11l11l1l1_opy_(cls.bs_config)
            })
        if bstack1111111lll_opy_.get(bstack11ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬᴆ")):
            os.environ[bstack11ll1l_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡉࡃࡖࡌࡊࡊ࡟ࡊࡆࠪᴇ")] = bstack1111111lll_opy_[bstack11ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧᴈ")]
        if bstack1111111lll_opy_[bstack11ll1l_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ᴉ")].get(bstack11ll1l_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨᴊ"), {}).get(bstack11ll1l_opy_ (u"ࠨࡣ࡯ࡰࡴࡽ࡟ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࡷࠬᴋ")):
            os.environ[bstack11ll1l_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡁࡍࡎࡒ࡛ࡤ࡙ࡃࡓࡇࡈࡒࡘࡎࡏࡕࡕࠪᴌ")] = str(bstack1111111lll_opy_[bstack11ll1l_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪᴍ")][bstack11ll1l_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬᴎ")][bstack11ll1l_opy_ (u"ࠬࡧ࡬࡭ࡱࡺࡣࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࡴࠩᴏ")])
        else:
            os.environ[bstack11ll1l_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡅࡑࡒࡏࡘࡡࡖࡇࡗࡋࡅࡏࡕࡋࡓ࡙࡙ࠧᴐ")] = bstack11ll1l_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧᴑ")
        return [bstack1111111lll_opy_[bstack11ll1l_opy_ (u"ࠨ࡬ࡺࡸࠬᴒ")], bstack1111111lll_opy_[bstack11ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫᴓ")], os.environ[bstack11ll1l_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡂࡎࡏࡓ࡜ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࡖࠫᴔ")]]
    @classmethod
    def bstack111lll1111l_opy_(cls, bstack1111111lll_opy_):
        if bstack1111111lll_opy_.get(bstack11ll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᴕ")) == None:
            cls.bstack111lll11111_opy_()
            return [None, None]
        if bstack1111111lll_opy_[bstack11ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᴖ")][bstack11ll1l_opy_ (u"࠭ࡳࡶࡥࡦࡩࡸࡹࠧᴗ")] != True:
            cls.bstack111lll11111_opy_(bstack1111111lll_opy_[bstack11ll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧᴘ")])
            return [None, None]
        if bstack1111111lll_opy_[bstack11ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨᴙ")].get(bstack11ll1l_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪᴚ")):
            logger.debug(bstack11ll1l_opy_ (u"ࠪࡘࡪࡹࡴࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡄࡸ࡭ࡱࡪࠠࡤࡴࡨࡥࡹ࡯࡯࡯ࠢࡖࡹࡨࡩࡥࡴࡵࡩࡹࡱࠧࠧᴛ"))
            parsed = json.loads(os.getenv(bstack11ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬᴜ"), bstack11ll1l_opy_ (u"ࠬࢁࡽࠨᴝ")))
            capabilities = bstack1llll1ll_opy_.bstack111lll1l1ll_opy_(bstack1111111lll_opy_[bstack11ll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᴞ")][bstack11ll1l_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨᴟ")][bstack11ll1l_opy_ (u"ࠨࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧᴠ")], bstack11ll1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᴡ"), bstack11ll1l_opy_ (u"ࠪࡺࡦࡲࡵࡦࠩᴢ"))
            bstack111ll1ll11l_opy_ = capabilities[bstack11ll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡘࡴࡱࡥ࡯ࠩᴣ")]
            os.environ[bstack11ll1l_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪᴤ")] = bstack111ll1ll11l_opy_
            parsed[bstack11ll1l_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᴥ")] = capabilities[bstack11ll1l_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨᴦ")]
            os.environ[bstack11ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩᴧ")] = json.dumps(parsed)
            scripts = bstack1llll1ll_opy_.bstack111lll1l1ll_opy_(bstack1111111lll_opy_[bstack11ll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᴨ")][bstack11ll1l_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫᴩ")][bstack11ll1l_opy_ (u"ࠫࡸࡩࡲࡪࡲࡷࡷࠬᴪ")], bstack11ll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᴫ"), bstack11ll1l_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࠧᴬ"))
            bstack1111ll1l1_opy_.bstack1l11l1l1111_opy_(scripts)
            commands = bstack1111111lll_opy_[bstack11ll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧᴭ")][bstack11ll1l_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩᴮ")][bstack11ll1l_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡶࡘࡴ࡝ࡲࡢࡲࠪᴯ")].get(bstack11ll1l_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡷࠬᴰ"))
            bstack1111ll1l1_opy_.bstack1l111llll11_opy_(commands)
            bstack1111ll1l1_opy_.store()
        return [bstack111ll1ll11l_opy_, bstack1111111lll_opy_[bstack11ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ᴱ")]]
    @classmethod
    def bstack111ll1ll1l1_opy_(cls, response=None):
        os.environ[bstack11ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪᴲ")] = bstack11ll1l_opy_ (u"࠭࡮ࡶ࡮࡯ࠫᴳ")
        os.environ[bstack11ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫᴴ")] = bstack11ll1l_opy_ (u"ࠨࡰࡸࡰࡱ࠭ᴵ")
        os.environ[bstack11ll1l_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡉࡏࡎࡒࡏࡉ࡙ࡋࡄࠨᴶ")] = bstack11ll1l_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩᴷ")
        os.environ[bstack11ll1l_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡉࡃࡖࡌࡊࡊ࡟ࡊࡆࠪᴸ")] = bstack11ll1l_opy_ (u"ࠧࡴࡵ࡭࡮ࠥᴹ")
        os.environ[bstack11ll1l_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡅࡑࡒࡏࡘࡡࡖࡇࡗࡋࡅࡏࡕࡋࡓ࡙࡙ࠧᴺ")] = bstack11ll1l_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧᴻ")
        cls.bstack111ll1llll1_opy_(response, bstack11ll1l_opy_ (u"ࠣࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠣᴼ"))
        return [None, None, None]
    @classmethod
    def bstack111lll11111_opy_(cls, response=None):
        os.environ[bstack11ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧᴽ")] = bstack11ll1l_opy_ (u"ࠪࡲࡺࡲ࡬ࠨᴾ")
        os.environ[bstack11ll1l_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩᴿ")] = bstack11ll1l_opy_ (u"ࠬࡴࡵ࡭࡮ࠪᵀ")
        os.environ[bstack11ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪᵁ")] = bstack11ll1l_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬᵂ")
        cls.bstack111ll1llll1_opy_(response, bstack11ll1l_opy_ (u"ࠣࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠣᵃ"))
        return [None, None, None]
    @classmethod
    def bstack111lll11l11_opy_(cls, jwt, build_hashed_id):
        os.environ[bstack11ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ᵄ")] = jwt
        os.environ[bstack11ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨᵅ")] = build_hashed_id
    @classmethod
    def bstack111ll1llll1_opy_(cls, response=None, product=bstack11ll1l_opy_ (u"ࠦࠧᵆ")):
        if response == None:
            logger.error(product + bstack11ll1l_opy_ (u"ࠧࠦࡂࡶ࡫࡯ࡨࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠࡧࡣ࡬ࡰࡪࡪࠢᵇ"))
        for error in response[bstack11ll1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࡸ࠭ᵈ")]:
            bstack11llll1l1ll_opy_ = error[bstack11ll1l_opy_ (u"ࠧ࡬ࡧࡼࠫᵉ")]
            error_message = error[bstack11ll1l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᵊ")]
            if error_message:
                if bstack11llll1l1ll_opy_ == bstack11ll1l_opy_ (u"ࠤࡈࡖࡗࡕࡒࡠࡃࡆࡇࡊ࡙ࡓࡠࡆࡈࡒࡎࡋࡄࠣᵋ"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack11ll1l_opy_ (u"ࠥࡈࡦࡺࡡࠡࡷࡳࡰࡴࡧࡤࠡࡶࡲࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࠦᵌ") + product + bstack11ll1l_opy_ (u"ࠦࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡪࡵࡦࠢࡷࡳࠥࡹ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠤᵍ"))
    @classmethod
    def bstack111lll111l1_opy_(cls):
        if cls.bstack11l1111ll11_opy_ is not None:
            return
        cls.bstack11l1111ll11_opy_ = bstack11l1111l11l_opy_(cls.bstack111ll1ll1ll_opy_)
        cls.bstack11l1111ll11_opy_.start()
    @classmethod
    def bstack111lllllll_opy_(cls):
        if cls.bstack11l1111ll11_opy_ is None:
            return
        cls.bstack11l1111ll11_opy_.shutdown()
    @classmethod
    @bstack111ll1l1ll_opy_(class_method=True)
    def bstack111ll1ll1ll_opy_(cls, bstack11l111111l_opy_, event_url=bstack11ll1l_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡨࡡࡵࡥ࡫ࠫᵎ")):
        config = {
            bstack11ll1l_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧᵏ"): cls.default_headers()
        }
        logger.debug(bstack11ll1l_opy_ (u"ࠢࡱࡱࡶࡸࡤࡪࡡࡵࡣ࠽ࠤࡘ࡫࡮ࡥ࡫ࡱ࡫ࠥࡪࡡࡵࡣࠣࡸࡴࠦࡴࡦࡵࡷ࡬ࡺࡨࠠࡧࡱࡵࠤࡪࡼࡥ࡯ࡶࡶࠤࢀࢃࠢᵐ").format(bstack11ll1l_opy_ (u"ࠨ࠮ࠣࠫᵑ").join([event[bstack11ll1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ᵒ")] for event in bstack11l111111l_opy_])))
        response = bstack1lll111l_opy_(bstack11ll1l_opy_ (u"ࠪࡔࡔ࡙ࡔࠨᵓ"), cls.request_url(event_url), bstack11l111111l_opy_, config)
        bstack1l111lllll1_opy_ = response.json()
    @classmethod
    def bstack1l11lll11_opy_(cls, bstack11l111111l_opy_, event_url=bstack11ll1l_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡧࡴࡤࡪࠪᵔ")):
        logger.debug(bstack11ll1l_opy_ (u"ࠧࡹࡥ࡯ࡦࡢࡨࡦࡺࡡ࠻ࠢࡄࡸࡹ࡫࡭ࡱࡶ࡬ࡲ࡬ࠦࡴࡰࠢࡤࡨࡩࠦࡤࡢࡶࡤࠤࡹࡵࠠࡣࡣࡷࡧ࡭ࠦࡷࡪࡶ࡫ࠤࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥ࠻ࠢࡾࢁࠧᵕ").format(bstack11l111111l_opy_[bstack11ll1l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪᵖ")]))
        if not bstack1llll1ll_opy_.bstack111lll11ll1_opy_(bstack11l111111l_opy_[bstack11ll1l_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫᵗ")]):
            logger.debug(bstack11ll1l_opy_ (u"ࠣࡵࡨࡲࡩࡥࡤࡢࡶࡤ࠾ࠥࡔ࡯ࡵࠢࡤࡨࡩ࡯࡮ࡨࠢࡧࡥࡹࡧࠠࡸ࡫ࡷ࡬ࠥ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦ࠼ࠣࡿࢂࠨᵘ").format(bstack11l111111l_opy_[bstack11ll1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ᵙ")]))
            return
        bstack1l1l11ll1_opy_ = bstack1llll1ll_opy_.bstack111lll1lll1_opy_(bstack11l111111l_opy_[bstack11ll1l_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧᵚ")], bstack11l111111l_opy_.get(bstack11ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭ᵛ")))
        if bstack1l1l11ll1_opy_ != None:
            if bstack11l111111l_opy_.get(bstack11ll1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧᵜ")) != None:
                bstack11l111111l_opy_[bstack11ll1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࠨᵝ")][bstack11ll1l_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࡠ࡯ࡤࡴࠬᵞ")] = bstack1l1l11ll1_opy_
            else:
                bstack11l111111l_opy_[bstack11ll1l_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࡡࡰࡥࡵ࠭ᵟ")] = bstack1l1l11ll1_opy_
        if event_url == bstack11ll1l_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡥࡹࡩࡨࠨᵠ"):
            cls.bstack111lll111l1_opy_()
            logger.debug(bstack11ll1l_opy_ (u"ࠥࡷࡪࡴࡤࡠࡦࡤࡸࡦࡀࠠࡂࡦࡧ࡭ࡳ࡭ࠠࡥࡣࡷࡥࠥࡺ࡯ࠡࡤࡤࡸࡨ࡮ࠠࡸ࡫ࡷ࡬ࠥ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦ࠼ࠣࡿࢂࠨᵡ").format(bstack11l111111l_opy_[bstack11ll1l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨᵢ")]))
            cls.bstack11l1111ll11_opy_.add(bstack11l111111l_opy_)
        elif event_url == bstack11ll1l_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪᵣ"):
            cls.bstack111ll1ll1ll_opy_([bstack11l111111l_opy_], event_url)
    @classmethod
    @bstack111ll1l1ll_opy_(class_method=True)
    def bstack1l1lllll_opy_(cls, logs):
        bstack111ll1l1l1l_opy_ = []
        for log in logs:
            bstack111lll11l1l_opy_ = {
                bstack11ll1l_opy_ (u"࠭࡫ࡪࡰࡧࠫᵤ"): bstack11ll1l_opy_ (u"ࠧࡕࡇࡖࡘࡤࡒࡏࡈࠩᵥ"),
                bstack11ll1l_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧᵦ"): log[bstack11ll1l_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨᵧ")],
                bstack11ll1l_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ᵨ"): log[bstack11ll1l_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧᵩ")],
                bstack11ll1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡢࡶࡪࡹࡰࡰࡰࡶࡩࠬᵪ"): {},
                bstack11ll1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᵫ"): log[bstack11ll1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᵬ")],
            }
            if bstack11ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᵭ") in log:
                bstack111lll11l1l_opy_[bstack11ll1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᵮ")] = log[bstack11ll1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᵯ")]
            elif bstack11ll1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᵰ") in log:
                bstack111lll11l1l_opy_[bstack11ll1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᵱ")] = log[bstack11ll1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᵲ")]
            bstack111ll1l1l1l_opy_.append(bstack111lll11l1l_opy_)
        cls.bstack1l11lll11_opy_({
            bstack11ll1l_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫᵳ"): bstack11ll1l_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬᵴ"),
            bstack11ll1l_opy_ (u"ࠩ࡯ࡳ࡬ࡹࠧᵵ"): bstack111ll1l1l1l_opy_
        })
    @classmethod
    @bstack111ll1l1ll_opy_(class_method=True)
    def bstack111ll1lll1l_opy_(cls, steps):
        bstack111lll1ll1l_opy_ = []
        for step in steps:
            bstack111ll1l1ll1_opy_ = {
                bstack11ll1l_opy_ (u"ࠪ࡯࡮ࡴࡤࠨᵶ"): bstack11ll1l_opy_ (u"࡙ࠫࡋࡓࡕࡡࡖࡘࡊࡖࠧᵷ"),
                bstack11ll1l_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫᵸ"): step[bstack11ll1l_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᵹ")],
                bstack11ll1l_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪᵺ"): step[bstack11ll1l_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫᵻ")],
                bstack11ll1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᵼ"): step[bstack11ll1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᵽ")],
                bstack11ll1l_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭ᵾ"): step[bstack11ll1l_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧᵿ")]
            }
            if bstack11ll1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᶀ") in step:
                bstack111ll1l1ll1_opy_[bstack11ll1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᶁ")] = step[bstack11ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᶂ")]
            elif bstack11ll1l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᶃ") in step:
                bstack111ll1l1ll1_opy_[bstack11ll1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᶄ")] = step[bstack11ll1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᶅ")]
            bstack111lll1ll1l_opy_.append(bstack111ll1l1ll1_opy_)
        cls.bstack1l11lll11_opy_({
            bstack11ll1l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩᶆ"): bstack11ll1l_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪᶇ"),
            bstack11ll1l_opy_ (u"ࠧ࡭ࡱࡪࡷࠬᶈ"): bstack111lll1ll1l_opy_
        })
    @classmethod
    @bstack111ll1l1ll_opy_(class_method=True)
    @measure(event_name=EVENTS.bstack11lllllll_opy_, stage=STAGE.bstack1111l111_opy_)
    def bstack1111111l_opy_(cls, screenshot):
        cls.bstack1l11lll11_opy_({
            bstack11ll1l_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬᶉ"): bstack11ll1l_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭ᶊ"),
            bstack11ll1l_opy_ (u"ࠪࡰࡴ࡭ࡳࠨᶋ"): [{
                bstack11ll1l_opy_ (u"ࠫࡰ࡯࡮ࡥࠩᶌ"): bstack11ll1l_opy_ (u"࡚ࠬࡅࡔࡖࡢࡗࡈࡘࡅࡆࡐࡖࡌࡔ࡚ࠧᶍ"),
                bstack11ll1l_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩᶎ"): datetime.datetime.utcnow().isoformat() + bstack11ll1l_opy_ (u"࡛ࠧࠩᶏ"),
                bstack11ll1l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᶐ"): screenshot[bstack11ll1l_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨᶑ")],
                bstack11ll1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᶒ"): screenshot[bstack11ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᶓ")]
            }]
        }, event_url=bstack11ll1l_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪᶔ"))
    @classmethod
    @bstack111ll1l1ll_opy_(class_method=True)
    def bstack1ll1l11111_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack1l11lll11_opy_({
            bstack11ll1l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪᶕ"): bstack11ll1l_opy_ (u"ࠧࡄࡄࡗࡗࡪࡹࡳࡪࡱࡱࡇࡷ࡫ࡡࡵࡧࡧࠫᶖ"),
            bstack11ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪᶗ"): {
                bstack11ll1l_opy_ (u"ࠤࡸࡹ࡮ࡪࠢᶘ"): cls.current_test_uuid(),
                bstack11ll1l_opy_ (u"ࠥ࡭ࡳࡺࡥࡨࡴࡤࡸ࡮ࡵ࡮ࡴࠤᶙ"): cls.bstack11l11ll111_opy_(driver)
            }
        })
    @classmethod
    def bstack11l11ll1l1_opy_(cls, event: str, bstack11l111111l_opy_: bstack111llll1ll_opy_):
        bstack11l111lll1_opy_ = {
            bstack11ll1l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨᶚ"): event,
            bstack11l111111l_opy_.bstack111ll111ll_opy_(): bstack11l111111l_opy_.bstack11l111l11l_opy_(event)
        }
        cls.bstack1l11lll11_opy_(bstack11l111lll1_opy_)
        result = getattr(bstack11l111111l_opy_, bstack11ll1l_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬᶛ"), None)
        if event == bstack11ll1l_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧᶜ"):
            threading.current_thread().bstackTestMeta = {bstack11ll1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᶝ"): bstack11ll1l_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩᶞ")}
        elif event == bstack11ll1l_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫᶟ"):
            threading.current_thread().bstackTestMeta = {bstack11ll1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪᶠ"): getattr(result, bstack11ll1l_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᶡ"), bstack11ll1l_opy_ (u"ࠬ࠭ᶢ"))}
    @classmethod
    def on(cls):
        if (os.environ.get(bstack11ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪᶣ"), None) is None or os.environ[bstack11ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫᶤ")] == bstack11ll1l_opy_ (u"ࠣࡰࡸࡰࡱࠨᶥ")) and (os.environ.get(bstack11ll1l_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧᶦ"), None) is None or os.environ[bstack11ll1l_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨᶧ")] == bstack11ll1l_opy_ (u"ࠦࡳࡻ࡬࡭ࠤᶨ")):
            return False
        return True
    @staticmethod
    def bstack111lll111ll_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1ll11l1l11_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack11ll1l_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫᶩ"): bstack11ll1l_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩᶪ"),
            bstack11ll1l_opy_ (u"࡙ࠧ࠯ࡅࡗ࡙ࡇࡃࡌ࠯ࡗࡉࡘ࡚ࡏࡑࡕࠪᶫ"): bstack11ll1l_opy_ (u"ࠨࡶࡵࡹࡪ࠭ᶬ")
        }
        if os.environ.get(bstack11ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ᶭ"), None):
            headers[bstack11ll1l_opy_ (u"ࠪࡅࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪᶮ")] = bstack11ll1l_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࢀࢃࠧᶯ").format(os.environ[bstack11ll1l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠤᶰ")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack11ll1l_opy_ (u"࠭ࡻࡾ࠱ࡾࢁࠬᶱ").format(bstack111ll1lll11_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack11ll1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫᶲ"), None)
    @staticmethod
    def bstack11l11ll111_opy_(driver):
        return {
            bstack11lll1111ll_opy_(): bstack11lllll1111_opy_(driver)
        }
    @staticmethod
    def bstack111lll1l111_opy_(exception_info, report):
        return [{bstack11ll1l_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫᶳ"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack111l11ll1l_opy_(typename):
        if bstack11ll1l_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࠧᶴ") in typename:
            return bstack11ll1l_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࡋࡲࡳࡱࡵࠦᶵ")
        return bstack11ll1l_opy_ (u"࡚ࠦࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠧᶶ")