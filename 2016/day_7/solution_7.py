def load_data(file, solution):
    supports_tls = 0
    supports_ssl = 0
    data = open(file, 'r')
    for line in data:
        stripped = line.strip()
        ignore_doubles = False
        does_supports_tls = False
        aba = []
        bab = []
        for i in range(0, len(stripped)):
            if stripped[i] == "[":
                ignore_doubles = True
            elif stripped[i] == "]":
                ignore_doubles = False

            if solution == 1:
                if i in range(2, len(stripped) - 1):
                    if stripped[i-1] == stripped[i]:
                        if stripped[i+1] == stripped[i-2] and stripped[i] != stripped[i+1]:
                            if ignore_doubles:
                                does_supports_tls = False
                                break
                            else:
                                does_supports_tls = True

            # check for part 2
            if solution == 2:
                if i in range(1, len(stripped) - 1):
                    if stripped[i - 1] == stripped[i + 1]:
                        if ignore_doubles:
                            bab.append(f"{stripped[i-1]}{stripped[i]}{stripped[i+1]}")
                        else:
                            aba.append(f"{stripped[i - 1]}{stripped[i]}{stripped[i + 1]}")

                    if len(aba) > 0 and len(bab) > 0:
                        if detect_ssl(aba, bab):
                            supports_ssl += 1
                            break

        if does_supports_tls:
            supports_tls += 1

    data.close()
    return [supports_tls, supports_ssl]


def detect_ssl(ab, ba):
    for a in ab:
        for b in ba:
            if a[0] == b[1] and a[1] == b[0]:
                return True
    return False


if __name__ == "__main__":
    result = load_data("data_7", 1)
    print(f"Number of TLS supported ip addresses:{result[0]}")

    result = load_data("data_7", 2)
    print(f"Number of SSL supported ip addresses:{result[1]}")
