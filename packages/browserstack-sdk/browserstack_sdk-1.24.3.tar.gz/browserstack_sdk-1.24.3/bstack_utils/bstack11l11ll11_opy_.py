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
import json
class bstack1l111l11l1l_opy_(object):
  bstack11l1l11l_opy_ = os.path.join(os.path.expanduser(bstack11lll_opy_ (u"ࠫࢃ࠭ᕭ")), bstack11lll_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᕮ"))
  bstack1l111l111ll_opy_ = os.path.join(bstack11l1l11l_opy_, bstack11lll_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳ࠯࡬ࡶࡳࡳ࠭ᕯ"))
  commands_to_wrap = None
  perform_scan = None
  bstack11l1ll1l11_opy_ = None
  bstack1ll11l1ll1_opy_ = None
  bstack1l111l1llll_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack11lll_opy_ (u"ࠧࡪࡰࡶࡸࡦࡴࡣࡦࠩᕰ")):
      cls.instance = super(bstack1l111l11l1l_opy_, cls).__new__(cls)
      cls.instance.bstack1l111l11l11_opy_()
    return cls.instance
  def bstack1l111l11l11_opy_(self):
    try:
      with open(self.bstack1l111l111ll_opy_, bstack11lll_opy_ (u"ࠨࡴࠪᕱ")) as bstack11l111l1l_opy_:
        bstack1l111l111l1_opy_ = bstack11l111l1l_opy_.read()
        data = json.loads(bstack1l111l111l1_opy_)
        if bstack11lll_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡶࠫᕲ") in data:
          self.bstack1l111lllll1_opy_(data[bstack11lll_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡷࠬᕳ")])
        if bstack11lll_opy_ (u"ࠫࡸࡩࡲࡪࡲࡷࡷࠬᕴ") in data:
          self.bstack1l111l11ll1_opy_(data[bstack11lll_opy_ (u"ࠬࡹࡣࡳ࡫ࡳࡸࡸ࠭ᕵ")])
    except:
      pass
  def bstack1l111l11ll1_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts[bstack11lll_opy_ (u"࠭ࡳࡤࡣࡱࠫᕶ")]
      self.bstack11l1ll1l11_opy_ = scripts[bstack11lll_opy_ (u"ࠧࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࠫᕷ")]
      self.bstack1ll11l1ll1_opy_ = scripts[bstack11lll_opy_ (u"ࠨࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࡘࡻ࡭࡮ࡣࡵࡽࠬᕸ")]
      self.bstack1l111l1llll_opy_ = scripts[bstack11lll_opy_ (u"ࠩࡶࡥࡻ࡫ࡒࡦࡵࡸࡰࡹࡹࠧᕹ")]
  def bstack1l111lllll1_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack1l111l111ll_opy_, bstack11lll_opy_ (u"ࠪࡻࠬᕺ")) as file:
        json.dump({
          bstack11lll_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡸࠨᕻ"): self.commands_to_wrap,
          bstack11lll_opy_ (u"ࠧࡹࡣࡳ࡫ࡳࡸࡸࠨᕼ"): {
            bstack11lll_opy_ (u"ࠨࡳࡤࡣࡱࠦᕽ"): self.perform_scan,
            bstack11lll_opy_ (u"ࠢࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࠦᕾ"): self.bstack11l1ll1l11_opy_,
            bstack11lll_opy_ (u"ࠣࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࡘࡻ࡭࡮ࡣࡵࡽࠧᕿ"): self.bstack1ll11l1ll1_opy_,
            bstack11lll_opy_ (u"ࠤࡶࡥࡻ࡫ࡒࡦࡵࡸࡰࡹࡹࠢᖀ"): self.bstack1l111l1llll_opy_
          }
        }, file)
    except:
      pass
  def bstack1llll1l11_opy_(self, bstack1ll1l1ll1l1_opy_):
    try:
      return any(command.get(bstack11lll_opy_ (u"ࠪࡲࡦࡳࡥࠨᖁ")) == bstack1ll1l1ll1l1_opy_ for command in self.commands_to_wrap)
    except:
      return False
bstack11l11ll11_opy_ = bstack1l111l11l1l_opy_()