# What's up with `curl`?

As far as I am aware, the fact that `curl` didn't work is due to two errors. There is one local error, and one error on the script:
  * The Local Error: There is some sort of [cran.r-project.org](https://cran.r-project.org) package missing causing `apt-get update` to fail. I simply removed all packages for R, and it worked again.
  * The Script Error: When checking for network connectivity, the IP Address 8.8.8.8 is pinged, which seems to be invalid. Wes suggested pinging [www.ic.ac.uk](https://www.ic.ac.uk) instead, and this seems to work.
  
