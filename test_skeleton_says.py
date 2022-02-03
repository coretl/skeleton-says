from skeleton_says import say

skeleton_saying_hello = r"""
 -------
( Hello )
 -------
  \
   \  .-.
    \(o.o)
      |=|
     __|__
   //.=|=.\\
  // .=|=. \\
  \\ .=|=. //
   \\(_=_)//
    (:| |:)
     || ||
     () ()
     || ||
     || ||
l42 ==' '==
"""

def test_say_command_says_hello():
    assert say("Hello") == skeleton_saying_hello
