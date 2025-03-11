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
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11lll1l1l1l_opy_, bstack1llll1lll1_opy_, bstack11l1ll1l_opy_, bstack1l1lllll1l_opy_, \
    bstack11llllllll1_opy_
from bstack_utils.measure import measure
def bstack1l1ll11lll_opy_(bstack11l1111111l_opy_):
    for driver in bstack11l1111111l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1ll11l111_opy_, stage=STAGE.bstack1111l111_opy_)
def bstack11lll1lll_opy_(driver, status, reason=bstack11ll1l_opy_ (u"ࠫࠬ᱊")):
    bstack1l1l11lll_opy_ = Config.bstack11l1lll11_opy_()
    if bstack1l1l11lll_opy_.bstack111l1ll1ll_opy_():
        return
    bstack1l11lll11l_opy_ = bstack1ll1l11ll1_opy_(bstack11ll1l_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨ᱋"), bstack11ll1l_opy_ (u"࠭ࠧ᱌"), status, reason, bstack11ll1l_opy_ (u"ࠧࠨᱍ"), bstack11ll1l_opy_ (u"ࠨࠩᱎ"))
    driver.execute_script(bstack1l11lll11l_opy_)
@measure(event_name=EVENTS.bstack1ll11l111_opy_, stage=STAGE.bstack1111l111_opy_)
def bstack11l1llll_opy_(page, status, reason=bstack11ll1l_opy_ (u"ࠩࠪᱏ")):
    try:
        if page is None:
            return
        bstack1l1l11lll_opy_ = Config.bstack11l1lll11_opy_()
        if bstack1l1l11lll_opy_.bstack111l1ll1ll_opy_():
            return
        bstack1l11lll11l_opy_ = bstack1ll1l11ll1_opy_(bstack11ll1l_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭᱐"), bstack11ll1l_opy_ (u"ࠫࠬ᱑"), status, reason, bstack11ll1l_opy_ (u"ࠬ࠭᱒"), bstack11ll1l_opy_ (u"࠭ࠧ᱓"))
        page.evaluate(bstack11ll1l_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣ᱔"), bstack1l11lll11l_opy_)
    except Exception as e:
        print(bstack11ll1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢࡩࡳࡷࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡿࢂࠨ᱕"), e)
def bstack1ll1l11ll1_opy_(type, name, status, reason, bstack1lll11111_opy_, bstack1ll1l1l11l_opy_):
    bstack1lll11lll_opy_ = {
        bstack11ll1l_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩ᱖"): type,
        bstack11ll1l_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭᱗"): {}
    }
    if type == bstack11ll1l_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭᱘"):
        bstack1lll11lll_opy_[bstack11ll1l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ᱙")][bstack11ll1l_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᱚ")] = bstack1lll11111_opy_
        bstack1lll11lll_opy_[bstack11ll1l_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᱛ")][bstack11ll1l_opy_ (u"ࠨࡦࡤࡸࡦ࠭ᱜ")] = json.dumps(str(bstack1ll1l1l11l_opy_))
    if type == bstack11ll1l_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪᱝ"):
        bstack1lll11lll_opy_[bstack11ll1l_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᱞ")][bstack11ll1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᱟ")] = name
    if type == bstack11ll1l_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨᱠ"):
        bstack1lll11lll_opy_[bstack11ll1l_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᱡ")][bstack11ll1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᱢ")] = status
        if status == bstack11ll1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᱣ") and str(reason) != bstack11ll1l_opy_ (u"ࠤࠥᱤ"):
            bstack1lll11lll_opy_[bstack11ll1l_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᱥ")][bstack11ll1l_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫᱦ")] = json.dumps(str(reason))
    bstack1111111ll_opy_ = bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪᱧ").format(json.dumps(bstack1lll11lll_opy_))
    return bstack1111111ll_opy_
def bstack11ll11ll11_opy_(url, config, logger, bstack1l1lll1l1_opy_=False):
    hostname = bstack1llll1lll1_opy_(url)
    is_private = bstack1l1lllll1l_opy_(hostname)
    try:
        if is_private or bstack1l1lll1l1_opy_:
            file_path = bstack11lll1l1l1l_opy_(bstack11ll1l_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᱨ"), bstack11ll1l_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭ᱩ"), logger)
            if os.environ.get(bstack11ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡎࡐࡖࡢࡗࡊ࡚࡟ࡆࡔࡕࡓࡗ࠭ᱪ")) and eval(
                    os.environ.get(bstack11ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡏࡑࡗࡣࡘࡋࡔࡠࡇࡕࡖࡔࡘࠧᱫ"))):
                return
            if (bstack11ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧᱬ") in config and not config[bstack11ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨᱭ")]):
                os.environ[bstack11ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡒࡔ࡚࡟ࡔࡇࡗࡣࡊࡘࡒࡐࡔࠪᱮ")] = str(True)
                bstack11l111111ll_opy_ = {bstack11ll1l_opy_ (u"࠭ࡨࡰࡵࡷࡲࡦࡳࡥࠨᱯ"): hostname}
                bstack11llllllll1_opy_(bstack11ll1l_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭ᱰ"), bstack11ll1l_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭ᱱ"), bstack11l111111ll_opy_, logger)
    except Exception as e:
        pass
def bstack1l1ll11ll1_opy_(caps, bstack11l111111l1_opy_):
    if bstack11ll1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᱲ") in caps:
        caps[bstack11ll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᱳ")][bstack11ll1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪᱴ")] = True
        if bstack11l111111l1_opy_:
            caps[bstack11ll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᱵ")][bstack11ll1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᱶ")] = bstack11l111111l1_opy_
    else:
        caps[bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࠬᱷ")] = True
        if bstack11l111111l1_opy_:
            caps[bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩᱸ")] = bstack11l111111l1_opy_
def bstack11l111ll1ll_opy_(bstack11l111l1l1_opy_):
    bstack11l11111l11_opy_ = bstack11l1ll1l_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠩࡷࡩࡸࡺࡓࡵࡣࡷࡹࡸ࠭ᱹ"), bstack11ll1l_opy_ (u"ࠪࠫᱺ"))
    if bstack11l11111l11_opy_ == bstack11ll1l_opy_ (u"ࠫࠬᱻ") or bstack11l11111l11_opy_ == bstack11ll1l_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ᱼ"):
        threading.current_thread().testStatus = bstack11l111l1l1_opy_
    else:
        if bstack11l111l1l1_opy_ == bstack11ll1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᱽ"):
            threading.current_thread().testStatus = bstack11l111l1l1_opy_