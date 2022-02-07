How to embed in your own application
====================================

You can use the `../reference/api` to embed the skeleton talking in your own application.

For instance you could::

    from skeleton_says.say import say

    text = get_user_input()
    art = say(text)
    send_to_user(art)
