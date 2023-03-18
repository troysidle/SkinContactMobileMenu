import ftplib

# FTP server credentials
ftp_server = "ftp.skincontact.nyc"
ftp_user = "skincont"
ftp_password = "Rs7hKM4.l!eL85"

# Connect to FTP server
ftp = ftplib.FTP(ftp_server)
ftp.login(ftp_user, ftp_password)

# Set passive mode
ftp.set_pasv(True)

# Navigate to directory
ftp.cwd("/public_html")

# Upload a file and overwrite if it already exists
filename = "MobileMenu.html"
with open(filename, "rb") as file:
    ftp.storbinary("STOR " + filename, file)

# Close the connection
ftp.quit()
