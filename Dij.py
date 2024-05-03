from collections import deque

def shortest_path(adj, n, src):
    dist = [float('inf')] * n
    dist[src] = 0
    q = deque([src])

    while q:
        node = q.popleft()

        for neighbor in adj[node]:
            if dist[node] + 1 < dist[neighbor]:
                dist[neighbor] = dist[node] + 1
                q.append(neighbor)

    stations = [
        "LBnagar", "Victoria_memorial", "chaitanyapuri", "Dilshukhnagar", "moosrambagh", "NewMarket",
        "malakpet", "MGbusstation", "Osmania_medical", "Gandhibhavan", "Nampally", "Assembly", "Lakdikapool",
        "Khairtabad", "Irrummanzil", "Panjagutta", "Ameerpet", "SRnagar", "ESIhospital", "Erragadda",
        "Bharatnagar", "Moosapet", "DR_BRambedkar", "Kukatpally", "KPHBcolony", "JNTUcollege", "Miyapur",
        "Sultanbazar", "Narayanguda", "Chikkadpali", "RTCxroads", "Musheerabad", "Gandhihospital", "Secbadwest",
        "Paradeground", "Nagole", "Uppal", "stadium", "NGRI", "Habsiguda", "Tarnaka", "Mettuguda", "Secbadeast",
        "Paradise", "Rasoolpura", "PrakashNagar", "Begumpet", "MathuraNagar", "Yusufguda", "Jubliehills",
        "JH-checkpost", "Peddamagudi", "Madhapur", "Dugamcheruvu", "Hitechcity", "raidurg"
    ]

    print("From", stations[src], "to all other stations:")

    for i in range(n):
        print(f"From {stations[src]} to {stations[i]} : {dist[i]}")

if __name__ == "__main__":
    n = 56
    adj = [[] for _ in range(n)]

    # LB NAGAR TO MIYAPUR
    adj[0].append(1)

    for i in range(1, 8):
        adj[i].extend([i - 1, i + 1])

    adj[8].extend([7, 27, 9])

    for i in range(9, 16):
        adj[i].extend([i - 1, i + 1])

    adj[16].extend([15, 46, 17, 47])

    for i in range(17, 26):
        adj[i].extend([i - 1, i + 1])

    adj[26].append(25)

    # MG Bus Station line
    adj[27].extend([9, 28])

    for i in range(28, 34):
        adj[i].extend([i - 1, i + 1])

    adj[34].extend([42, 33, 43])

    # NAGOLE TO RAIDURG
    adj[35].append(36)

    for i in range(36, 42):
        adj[i].extend([i - 1, i + 1])

    adj[42].extend([41, 34])
    adj[43].extend([34, 44])

    for i in range(44, 55):
        adj[i].extend([i - 1, i + 1])

    adj[55].append(54)

    stations_info = "\n".join(f"Enter value {i} for {stations[i]} Station" for i in range(n))

    print("PLEASE SELECT YOUR SOURCE STATION NUMBER FROM THE BELOW OPTIONS")
    print(stations_info)

    src = int(input("Enter the source STATION: "))

    print("THE SHORTEST PATH FROM SOURCE TO ALL OTHER STATIONS:")
    shortest_path(adj, n, src)
