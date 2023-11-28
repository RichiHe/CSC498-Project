Run Main.py and follow the instruction

You will need to provide a,b, and p for the curve first.

Then you can either Encrypt a message, Decrypt a message, or select a generator
and a private key

The first thing Bob should do is to selece a generator and a private key

Bob will have to memorize the generator and the public key created.

Now when Alice gets the generator and the public key, she can encrypt a message.

Base on the order of group, Alice will know whether she can send a message with
anything in this string: "abcdefghijklmnopqrstuvwxyz0123456789 .,"

After writing the message, Alice should input the generator and the public key,
and the ciphertext will be printed, in the form x y x y x y x y ....

With ciphertext in the form that how it is printed, Bob can decrypt using the
private key k, and he should get what Alice input.
