# Code Name:
# Developer: 
# Date:
# Objective:
# History:

# configuration - START
login_username = 'blah'
login_password = 'blah'
reply_to_email = 'blah'
# configuration - END

import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions # available since 2.26.0
from selenium.webdriver.support import expected_conditions # available since 2.26.0
from selenium.webdriver.common.by import By

chromedriver = "D:/2015/coding_projects/auto_login_form_filler/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
#browser = webdriver.Firefox()
browser.get('https://www.productreview.com.au/u/login.html')
emailElem = browser.find_element_by_id('_username')
emailElem.send_keys(login_username)
passwordElem = browser.find_element_by_id('_password')
passwordElem.send_keys(login_password)
passwordElem.submit()
#print browser.page_source
print "passwordElem.submit() done"
browser.get('http://www.productreview.com.au/brand-manager/platform/')

print "brand manager page loaded"

ReviewInvitesElement = browser.find_element_by_partial_link_text('Review Invitations')
print "element=", ReviewInvitesElement
ReviewInvitesElement.click()

# this loads https://www.productreview.com.au/brand-manager/platform/3792/emailings.
# click action need to carry data.

print "review invitations page loaded."

InviteCustomersElement = browser.find_element_by_partial_link_text('Invite customers')
print "element=", InviteCustomersElement
InviteCustomersElement.click()


print "Invite customers."
#this loads https://www.productreview.com.au/brand-manager/platform/3792/emailings/invite

#now fill in reply to email and load invitation file
#<input type="email" id="emailing_replyToEmail" name="emailing[replyToEmail]" required="required" placeholder="customer.service@your-company.com" class=" form-control">
replyToEmailElement = browser.find_element_by_id('emailing_replyToEmail')
print 'replyToEmailElement=', replyToEmailElement
replyToEmailElement.send_keys(reply_to_email)

#<input type="file" id="emailing_invitationFile" name="emailing[invitationFile]" required="required">
invitationFileElement = browser.find_element_by_id('emailing_invitationFile')
print 'invitationFileElement=', invitationFileElement
"""
NB: looked at automating the customer details file. 
impossible to automate due to users locating files in unknown local directories.
also risky due to inconsistent path issues on different OS.
absolute_file_path = "absolute file path required"#nb: escape \ issues
invitation_file = absolute_file_path+'customer_invitation_email.csv'
print "invitation_file=",invitation_file
element.send_keys(absolute_file_path+invitation_file)
"""
invitationFileElement.send_keys()
invitationFileElement.click()

#<input id="confirm" type="checkbox" name="confirm" value="1">
#confirmElement = browser.find_element_by_name('confirm')
#print "find_element_by_id('confirm'), element=", confirmElement
confirmElement2 = browser.find_element_by_id("confirm")
print "find_element_by_id('confirm'), element=", confirmElement2
confirmElement2.click()
print "checkbox selected."


#<button id="submit" type="submit" class="btn btn-primary btn-lg text-center col-md-4">Continue</button>
submitElement = browser.find_element_by_id("submit")
#submitElement = browser.find_element_by_id("Continue")
submitElement.click()
submitElement.click
print "submitElement, element=", submitElement
print "form submitted."
# prints submitElement, element= <selenium.webdriver.remote.webelement.WebElement (session="d397808a9616609eb02386957de69f17", element="0.6719081993295286-4")>

#<button type="submit" id="form_confirm" name="form[confirm]" class="btn btn-large btn-primary">Send invitations</button>
#automate this button to execute the auto emailing on confirmation page.