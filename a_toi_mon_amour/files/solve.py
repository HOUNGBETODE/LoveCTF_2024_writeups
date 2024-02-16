import cryptocode

chiffre = "zlp/GiKHRGogjU0WNYZo7G2NfweQzwRPykgwuC+/IoYiBHJC/bSsMYPD8PNSQ6qhz+t5Q0jdcUNuTcE=* 1uXiyTAqAlrNq05cnyHLpA==*5aKL6ToIiPl47Oev5LFBbw==*jT2KmX2pXO6BCMLasrLScg=="

cle = "Saint-Valentin"

message = cryptocode.decrypt(chiffre, cle)

print(message)