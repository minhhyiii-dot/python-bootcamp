initial_watchlist = ["VCB", "MBB", "BID", "MBB", "TCB"]

initial_watchlist.append("ACB")
initial_watchlist.extend(["CTG", "VPB"])
initial_watchlist.insert(2, "STB")
initial_watchlist.remove("MBB")
discarded = initial_watchlist.pop()
initial_watchlist.sort(reverse=True)

print(initial_watchlist)
print(discarded)
print(initial_watchlist.count("MBB"))
print(initial_watchlist.index("VCB"))
