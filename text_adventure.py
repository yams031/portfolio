start= '''    Its Sunday. You are about to walk your dog, but as soon as
you walk out the door, you get a call from your boss telling you to
fill in for a coworker. You tell him that you never work on weekends,
but he tells you that if you dont come in and on time, youll be fired.'''
print(start)
user_input= input('''    Cut your weekend short by going home and getting
ready for work OR continue to walk your dog?
    (Type 'home' or 'walk')
''')

if user_input=="home":
    print('''    You turn around and go home to get ready for work. Your dog
    despises you. You get ready. When you walk out your room, youre greeted
    with a fresh dog-made stain on your couch.''')
    print('''    You get to work and spend the rest of the day glad you
    werent fired. END''')
if user_input =="walk":
    print('''    you never really liked your job anyway. you go ahead and
    walk your dog.''')
    print('''    your boss fires you''')
    print('''    you call your friend to tell her how you lost your job and
    she tells you of a new job opportunity in her company and offers you the
    job.END''')
