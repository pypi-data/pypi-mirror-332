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
from urllib.parse import urlparse
from bstack_utils.config import Config
from bstack_utils.messages import bstack11l1llll111_opy_
bstack1l1l11lll_opy_ = Config.bstack11l1lll11_opy_()
def bstack11l11l11l11_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack11l11l111ll_opy_(bstack11l11l11ll1_opy_, bstack11l11l11lll_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack11l11l11ll1_opy_):
        with open(bstack11l11l11ll1_opy_) as f:
            pac = PACFile(f.read())
    elif bstack11l11l11l11_opy_(bstack11l11l11ll1_opy_):
        pac = get_pac(url=bstack11l11l11ll1_opy_)
    else:
        raise Exception(bstack11ll1l_opy_ (u"࠭ࡐࡢࡥࠣࡪ࡮ࡲࡥࠡࡦࡲࡩࡸࠦ࡮ࡰࡶࠣࡩࡽ࡯ࡳࡵ࠼ࠣࡿࢂ࠭ᯪ").format(bstack11l11l11ll1_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack11ll1l_opy_ (u"ࠢ࠹࠰࠻࠲࠽࠴࠸ࠣᯫ"), 80))
        bstack11l11l1l111_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack11l11l1l111_opy_ = bstack11ll1l_opy_ (u"ࠨ࠲࠱࠴࠳࠶࠮࠱ࠩᯬ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack11l11l11lll_opy_, bstack11l11l1l111_opy_)
    return proxy_url
def bstack1l11111l1_opy_(config):
    return bstack11ll1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬᯭ") in config or bstack11ll1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧᯮ") in config
def bstack1l11ll1l1l_opy_(config):
    if not bstack1l11111l1_opy_(config):
        return
    if config.get(bstack11ll1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧᯯ")):
        return config.get(bstack11ll1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨᯰ"))
    if config.get(bstack11ll1l_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪᯱ")):
        return config.get(bstack11ll1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼ᯲ࠫ"))
def bstack1111l11ll_opy_(config, bstack11l11l11lll_opy_):
    proxy = bstack1l11ll1l1l_opy_(config)
    proxies = {}
    if config.get(bstack11ll1l_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼ᯳ࠫ")) or config.get(bstack11ll1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭᯴")):
        if proxy.endswith(bstack11ll1l_opy_ (u"ࠪ࠲ࡵࡧࡣࠨ᯵")):
            proxies = bstack1lllll1lll_opy_(proxy, bstack11l11l11lll_opy_)
        else:
            proxies = {
                bstack11ll1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪ᯶"): proxy
            }
    bstack1l1l11lll_opy_.bstack1l1111l1_opy_(bstack11ll1l_opy_ (u"ࠬࡶࡲࡰࡺࡼࡗࡪࡺࡴࡪࡰࡪࡷࠬ᯷"), proxies)
    return proxies
def bstack1lllll1lll_opy_(bstack11l11l11ll1_opy_, bstack11l11l11lll_opy_):
    proxies = {}
    global bstack11l11l111l1_opy_
    if bstack11ll1l_opy_ (u"࠭ࡐࡂࡅࡢࡔࡗࡕࡘ࡚ࠩ᯸") in globals():
        return bstack11l11l111l1_opy_
    try:
        proxy = bstack11l11l111ll_opy_(bstack11l11l11ll1_opy_, bstack11l11l11lll_opy_)
        if bstack11ll1l_opy_ (u"ࠢࡅࡋࡕࡉࡈ࡚ࠢ᯹") in proxy:
            proxies = {}
        elif bstack11ll1l_opy_ (u"ࠣࡊࡗࡘࡕࠨ᯺") in proxy or bstack11ll1l_opy_ (u"ࠤࡋࡘ࡙ࡖࡓࠣ᯻") in proxy or bstack11ll1l_opy_ (u"ࠥࡗࡔࡉࡋࡔࠤ᯼") in proxy:
            bstack11l11l11l1l_opy_ = proxy.split(bstack11ll1l_opy_ (u"ࠦࠥࠨ᯽"))
            if bstack11ll1l_opy_ (u"ࠧࡀ࠯࠰ࠤ᯾") in bstack11ll1l_opy_ (u"ࠨࠢ᯿").join(bstack11l11l11l1l_opy_[1:]):
                proxies = {
                    bstack11ll1l_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ᰀ"): bstack11ll1l_opy_ (u"ࠣࠤᰁ").join(bstack11l11l11l1l_opy_[1:])
                }
            else:
                proxies = {
                    bstack11ll1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨᰂ"): str(bstack11l11l11l1l_opy_[0]).lower() + bstack11ll1l_opy_ (u"ࠥ࠾࠴࠵ࠢᰃ") + bstack11ll1l_opy_ (u"ࠦࠧᰄ").join(bstack11l11l11l1l_opy_[1:])
                }
        elif bstack11ll1l_opy_ (u"ࠧࡖࡒࡐ࡚࡜ࠦᰅ") in proxy:
            bstack11l11l11l1l_opy_ = proxy.split(bstack11ll1l_opy_ (u"ࠨࠠࠣᰆ"))
            if bstack11ll1l_opy_ (u"ࠢ࠻࠱࠲ࠦᰇ") in bstack11ll1l_opy_ (u"ࠣࠤᰈ").join(bstack11l11l11l1l_opy_[1:]):
                proxies = {
                    bstack11ll1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨᰉ"): bstack11ll1l_opy_ (u"ࠥࠦᰊ").join(bstack11l11l11l1l_opy_[1:])
                }
            else:
                proxies = {
                    bstack11ll1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪᰋ"): bstack11ll1l_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨᰌ") + bstack11ll1l_opy_ (u"ࠨࠢᰍ").join(bstack11l11l11l1l_opy_[1:])
                }
        else:
            proxies = {
                bstack11ll1l_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ᰎ"): proxy
            }
    except Exception as e:
        print(bstack11ll1l_opy_ (u"ࠣࡵࡲࡱࡪࠦࡥࡳࡴࡲࡶࠧᰏ"), bstack11l1llll111_opy_.format(bstack11l11l11ll1_opy_, str(e)))
    bstack11l11l111l1_opy_ = proxies
    return proxies