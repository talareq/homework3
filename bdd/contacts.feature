Scenario Outline: Add new contact
    Given a contact list
    Given a contact with <firstname> and <lastname>
    When I add a new contact to the list
    Then the new contact list is equal to the old list with the added contact

    Examples:
    | firstname  | lastname  |
    | firstname1 | lastname1 |
    | firstname2 | lastname2 |


Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new list is equal to the old list without the deleted contact


Scenario: Modify a contact
  Given a non-empty contact list
  Given a random contact from the list
  Given a contact with <firstname> and <lastname>
  When I modify the contact from the list
  Then the new list is equal to the old list

      Examples:
    | firstname  | lastname  |
    | firstname1 | lastname1 |
    | firstname2 | lastname2 |