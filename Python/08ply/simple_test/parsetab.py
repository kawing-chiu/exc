
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'C5B469704DC7408B291E016C1BAD23B6'
    
_lr_action_items = {'NUMBER':([3,8,9,10,11,],[4,4,4,4,4,]),'PLUS':([4,5,6,7,12,13,14,15,],[-8,8,-4,-7,-2,-3,-6,-5,]),'MINUS':([4,5,6,7,12,13,14,15,],[-8,9,-4,-7,-2,-3,-6,-5,]),'TIMES':([4,6,7,12,13,14,15,],[-8,11,-7,11,11,-6,-5,]),'NAME':([0,],[2,]),'$end':([1,4,5,6,7,12,13,14,15,],[0,-8,-1,-4,-7,-2,-3,-6,-5,]),'EQUALS':([2,],[3,]),'DIVIDE':([4,6,7,12,13,14,15,],[-8,10,-7,10,10,-6,-5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'factor':([3,8,9,10,11,],[7,7,7,14,15,]),'assign':([0,],[1,]),'expr':([3,],[5,]),'term':([3,8,9,],[6,12,13,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> assign","S'",1,None,None,None),
  ('assign -> NAME EQUALS expr','assign',3,'p_assign','parser.py',7),
  ('expr -> expr PLUS term','expr',3,'p_expr','parser.py',12),
  ('expr -> expr MINUS term','expr',3,'p_expr','parser.py',13),
  ('expr -> term','expr',1,'p_expr','parser.py',14),
  ('term -> term TIMES factor','term',3,'p_term','parser.py',19),
  ('term -> term DIVIDE factor','term',3,'p_term','parser.py',20),
  ('term -> factor','term',1,'p_term','parser.py',21),
  ('factor -> NUMBER','factor',1,'p_factor','parser.py',26),
]
