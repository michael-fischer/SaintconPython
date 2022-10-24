
There are some steps required to configure Burp to run properly. 

- Start Burp
- Configure browser to use Burp
- Visit http://burp
- Download the "CA Certificate" from the top right hand side
- Open a terminal and navigate to the file you downloaded
- run the command  `openssl x509 -inform der -in cacert.der -out certificate.pem`
- This pem file can now be used to validate the cert.