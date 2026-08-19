def word_ladder_builder(start: str, end: str, wordlist: list[str]) -> int:
    ws = set(wordlist)
    if end not in ws:
        return 0
    if start in ws:
        ws.remove(start)
    que = [(start,1)]
    ind = 0
    while ind < (len(que)):
        wl , steps = que[ind]
        if wl == end:
            return steps
        for i in range(len(ws)):
            for c in range(97,123):
                ca = chr(c)
                if ca == wl[i]:
                    continue
                nw = wl[:i] + ca + wl[i+1:]
                
                if nw in ws:
                    ws.remove(nw)
                    que.append((nw, steps + 1))
    return 0

print(word_ladder_builder("hit", "cog", [
    "hot",
    "dot",
    "dog",
    "lot",
    "log",
    "cog"
]))



print(word_ladder_builder("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
