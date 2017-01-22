*** Settings ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures



*** Test Cases ***
Add New group
    $(old_list)=   Get Group List
    $(group)=  New Group  name1  header1  footer1
    Create Group  $(group)
    $(new_list)=  Get Group List
    Append To List   $(old_list)  $(group)
    Group List Should Be Equal  $(new_list)  $(old_list)