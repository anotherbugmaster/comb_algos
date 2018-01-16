def try_kuhn(vertice, used, x_matches, y_matches, vertice_neighbors):
    if used[vertice]:
        return False
    used[vertice] = True

    for to in vertice_neighbors[vertice]:
        if (y_matches[to] is None
            or try_kuhn(
                    y_matches[to], used, x_matches, y_matches,
                    vertice_neighbors
                )
        ):
            y_matches[to] = vertice
            x_matches[vertice] = to
            return True

    return False


def main():
    with open('../In4_2.txt', 'r') as reader:
        k, l = (int(e) for e in reader.readline().split())

        vertice_neighbors = [[] for _ in range(k)]

        for idx in range(k):
            vertice_neighbors[idx].extend(int(e) - 1 for e in
                                          reader.readline().split()[:-1])

    x_matches = [None for _ in range(k)]
    y_matches = [None for _ in range(l)]

    for vertice in range(k):
        used = [False for _ in range(k)]
        is_found = try_kuhn(vertice, used, x_matches, y_matches,
                          vertice_neighbors)
        if not is_found:
            with open('out.txt', 'w+') as writer:
                writer.write('N\n')
                writer.write(str(vertice + 1) + '\n')
            return

    with open('out.txt', 'w+') as writer:
        writer.write('Y\n')
        writer.write(" ".join([str(v + 1) for v in x_matches]))


if __name__ == "__main__":
    main()
