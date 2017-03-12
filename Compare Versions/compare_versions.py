def compare_versions(version1, version2):
    if '.' not in version1 and '.' not in version2:
        if int(version1) > int(version2) or int(version1) == int(version2):
            return True
        else:
            return False
    elif '.' in version1 and '.' in version2:
        a = version1.split('.')
        b = version2.split('.')
        print(a)
        print(b)
        if len(a) == len(b):
            c = zip(a, b)
            for i in c:
                if (i[0]) < (i[1]):
                    return False
                else:
                    return True
        elif len(a) > len(b):
            c = zip(a, b)
            for i in c:
                if (i[0]) < (i[1]):
                    return False
                elif int(i[0]) > int(i[1]):
                    return True
            else:
                return True

        elif len(a) < len(b):
            c = zip(a, b)
            for i in c:
                if int(i[0]) < int(i[1]):
                    return False
                elif int(i[0]) > int(i[1]):
                    return True

            else:
                return False
