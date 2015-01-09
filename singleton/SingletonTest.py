from singleton import Singleton


@Singleton
class SingletonOK:
    pass


class SingletonNOK:
    pass

if __name__ == "__main__":
    # with annotation
    a = SingletonOK()
    b = SingletonOK()
    print('Mit Annotation @Singleton:')
    print("Das Objekt %s == %s (%s)" % (a, b, a is b))
    # without annotation
    a = SingletonNOK()
    b = SingletonNOK()
    print('Ohne Annotation @Singleton:')
    print("Die Adresse %s == %s (%s)" % (id(a), id(b), a is b))

