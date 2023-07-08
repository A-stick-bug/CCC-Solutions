x = int(input())

for i in range(x):
    subject_count = int(input())
    verb_count = int(input())
    object_count = int(input())

    subjects, verbs, objects = [],[],[]

    for _ in range(subject_count):
        subject = input()
        subjects.append(subject)

    for _ in range(verb_count):
        verb = input()
        verbs.append(verb)

    for _ in range(object_count):
        object = input()
        objects.append(object)

    for s in subjects:
        for v in verbs:
            for o in objects:
                print(f"{s} {v} {o}.")

