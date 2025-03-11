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
import os
from urllib.parse import urlparse
from bstack_utils.config import Config
from bstack_utils.messages import bstack11l1ll1l111_opy_
bstack11lll111l1_opy_ = Config.bstack1ll1ll1l1l_opy_()
def bstack11l111l1ll1_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack11l111l1l1l_opy_(bstack11l111l1l11_opy_, bstack11l111ll111_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack11l111l1l11_opy_):
        with open(bstack11l111l1l11_opy_) as f:
            pac = PACFile(f.read())
    elif bstack11l111l1ll1_opy_(bstack11l111l1l11_opy_):
        pac = get_pac(url=bstack11l111l1l11_opy_)
    else:
        raise Exception(bstack11lll_opy_ (u"ࠨࡒࡤࡧࠥ࡬ࡩ࡭ࡧࠣࡨࡴ࡫ࡳࠡࡰࡲࡸࠥ࡫ࡸࡪࡵࡷ࠾ࠥࢁࡽࠨᰝ").format(bstack11l111l1l11_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack11lll_opy_ (u"ࠤ࠻࠲࠽࠴࠸࠯࠺ࠥᰞ"), 80))
        bstack11l111l11ll_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack11l111l11ll_opy_ = bstack11lll_opy_ (u"ࠪ࠴࠳࠶࠮࠱࠰࠳ࠫᰟ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack11l111ll111_opy_, bstack11l111l11ll_opy_)
    return proxy_url
def bstack111llllll_opy_(config):
    return bstack11lll_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧᰠ") in config or bstack11lll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩᰡ") in config
def bstack1ll111lll_opy_(config):
    if not bstack111llllll_opy_(config):
        return
    if config.get(bstack11lll_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩᰢ")):
        return config.get(bstack11lll_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪᰣ"))
    if config.get(bstack11lll_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬᰤ")):
        return config.get(bstack11lll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ᰥ"))
def bstack1lll1l11ll_opy_(config, bstack11l111ll111_opy_):
    proxy = bstack1ll111lll_opy_(config)
    proxies = {}
    if config.get(bstack11lll_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ᰦ")) or config.get(bstack11lll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨᰧ")):
        if proxy.endswith(bstack11lll_opy_ (u"ࠬ࠴ࡰࡢࡥࠪᰨ")):
            proxies = bstack1l111llll1_opy_(proxy, bstack11l111ll111_opy_)
        else:
            proxies = {
                bstack11lll_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬᰩ"): proxy
            }
    bstack11lll111l1_opy_.bstack111l1111_opy_(bstack11lll_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡙ࡥࡵࡶ࡬ࡲ࡬ࡹࠧᰪ"), proxies)
    return proxies
def bstack1l111llll1_opy_(bstack11l111l1l11_opy_, bstack11l111ll111_opy_):
    proxies = {}
    global bstack11l111l1lll_opy_
    if bstack11lll_opy_ (u"ࠨࡒࡄࡇࡤࡖࡒࡐ࡚࡜ࠫᰫ") in globals():
        return bstack11l111l1lll_opy_
    try:
        proxy = bstack11l111l1l1l_opy_(bstack11l111l1l11_opy_, bstack11l111ll111_opy_)
        if bstack11lll_opy_ (u"ࠤࡇࡍࡗࡋࡃࡕࠤᰬ") in proxy:
            proxies = {}
        elif bstack11lll_opy_ (u"ࠥࡌ࡙࡚ࡐࠣᰭ") in proxy or bstack11lll_opy_ (u"ࠦࡍ࡚ࡔࡑࡕࠥᰮ") in proxy or bstack11lll_opy_ (u"࡙ࠧࡏࡄࡍࡖࠦᰯ") in proxy:
            bstack11l111l11l1_opy_ = proxy.split(bstack11lll_opy_ (u"ࠨࠠࠣᰰ"))
            if bstack11lll_opy_ (u"ࠢ࠻࠱࠲ࠦᰱ") in bstack11lll_opy_ (u"ࠣࠤᰲ").join(bstack11l111l11l1_opy_[1:]):
                proxies = {
                    bstack11lll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨᰳ"): bstack11lll_opy_ (u"ࠥࠦᰴ").join(bstack11l111l11l1_opy_[1:])
                }
            else:
                proxies = {
                    bstack11lll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪᰵ"): str(bstack11l111l11l1_opy_[0]).lower() + bstack11lll_opy_ (u"ࠧࡀ࠯࠰ࠤᰶ") + bstack11lll_opy_ (u"ࠨ᰷ࠢ").join(bstack11l111l11l1_opy_[1:])
                }
        elif bstack11lll_opy_ (u"ࠢࡑࡔࡒ࡜࡞ࠨ᰸") in proxy:
            bstack11l111l11l1_opy_ = proxy.split(bstack11lll_opy_ (u"ࠣࠢࠥ᰹"))
            if bstack11lll_opy_ (u"ࠤ࠽࠳࠴ࠨ᰺") in bstack11lll_opy_ (u"ࠥࠦ᰻").join(bstack11l111l11l1_opy_[1:]):
                proxies = {
                    bstack11lll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪ᰼"): bstack11lll_opy_ (u"ࠧࠨ᰽").join(bstack11l111l11l1_opy_[1:])
                }
            else:
                proxies = {
                    bstack11lll_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬ᰾"): bstack11lll_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣ᰿") + bstack11lll_opy_ (u"ࠣࠤ᱀").join(bstack11l111l11l1_opy_[1:])
                }
        else:
            proxies = {
                bstack11lll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨ᱁"): proxy
            }
    except Exception as e:
        print(bstack11lll_opy_ (u"ࠥࡷࡴࡳࡥࠡࡧࡵࡶࡴࡸࠢ᱂"), bstack11l1ll1l111_opy_.format(bstack11l111l1l11_opy_, str(e)))
    bstack11l111l1lll_opy_ = proxies
    return proxies