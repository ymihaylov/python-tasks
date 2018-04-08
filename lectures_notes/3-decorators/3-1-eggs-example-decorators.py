def served_by(server):
    def decorator(func):
        def cached_server(n):
            return '{}, dear {}'.format(func(n), server)
        return cached_server

    return decorator


def thank_you(func):
    def with_thanks(n):
        return '{}. Thank you very much!'.format(func(n))

    return with_thanks


@thank_you
@served_by('sir')
def spam(n):
    spams = ('spam', ) * (n - 1)

    return 'I would like {} and spam'.format(", ".join(spams))


@thank_you
@served_by('madam')
def eggs(n):
    return 'I would like {} eggs'.format(n)

print(eggs(2))
