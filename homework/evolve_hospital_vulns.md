# Mal-Practice Hospital Vulnerability Report

## Insecure password reset form  
**Severity:** Critical  
**Description:** Unauthorized users can reset passwords for valid accounts with only the account username and registered email address.  

**Steps to Reproduce**  
1. Click on the `Forgot Password?` link on the main page login form
2. On the **User Lookup** form, provide valid username and email address credentials, which can be gleaned from publicly-available information on the website (e.g. `drjratliff`, `djratliff@hack.evolvesecurity.io`)
3. Select `Doctor` and click `Submit`
4. The following **Password Reset** form allows the attacker to immediately set a new password for the account and login legitimately

**Impact:**  
This vulnerability essentially allows any user to access any other user's Evolve Hospital account and view sensitive personal, medical, and payment information. Due to the standard username convention detailed on the website and the relative ease of determining a user's email address (especially for Doctors, who share the Evolve Hospital email domain), all patient and personnel records are exposed. Further, the integrity of any actions taken within the Account portal, including bill payment and patient record-keeping, cannot be guaranteed.

**Suggested Remediation:**
* Re-implement password reset process to add steps in between provision of account credentials and password reset. Ensure that the user who is providing account credentials authenticates prior to being able to set a password for the account, such as by emailing a password reset link and requiring that the user have access to the registered email address.

**The following steps are not sufficient measures to address this vulnerability, but implemented with the first recommendation, can further add security to the process.**  
* Remove information about username standardization from website to increase the difficulty of determining the correct username/email address combination required to trigger a password reset. 
* Update error messages on the Login and Password Reset form to generic text to avoid specifying whether the username, password, or email address is incorrect on the login attempt. 



## Sensitive data exposure & parameter tampering in Bill Payment area  
**Severity:** Critical  
**Description:** The bill payment area shows full credit card details and allows manipulation of payment data fields.  

**Steps to Reproduce**  
1. Once logged into a patient account, click on `My Account`
2. Inspect the website with your browser (using `Google Chrome for Mac 79.0.3945.88`) and search for the text `ccno`. The credit card number is masked in the web interface, but shown in its entirety in the `option value` field.
3. Similarly, search `secno` and view its `option value` to view the exposed security code code for the credit card
4. Using the Inspector, these values can also be modified to provide an alternate credit card value and security code prior to submission (e.g. type in someone else's credit card number in the `option value` tag)

**Impact:**  
Coupled with the above vulnerability with password reset, the ability to view and and manipulate credit card information fields puts all sensitive patient billing information into jeopardy. An attacker can easily gain patients' saved credit card number, expiration date, and security codes for malicious use.  

Patients (or attackers using patient accounts) could also potentially manipulate the bill payment form fields to create transactions credited to their accounts with unrecognized or other patients' credit card information. 

**Suggested Remediation:**  
* Remove raw payment values (credit card number, security code) from Bill Payment form and instead store and validate payment information on the server side.
* Credit card number should be encrypted in transit and storage and should never appear in the client interface (or anywhere else) in its raw form. The security code value should be purged and not surfaced in the form (as it is against PCI-DSS standards to store this value at all).
* Add validations to Bill Payment form to ensure that users cannot take unexpected actions by tampering with form parameters, including preventing negative amounts.
